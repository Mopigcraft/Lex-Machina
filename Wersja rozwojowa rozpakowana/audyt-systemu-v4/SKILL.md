---
name: audyt-systemu-v4
description: "Audyt jakości, spójności i bezpieczeństwa systemu prawnych skilli: zależności, wersje, mapy Dz.U., treść merytoryczna, propagacja zmian, deduplikacja i bramki jakości."
dependencies:
  requires:
    - shared
version: "6.231"   # zawsze w cudzysłowie (6.10 bez niego = float 6.1)
type: governance-audit
compatibility: "host-neutral; file read/write, fresh legal-source lookup and optional archive/UI operations mapped by the runtime adapter"
entrypoint: SKILL.md
modules:
  - modules/MOD-INTERLINIE.md
  - modules/MOD-WSTAWKI.md
  - modules/MOD-DESCRIPTION.md
  - modules/MOD-TRESC-MERYTORYCZNA.md
  - modules/MOD-PROPAGACJA-NOWELIZACJI.md
widgets:
  - widgets/WIDGET-MENU.md
references:
  - references/AUDIT-JOURNAL.md
  - references/F-113-PREFLIGHT-2026-08-26.md
  - references/HISTORIA-ZMIAN-PLIKOW.md
  - references/CHANGELOG.md
  - references/F-171-pomiar-domen-2026-09-09.md
  - references/F-152-pomiar-domen-2026-09-04.md
  - references/PORTALE-ORZECZNICZE-API.md
  - references/WARN-OTWARTE.md
  - references/CHECKLIST-DEDUP.md
  - references/mapa_dzu_2026-10-04.md
  - references/mapa_dzu_2026-08-28.md
  - references/ALIASY-NAZW-AKTOW.md
  - references/SKRYPTY-RECZNE.md
  - references/PROTOKOL-WYKONAWCZY-F113.md
  - references/PLAN-TESTU-BRAMEK-F113.md
  - references/REGRESSION-TEST-PLAN.md
  - references/SYNC-DZU-AUTOMATYCZNY.md
  - references/HARMONOGRAM-CRON.md
  - references/SCHEDULED-TASK-COWORK.md
  - references/PAMIEC-TRWALA-ROUTER.md
  - references/FORMAT-RAPORTU-ROZNIC.md
  - references/F-108-lista-MS-egzamin-2026.md
  - references/COWORK-HARMONOGRAM-NATYWNY.md
  - references/raporty-pokrycia-2026-08-13/
  - references/PLAN-POMIARU-BRAMEK-UNIWERSALNY.md
  - references/REJESTR-BRAMEK-POMIAR.json
  - references/REJESTR-KORPUSU-POMIAROWEGO.md
  - references/zasady-i-struktura.md
  - references/faza-0-2.md
  - references/faza-3-7.md
