# HARD GATE MRG, STEP-DISCLOSURE i CG-GATE — pełna treść

## ⛔⛔⛔ HARD GATE MRG — MANDATORY-REREAD-GATE ⛔⛔⛔

> Ten blok jest WIĄŻĄCY i NADRZĘDNY wobec „pamięci" modelu o treści plików
> oraz wobec chęci szybkiego dostarczenia pisma.
> Powstał po sprawie [SYGN-SPRAWY]: brak ponownego wczytania = brak wiedzy o krokach.
> Cel: przed każdym krokiem [CP] i przed każdą odpowiedzią w pipeline pisma
> stan checkpointów oraz rejestr kroków są odczytywane ze ŚWIEŻEJ wersji z dysku —
> nigdy z pamięci modelu, która może zawierać poprzednią wersję pliku.

```
⛔ MRG-GATE — AKTYWNY OD KROK 0 DO present_files, BEZ WYJĄTKÓW

REGUŁA MRG: Przed KAŻDĄ odpowiedzią w pipeline pisma procesowego ORAZ
przed KAŻDYM krokiem oznaczonym [CP], model MUSI wykonać OBA wywołania:
  1. view shared/CP-GATE.md
  2. view shared/MOD-STEP-TRACKER.md
Następnie zaktualizować CP-REJESTR (§2 CP-GATE.md) oraz REJESTR KROKÓW
(FAZA 0 MOD-STEP-TRACKER) WYŁĄCZNIE na podstawie ŚWIEŻO odczytanej treści.

⛔ Wywołanie view() jest OBOWIĄZKOWE nawet jeśli:
  • pliki były już wczytane wcześniej w tej samej sesji,
  • model „pamięta" ich treść,
  • użytkownik nie prosił o odczyt,
  • jest to „prosty" krok pośredni,
  • plik „nie zmieniał się" od ostatniego odczytu.

⛔ ZAKAZY MRG (bezwzględne):
  • ZAKAZ polegania na pamięci modelu zamiast wywołania view().
  • ZAKAZ pominięcia odczytu „bo to ten sam plik co poprzednio".
  • ZAKAZ pominięcia odczytu gdy plik „nie zmieniał się" od ostatniego razu.
  • ZAKAZ zamknięcia jakiegokolwiek [CP] bez uprzedniego podwójnego view().
  • ZAKAZ wpisania do pisma jakiejkolwiek treści checkpointu/rejestru
    odtworzonej z pamięci zamiast z bieżącego odczytu.

UZASADNIENIE (dlaczego tylko view() gwarantuje poprawność):
  • Pliki mogą być aktualizowane między odpowiedziami.
  • Pamięć modelu może zawierać poprzednią wersję pliku.
  • Jedynie view() gwarantuje odczyt aktualnej wersji z dysku.

⛔ AUTODIAGNOZA MRG (przed każdym raportem [CP] i przed present_files):
  Zadaj sobie 1 pytanie: „Czy w TEJ odpowiedzi wywołałem view() na OBU
  plikach (CP-GATE.md + MOD-STEP-TRACKER.md) przed bieżącym [CP]?"
  Jeśli NIE → NIE zamykaj [CP], NIE wywołuj present_files — najpierw OBA view().
```

> Reguła interpretacyjna MRG: „ponowne wczytanie" = fizyczne wywołanie
> narzędzia view() w bieżącej odpowiedzi. Nie jest nim odtworzenie treści
> z pamięci ani odwołanie się do wcześniejszego wczytania w historii rozmowy.
> Lista pozycji [CP] objętych regułą = pełny CP-REJESTR (§2 CP-GATE.md):
> CP-1a, CP-1b, CP-1c-*, CP-PD, CP-1d-*, CP-W1, CP-PRE-W2, CP-ATAK,
> CP-PODMIOT, CP-QUALITY, CP-AUDYT, CP-PEER.

## ⛔⛔⛔ HARD GATE STEP-DISCLOSURE — INFORMACJA WARUNKOWA ⛔⛔⛔

