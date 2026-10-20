#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""check_refaktor_skilli.py — dowód, że odchudzony SKILL.md nie zgubił treści ani bramek.

PO CO ISTNIEJE
  Refaktor przenosi treść etapów ze SKILL.md do references/*.md (progressive disclosure),
  żeby skill ładował mniej kontekstu przy aktywacji. Ryzyko: po cichu zgubiona linia prawna,
  zniknięta nazwa bramki (model „nie wie, że bramka istnieje”), plik nigdzie niepodlinkowany,
  zmieniony `description` (to jest TRIGGER). Ten skrypt porównuje drzewo BAZOWE (zamrożone,
  sprzed refaktoru) z bieżącym i sprawdza:

  R1 ZACHOWANIE TREŚCI   każda niepusta linia SKILL.md z BAZY (dla prawo-polskie-v2 także
                         ROUTING-MAP.md) po normalizacji występuje wśród linii WSZYSTKICH plików
                         tekstowych tego skilla w drzewie bieżącym (z krotnością: duplikat nie
                         może zniknąć bez wpisu w references/REFAKTOR-ALLOWLIST.md).
  R2 INDEKS BRAMEK       każdy nagłówek BAZOWEGO SKILL.md ze słowem GATE/KROK/ETAP/CHECKPOINT/
                         SELF-CHECK/HARD/ZAKAZ/BLOK ma swój tytuł wspomniany w BIEŻĄCYM SKILL.md.
  R3 ODESŁANIA           plik skilla (nie SKILL.md), który zawiera przeniesione linie bazy, jest
                         podlinkowany ścieżką względną ze SKILL.md (części ROUTING-MAP także z
                         ROUTING-MAP.md) i wpisany do rejestru frontmatteru (logika T22);
                         każda ścieżka względna ze SKILL.md wskazuje istniejący plik.
  R4 BUDŻET              SKILL.md <= 500 linii i <= 32 000 B; frontmatter <= 60 linii.
  R5 FRONTMATTER         name, description i listy dependencies identyczne jak w bazie.

UŻYCIE
  python check_refaktor_skilli.py --base-dir <BAZA> --repo-root <BIEŻĄCE> [--skills a,b]
  python check_refaktor_skilli.py --repo-root <BIEŻĄCE> --budget-only [--skills a,b]
  python check_refaktor_skilli.py --selftest
  Domyślnie: skille, których SKILL.md (albo ROUTING-MAP.md) różni się od bazy.

TEST BEHAWIORALNY (poza tym skryptem; ocenia orkiestrator, LLM-sędzia): tests/eval-refaktor/cases.json
  — 36 scenariuszy × 3-4 pytań o PROCES dla 12 skilli, `expected` wyprowadzone z bazy; instrukcja w kluczu `_instructions`.

KODY WYJŚCIA  0 = PASS, 1 = FAIL, 2 = błąd użycia.
Tylko biblioteka standardowa.
"""

import argparse
import os
import re
import shutil
import sys
import tempfile
from collections import Counter
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):  # konsola Windows (cp1250)
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

sys.path.insert(0, str(Path(__file__).resolve().parent))

# ---------------------------------------------------------------------------
# STAŁE
# ---------------------------------------------------------------------------
MAX_SKILL_LINES = 500
MAX_SKILL_BYTES = 32_000
MAX_FRONTMATTER_LINES = 60
BYTES_PER_TOKEN = 3.2

# Adnotacje audytowe, które wolno wyciąć (jedyne miejsce definicji; wzorce zachowawcze).
ANNOTATION_PATTERNS = [
    r"\((?:dodane|dodano|zmienione|zmieniono|rozszerzone)(?=[^()]*audy)(?:[^()]|\([^()]*\))*\)",
    r"\(audyt [0-9](?:[^()]|\([^()]*\))*\)",
]
_ANN_RE = [re.compile(p, re.I) for p in ANNOTATION_PATTERNS]

GATE_WORDS = ("GATE", "KROK", "ETAP", "CHECKPOINT", "SELF-CHECK", "HARD", "ZAKAZ", "BLOK")
_GATE_RE = re.compile(r"(?<!\w)(?:%s)" % "|".join(re.escape(w) for w in GATE_WORDS))  # rozróżnia wielkość liter

# Dodatkowe pliki bazowe objęte R1 (obok SKILL.md).
EXTRA_BASE_FILES = {"prawo-polskie-v2": ["ROUTING-MAP.md"]}
ALLOWLIST_REL = "references/REFAKTOR-ALLOWLIST.md"
R3_EXEMPT_NAMES = ("CHANGELOG.md",)          # istniejący, zarejestrowany dziennik zmian
REGISTRY_KEYS = ("modules", "references", "scripts", "widgets")
SKIP_DIRS = {"__pycache__", "node_modules", ".git"}
MAX_TEXT_BYTES = 8_000_000

# ---------------------------------------------------------------------------
# NORMALIZACJA I ODCZYT
# ---------------------------------------------------------------------------
_SEP_RE = re.compile(r"^[-=_*:|\s]+$")
_YAML_BLOCK_KEY_RE = re.compile(r"^[A-Za-z_][\w-]*:\s*[|>][+-]?$")  # `changelog: |` — szkielet YAML, nie treść


def strip_annotations(s: str) -> str:
    for rx in _ANN_RE:
        s = rx.sub("", s)
    return s


def norm_line(line: str) -> str:
    """Pusty napis = linia pomijana (separator, ogrodzenie kodu, sama adnotacja)."""
    s = strip_annotations(line.strip()).strip()
    if not s or s.startswith("```") or _SEP_RE.match(s) or _YAML_BLOCK_KEY_RE.match(s):
        return ""
    while True:
        t = s
        t = re.sub(r"^>+\s*", "", t)
        t = re.sub(r"^#{1,6}\s+", "", t)
        t = re.sub(r"^(?:[-*+]|\d+[.)])\s+", "", t)
        t = t.strip()
        if t == s:
            break
        s = t
    s = re.sub(r"\s+", " ", s).strip()
    if not s or _SEP_RE.match(s):
        return ""
    return s


def norm_title(s: str) -> str:
    return re.sub(r"\s+", " ", norm_line(s).replace("*", "").replace("`", "")).strip()


def read_text(path: Path):
    try:
        b = path.read_bytes()
    except OSError:
        return None
    if len(b) > MAX_TEXT_BYTES or b"\0" in b:
        return None
    try:
        return b.decode("utf-8").replace("\r\n", "\n")
    except UnicodeDecodeError:
        return None


def skill_files(skill_dir: Path):
    """Pliki tekstowe skilla: {rel_posix: tekst}."""
    out = {}
    for base, dirs, names in os.walk(skill_dir):
        dirs[:] = sorted(d for d in dirs if d not in SKIP_DIRS)
        for n in sorted(names):
            p = Path(base) / n
            t = read_text(p)
            if t is not None:
                out[p.relative_to(skill_dir).as_posix()] = t
    return out


def split_frontmatter(text: str):
    """(linie frontmattera bez ---, linie ciała) albo (None, wszystkie linie)."""
    lines = text.split("\n")
    if not lines or lines[0].rstrip() != "---":
        return None, lines
    for i in range(1, len(lines)):
        if lines[i].rstrip() == "---":
            return lines[1:i], lines[i + 1:]
    return None, lines


def top_level_blocks(fm_lines):
    blocks, key = {}, None
    for l in fm_lines:
        m = re.match(r"^([A-Za-z_][\w-]*):(.*)$", l)
        if m:
            key = m.group(1)
            blocks[key] = [m.group(2)]
        elif key is not None:
            blocks[key].append(l)
    return blocks


def scalar_value(block):
    if not block:
        return None
    parts = [block[0].strip()] + [x.strip() for x in block[1:] if x.strip() and not x.strip().startswith("#")]
    text = " ".join(p for p in parts if p)
    text = re.sub(r"^[>|][+-]?\s*", "", text)
    text = text.strip()
    if len(text) >= 2 and text[0] == text[-1] and text[0] in "\"'":
        text = text[1:-1]
    return re.sub(r"\s+", " ", text).strip()


def dependency_items(block):
    out, sub = {}, ""
    for l in block or []:
        m = re.match(r"^\s{1,}([A-Za-z_][\w-]*):\s*$", l)
        if m:
            sub = m.group(1)
            continue
        m = re.match(r"^\s*-\s+(.*)$", l)
        if m:
            v = re.split(r"\s+#", m.group(1))[0].strip().strip("\"'")
            out.setdefault(sub, []).append(v)
    return {k: sorted(v) for k, v in out.items()}


def parse_allowlist(text):
    """-> (set znormalizowanych linii, błędy). Wpis: `linia # powód`."""
    entries, errs = set(), []
    for nr, l in enumerate((text or "").split("\n"), 1):
        if not l.strip() or l.lstrip().startswith(("#", "<!--")) or _SEP_RE.match(l.strip()):
            continue
        if " # " not in l:
            errs.append(f"{ALLOWLIST_REL}:{nr}: wpis bez powodu (` # powód`)")
            continue
        line, reason = l.rsplit(" # ", 1)
        if not reason.strip():
            errs.append(f"{ALLOWLIST_REL}:{nr}: pusty powód")
            continue
        n = norm_line(line)
        if n:
            entries.add(n)
    return entries, errs


# ---------------------------------------------------------------------------
# REGUŁY
# ---------------------------------------------------------------------------
def base_sources(skill, bfiles):
    srcs = [("SKILL.md", bfiles.get("SKILL.md", ""))]
    for extra in EXTRA_BASE_FILES.get(skill, []):
        if extra in bfiles:
            srcs.append((extra, bfiles[extra]))
    return srcs


def check_r1(skill, bfiles, cfiles):
    corpus = Counter()
    for rel, t in cfiles.items():
        if rel == ALLOWLIST_REL:
            continue
        for l in t.split("\n"):
            n = norm_line(l)
            if n:
                corpus[n] += 1
    allow, errs = parse_allowlist(cfiles.get(ALLOWLIST_REL))
    base_total = Counter()
    for _, t in base_sources(skill, bfiles):
        for l in t.split("\n"):
            n = norm_line(l)
            if n:
                base_total[n] += 1
    bad_allow = [a for a in allow if base_total.get(a, 0) < 2]
    probs = list(errs)
    probs += [f"ALLOWLIST: wpis nie jest zduplikowaną linią bazy (dozwolone tylko duplikaty): {a[:90]!r}" for a in bad_allow]
    allow -= set(bad_allow)
    seen = Counter()
    for label, t in base_sources(skill, bfiles):
        for nr, l in enumerate(t.split("\n"), 1):
            n = norm_line(l)
            if not n:
                continue
            seen[n] += 1
            have = corpus.get(n, 0)
            if seen[n] <= have:
                continue
            if n in allow and have >= 1:
                continue
            kind = "BRAK" if have == 0 else f"DUPLIKAT {seen[n]}/{base_total[n]} (jest {have})"
            probs.append(f"{kind} — baza {label}:{nr}: {n[:140]}")
    return probs


def base_headings(skill_md_text):
    _, body = split_frontmatter(skill_md_text)
    out, fence = [], False
    for nr, l in enumerate(body, 1):
        if l.lstrip().startswith("```"):
            fence = not fence
            continue
        if fence:
            continue
        m = re.match(r"^#{1,6}\s+(.*)$", l)
        if m:
            title = strip_annotations(m.group(1)).strip()
            if _GATE_RE.search(title):
                out.append((nr, norm_title(title)))
    return out


def check_r2(bskill, cskill):
    _, cbody = split_frontmatter(cskill)
    lines = [norm_title(l) for l in cbody]
    probs = []
    for nr, title in base_headings(bskill):
        if title and not any(title in l for l in lines):
            probs.append(f"bramka/etap „{title[:110]}” (nagłówek bazy, linia ciała {nr}) niewspomniana w SKILL.md")
    return probs


def registry_entries(skill_md_text, key):
    from check_frontmatter_rejestracja import frontmatter, wpisy_klucza  # logika T22
    fm = frontmatter(skill_md_text)
    return None if fm is None else wpisy_klucza(fm, key)


def referenced_paths(skill_md_text, skill_dir_names, skill=""):
    """Ścieżki względne `<katalog skilla>/...` wymienione w SKILL.md (bez wzorców z placeholderami)."""
    if not skill_dir_names:
        return []
    pref = "(?:%s/)?" % re.escape(skill) if skill else ""
    rx = re.compile(r"(?<![\w./-])" + pref + r"((?:%s)/[^\s`\"'<>()|,;\]\[{}*…]+)"
                    % "|".join(re.escape(d) for d in sorted(skill_dir_names, key=len, reverse=True)))
    out = []
    for m in rx.finditer(skill_md_text):
        nxt = skill_md_text[m.end():m.end() + 1]
        if nxt in ("*", "<", "{", "…", "["):
            continue
        p = m.group(1).rstrip(".,;:!?")
        if p and ".." not in p.split("/"):
            out.append(p)
    return sorted(set(out))


def check_r3(skill, skill_dir, bfiles, cfiles, bskill_dir=None):
    probs = []
    cskill = cfiles.get("SKILL.md", "")
    cur_skill_lines = {norm_line(l) for l in cskill.split("\n")} - {""}
    moved = set()
    for _, t in base_sources(skill, bfiles):
        moved |= {norm_line(l) for l in t.split("\n")} - {""}
    moved -= cur_skill_lines
    map_files = set(EXTRA_BASE_FILES.get(skill, []))
    map_text = cfiles.get("ROUTING-MAP.md", "") if map_files else ""
    for rel, t in sorted(cfiles.items()):
        if rel in ("SKILL.md", ALLOWLIST_REL) or rel in map_files or Path(rel).name in R3_EXEMPT_NAMES:
            continue
        if bfiles.get(rel) == t:
            continue                      # plik niezmieniony względem bazy — nie jest wynikiem refaktoru
        file_lines = {norm_line(l) for l in t.split("\n")} - {""}
        if not (file_lines & moved):
            continue
        _, cbody = split_frontmatter(cskill)
        ok = rel in "\n".join(cbody) or (rel in map_text)  # rejestr we frontmatterze to nie odesłanie
        if not ok:
            probs.append(f"plik z przeniesioną treścią niepodlinkowany ze SKILL.md (ścieżką względną): {rel}")
        head = rel.split("/")[0]
        if head in REGISTRY_KEYS and "/" in rel:
            reg = registry_entries(cskill, head)
            if reg is not None and os.path.basename(rel) not in {os.path.basename(x) for x in reg}:
                probs.append(f"plik z przeniesioną treścią bez wpisu w rejestrze `{head}:` frontmattera (T22): {rel}")
    names = {p.split("/")[0] for p in cfiles if "/" in p}
    base_refs = set(referenced_paths(bfiles.get("SKILL.md", ""), names, skill))
    for p in referenced_paths(cskill, names, skill):
        if not (skill_dir / p).exists() and p not in base_refs:
            probs.append(f"ścieżka ze SKILL.md nie istnieje: {p}")
    return probs


def size_info(text):
    b = len(text.encode("utf-8"))
    return {"lines": len(text.splitlines()), "bytes": b, "tokens": int(round(b / BYTES_PER_TOKEN))}


def check_r4(cskill):
    probs = []
    s = size_info(cskill)
    if s["lines"] > MAX_SKILL_LINES:
        probs.append(f"SKILL.md {s['lines']} linii > {MAX_SKILL_LINES}")
    if s["bytes"] > MAX_SKILL_BYTES:
        probs.append(f"SKILL.md {s['bytes']} B > {MAX_SKILL_BYTES} B")
    fm, _ = split_frontmatter(cskill)
    if fm is None:
        probs.append("brak frontmattera (---)")
    else:
        n = frontmatter_budget_lines(fm)
        if n > MAX_FRONTMATTER_LINES:
            probs.append(f"frontmatter {n} linii (bez rejestrów) > {MAX_FRONTMATTER_LINES}")
    return probs


# Rejestry plików i zależności to listy maszynowe (T22, R5) — nie liczą się do budżetu
# frontmattera; budżet dotyczy prozy/historii, która trafia do kontekstu bez potrzeby.
REGISTRY_KEYS = ("modules", "references", "scripts", "widgets", "dependencies")


def frontmatter_budget_lines(fm_lines):
    blocks = top_level_blocks(fm_lines)
    registry = sum(len(blocks[k]) - 1 for k in REGISTRY_KEYS if k in blocks)
    return len(fm_lines) - registry


def check_r5(bskill, cskill):
    bfm, _ = split_frontmatter(bskill)
    cfm, _ = split_frontmatter(cskill)
    if bfm is None or cfm is None:
        return ["brak frontmattera w bazie albo w bieżącym SKILL.md"]
    bb, cb = top_level_blocks(bfm), top_level_blocks(cfm)
    probs = []
    for key in ("name", "description"):
        bv, cv = scalar_value(bb.get(key)), scalar_value(cb.get(key))
        if bv != cv:
            probs.append(f"`{key}` zmienione: baza {str(bv)[:80]!r} -> teraz {str(cv)[:80]!r}")
    if dependency_items(bb.get("dependencies")) != dependency_items(cb.get("dependencies")):
        probs.append("listy `dependencies` różne od bazy")
    return probs


# ---------------------------------------------------------------------------
# ORKIESTRACJA
# ---------------------------------------------------------------------------
def list_skills(root: Path):
    return sorted(d.name for d in root.iterdir() if d.is_dir() and (d / "SKILL.md").is_file())


def changed(skill, base: Path, cur: Path):
    for rel in ["SKILL.md"] + EXTRA_BASE_FILES.get(skill, []):
        a, b = read_text(base / skill / rel), read_text(cur / skill / rel)
        if a != b:
            return True
    return False


def evaluate(base, cur, skills, budget_only=False):
    """-> list wyników: {skill, rules:{R:list problemów|None}, before, after}."""
    res = []
    for sk in skills:
        r = {"skill": sk, "rules": {}, "before": None, "after": None}
        cdir = cur / sk
        cfiles = skill_files(cdir) if cdir.is_dir() else {}
        if "SKILL.md" not in cfiles:
            r["rules"]["R1"] = [f"brak {sk}/SKILL.md w drzewie bieżącym"]
            res.append(r)
            continue
        r["after"] = size_info(cfiles["SKILL.md"])
        r["rules"]["R4"] = check_r4(cfiles["SKILL.md"])
        if not budget_only:
            bdir = base / sk
            if not (bdir / "SKILL.md").is_file():
                for k in ("R1", "R2", "R3", "R5"):
                    r["rules"][k] = [f"brak {sk}/SKILL.md w BAZIE"]
            else:
                bfiles = skill_files(bdir)
                r["before"] = size_info(bfiles["SKILL.md"])
                r["rules"]["R1"] = check_r1(sk, bfiles, cfiles)
                r["rules"]["R2"] = check_r2(bfiles["SKILL.md"], cfiles["SKILL.md"])
                r["rules"]["R3"] = check_r3(sk, cdir, bfiles, cfiles)
                r["rules"]["R5"] = check_r5(bfiles["SKILL.md"], cfiles["SKILL.md"])
        res.append(r)
    return res


def report(res, budget_only, out=print):
    rules = ("R4",) if budget_only else ("R1", "R2", "R3", "R4", "R5")
    out("%-42s %s   %-17s %-17s %s" % ("SKILL", "  ".join("%-4s" % x for x in rules),
                                      "linie przed>po", "bajty przed>po", "tokeny~ przed>po"))
    tot_b = tot_a = tl_b = tl_a = tt_b = tt_a = 0
    fail = False
    for r in res:
        cells = []
        for k in rules:
            v = r["rules"].get(k)
            cells.append("%-4s" % ("--" if v is None else ("ok" if not v else "FAIL")))
            if v:
                fail = True
        b, a = r["before"], r["after"]
        f = lambda x, key: "-" if x is None else str(x[key])
        out("%-42s %s   %-17s %-17s %s" % (r["skill"], "  ".join(cells),
                                           f(b, "lines") + ">" + f(a, "lines"),
                                           f(b, "bytes") + ">" + f(a, "bytes"),
                                           f(b, "tokens") + ">" + f(a, "tokens")))
        if a:
            tot_a += a["bytes"]; tl_a += a["lines"]; tt_a += a["tokens"]
        if b:
            tot_b += b["bytes"]; tl_b += b["lines"]; tt_b += b["tokens"]
    out("RAZEM aktywacja: linie %d>%d, bajty %d>%d, tokeny~ %d>%d" % (tl_b, tl_a, tot_b, tot_a, tt_b, tt_a))
    for r in res:
        for k in rules:
            for p in (r["rules"].get(k) or []):
                out("  [%s] %s: %s" % (k, r["skill"], p))
    return not fail


def run(base, cur, skills_arg, budget_only, out=print):
    cur = Path(cur)
    if budget_only:
        skills = skills_arg or list_skills(cur)
        res = evaluate(None, cur, skills, True)
        ok = report(res, True, out)
        out("WYNIK R4 (budżet): %s — %d skilli" % ("PASS" if ok else "FAIL", len(res)))
        return 0 if ok else 1
    base = Path(base)
    if skills_arg:
        skills = skills_arg
    else:
        skills = [s for s in list_skills(base) if changed(s, base, cur)]
    if not skills:
        out("0 skills changed — nic do sprawdzenia.")
        out("WYNIK: PASS")
        return 0
    out("Skilli w zakresie: %d" % len(skills))
    res = evaluate(base, cur, skills)
    ok = report(res, False, out)
    out("WYNIK: %s" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


# ---------------------------------------------------------------------------
# SELFTEST — mutacje na syntetycznych fixture'ach
# ---------------------------------------------------------------------------
_BASE_SKILL = """---
name: demo-skill
version: "1.0"
description: "UŻYWAJ, gdy użytkownik prosi o demo. Nie przy innych sprawach."
dependencies:
  requires:
    - shared
    - inny-skill   # komentarz
  called_by:
    - router
references:
  - references/CHANGELOG.md
changelog: |
  1.0 długa historia wersji która ma trafić do CHANGELOG
---
# Demo skill

## Wprowadzenie (dodane w audycie 3.4)
Użyj tego skilla, gdy użytkownik prosi o demo.

## ETAP 1 — Zbieranie danych
- Zapytaj o sygnaturę sprawy.
- Art. 123 § 4 KPC: termin wynosi 7 dni.

## GATE A — Weryfikacja źródeł
> Nie podawaj przepisu bez sprawdzenia w źródle.
| a | b |
|---|---|
| Art. 5 KC | zasady współżycia |

## ETAP 2 — Opracowanie
1. Sporządź zestawienie.
2. Art. 999 KPC: dowód z przesłuchania.

## Uwagi końcowe
Koniec.
"""

_CUR_SKILL = """---
name: demo-skill
version: "1.0"
description: "UŻYWAJ, gdy użytkownik prosi o demo. Nie przy innych sprawach."
dependencies:
  requires:
    - inny-skill   # komentarz
    - shared
  called_by:
    - router
references:
  - references/CHANGELOG.md
  - references/etap-1.md
  - references/etap-2.md
---
# Demo skill

## Wprowadzenie
Użyj tego skilla, gdy użytkownik prosi o demo.

## Indeks etapów i bramek
- ETAP 1 — Zbieranie danych: `view demo-skill/references/etap-1.md`
- GATE A — Weryfikacja źródeł: `view demo-skill/references/etap-1.md`
- ETAP 2 — Opracowanie: `view demo-skill/references/etap-2.md`

## Uwagi końcowe
Koniec.
"""

_ETAP1 = """# ETAP 1 — Zbieranie danych
- Zapytaj o sygnaturę sprawy.
- Art. 123 § 4 KPC: termin wynosi 7 dni.

## GATE A — Weryfikacja źródeł
> Nie podawaj przepisu bez sprawdzenia w źródle.
| a | b |
|---|---|
| Art. 5 KC | zasady współżycia |
"""

_ETAP2 = """# ETAP 2 — Opracowanie
1. Sporządź zestawienie.
2. Art. 999 KPC: dowód z przesłuchania.
"""

_CHANGELOG = "# Changelog\n1.0 długa historia wersji która ma trafić do CHANGELOG\n"

_PP_BASE_SKILL = "---\nname: prawo-polskie-v2\ndescription: \"Mapa prawa.\"\n---\n# Prawo\nPrzeczytaj ROUTING-MAP.md.\n"
_PP_CUR_SKILL = ("---\nname: prawo-polskie-v2\ndescription: \"Mapa prawa.\"\n---\n# Prawo\n"
                 "Przeczytaj ROUTING-MAP.md.\nWłaściwy plik: routing/DR-01.md.\n")
_PP_BASE_MAP = "# Mapa\n## DR-01\n| Ustawa | Moduł |\n|---|---|\n| KC | mod-kc |\n"
_PP_CUR_MAP = "# Mapa\n- DR-01: `routing/DR-01.md`\n"
_PP_DR01 = "## DR-01\n| Ustawa | Moduł |\n|---|---|\n| KC | mod-kc |\n"


def _w(root: Path, rel: str, text: str):
    p = root / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text, encoding="utf-8", newline="\n")


def build_fixture(tmp: Path):
    base, cur = tmp / "base", tmp / "cur"
    for root, skill in ((base, _BASE_SKILL), (cur, _CUR_SKILL)):
        _w(root, "demo-skill/SKILL.md", skill)
        _w(root, "demo-skill/references/CHANGELOG.md", _CHANGELOG)
        _w(root, "prawo-polskie-v2/SKILL.md", _PP_BASE_SKILL if root is base else _PP_CUR_SKILL)
    _w(cur, "demo-skill/references/etap-1.md", _ETAP1)
    _w(cur, "demo-skill/references/etap-2.md", _ETAP2)
    _w(base, "prawo-polskie-v2/ROUTING-MAP.md", _PP_BASE_MAP)
    _w(cur, "prawo-polskie-v2/ROUTING-MAP.md", _PP_CUR_MAP)
    _w(cur, "prawo-polskie-v2/routing/DR-01.md", _PP_DR01)
    return base, cur


def _edit(path: Path, old: str, new: str):
    s = path.read_text(encoding="utf-8")
    if old not in s:
        raise RuntimeError(f"mutacja nieaktualna: {old[:40]!r} w {path.name}")
    path.write_text(s.replace(old, new, 1), encoding="utf-8", newline="\n")


def selftest():
    import io
    from contextlib import redirect_stdout
    ok_all = True
    wyniki = []

    def scenario(label, mutate, skills, expect_rules, budget_only=False):
        nonlocal ok_all
        with tempfile.TemporaryDirectory(prefix="refaktor-selftest-") as t:
            base, cur = build_fixture(Path(t))
            mutate(cur)
            res = evaluate(None if budget_only else base, cur, skills, budget_only)
            failed = {k for r in res for k, v in r["rules"].items() if v}
        good = failed == set(expect_rules)
        ok_all &= good
        wyniki.append((good, label, sorted(failed), sorted(expect_rules)))

    S = ["demo-skill"]
    scenario("(a) fixture po refaktorze przechodzi", lambda c: None, S + ["prawo-polskie-v2"], [])
    scenario("(b) usunięta przeniesiona linia prawna -> R1",
             lambda c: _edit(c / "demo-skill/references/etap-2.md", "2. Art. 999 KPC: dowód z przesłuchania.\n", ""), S, ["R1"])
    scenario("(b2) usunięta linia z ROUTING-MAP -> R1",
             lambda c: _edit(c / "prawo-polskie-v2/routing/DR-01.md", "| KC | mod-kc |\n", ""), ["prawo-polskie-v2"], ["R1"])
    scenario("(c) usunięta nazwa bramki ze SKILL.md -> R2",
             lambda c: _edit(c / "demo-skill/SKILL.md", "- GATE A — Weryfikacja źródeł: `view demo-skill/references/etap-1.md`\n", ""), S, ["R2"])
    scenario("(d) przeniesiony plik niepodlinkowany -> R3",
             lambda c: _edit(c / "demo-skill/SKILL.md",
                             "- ETAP 2 — Opracowanie: `view demo-skill/references/etap-2.md`\n", "- ETAP 2 — Opracowanie\n"), S, ["R3"])
    scenario("(d2) plik bez wpisu w rejestrze frontmattera -> R3",
             lambda c: _edit(c / "demo-skill/SKILL.md", "  - references/etap-2.md\n", ""), S, ["R3"])
    scenario("(d3) ścieżka ze SKILL.md nie istnieje -> R3",
             lambda c: _edit(c / "demo-skill/SKILL.md", "Koniec.", "Koniec.\n`view demo-skill/references/nie-ma.md`"), S, ["R3"])
    scenario("(e) SKILL.md ponad budżet linii -> R4",
             lambda c: (c / "demo-skill/SKILL.md").open("a", encoding="utf-8", newline="\n").write("x\n" * 600), S, ["R4"])
    scenario("(e2) SKILL.md ponad budżet bajtów -> R4",
             lambda c: (c / "demo-skill/SKILL.md").open("a", encoding="utf-8", newline="\n").write("x" * 33000 + "\n"), S, ["R4"])
    scenario("(e3) frontmatter > 60 linii -> R4",
             lambda c: _edit(c / "demo-skill/SKILL.md", "references:\n", "".join(f"k{i}: v\n" for i in range(70)) + "references:\n"), S, ["R4"])
    scenario("(f) zmieniony description -> R5",
             lambda c: _edit(c / "demo-skill/SKILL.md", "o demo.", "o demo i więcej."), S, ["R1", "R5"])  # linia description jest też linią bazy
    scenario("(f2) zmieniona lista dependencies -> R5",
             lambda c: _edit(c / "demo-skill/SKILL.md", "    - router\n", "    - router\n    - nowy\n"), S, ["R5"])
    scenario("(g) zmiana wyłącznie adnotacji przechodzi",
             lambda c: _edit(c / "demo-skill/SKILL.md", "## Wprowadzenie\n", "## Wprowadzenie (dodane w audycie 9.9)\n"), S, [])

    def _dup(c):
        _edit(c / "demo-skill/references/etap-1.md", "- Zapytaj o sygnaturę sprawy.\n", "- Zapytaj o sygnaturę sprawy.\n- Zapytaj o sygnaturę sprawy.\n")
        _w(c, "demo-skill/references/REFAKTOR-ALLOWLIST.md", "- Zapytaj o sygnaturę sprawy. # duplikat\n")

    def _base_dup_scenario():
        nonlocal ok_all
        with tempfile.TemporaryDirectory(prefix="refaktor-selftest-") as t:
            base, cur = build_fixture(Path(t))
            _edit(base / "demo-skill/SKILL.md", "- Zapytaj o sygnaturę sprawy.\n", "- Zapytaj o sygnaturę sprawy.\n- Zapytaj o sygnaturę sprawy.\n")
            r1 = evaluate(base, cur, S)[0]["rules"]["R1"]          # duplikat zgubiony -> FAIL
            _w(cur, "demo-skill/references/REFAKTOR-ALLOWLIST.md", "- Zapytaj o sygnaturę sprawy. # byte-identyczny duplikat\n")
            r2 = evaluate(base, cur, S)[0]["rules"]["R1"]          # z allowlistą -> PASS
            _w(cur, "demo-skill/references/REFAKTOR-ALLOWLIST.md", "- Art. 999 KPC: dowód z przesłuchania. # nie duplikat\n")
            _edit(cur / "demo-skill/references/etap-2.md", "2. Art. 999 KPC: dowód z przesłuchania.\n", "")
            r3 = evaluate(base, cur, S)[0]["rules"]["R1"]          # allowlista nie ratuje utraty jedynej linii
        good = bool(r1) and not r2 and bool(r3)
        ok_all &= good
        wyniki.append((good, "(h) allowlista: tylko duplikaty (utrata duplikatu FAIL, z allowlistą PASS, jedyna linia FAIL)",
                       [], []))

    _base_dup_scenario()
    scenario("(i) R4 w trybie --budget-only: fixture OK", lambda c: None, S, [], budget_only=True)
    scenario("(i2) R4 w trybie --budget-only: za duży -> FAIL",
             lambda c: (c / "demo-skill/SKILL.md").open("a", encoding="utf-8", newline="\n").write("x\n" * 600), S, ["R4"], budget_only=True)

    # kod wyjścia w pełnym przebiegu: bez zmian = 0 skilli, PASS
    with tempfile.TemporaryDirectory(prefix="refaktor-selftest-") as t:
        base, _ = build_fixture(Path(t))
        buf = io.StringIO()
        with redirect_stdout(buf):
            code = run(base, base, None, False)
        good = code == 0 and "0 skills changed" in buf.getvalue()
        ok_all &= good
        wyniki.append((good, "(j) baza = bieżące -> 0 skills changed, PASS", [], []))

    print("SELFTEST check_refaktor_skilli — %d scenariuszy" % len(wyniki))
    for good, label, got, exp in wyniki:
        extra = "" if good else "   (oczekiwano %s, jest %s)" % (exp, got)
        print("  %s %s%s" % ("OK  " if good else "FAIL", label, extra))
    print("WYNIK SELFTEST: %s" % ("PASS" if ok_all else "FAIL"))
    return 0 if ok_all else 1


def main():
    ap = argparse.ArgumentParser(description="Kontrola refaktoru skilli (R1–R5)")
    ap.add_argument("--base-dir", default=None, help="korzeń skilli BAZOWYCH (zamrożony)")
    ap.add_argument("--repo-root", default=None, help="korzeń skilli bieżących")
    ap.add_argument("--skills", default="", help="lista po przecinku (domyślnie: skille ze zmienionym SKILL.md)")
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--budget-only", action="store_true", help="tylko R4, bez bazy")
    try:
        a = ap.parse_args()
    except SystemExit as e:
        return 2 if e.code else 0
    if a.selftest:
        return selftest()
    root = a.repo_root or os.environ.get("LEX_MACHINA_ROOT") or os.environ.get("REPO_ROOT") \
        or str(Path(__file__).resolve().parents[2])
    if not Path(root).is_dir():
        print("BŁĄD: --repo-root nie jest katalogiem: %s" % root)
        return 2
    skills = [s.strip() for s in a.skills.split(",") if s.strip()]
    if not a.budget_only:
        if not a.base_dir or not Path(a.base_dir).is_dir():
            print("BŁĄD: wymagane --base-dir (istniejący katalog) albo --budget-only / --selftest")
            return 2
    for s in skills:
        if not (Path(root) / s).is_dir():
            print("BŁĄD: brak skilla w --repo-root: %s" % s)
            return 2
    return run(a.base_dir, root, skills, a.budget_only)


if __name__ == "__main__":
    sys.exit(main())