scripts:
  - scripts/check_wartosci_prawne.py
  - scripts/check_oplaty_mapa.py
  - scripts/check_utrata_tresci.py
  - scripts/check_wydanie.py
  - scripts/check_archiwa_repo.py
  - scripts/check_wejscie_dokumentu.py
  - scripts/check_eli_extract.py
  - scripts/check_plugin_manifest.py
  - scripts/check_kontrakt_rachunek.py
  - scripts/check_sekrety.py
  - scripts/check_graf_przyczynowy.py
  - scripts/check_mapy_aktow.py
  - scripts/test_mac_ce_litery.py
  - scripts/test_konstytucja_tekst_czysty.py
  - scripts/napraw_tekst_dzu.py
  - scripts/check_osiagalnosc_shared.py
  - scripts/check_testy_skilli.py
  - scripts/test_mutacje_zestawu.py
  - scripts/check_sieroty.py
  - scripts/_lex_common.py
  - scripts/check_limit_plikow.py
  - scripts/check_tabele_satelickie.py
  - scripts/check_podmiana_aktu.py
  - scripts/check_widmowe_pokrycie.py
  - scripts/weryfikator_sygnatur.py
  - scripts/test_konstytucja_tekst_czysty.py
  - scripts/test_pokrycie_orkiestratora.py
  - scripts/test_module_registration.py
  - scripts/test_module_count.py
  - scripts/test_cross_map_dzu.py
  - scripts/test_header_snapshot.py
  - scripts/test_title_scope_match.py
  - scripts/test_moved_to_shared.py
  - scripts/check_wersje_changelog.py
  - scripts/check_dlugosc_modulow.py
  - scripts/build_ramie_kontrolne_f113.py
  - scripts/build_ramie_kontrolne.py
  - scripts/ocena_transkryptow_f113.py
  - scripts/check_description.py
  - scripts/check_sync_aktow.py
  - scripts/run_regression_suite.py
  - scripts/ci_check_shared.py
  - scripts/check_rejestracja_modulow.py
  - scripts/check_coverage_coherence.py
  - scripts/sync_dzu_eli.py
  - scripts/audit_tj_inventory.py
  - scripts/audit_amendment_scope.py
  - scripts/check_status_podstaw.py
  - scripts/check_wyjatek_gate_eli.py
  - scripts/check_checksums.py
  - scripts/check_nowelizacje_po_tj.py
  - scripts/check_frontmatter_yaml.py
  - scripts/check_domeny_allowlist.py
  - scripts/test_router_contract.py
  - scripts/check_frontmatter_rejestracja.py
  - scripts/test_f108_trade.py
  - scripts/test_f108_consistency.py
  - scripts/mock_eli_server_test.py
  - scripts/bootstrap_last_sync_date.py
  - scripts/dostarcz_skill.sh
  - scripts/install_precommit_hook.sh
  - scripts/check_refaktor_skilli.py
  - scripts/README.md
---

> **Universal runtime:** przed wykonaniem zastosuj kanoniczny `shared/UNIVERSAL-RUNTIME-ADAPTER.md` z osobnego skilla `shared`. Lokalna sekcja adaptera poniżej jedynie go doprecyzowuje.


## ADAPTER RUNTIME — PORTABILITY (ChatGPT / Claude / inne hosty)

Ta sekcja zmienia wyłącznie wykonanie operacji technicznych. Tryby audytu, zasady kontroli merytorycznej, map Dz.U., deduplikacji, propagacji zmian, rejestrów i bramek jakości pozostają bez zmian.

1. `view audyt-systemu-v4/<plik>` oraz względne odwołania do `modules/`, `references/`, `scripts/` i `widgets/` oznaczają świeży odczyt lokalnego zasobu tego skilla. Literalna ścieżka `/mnt/skills/user` nie jest wymagana.
2. `view shared/<plik>` oznacza świeży odczyt z osobnego, kanonicznego skilla `shared`. NIE kopiuj `shared` do paczki audytora. Brak obowiązkowego zasobu = fail-closed.
3. `view <inny-skill>/<plik>` oznacza odczyt/aktywację osobnego skilla przez mechanizm hosta. Audyt może kontrolować zależności między skillami, ale nie vendoryzuje ich.
4. `web_search` / `web_fetch` oznaczają świeże wyszukanie i odczyt źródła przez równoważną funkcję hosta. Przy audycie prawa zachowaj wymóg źródeł oficjalnych i nie traktuj pamięci modelu jako weryfikacji.
5. `present_files`, `create_file`, `show_widget`, `visualize:read_me`, Cowork i podobne nazwy są operacjami semantycznymi. Użyj równoważnej natywnej funkcji hosta, jeśli istnieje; jeśli nie, zastosuj tekstowy/plikowy fallback bez fikcyjnego raportowania wykonania.
6. Skrypty w `scripts/` mają wykrywać root repo względnie lub z `REPO_ROOT`/`LEX_MACHINA_ROOT`; nie zakładaj `/mnt/skills/user`. Twardy limit wydania pozostaje 200 plików na skill.
7. Audyt treści i narzędzi może raportować Claude-specific lub ChatGPT-specific tokeny jako portability warnings; sama obecność legacy nazwy nie jest automatycznie błędem, jeśli adapter semantyczny zapewnia równoważne wykonanie.
8. Nie ujawniaj prywatnego chain-of-thought jako produktu audytu. Raportuj wykryte fakty, ślady weryfikacji, testy, różnice, ryzyka i rekomendowane poprawki.

**Zasada nadrzędna:** instrukcje, które są już zrozumiałe i wykonalne w bieżącym hoście, wykonuj bez konwersji. Adapter działa wyłącznie na granicy runtime.


