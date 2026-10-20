# ETAP W3: bramka dopuszczalności pytań

> Plik obowiązkowy przed wygenerowaniem pierwszego pytania W3. Treść przeniesiona dosłownie z SKILL.md (refaktor 2026-10-20); SKILL.md zawiera nagłówki i streszczenia.

## ETAP W3 — PYTANIA

### Cel etapu

Wygenerowanie kompletnego zestawu pytań podzielonych na bloki,
z pełną bramką dla każdego pytania i finalną macierzą.

---

### QUESTION-ADMISSIBILITY-GATE

> ⛔ PIPELINE FPW (FAKT → PODSTAWA PRAWNA → WNIOSEK) — obowiązkowy przed każdym pytaniem.
> Pełna procedura: `view przesluchanie-swiadkow-v2-min90/references/QUESTION-ADMISSIBILITY-GATE.md`

> 🔴 **GATE-DEFAULT-NOW (dodane w audycie 3.6):**
> QUESTION-ADMISSIBILITY-GATE, WHY-GATE i SAFE-Q stosuje się **w momencie
> generowania pierwszej wersji pytań**, nie dopiero gdy użytkownik poprosi
> o ocenę, audyt lub scoring 0-10. Wygenerowanie pytania łamiącego WHY-GATE
> lub zakładającego nieudowodniony fakt, z zamiarem "poprawię jeśli użytkownik
> zapyta" — jest błędem procesu, niezależnie od tego, czy użytkownik
> ostatecznie o ocenę poprosi. Jeśli pytanie nie przechodzi bramki, nie trafia
> do wersji roboczej — trafia od razu do BLOKU E z alternatywą.

> 🔴 **FACT-CROSS-CHECK-GATE (dodane w audycie 3.7):**
> FPW-1 (FAKT) nie może być zaakceptowany na podstawie samego brzmienia
> pytania — musi zostać **zestawiony z faktyczną treścią źródłowego
> dokumentu**, jeśli dokument ten jest dostępny w rozmowie. Dotyczy to
> zwłaszcza pytań formułujących twierdzenie negatywne o dokumencie
> ("dokument nie zawiera X", "brak w nim Y") — takie twierdzenie wymaga
> aktywnego sprawdzenia treści dokumentu przed akceptacją pytania, nie
> tylko przyjęcia go na wiarę, bo łatwo o nieścisłość, którą świadek lub
> pełnomocnik przeciwnej strony obnaży na sali (np. dokument faktycznie
> zawiera jedną, ogólną datę i ogólnikowy opis, więc twierdzenie
> "nie zawiera dat i opisu" jest fałszywe, mimo że intencja pytania —
> wykazanie niewystarczającej konkretności — jest słuszna). Jeśli treść
> dokumentu nie jest dostępna w rozmowie, oznacz FPW-1 jako ⚠️ NIEZWERYFIKOWANE
> i zapytaj użytkownika o dokument, zamiast przyjmować twierdzenie wprost.

> 🔴 **QUOTE-VERIFICATION-DEFAULT (dodane w audycie 3.7):**
> Każdy fragment tekstu przedstawiany jako dosłowny cytat z dokumentu
> (do użycia w pytaniu konfrontacyjnym / technice loopingu) jest
> weryfikowany słowo-w-słowo względem źródła **w momencie jego
> zaproponowania**, nie dopiero gdy użytkownik o to wprost zapyta.
> Wynik weryfikacji (zgodny / zgodny ze skrótem oznaczonym wielokropkiem /
> niezgodny) podaje się przy pytaniu. Cytatu niemożliwego do zweryfikowania
> względem dostępnego źródła nie włącza się do pytania — oznacza się jako
> wymagający weryfikacji przed użyciem.

Każde pytanie musi zawierać:

```
FPW-1 FAKT:   [fakt procesowy + źródło: dok_id/strona/zeznanie/domniemanie]
FPW-2 PRAWO:  [przepis → weryfikacja w ELI (RZĄD 1) → ✅ [VER: ELI DU/RRRR/NNN, data] lub ⚠️ BRAK]
FPW-3 WNIOSEK:→ TAK: [skutek dla tezy] | → NIE: [skutek dla tezy]
              Ryzyko FPW: BEZPIECZNE / RYZYKO-ODPOWIEDŹ / RYZYKO-KONTROLA / RYZYKO-KUMULACJA

PYTANIE:      [treść pytania]
CEL:          [co chcę uzyskać procesowo]
TEZA:         [której tezie z W2 służy]
TYP:          [otwarte / zamknięte / kontrolne / pułapkowe / impeachment]
DOWÓD KON.:   [dowód który potwierdzi lub obali odpowiedź] / [brak → aktywuj SAFE-Q]
RYZYKO:       [podtyp: RYZYKO-KONTROLA / RYZYKO-ODPOWIEDŹ / RYZYKO-KUMULACJA + opis]
DOPUSZCZ.:    [dopuszczalne / ryzykowne / niedopuszczalne + podstawa prawna ✅]
```

**Reguła WHY-GATE (twardy zakaz w trybie cross):**
```
⛔ WHY-GATE — jeśli model = ONE-FACT lub świadek = wrogi/strony przeciwnej:
  Pytania "dlaczego / po co / w jakim celu / jak to możliwe" są ZAKAZANE.
  Klasyfikacja: RYZYKO-KONTROLA → automatyczny BLOK E.
  Wyjątek: świadek lojalny w modelu PEACE lub LEJEK — dopuszczalne.
```

**Reguła SAFE-Q (brak dowodu kontrolnego):**
```
Jeśli DOWÓD KON. = brak:
  → Przeformułuj pytanie tak, by obie odpowiedzi (TAK i NIE) były
    procesowo użyteczne lub neutralne.
  → Jeśli przeformułowanie niemożliwe → pytanie do BLOKU E.
  → Nie zadawaj pytania bez dowodu kontrolnego do BLOKU D (impeachment).
```

**Reguła FPW-RISK:**
```
Jeśli FPW-3 wskazuje, że odpowiedź NIE jest aktywnie szkodliwa dla tezy
→ pytanie automatycznie BLOK E (ryzykowne).
Podtyp RYZYKO-ODPOWIEDŹ.
```

**Podstawy prawne dopuszczalności — weryfikuj przez HARDGATE, nie z pamięci:**

```
⛔ HARDGATE — przed podaniem jakiejkolwiek podstawy prawnej:
  view shared/PRAWO-HARDGATE.md

Podstawy wymagające weryfikacji online (przykłady — nie wyczerpująca lista):
  KPC: pytania sugestywne (art. 271), zakaz zeznań co do faktów objętych tajemnicą
       (art. 261), zakaz zeznań małżonka i bliskich (art. 261 §1)
  KPK: zakaz dowodowy (art. 168a, 174, 178, 199), prawo do odmowy zeznań (art. 182),
       zwolnienie z zachowania tajemnicy (art. 180), konfrontacja (art. 172)
  KPW: odpowiednie stosowanie KPK (art. 39, 41)
  KPA: zeznania w postępowaniu administracyjnym (art. 83, 86)

Dla każdej powołanej podstawy → odczyt z ELI (RZĄD 1) → oznacz ✅ [VER: ELI DU/RRRR/NNN, data]
```

**Pełna logika klasyfikacji pytań:**
`view przesluchanie-swiadkow-v2-min90/references/QUESTION-ADMISSIBILITY-GATE.md`

---