> Ten blok jest WIĄŻĄCY i NADRZĘDNY wobec chęci szybkiego dostarczenia pisma.
> Powstał po sprawie [SYGN-SPRAWY] (2026-06-24), w której pismo zostało wydane
> z pominięciem kilkunastu kroków kontroli jakości — BEZ poinformowania użytkownika.
> Cel: każde pominięcie lub krok jeszcze-do-zrobienia MUSI być ujawniony, zanim
> użytkownik dostanie plik. Żaden krok nie może zostać „cicho" przeskoczony.

```
⛔ SD-GATE — AKTYWNY OD STARTU DO present_files, BEZ WYJĄTKÓW

KROK A — ST-INIT (na starcie, raz):
  view shared/MOD-STEP-TRACKER.md → zainicjuj REJESTR kroków.
  Każdy krok pipeline = jeden wpis ze statusem: ○ OCZEKUJE.

KROK B — ST-TRACK (w trakcie):
  Po każdym kroku ustaw status:
    ✅ WYKONANY  |  ⚠️ POMINIĘTY (+powód)  |  — N/A (+uzasadnienie)
  N/A musi być uzasadnione (np. „brak dowodów pośrednich" dla MOD-LANCUCH).

KROK C — ST-FINAL (OBOWIĄZKOWY i BLOKUJĄCY przed KAŻDYM present_files pisma):
  Wyświetl PEŁNY REJESTR KROKÓW (format FAZA 3 z MOD-STEP-TRACKER):
  kroki ✅ wykonane | ⚠️ pominięte (+powód) | ○ oczekujące | — N/A | STATUS PISMA.

⛔ INFORMACJA WARUNKOWA (sedno bramki):
  Policz kroki WYMAGANE, których status ≠ ✅ WYKONANY i ≠ — N/A
  (tj. wszystkie ⚠️ POMINIĘTY oraz ○ OCZEKUJE).

  • Jeśli liczba = 0:
       STATUS PISMA = ✅ FINAL — GOTOWE DO ZŁOŻENIA.
       Dozwolone present_files bez dalszych pytań.
       Tryb PRAWNIK/kancelaria lub żądanie użytkownika → po present_files:
       `view modules/MOD-AUDIT-BUNDLE.md` (paczka audytowa AI Act art. 12 —
       deliverable dla audytora, nigdy dla sądu ani kontrahenta).

  • Jeśli liczba ≥ 1  →  WARUNEK SPEŁNIONY → URUCHOM INFORMACJĘ WARUNKOWĄ:
       1) STATUS PISMA = ⚠️ DRAFT — NIEZWERYFIKOWANY (X krok(ów) pominięto/do zrobienia).
       2) .docx MUSI nosić wzmocniony watermark „DRAFT — NIEZWERYFIKOWANY"
          (zgodnie z CP-GATE; brak watermarku = błąd krytyczny).
       3) Wyświetl blok ujawnienia:

          ┌─────────────────────────────────────────────────────────────┐
          │ ⚠️ INFORMACJA WARUNKOWA — PISMO NIEPEŁNE                      │
          │                                                             │
          │ Kroki pominięte lub jeszcze do wykonania:                   │
          │  ⚠️/○ [ID] [nazwa] — [powód / co to weryfikuje]            │
          │  ...                                                        │
          │                                                             │
          │ Skutek dla jakości pisma:                                   │
          │  → [czego nie sprawdzono / jakie ryzyko procesowe]          │
          │                                                             │
          │ Decyzja:                                                    │
          │  a) Akceptuję pismo jako DRAFT (bez tych kroków)            │
          │  b) Wykonaj brakujące kroki przed dostarczeniem (zalecane)  │
          └─────────────────────────────────────────────────────────────┘

       4) ⛔ ZAKOŃCZ ODPOWIEDŹ. Czekaj na decyzję a/b.
          - „a"/„tak"  → present_files z plikiem DRAFT — NIEZWERYFIKOWANY.
          - „b"/„nie" → wykonaj brakujące kroki, potem ponów ST-FINAL.

⛔ ZAKAZ-14 (bezwzględny):
  • ZAKAZ present_files jakiegokolwiek pisma BEZ uprzedniego ST-FINAL.
  • ZAKAZ statusu ✅ FINAL, gdy istnieje choćby jeden krok ⚠️ POMINIĘTY lub ○ OCZEKUJE.
  • ZAKAZ „cichego" przeskoku — pominięcie BEZ ujawnienia = błąd krytyczny pipeline.
  • Polecenie „dalej"/„kontynuuj"/„generuj" NIE zwalnia z ST-FINAL ani z INFORMACJI WARUNKOWEJ.

⛔ AUTODIAGNOZA KOŃCOWA (wykonaj tuż przed present_files, nawet jeśli „wydaje się gotowe"):
  Zadaj sobie 1 pytanie: „Czy wyświetliłem REJESTR KROKÓW (ST-FINAL) w tej odpowiedzi?"
  Jeśli NIE → NIE wywołuj present_files. Najpierw ST-FINAL.
```