# audyt-systemu-v4 — Orchestrator Audytu Systemu Prawnego

## Cel
Audyt jakości, spójności i bezpieczeństwa systemu prawniczych skilli AI.
Po zakończeniu audytu: **obowiązkowa aktualizacja plików references**.

> ⚙️ **ZASADA 11 (STAŁA):** zakres audytu = WSZYSTKIE skille prawne (także proceduralne — wtedy audytowane są domyślnie stosowane bramki jakości); wpis w `AUDIT-JOURNAL.md` z jawnym wskazaniem skilla proceduralnego.
> ⚙️ **ZASADA 12 (STAŁA):** audyt map Dz.U. (FAZA 3A–3D) i audyt treści merytorycznej modułów (FAZA 3E) to dwa odrębne, obowiązkowe zakresy; FAZA 3E uruchamia się automatycznie po zmianie statusu aktu; zamknięcie FAZA 3 bez 3E = **CRIT**.
> ⚙️ **ZASADA 13 (STAŁA):** ponowna weryfikacja oznaczeń/skrótów prawnych, wytrwałość wyszukiwania, `⚠️ [NIEWERYFIKOWANE]` przy każdym użyciu (źródło: `shared/PRAWO-HARDGATE.md`); naruszenie = **CRIT**.
> ⚙️ **ZASADA 14 (STAŁA):** gradacja źródeł przy weryfikacji merytorycznej (FAZA 3E) wg `shared/HIERARCHIA-ZRODEL.md` (Rząd 1 ELI zawsze pierwszy; Rząd 3 nigdy jako jedyne źródło; wynik wskazuje Rząd); naruszenie = **WARN**.
> ⚙️ **ZASADA 15 (STAŁA):** historia zmian skilla mieszka wyłącznie w `references/CHANGELOG.md` (w SKILL.md tylko odesłanie; pole `changelog:` YAML krótkie, do ~15 linii); egzekwuje T12.

**WCZYTAJ (obowiązkowo, fail-closed):** view audyt-systemu-v4/references/zasady-i-struktura.md — pełne brzmienie ZASAD 11–15; przeczytaj przed FAZĄ 3/3E oraz przed każdą zmianą w historii zmian skilla.
---

## FAZA 0 — WCZYTANIE REFERENCES (ZAWSZE PIERWSZE)

*(Notatka historyczna „NAPRAWA 2026-08-15 (F-80)” — w `references/faza-0-2.md`.)*

Przed jakimkolwiek działaniem wczytaj:

```
ODCZYT DZIENNIKA (wyłącznie potrzebny fragment — procedura niżej)
view audyt-systemu-v4/references/WARN-OTWARTE.md
view audyt-systemu-v4/references/CHECKLIST-DEDUP.md
USTAL AKTUALNA_MAPA_DZU: wylistuj references/mapa_dzu_YYYY-MM-DD.md,
wybierz plik z najpóźniejszą datą w nazwie i sprawdź, że da się go odczytać
view AKTUALNA_MAPA_DZU
```

⛔ **Nie wczytuj całego `AUDIT-JOURNAL.md`** (ok. 71 tys. linii, ok. 4 MB) — ani
w FAZIE 0, ani w 7A. Odczytuj tylko potrzebny fragment:

```bash
J=audyt-systemu-v4/references/AUDIT-JOURNAL.md
# najnowszy wpis = najwyższy identyfikator AUDYT-…, nie ostatnia pozycja w pliku
N=$(grep -n '^## AUDYT-[0-9]' "$J" | LC_ALL=C sort -t' ' -k2,2 | tail -1 | cut -d: -f1)
# odczyt najnowszego wpisu: od linii N do nagłówka następnego wpisu
sed -n "${N},$((N+120))p" "$J" | awk 'NR>1 && /^## /{exit} {print}'
# szablon wpisu (tylko przy pisaniu, FAZA 6/7A)
S=$(grep -n '^## SZABLON NOWEGO WPISU' "$J" | cut -d: -f1); sed -n "${S},$((S+38))p" "$J"
```

Wcześniejsze wpisy czytaj tylko wtedy, gdy zadanie ich wymaga (np. `grep -n
'AUDYT-2026-08-15h' "$J"` → odczyt zakresu linii tego wpisu).

⛔ Nie wpisuj na stałe daty bieżącej mapy w procedurze. Każda nowa generacja
zmienia nazwę pliku; brak dynamicznego wyboru powodował odwołania do usuniętej
mapy z 2026-08-21 mimo obecności mapy z 2026-08-26. Brak choć jednego pliku
`mapa_dzu_YYYY-MM-DD.md` albo błąd odczytu najnowszego = CRIT i STOP.

Celem jest ustalenie:
- Jaki był wynik ostatniego audytu (AUDIT-JOURNAL.md → ostatni wpis `## AUDYT-YYYY-MM-DD`)
- Czy wprowadzane zmiany dotyczą pojęcia już skatalogowanego w CHECKLIST-DEDUP.md
  (jeśli TAK → edytuj lokalizację kanoniczną, NIE twórz nowego wpisu — patrz
  "PROCEDURA UŻYCIA" w CHECKLIST-DEDUP.md)
- Czy edytowany moduł jest na liście modułów >400 linii (NOTA-4 w
  CHECKLIST-DEDUP.md) — jeśli TAK, rozważ podział "przy okazji"
- Jakie WARN/flagi są otwarte i wymagają zamknięcia — źródło: `WARN-OTWARTE.md`
  (ZASADA 10), NIE przeszukiwanie całego AUDIT-JOURNAL.md
- Jaka jest aktualna mapa skilli i Dz.U.

---

## FAZA 0B — INTERAKTYWNY WYBÓR ZAKRESU

Gdy użytkownik wywołuje audyt **bez precyzowania zakresu** (np. "przeprowadź audyt", "audytuj system"):

1. Wyrenderuj menu wielokrotnego wyboru: `show_widget(path="audyt-systemu-v4/widgets/WIDGET-MENU.md")` — host czyta kod JSX z pliku; nie przepisuj go.

2. Host bez `path`: `view audyt-systemu-v4/widgets/WIDGET-MENU.md` → `show_widget` z kodem JSX z pliku.

3. Czekaj na wybór użytkownika. Po otrzymaniu — uruchom **tylko wskazane fazy/moduły**.

Gdy użytkownik podał konkretny tryb lub zakres → pomiń widget, przejdź bezpośrednio do właściwej fazy.

---

## FAZA 0C — ZADANIE CYKLICZNE W COWORK (POZYCJA 11, TYLKO NA ŻĄDANIE)

**WCZYTAJ (obowiązkowo, fail-closed):** view audyt-systemu-v4/references/faza-0-2.md — przed wykonaniem FAZY 0C, 0D lub 0E (tylko gdy wybrano tę pozycję menu / padło odpowiednie polecenie).


Wyłącznie na wyraźne żądanie / wybór pozycji 11 menu. ⛔ Nigdy nie proponuj zadania cyklicznego automatycznie.

## FAZA 0D — KONTRAKT ROUTERA W PREFERENCJACH (POZYCJA 13, od 6.125)

Po wyborze pozycji 13 / „zsynchronizuj pamięć routera”: porównanie preferencji z regułami UP-1…UP-6 wg `references/PAMIEC-TRWALA-ROUTER.md` (kontrola, bez zapisu).

## FAZA 0E — INSTALACJA SERWERÓW MCP (POZYCJA 14; wybór serwerów i klucz CEIDG od 6.152)

Po wyborze pozycji 14 / „zainstaluj serwery MCP”: trzy tury (lista wyboru, instalacja + prośba o klucz CEIDG, zapis w dzienniku bez tokenu), narzędzie `mcp-servers/instaluj_serwery_mcp.py`.



---

## FAZA 1 — INWENTARYZACJA SYSTEMU

```bash
find "${LEX_MACHINA_SKILLS_ROOT:?}" -not -path "*/archive/*" | sort
```

Jeżeli host nie udostępnia zmiennej, najpierw rozwiąż semantyczny katalog
zainstalowanych skilli wg adaptera runtime i użyj jego rzeczywistej ścieżki.

Zbuduj tabelę: skill → liczba plików → rozmiar → status (✅/⚠️/❌).