> Reguła interpretacyjna: „informacja warunkowa" = informacja, której wyświetlenie
> jest WARUNKOWANE istnieniem ≥1 kroku pominiętego/oczekującego. Warunek spełniony →
> informacja OBOWIĄZKOWA + STOP. Warunek niespełniony → pismo FINAL, bez pytań.

## ⛔⛔⛔ HARD GATE WARUNKOWY — AKCEPTACJA STARTU + WCZYTANIE CHECKLISTY ⛔⛔⛔

> Ten blok wykonuje się JEDNORAZOWO — na samym początku każdej sesji z tym skillem,
> przed jakimkolwiek działaniem merytorycznym (przed Test A / Test B / Test C).
> Jest WIĄŻĄCY i nie może być pominięty nawet gdy użytkownik podał już wszystkie dane.
>
> Cel: użytkownik ZAWSZE wie, że (a) pipeline ma wiele etapów, (b) nie wszystkie
> mogły zostać wykonane w przeszłości lub mogą zostać pominięte w tej sesji,
> (c) każde pominięcie będzie jawne — nigdy ciche.

```
⛔ CG-GATE (CONDITIONAL GATE) — WYKONAJ JAKO ABSOLUTNIE PIERWSZY KROK

KROK CG-1 — INFORMACJA WSTĘPNA (wyświetl użytkownikowi przed startem):

  ┌─────────────────────────────────────────────────────────────────────────┐
  │ ⚠️ INFORMACJA PRZED STARTEM — PISMA PROCESOWE v3                        │
  │                                                                         │
  │ Ten skill realizuje wieloetapowy pipeline kancelaryjny (W1 → W2 → W3)  │
  │ z kilkunastoma obowiązkowymi krokami kontroli jakości.                  │
  │                                                                         │
  │ Ważne zastrzeżenie:                                                     │
  │  → Nie wszystkie kroki pipeline'u mogły zostać wykonane w poprzednich  │
  │    sesjach dotyczących tej sprawy.                                      │
  │  → W tej sesji każde pominięcie kroku będzie jawnie zgłoszone         │
  │    (INFORMACJA WARUNKOWA) — nigdy ciche.                               │
  │  → Jeśli pominięto kroki wcześniej i sprawa jest kontynuowana,        │
  │    zaleca się poinformowanie o tym fakcie teraz.                       │
  │                                                                         │
  │ Po Twojej akceptacji wczytam pełną listę kroków i checklistę,          │
  │ a następnie przystąpię do pracy.                                        │
  │                                                                         │
  │ Czy akceptujesz powyższe warunki i chcesz kontynuować?                 │
  │  a) Tak, akceptuję — wczytaj checklistę i rozpocznij                   │
  │  b) Nie — zakończ lub wyjaśnij wątpliwości                             │
  └─────────────────────────────────────────────────────────────────────────┘

  ⛔ ZAKOŃCZ ODPOWIEDŹ PO WYŚWIETLENIU CG-1. Czekaj na decyzję a/b.
  ⛔ NIE wykonuj żadnego kroku merytorycznego przed akceptacją.

KROK CG-2 — PO OTRZYMANIU AKCEPTACJI „a" (WCZYTANIE CHECKLISTY):

  Wykonaj WSZYSTKIE poniższe view() w podanej kolejności:

  1. view pisma-procesowe-v3/references/AUTOMAT-STANOW.md
     → Zawiera: PROTOKÓŁ CHECKPOINT, AUTOMAT STANÓW (STAN 0–3 z KROK 0-TRACKER),
       MAPA CHECKPOINTÓW, ZAKAZY 1–13, REGUŁA NAPRAWY, REGUŁA-KONTYNUACJA,
       REGUŁA AUTODIAGNOZY.

  2. view pisma-procesowe-v3/references/SELF-CHECK-PISMA.md
     → Zawiera: SELF-CHECK przed każdą odpowiedzią (pełna checklista CP),
       REGUŁA FINALNA (11 pytań).

  3. view pisma-procesowe-v3/references/MODULY-MAPA.md
     → Zawiera: matryca engines per etap, pliki kanoniczne shared z triggerami.

  Po wczytaniu — wyświetl użytkownikowi REJESTR KROKÓW (format ST-INIT):

  ┌─────────────────────────────────────────────────────────────────────────┐
  │ ✅ CHECKLIST WCZYTANA — PIPELINE AKTYWNY                                │
  │                                                                         │
  │ Kroki pipeline (status startowy):                                       │
  │  ○ KROK 0: CP-GATE + STEP-TRACKER (inicjalizacja)                      │
  │  ○ Test A / Test B / Test C (routing)                                   │
  │  ○ W1: CLAIM-VALIDATION [CP-1a]                                         │
  │  ○ W1: MOD-STRATEGIA-WYBOR [CP-1b] (gdy ≥2 ścieżki)                   │
  │  ○ W1: SKAN DOWODÓW / MACIERZ / ŁAŃCUCH [CP-1c-*]                     │
  │  ○ W1: MOD-DOKUMENT-ANOMALIE / MOD-POSZLAKI [CP-1d-*]                  │
  │  ○ W1: RAMA + STRATEGIA [CP-W1]                                         │
  │  ○ PRE-W2-GATE [CP-PRE-W2]                                              │
  │  ○ W2: PROJEKT PISMA + ATAK-NA-DRAFT [CP-ATAK]                         │
  │  ○ W3: PODMIOT-GATE [CP-PODMIOT]                                        │
  │  ○ W3: WERYFIKACJA + WALIDACJA [CP-QUALITY]                             │
  │  ○ W3: AUDYT-KOŃCOWY [CP-AUDYT]                                         │
  │  ○ W3: PEER-REVIEW + POST-VALIDATION [CP-PEER]                          │
  │                                                                         │
  │ Zastrzeżenie: nie wszystkie kroki muszą być wymagane w Twojej sprawie  │
  │ (N/A z uzasadnieniem). Każde pominięcie będzie jawnie zgłoszone.       │
  │                                                                         │
  │ Teraz przystępuję do KROKU 0 — routing.                                │
  └─────────────────────────────────────────────────────────────────────────┘

  Następnie wykonaj KROK 0 (CP-GATE → STEP-TRACKER → routing Test A/B/C).

⛔ ZAKAZ-15 (bezwzględny — nowy):
  • ZAKAZ pominięcia CG-GATE na starcie sesji.
  • ZAKAZ rozpoczęcia jakiegokolwiek kroku merytorycznego bez akceptacji „a".
  • ZAKAZ wczytania checklisty bez wyświetlenia najpierw bloku INFORMACJA WSTĘPNA.
  • Polecenie „zacznij pismo" / „pisz" / „generuj od razu" NIE zwalnia z CG-GATE.
```

> Wyjątek od CG-GATE: gdy użytkownik w tej samej wiadomości co trigger pisma
> explicite napisał „pomijam informację wstępną, znam pipeline" lub podobny
> jednoznaczny sygnał świadomości — CG-1 można zastąpić jednolinijkowym
> potwierdzeniem wczytania checklisty i natychmiast wykonać CG-2.
> Bez takiego sygnału: zawsze pełny CG-1 + czekanie na odpowiedź.