Porównaj z ostatnim snapshotem z AUDIT-JOURNAL.md (sekcja "STRUKTURA SYSTEMU — SNAPSHOT").
Wykryj: nowe skille, usunięte skille, zmienione rozmiary.

---

## FAZA 2 — WERYFIKACJA ZALEŻNOŚCI

**WCZYTAJ (obowiązkowo, fail-closed):** view audyt-systemu-v4/references/faza-0-2.md — przed wykonaniem 2A–2D (komendy, progi CRIT/WARN, procedury modułów).


### 2A — Spójność ścieżek

Każde `view`/`load` w SKILL.md wskazuje istniejący plik; nieistniejąca ścieżka = **CRIT**.

### 2B — Wersje skilli w cross-referencjach

Brak odwołań do usuniętych wersji skilli (np. v1 zamiast v2).

### 2C — Pole description: OBECNOŚĆ + profil uniwersalny ≤200 znaków

Procedura z `modules/MOD-DESCRIPTION.md`, kontrola automatyczna T14.

## FAZA 2D — CZYSTOŚĆ KODU (NOWE MODUŁY)

Moduły czystości działają zachowawczo (w razie wątpliwości ZOSTAW).

### 2D-1 — Zbędne interlinie

Procedura z `modules/MOD-INTERLINIE.md` (≥2 kolejne puste linie).

### 2D-2 — Wstawki opisowe

Procedura z `modules/MOD-WSTAWKI.md` (skan regex, kwalifikacja, usuwanie tylko jednoznacznie opisowych).



---

## FAZA 3 — WERYFIKACJA MAPY Dz.U.

**WCZYTAJ (obowiązkowo, fail-closed):** view audyt-systemu-v4/references/faza-3-7.md — przed wykonaniem FAZY 3 (3-PULL, 3A–3D) i FAZY 3E; ten plik MUSI być przeczytany przed zamknięciem FAZY 3.

Użyj `AKTUALNA_MAPA_DZU` ustalonej w FAZIE 0 (nie wybieraj mapy z daty zapamiętanej w tym pliku).

### 3-PULL — Synchronizacja DR-MAPA-AKTOW → ROUTING-MAP → mapa_dzu

Protokół pull PRZED 3A (TRYB DZU / pełny audyt): spójność mapa_dzu z tym, co mają skille DR.
ROUTING-MAP = indeks `prawo-polskie-v2/ROUTING-MAP.md` + tabele dziedzin `prawo-polskie-v2/routing/DR-xx.md` (od 2026-10-20).

### 3A — Nowe t.j. od ostatniego audytu

Nowe teksty jednolite kluczowych aktów w ELI (RZĄD 1).

### 3B — Aktualizacja statusów

Nowe t.j.: stary wpis `OK` → `PREV`, nowy wiersz `TJ` w mapie.

### 3D — Akty oczekujące na wejście w życie (MONITORING)

Legenda znaczników (w tym ⚠️ ALERT), vacatio legis, daty wejścia w życie.

### 3C — Rozporządzenia "do weryfikacji"

Otwarte WARN z poprzednich audytów dotyczące rozporządzeń.

## FAZA 3E — WERYFIKACJA TREŚCI MERYTORYCZNEJ MODUŁÓW (ZASADA 12)

Obowiązkowa po każdej zmianie statusu aktu w FAZIE 3: czy treść modułów DR (progi, terminy, definicje, przesłanki) odpowiada stanowi prawnemu; moduł `MOD-TRESC-MERYTORYCZNA.md`; zamknięcie FAZY 3 bez 3E = **CRIT**.



---

## FAZA 4 — TESTY ANTYHALUCYNACYJNE

**WCZYTAJ (obowiązkowo, fail-closed):** view audyt-systemu-v4/references/faza-3-7.md — przed wykonaniem FAZY 4, 5, 6 i 7 (7A obowiązkowo przed zamknięciem audytu).

### 4A — Zakaz cytowania z pamięci

Skan hardkodowanych Dz.U. bez kontekstu weryfikacji = **WARN**.

### 4B — PRAWO-HARDGATE obecny

Brak HARDGATE w routerze = **CRIT**.

---

## FAZA 5 — SCORING

Wynik 0–10 dla każdego skilla wg tabeli kryteriów i wag.

---

## FAZA 6 — RAPORT AUDYTU

Raport wg szablonu z AUDIT-JOURNAL.md (sekcje 1–6, w tym 4C treść merytoryczna).

---

## FAZA 7 — AKTUALIZACJA PLIKÓW REFERENCES ← OBOWIĄZKOWE

### 7A — Aktualizacja AUDIT-JOURNAL.md

Obowiązkowa po każdym audycie; dopisywanie wpisu wg procedury odczytu fragmentu (nie całego dziennika).

Wstawienie wpisu w miejsce N (pełna procedura — references/faza-3-7.md, sekcja 7A):

```bash
python3 - "$J" nowy_wpis.md "$N" <<'PY'
import sys
j, w, n = sys.argv[1], sys.argv[2], int(sys.argv[3])
linie = open(j, encoding="utf-8").read().split("\n")
nowe = open(w, encoding="utf-8").read().rstrip("\n").split("\n") + [""]
assert linie[n - 1].startswith("## AUDYT-"), "linia N nie jest nagłówkiem wpisu"
open(j, "w", encoding="utf-8").write("\n".join(linie[:n - 1] + nowe + linie[n - 1:]))
PY
```

### 7B — Aktualizacja mapa_dzu_YYYY-MM-DD.md

Warunkowa: gdy znaleziono nowe t.j. lub zmiany statusów Dz.U. (nowa generacja mapy, nie kopia archiwalnej).

### 7C — Aktualizacja WARN-OTWARTE.md (ZASADA 10)

Warunkowa: rozdział otwarte/zamknięte WARN.



---

## TRYBY WYWOŁANIA

### TRYB INTERAKTYWNY (menu wyboru) ← DOMYŚLNY
Wywołanie: "przeprowadź audyt" / "audytuj system" (bez zakresu)
→ Faza 0 → Faza 0B (widget menu) → czekaj na wybór → uruchom wybrane fazy.

### TRYB AUTO (pełny audyt)
Wywołanie: "pełny audyt" / "audyt kompletny"
→ Wykonaj Fazy 0–7 w całości.

### TRYB TARGETED (wybrany skill)
Wywołanie: "audytuj [nazwa-skilla]"
→ Faza 0 + Fazy 1–5 tylko dla wskazanego skilla + Faza 6 (skrócony raport) + Faza 7A.

### TRYB CZYSTOŚĆ (tylko interlinie + wstawki + description)
Wywołanie: "wyczyść skille" / "usuń zbędne interlinie" / "usuń wstawki opisowe" / "sprawdź description"
→ Faza 0 → Fazy 2C + 2D-1 + 2D-2 (lub podzbiór) → Faza 6 (skrócony) → Faza 7A.

### TRYB DZU (tylko mapa Dz.U.)
Wywołanie: "sprawdź mapę Dz.U." / "aktualizuj Dz.U."
→ Faza 0 + Faza 3 (A+B+C+D) + Faza 3E (automatycznie, jeśli 3A–3D wykryły zmianę) + Faza 7A + 7B.

### TRYB TREŚĆ (tylko weryfikacja merytoryczna modułów)
Wywołanie: "sprawdź czy moduł X wymaga aktualizacji po zmianie Y" / "zweryfikuj treść modułów po nowelizacji"
→ Faza 0 → Faza 3E bezpośrednio (pomija 3A–3D, wskazany akt/moduł podany przez użytkownika lub ostatni wpis MONITORING/mapa_dzu) → Faza 6 (skrócony, sekcja 4C) → Faza 7A.

### TRYB HARMONOGRAM (pozycja 11 — zadanie cykliczne w Cowork)
Wywołanie: "ustaw cotygodniowy audyt" / "zadanie cykliczne ISAP" / wybór pozycji 11 w menu
→ FAZA 0C → `references/SCHEDULED-TASK-COWORK.md` (bez uruchamiania faz audytowych)

### TRYB KONTRAKT ROUTERA (pozycja 13 — kontrola, bez zapisu)
Wywołanie: „zsynchronizuj pamięć routera” / wybór pozycji 13 w menu
→ FAZA 0D → `references/PAMIEC-TRWALA-ROUTER.md`

### TRYB WARN-CLOSE (zamknięcie ostrzeżeń)
Wywołanie: "zamknij otwarte warningi" / "sprawdź WARN-X"
→ Faza 0 → odczytaj otwarte flagi z `references/WARN-OTWARTE.md` (NIE grepuj
całego AUDIT-JOURNAL.md — to jest wolniejsze i mniej niezawodne, patrz
ZASADA 10) → weryfikacja online → Faza 7A → po zamknięciu: usuń wiersz
z WARN-OTWARTE.md, dodaj pełny wpis do AUDIT-JOURNAL.md.

---

## ZASADY KRYTYCZNE

1. **Nigdy nie cytuj przepisów ani sygnatur z pamięci** — weryfikacja tylko przez ELI (RZĄD 1) i oficjalne źródła orzeczeń.
2. **Każdy audyt kończy się aktualizacją AUDIT-JOURNAL.md** — bez wyjątków.
3. **Mapa Dz.U. aktualizowana tylko gdy potwierdzone zmiany online** — nie spekuluj.
4. **CRIT blokuje skill** — nie używaj skilla z otwartym CRIT.
5. **WARN nie blokuje** — ale musi być odnotowany w `references/WARN-OTWARTE.md`
   (nie tylko w AUDIT-JOURNAL.md) i zamknięty w przyszłym audycie (patrz ZASADA 10).
6. **Moduły czystości (interlinie, wstawki) działają zachowawczo** — w razie wątpliwości ZOSTAW, nie usuwaj.
7. ⛔ **ZASADA KOMPLETNOŚCI OUTPUTU (OUTPUT-COMPLETENESS) — NARUSZENIE = CRIT**
   Każda naprawa dostarczana jako kompletny skill (wszystkie pliki i podfoldery).
8. ⛔ **ZASADA WERYFIKACJI NUMERU NIEZALEŻNIE OD NAZWY:** jeśli nazwy aktów różnią się choć trochę, weryfikuj numer w RZĘDZIE 1 (najpierw ELI).
9. ⛔ **ZASADA PRZEGLĄDU OKRESOWEGO WARN:** otwarte WARN przeglądane i ponownie odnotowywane w kolejnych audytach.
10. ⛔ **ZASADA ROZDZIAŁU OTWARTE/ZAMKNIĘTE:** otwarte WARN w osobnym dzienniku `WARN-OTWARTE.md`, zamknięte w aktualnym.
11. ⛔ **ZASADA TREŚĆ-PO-MAPIE:** audyt numeru Dz.U. i audyt treści merytorycznej modułu to dwie różne kontrole (ZASADA 12).
12. ⛔ **ZASADA GRADACJI ŹRÓDEŁ PRZY WERYFIKACJI:** FAZA 3E stosuje `shared/HIERARCHIA-ZRODEL.md` jako metodologię (ZASADA 14).
13. ⛔ **ZASADA LIMITU DŁUGOŚCI MODUŁU:** moduł powyżej 1000 linii MUSI zostać podzielony wg rozdziałów aktu.
14. ⛔ **ZASADA BRAMKI WYJŚCIOWEJ ZGŁOSZENIA (AUDIT-CLAIM-GATE):** skill audytowy stosuje wobec własnych zgłoszeń ten sam kontrakt weryfikacyjny, którego pilnuje u innych.

**WCZYTAJ (obowiązkowo, fail-closed):** view audyt-systemu-v4/references/zasady-i-struktura.md — pełne brzmienie zasad 7–14; ZASADY 7 i 14 (OUTPUT-COMPLETENESS, AUDIT-CLAIM-GATE) MUSZĄ być przeczytane przed wydaniem naprawy lub zgłoszenia wyniku audytu.

---

## STRUKTURA KATALOGU

Drzewo katalogu skilla (przy zmianie liczby plików aktualizuj OBA miejsca: YAML `references:`/`scripts:` i to drzewo; wzorzec luki F-80).

**WCZYTAJ (obowiązkowo, fail-closed):** view audyt-systemu-v4/references/zasady-i-struktura.md — przy zmianie struktury katalogu skilla i przy aktualizacji drzewa plików.

---

*Wersja: 6.231 | Ostatnia aktualizacja: 2026-10-14 (AUDYT-2026-10-14a). Stopkę aktualizuj razem z polem `version`.*
