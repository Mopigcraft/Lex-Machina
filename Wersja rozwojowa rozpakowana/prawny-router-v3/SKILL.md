---
name: prawny-router-v3
version: "3.71"
type: orchestration
status: production
entrypoint: SKILL.md
compatibility: "web_search, web_fetch, file_read (view), create_file, show_widget — lub równoważne funkcje hosta wg shared/UNIVERSAL-RUNTIME-ADAPTER.md"
description: "UŻYWAJ ZAWSZE, gdy użytkownik prosi o analizę prawną, pismo lub ocenę materiału prawnego, w każdej jurysdykcji. Nie przy wzmiankach prawnych w pracy nad kodem (licencje, RODO)."
dependencies:
  requires:
    - shared
    - prawo-polskie-v2
    - przewodnik-prawny-v2
    - audyt-systemu-v4
    - orzeczenia-sadowe-v2
    - analizator-przepisow-v2
    - analizator-umow-v1
    - analizator-dowodow-v3
    - analiza-sadowa-v6
    - pisma-proste-v2
    - pisma-procesowe-v3
    - przesluchanie-swiadkow-v2-min90
    - chronologia-sprawy-v1
    - raport-sytuacyjny-v2
    - raport-klienta-v1
    - dr-01-ustroj-konstytucyjny-i-zrodla-prawa
    - dr-02-prawo-cywilne-rodzinne-gospodarcze
    - dr-03-prawo-karne-wykroczenia-egzekucja
    - dr-04-prawo-pracy-zus-swiadczenia
    - dr-05-prawo-administracyjne-sadowoadministracyjne
    - dr-06-podatki-finanse-publiczne-aml
    - dr-07-zamowienia-publiczne-fundusze-ue
    - dr-08-samorzad-terytorialny-prawo-lokalne
    - dr-09-budownictwo-srodowisko-energia-transport
    - dr-10-zdrowie-farmacja-zywnosc-rolnictwo
    - dr-11-cyfrowe-cyber-ai-dane-ip
    - dr-12-sadownictwo-prokuratura-zawody-prawnicze
    - dr-13-sluzby-bezpieczenstwo-informacje-niejawne
    - dr-14-prawo-ue-miedzynarodowe-prawa-czlowieka
    - dr-15-compliance-iso-governance-audyt
    - dr-16-pisma-strategia-dowody-orzecznictwo
  called_by:
    - użytkownik (punkt wejścia — brak nadrzędnego skilla)
required_modules: [shared/MCP-INTEGRACJA.md, shared/PRAWO-HARDGATE.md, shared/HIERARCHIA-ZRODEL.md, shared/DOSTEP-MASZYNOWY-API.md,
  shared/PORTALE-BRANZOWE-RZAD-2B.md, shared/MOD-STEP-TRACKER.md, shared/MOD-REJESTR-POKRYCIA-JEDNOSTEK.md,
  shared/MOD-KONTEKST-SESJI.md, shared/MOD-OS-CZASU-PRZESLANEK.md, shared/MOD-WYJATEK-GATE.md,
  shared/MOD-SKAN-DOWODOW-KOMPLETNY.md, shared/MOD-REJESTR-ZALACZNIKOW-CHECKPOINT.md, shared/MOD-PORCJOWANIE-DOWODOW.md,
  shared/PRE-W2-VERIFICATION-GATE.md, shared/CP-GATE.md, shared/DISCLAIMER.md, references/KROK0A-anonimizer.md,
  references/KROK1-detekcja.md, shared/TABELE-OPLAT.md, references/PROFIL-LEKKI.md, references/ZRODLA-AKTOW-FALLBACK.md,
  dr-16-pisma-strategia-dowody-orzecznictwo/modules/mod-narzedzie-kontroler-kompletnosci.md,
  references/AUDYT-KLUCZA-ODPOWIEDZI.md, shared/MOD-CN-GATE.md, shared/MOD-REM-GATE.md,
  dr-03-prawo-karne-wykroczenia-egzekucja/modules/mod-KK-kwalifikator-karnomaterialny.md]
---

## ŁADOWANE ZAWSZE — BEZWZGLĘDNIE

W każdej sprawie prawnej, przed analizą:

1. `view shared/PRAWO-HARDGATE.md` — świeża weryfikacja każdego powołania w tej turze.
2. `view references/KROK0A-anonimizer.md` — zamknij bramkę anonimizera.
3. `view references/KROK1-detekcja.md` — ustal tryb i jurysdykcję.
   Gdy w tej turze użytkownik dostarczył dokument, akta, korespondencję lub wklejony
   tekst: `view shared/MOD-WEJSCIE-DOKUMENTU.md` — WD-1 przed analizą, WD-2 przy każdym
   cytacie z materiału, WD-3 przed wynikiem (F-200; treści reguł nie kopiuje się — T35).
4. Wykonaj routing [1]–[11], wczytaj PRIMARY i wypisz ślad KROKU 3A.
5. Przy pierwszym URL: `view shared/HIERARCHIA-ZRODEL.md`; każdy URL musi mieć RZĄD 1/2A/2B/3.
   Dla aktów polskich wykonaj też `view references/ZRODLA-AKTOW-FALLBACK.md`.
6. Przed wysłaniem: `view references/SELF-CHECK.md` i wykonaj inwentarz VER-GRAIN.
7. Ostatnim elementem odpowiedzi prawnej musi być disclaimer z `shared/DISCLAIMER.md`.

⛔ **KOLEJNOŚĆ ODCZYTU — `view references/PROFIL-LEKKI.md`.** Rdzeń R-1…R-5
(ten plik, KROK 0A, KROK 1, PRAWO-HARDGATE, SELF-CHECK) jest nieredukowalny.
Pozostałe zasoby `required_modules` czyta się na wyzwalacz mechaniczny, najpóźniej
przed pierwszą czynnością, którą regulują. Odroczenie odczytu NIE jest pominięciem
bramki i NIE zwalnia z żadnej reguły — profil zmienia moment `view`, nigdy zakres
kontroli. Profil deklaruje się w bloku KROKU 3A.

Brak obowiązkowego odczytu lub źródła → `⛔ TRYB ZDEGRADOWANY` i jawne
`⚠️ [NIEWERYFIKOWANE]`; zakaz cichego użycia pamięci modelu.

## ADAPTER RUNTIME

Zastosuj `shared/UNIVERSAL-RUNTIME-ADAPTER.md`. Nazwy `view`, `web_search`,
`web_fetch`, `show_widget`, `create_file` i `present_files` oznaczają równoważne
operacje hosta. Odczyty `shared/...`, `references/...` i `<skill>/...` dotyczą
odpowiednich zainstalowanych skilli; nie kopiuj zależności do routera.

<!-- lex:wykonuje-aplikacja: RESOLVER -->
### PATH-SELFTEST — RESOLVER (od 3.57)

Skille mogą być zainstalowane jako pluginy z marketplace (claude.ai/Cowork:
`/mnt/skills/plugins/<plugin>:<skill>/`; Claude Code: `~/.claude/plugins/cache/…`),
jako skille wgrane (`/mnt/skills/user/<skill>/`) albo w obu formach naraz. Ścieżki
w plikach systemu są **adresami logicznymi** — nie odczytuj ich dosłownie.

1. **Bootstrap `shared`** — przed pierwszym `view shared/...`, gdy host ma powłokę:
   ```bash
   for d in /mnt/skills/*/shared /mnt/skills/*/*:shared "$HOME"/.claude/plugins/cache/*/shared/*; do
     [ -f "$d/SKILL.md" ] && printf '%s\t%s\n' "$(sed -n 's/^version: *"\{0,1\}\([0-9.]*\).*/\1/p' "$d/SKILL.md" | head -n 1)" "$d"
   done | sort -t "$(printf '\t')" -k1,1Vr
   ```
   Pierwsza pozycja = `shared` na tę sesję. Bez powłoki — wylistuj te katalogi
   narzędziem odczytu i porównaj `version:`.
2. Z wybranej kopii `view shared/UNIVERSAL-RUNTIME-ADAPTER.md` i stosuj **§1A
   RESOLVER-SKILLI** (R-1…R-5) do każdego kolejnego skilla: najwyższa wersja, przy
   remisie kopia z pluginu, jedna kopia na skill przez całą sesję, zakaz łączenia plików
   z dwóch kopii.
3. Dwie kopie o różnych wersjach → `⚠️ DUPLIKAT SKILLA` w KROKU 3A i jedno zdanie dla
   użytkownika na sesję: starą instalację należy usunąć.
4. Brak kopii albo ponowny błąd odczytu → `⛔ TRYB ZDEGRADOWANY — zasoby skilla
   niedostępne`; podaj zasób, sprawdzone lokalizacje i błąd, a każdą treść prawną
   oznacz `⚠️ [NIEWERYFIKOWANE]`.

Zapamiętaj mapę `skill → katalog` na sesję. Nazwa skilla w odwołaniu musi występować
w `dependencies.requires`; w przeciwnym razie zgłoś błąd ścieżki.

---

## ESKALACJE I OGRANICZENIA (przeniesione z frontmattera)

**WCZYTAJ (obowiązkowo, fail-closed):** `view prawny-router-v3/references/ESKALACJE-I-METADANE.md` — ZANIM orzekniesz o niedostępności jakiegokolwiek źródła, przy braku dostępu do rejestru (KRS/CEIDG), sprawie transgranicznej i weryfikacji rachunku kontrahenta (zawiera też `inputs`, `outputs`, `limitations`, `required_modules` z komentarzami).

- ⛔ Przed orzeczeniem o niedostępności źródła w kanale kodu: kształt żądania wg `shared/DOSTEP-MASZYNOWY-API.md` §1.
- Brak tekstu aktu z ISAP to stan normalny: ELI (api.sejm.gov.pl/eli, eli.gov.pl); dalej `references/ZRODLA-AKTOW-FALLBACK.md`.
- Brak źródła po wyczerpaniu alternatyw → `⚠️ [NIEWERYFIKOWANE]` i informacja dla użytkownika, bez cichej kontynuacji.
- Sprawa transgraniczna → weryfikacja NIE jest pomijana (UP-5). Brak klasyfikacji → [7] FALLBACK.
- Podmiot ⬛ bez dostępu do rejestru → STOP; ZAKAZ pisma z podmiotem ⬛. Biała lista VAT: maszynowo osiągalna (`shared/DOSTEP-MASZYNOWY-API.md` §4).
- Nie zastępuje porady radcy/adwokata (`shared/DISCLAIMER.md`, KROK 7 obowiązkowy).


# Router Prawny v3 — Spis Treści i Sekwencja Główna

## PREFERENCJE UŻYTKOWNIKA (aktywne w całej sprawie prawnej obsługiwanej przez router)

UP-1…UP-6 obowiązują od wczytania routera do końca sprawy prawnej — nie w rozmowach
bez sprawy prawnej (np. praca nad kodem z wzmianką o licencji lub RODO).

```
UP-1: router→v3 ZAWSZE pierwszy (przed jakimkolwiek skillem dziedzinowym) — każda jurysdykcja
UP-2: ELI PIERWSZY — kanon E-1…E-5 (shared/HIERARCHIA-ZRODEL.md):
      E-1 ELI (api.sejm.gov.pl/eli kanałem kodu → eli.gov.pl) — brzmienie, t.j., status;
      E-2 ISAP — wyłącznie adres dla człowieka i pomocnicza identyfikacja;
      E-3 LEX / Legalis → E-4 ArsLege — gdy aktu nie da się pobrać z RZĘDU 1
          (ELI ani ISAP: awaria serwera, timeout, blokada) — wtedy obowiązkowo;
      E-5 ⚠️ [NIEWERYFIKOWANE]. Szczegóły: references/ZRODLA-AKTOW-FALLBACK.md.
      Weryfikuj KAŻDE powołanie online; nigdy z pamięci.
UP-3: Sprawy karne → KROK1-detekcja.md kieruje do dr-03; kwalifikacja przez
         view dr-03-prawo-karne-wykroczenia-egzekucja/modules/mod-KK-kwalifikator-karnomaterialny.md
UP-4: HYBRID-VALIDATION przed każdym .docx
UP-5: Zagraniczne → pomiń prawo-polskie-v2 + ISAP; wczytaj
         shared/MIEDZYNARODOWE-GATES.md + shared/HIERARCHIA-ZRODEL-MIEDZYNARODOWE.md;
         PODMIANA BRAMEK: OŚ-GATE→MG-1 (ratyfikacja i zakres), WYJ-GATE→MG-2
         (wykładnia KWPT art. 31-33). ⛔ CN-GATE i REM-GATE NIE są podmieniane —
         działają w obu ścieżkach. Kanał: bash/curl DZIAŁA dla eur-lex.europa.eu
         i legal.un.org (zmierzone 2026-09-05, korekta F-162 — poprzednie brzmienie
         „NIE bash/curl" było fałszywe); dla unoosa/cites/icsid/uncitral
         web_search→web_fetch. Tabela kanałów: HIERARCHIA-ZRODEL-MIEDZYNARODOWE.md §2
UP-6: KAŻDA sprawa → CN-GATE przed analizą (shared/MOD-CN-GATE.md) i REM-GATE
         przed oddaniem (shared/MOD-REM-GATE.md). Bez podmiany, bez wyjątku
         jurysdykcyjnego
```

## SEKWENCJA GŁÓWNA

```
KROK 0  → Wczytaj ten plik → ⛔ HG-ACTIVE (blok powyżej) — potwierdź przed kontynuacją
KROK 0-ST → ⛔ [ST-INIT — STEP-TRACKER] (zaraz po HG-ACTIVE, przed jakimkolwiek krokiem):
          view shared/MOD-STEP-TRACKER.md → zainicjuj REJESTR kroków
          (FAZA 0). REJESTR aktywny przez całą sesję — niezależnie od tego, czy później
          zostanie wczytany skill dziedzinowy (np. pisma-procesowe-v3).
          ⛔ ST-FINAL (FAZA 3 MOD-STEP-TRACKER) jest BEZWZGLĘDNIE BLOKUJĄCY przed KAŻDYM
          present_files pisma/.docx — także gdy pismo generowane jest bezpośrednio z routera
          bez pełnego pipeline pisma-procesowe-v3. Polecenia „dalej"/„kontynuuj"/„generuj"
          NIE zwalniają z ST-FINAL ani z obowiązku raportowania pominięć (FAZA 2).
KROK 0-RPK → Gdy zakres obejmuje ≥10 ponumerowanych jednostek albo pracę
          partiami nad wyliczoną listą: view shared/MOD-REJESTR-POKRYCIA-JEDNOSTEK.md
          i wykonaj RPK-INIT/RPK-COMMIT/RPK-RESUME zgodnie z modułem.
KROK 0A → [ANONIMIZER] → view references/KROK0A-anonimizer.md
KROK 0B → [KONTEKST SESJI] → wykryj czy użytkownik wkleił/wgrał plik
          kontekstu (# KONTEKST SESJI...) lub czy napisał "masz kontekst" /
          "wczytaj sesję" / "plik z poprzedniej sesji" — jeśli TAK:
          view shared/MOD-KONTEKST-SESJI.md → wykonaj
          TRYB IMPORT (§4). IMPORT_AKTYWNY = true dla tej sesji.
          Jeśli NIE — pomiń, kontynuuj do KROK 1.
KROK 0C → Gdy są pliki lub wzmianka o załącznikach: najpierw view
          shared/MOD-SKAN-DOWODOW-KOMPLETNY.md i wykonaj pełny SD-VER.
          Po raporcie SD-VER zakończ turę. Dla dużych materiałów wykonaj też
          shared/MOD-PORCJOWANIE-DOWODOW.md; jego STOP/checkpointy są blokujące.
KROK 0D → [STATUS PODMIOTÓW — OZNACZENIE ⬛] → obowiązkowy gdy w materiałach widoczne
          dane podmiotów (spółki, organy, sądy, fundusze):
          ⛔ Każdy podmiot niebędący osobą prywatną = natychmiast ⬛ [DO WERYFIKACJI]
          ⛔ Status ⬛ utrzymuje się aż do faktycznego web_search/web_fetch w tej sesji
          ⛔ ZAKAZ wstawiania danych ⬛ do pisma / argumentacji bez weryfikacji
          Szczegóły + STATUS-LIFECYCLE: view shared/PRE-W2-VERIFICATION-GATE.md (PRE-W2.0)
          Wyjątki (NIE oznaczaj): imię/nazwisko, adres, PESEL osoby fizycznej
KROK 1  → [DETEKCJA TRYBU + HARD GATE] → view references/KROK1-detekcja.md
KROK 2  → [ROUTING [1]–[11]] → poniżej w tym pliku
KROK 3  → Załaduj PRIMARY → SECONDARY → FALLBACK
          ⛔ [R-3.54-a] Skill dziedzinowy (DR-01…DR-16) wczytuj PRZED weryfikacją
          przepisów, nie po niej — to on wskazuje, które przepisy weryfikować.
          Odroczenie DR-xx „do czasu weryfikacji” jest niedopuszczalne.
          ⛔ [R-3.54-b] Gdy sprawa dotyczy odpowiedzi na wezwanie / zarządzenie
          sądu: przed decyzją PRIMARY / ODRZUCONE odczytaj treść wezwania.
          Wezwanie żądające stanowiska, twierdzeń lub wniosków dowodowych →
          pisma-procesowe-v3; wyłącznie uzupełnienie braku formalnego lub
          przedłożenie dokumentu → pisma-proste-v2. Powód odrzucenia w KROKU 3A
          musi wskazywać, co wynika z treści wezwania.
KROK 3A → [ŚLAD ROUTINGU — OBOWIĄZKOWY]
          Bezpośrednio po KROK 3, PRZED przejściem do KROK 4, wypisz blok:
          ```
          TRYB: [LAIK / PRAWNIK]
          PRIMARY: [nazwa skilla] — ROUTER-WCZYTANY: [TAK: ścieżka view / NIE]
          SECONDARY: [nazwa(-y) skilla] — ROUTER-WCZYTANY: [TAK / NIE / N-D]
          ODRZUCONE: [skille rozważone i odrzucone] — powód: [jedno zdanie]
          PROFIL: [PEŁNY / LEKKI] — rdzeń R-1…R-5: [TAK]
          ODROCZONE: [zasób — wyzwalacz, który jeszcze nie padł / BRAK]
          WERSJA ROUTERA: [numer z YAML frontmatter tego pliku]
          RESOLVER: shared → [katalog] (v[wersja]); DUPLIKATY: [BRAK / skill v1 i v2]
          ```
          ⛔ Gdy `ROUTER-WCZYTANY: NIE` dla PRIMARY (np. z powodu braku
          dostępu do narzędzi plikowych w danym środowisku) — poprzedź
          resztę odpowiedzi nagłówkiem `⛔ TRYB ZDEGRADOWANY — router
          niewczytany`. Efekt uboczny pożądany: rozbraja sprzeczność
          „zakaz narzędzi plikowych + wykonaj routing" — brak wczytania
          staje się zadeklarowanym, jawnym stanem, nie milczącym
          pominięciem karanym jako uchybienie (patrz F-113 zakres (a)).
          `ROUTER-WCZYTANY: TAK` wymaga faktycznego odczytu w tej turze;
          kontrolę antyfasadową wykonaj z `references/SELF-CHECK.md`.
KROK 4  → Wykonaj analizę / zbierz dane
KROK 5  → Sprawdź TYP WYJŚCIA → SEKWENCJA END-TO-END → poniżej
KROK 5B → [EXPORT KONTEKSTU] → po KROK 5 jeśli sesja zawierała KROK 3B
           (analizator-dowodow-v3) lub W3 (pisma-procesowe-v3):
           view shared/MOD-KONTEKST-SESJI.md → wykonaj
           TRYB EXPORT (§3) — generuj plik .md i present_files.
KROK 6  → Jeśli pismo → generuj .docx
          Kontrola jakości i statusu DRAFT/FINAL zarządzana przez pisma-procesowe-v3
          (shared/CP-GATE.md). Router nie ingeruje w pipeline CP — tylko deleguje.
          ⛔ KROK 6-ST — ST-FINAL (BLOKUJĄCY): przed present_files KAŻDEGO pisma/.docx
          wyświetl PEŁNY REJESTR KROKÓW (FAZA 3 MOD-STEP-TRACKER). Jeśli STATUS =
          ⚠️ DRAFT — NIEZWERYFIKOWANY → pokaż raport pominięć (FAZA 2) i czekaj na decyzję
          a/b. ZAKAZ present_files bez uprzedniego ST-FINAL — także gdy router generuje
          pismo bez pełnego pipeline pisma-procesowe-v3.
KROK 7  → DISCLAIMER → view shared/DISCLAIMER.md
```

> ⛔ KROK 0A jest BRAMKĄ TWARDĄ. Żaden kolejny krok nie może być wykonany
> jeśli KROK 0A nie jest zamknięty (decyzja_sesji ≠ null).

---

## KROK 2 — ROUTING [1]–[11]

### [1] DOKUMENT / UMOWA
`umowa / OWU / kontrakt / ugoda / regulamin / testament / "czy mogę podpisać" / "klauzule"`
→ PRIMARY: `view analizator-umow-v1/SKILL.md`
→ SECONDARY: `orzeczenia-sadowe-v2` · FALLBACK: `przewodnik-prawny-v2`
→ „Na umowie zlecenie / o pracę / o dzieło” to podstawa zatrudnienia osoby, nie umowa do analizy → [10].
→ [1] wchodzi, gdy umowa jest przedmiotem pracy: analiza, sprawdzenie, napisanie, negocjacje, podpisanie, klauzule, zapisy. Umowa jako tło sporu („brak zgodności towaru z umową”, „deweloper nie wykonał umowy”, „umowa międzynarodowa”) → [10].

### [2] AKTA / WYROK / ANALIZA SZANS
`wyrok / nakaz zapłaty / wezwanie / pismo przeciwnika / "przeanalizuj wyrok" / "przeanalizuj orzeczenie" / "przeanalizuj postanowienie" / "analiza wyroku" / "analiza postanowienia" / "oceń wyrok" / "oceń postanowienie" / "jakie mam szanse" / "oceń szanse" / "szanse wygrania" / analiza akt / analiza pozycji`
→ Analiza wyroku, który użytkownik ma (także wyroku sądu apelacyjnego), to [2], nie [3]: „apelacyjny” nazywa sąd, nie pismo. Wyroku trzeba najpierw poszukać → [5] (`orzeczenia-sadowe-v2`), potem jego analiza (`analiza-sadowa-v6` jako SECONDARY).
→ PRIMARY: `view analiza-sadowa-v6/SKILL.md`
→ SECONDARY: `analizator-dowodow-v3`, `orzeczenia-sadowe-v2` · FALLBACK: `przewodnik-prawny-v2`

### [3] PISMO ZŁOŻONE
`pozew / apelacja / odpowiedź na pozew / zażalenie / skarga / odwołanie od wypowiedzenia / odwołanie od decyzji / odwołanie do sądu / odwołanie do KIO / skarga do WSA / pismo wielowątkowe`
→ PRIMARY: `view pisma-procesowe-v3/SKILL.md`
→ SECONDARY: `orzeczenia-sadowe-v2`, `analiza-sadowa-v6` · Wyjście: **obowiązkowo .docx**

### [4] PISMO PROSTE (1 wątek, 1 podstawa prawna)
`sprzeciw od nakazu / klauzula / przywrócenie terminu / wgląd / uzasadnienie / wezwanie do zapłaty`
→ PRIMARY: `view pisma-proste-v2/SKILL.md`
→ NIE używaj gdy >1 wątek → [3] · Wyjście: **obowiązkowo .docx**

### [5] ORZECZNICTWO
`"znajdź wyrok" / "znajdź orzeczenie" / "wyszukaj wyrok" / "wyszukaj orzeczenie" / "podaj wyrok" / "podaj orzeczenie" / "zweryfikowany wyrok" / "wyrok Sądu Najwyższego" / "orzeczenie Sądu Najwyższego" / "orzecznictwo" / "precedens" / "linia orzecznicza" / weryfikacja sygnatury`
→ Wyszukanie lub weryfikacja orzeczenia („wyszukaj wyrok SN”, „podaj zweryfikowany wyrok”) to [5], nie [2]: [2] analizuje wyrok, który użytkownik ma; nazwa sądu (SN, NSA) wskazuje źródło, nie dziedzinę sprawy.
→ PRIMARY: `view orzeczenia-sadowe-v2/SKILL.md`
→ SECONDARY: `analiza-sadowa-v6`

### [6] DOWODY / TERMINY / KOSZTY
`maile / SMS / nagrania / faktury / terminy procesowe / policz termin / termin na wniesienie / jako dowód / czy to dowód / moc dowodowa / koszty sądowe / opłaty komornicze`
→ PRIMARY: `view analizator-dowodow-v3/SKILL.md`
→ SECONDARY: `analiza-sadowa-v6`
→ Maile / SMS / nagrania / faktury wskazują [6], gdy pytanie dotyczy dowodu (ocena, wykorzystanie); sama opowieść o sprawie („SMS-y i śledzenie”, „wystawiłem fakturę, a kontrahent nie płaci”) → [10].

### [7] ZAGUBIONY / FALLBACK
`"co mam zrobić" / "od czego zacząć" / wyjaśnienie wyniku / walidacja przepisu`
→ PRIMARY: `view przewodnik-prawny-v2/SKILL.md`
→ SECONDARY: `prawo-polskie-v2`

### [8] PRZESŁUCHANIE ŚWIADKA
`świadek / cross-examination / biegły / pytania do świadka / rozbicie zeznania`
→ PRIMARY: `view przesluchanie-swiadkow-v2-min90/SKILL.md`
→ SECONDARY: `analizator-dowodow-v3`, `analiza-sadowa-v6`
→ [8] wchodzi przy przygotowaniu przesłuchania, pytań do świadka lub biegłego albo rozbiciu zeznania. Świadek lub biegły wspomniany w opowieści o sprawie („biegły nie stawił się na rozprawę”) → [10]; biegły rewident to nie biegły sądowy → [10].

### [9] ANALIZA PRZEPISU
`"art. X" / "§ Y" / przesłanki / wykładnia / "czy mnie dotyczy"`
→ PRIMARY: `view analizator-przepisow-v2/SKILL.md`
→ SECONDARY: `orzeczenia-sadowe-v2`, `pisma-procesowe-v3`

### [10] BEZ KLASYFIKACJI — ROUTER DZIEDZINOWY
`mandat / ZUS / alimenty / stalking / mobbing / eksmisja / deweloper / upadłość / RODO
/ zatrzymanie / mediacja / komornik / rozwód / zachowek / AI Act / sprawa wielodziedzinowa`
→ PRIMARY: `view prawo-polskie-v2/SKILL.md`

### [11] WERYFIKACJA CUDZEGO MATERIAŁU PRAWNEGO — KLUCZ / OPINIA / CUDZA ANALIZA
`"porównaj z kluczem" / "oto klucz odpowiedzi" / "sprawdź tę opinię" / "zweryfikuj tę
analizę" / "czy te przepisy się zgadzają" / "co jest nie tak w tym piśmie" / recenzja
cudzego opracowania / notatki egzaminacyjne / materiał z innego AI do sprawdzenia`
→ PRIMARY: `view analizator-przepisow-v2/SKILL.md`
→ SECONDARY: właściwy `dr-XX` domeny materiału (merytoryka) + `orzeczenia-sadowe-v2`
  (gdy materiał powołuje sygnatury) · FALLBACK: `przewodnik-prawny-v2`
→ OBOWIĄZKOWO: `view references/AUDYT-KLUCZA-ODPOWIEDZI.md` i wykonaj protokół
  K0–K6 przed sformułowaniem werdyktu porównawczego.

Materiał wejściowy traktuj jako hipotezę do sprawdzenia. Ziarnistość, rejestr
pokrycia, test spójności i werdykty są kanonicznie opisane w pliku K0–K6.

Przy nakładaniu się skilli: `view shared/ACTIVATION-MATRIX.md`.

**Routing BJ–BW (ZUS / niepełnosprawność / zawody zaufania):**
`view prawny-router-v3/references/ROUTING-BJ-BW.md`

**Zasada odciążenia routera:** Router NIE jest bazą prawa materialnego — tylko orkiestruje.
Nie dubluj treści modułów dziedzinowych w routerze.

---

## KROK 5–6 — SEKWENCJA END-TO-END

```
CZY WYNIK TO PISMO [3] lub [4]?
├── TAK
│   ├── ⛔ Materiały źródłowe? TAK → view shared/FAKTY_v2.md (F0-F3)
│   │                           NIE → każdy fakt bez źródła = ⬛ [UZUPEŁNIJ]
│   ├── pisma-procesowe-v3 lub pisma-proste-v2 → treść
│   ├── HYBRID-VALIDATION (policz ⬛) → view shared/HYBRID-VALIDATION.md
│   ├── view HOST_CAPABILITY[document_generation] → generuj .docx → present_files
│   └── Instrukcja złożenia (LAIK: "Wydrukuj i złóż w sądzie...")
├── ANALIZA / RAPORT?
│   ├── LAIK → przewodnik-prawny-v2 (KROK H) → widget + opcje
│   └── PRAWNIK → surowy raport → "Czy wygenerować pismo?"
└── ORZECZNICTWO? → Linki do baz + cytowania → opcja "Dołącz do pisma"
```


**WCZYTAJ (obowiązkowo, fail-closed):** `view prawny-router-v3/references/BRAMKI-GLOWNE.md` — PRZED wykonaniem którejkolwiek z czterech bramek poniżej (CN-GATE, bramka chronologiczna, WYJ-GATE, REM-GATE). Bez odczytu pliku bramka jest niewykonana. Wyzwalacze są mechaniczne (liczbowe), nie ocenne; polecenia „krótko" / „szybko" / „tylko odpowiedz" NIE zwalniają z bramek (przy zerze trafień blok ma jedną linię, ale musi być).

**BRAMKA NORMY CENTRALNEJ** (auto, PRZED wszystkimi pozostałymi) — CN-GATE:
wyzwalacz: odpowiedź zawiera rozstrzygnięcie, zarzut, roszczenie albo kwalifikację → `view shared/MOD-CN-GATE.md`; dla każdej osi sporu jedna jednostka redakcyjna i CN-1 (czasowy), CN-2 (podmiotowy), CN-3 (przedmiotowy). ⛔ BLOKUJĄCA: „NIE" = ZAKAZ kontynuacji na tej normie; wykonuje się PRZED OŚ-GATE i WYJ-GATE; OVERRIDE tylko wg zasad z pliku.

**BRAMKA CHRONOLOGICZNA** (auto, przed KROK 4) — TOR A (OŚ-GATE) i TOR B:
TOR A: ≥2 daty w stanie faktycznym → `view shared/MOD-OS-CZASU-PRZESLANEK.md`, OŚ-1…OŚ-4, blok WIDOCZNY przed konkluzją. TOR B: ≥2 dokumenty wieloetapowe lub słowa „chronologia"/„oś czasu"/„timeline" → `view chronologia-sprawy-v1/SKILL.md`. Tory niezależne.

**BRAMKA WYJĄTKÓW** (auto, przed KROK 4) — WYJ-GATE:
wyzwalacz: ≥1 powołany artykuł → `view shared/MOD-WYJATEK-GATE.md`, zamiatania S1 (sąsiedztwo), S2 (krawędzie jednostki), S3 (akty powiązane), S4 (przepisy przejściowe); blok WIDOCZNY przy pierwszym powołaniu aktu; każda pozycja zamknięta wpisem „brak" albo nazwanym skutkiem.

**BRAMKA ŚRODKA NAPRAWCZEGO** (auto, przed oddaniem) — REM-GATE:
wyzwalacz: oddajesz analizę, opinię, raport albo pismo → `view shared/MOD-REM-GATE.md`, REM-1 (zakaz sierocego oddalenia), REM-2 (zakaz non liquet), REM-3 (znacznik ≠ siła), REM-4 (budżet pokrycia); blok WIDOCZNY w odpowiedzi; wykonuje się PRZED HYBRID-VALIDATION.

---

## REGUŁY NADRZĘDNE

- **Reguła 1 — wejście:** router jest pierwszym krokiem; wczytaj PRIMARY przed analizą.
- **Reguła 1C — pliki:** wykonaj KROK 0C i PD0; status krytyczny blokuje analizę.
- **Reguła 2 — anonimizacja:** zamknij KROK 0A przed analizą.
- **Reguła 3 — HARD GATE:** przed analizą wykonaj KROK 1B.
- **Reguła 4 — niejednoznaczność:** zadaj jedno pytanie, nie zakładaj trybu.
- **Reguła 5 — kreator:** żądanie kreatora uruchamia go natychmiast.
- **Reguła 6 — pismo:** deleguj do właściwego skilla i wygeneruj `.docx`.
- **Reguła 7 — LAIK:** raport przez `przewodnik-prawny-v2`, KROK H.
- **Reguła 7B — menu:** pytanie o możliwości → przewodnik, KROK M.
- **Reguła 7C — Q&A:** pytania użytkownika → przewodnik, KROK Q.
- **Reguła 8 — termin:** termin zawity sprawdź przed pozostałymi kwestiami.
- **Reguła 9 — trwałość HARD GATE:** każda tura podlega `shared/PRAWO-HARDGATE.md`.
- **Reguła 10 — walidacja:** przed generowaniem wykonaj HYBRID-VALIDATION; zero ⬛ przed oddaniem.
- **Reguła 11 — dostawa:** `present_files` po walidacji, przed disclaimerem.
- **Reguła 11a — kroki:** wykonaj ST-INIT i blokujące ST-FINAL z `shared/MOD-STEP-TRACKER.md`.
- **Reguła 12 — chronologia:** wykonaj bramkę chronologiczną — TOR A (OŚ-GATE) przy ≥2 datach w stanie faktycznym, TOR B przy ≥2 dokumentach wieloetapowych. Tory niezależne.
- **Reguła 12a — wyjątki:** powołujesz artykuł → wykonaj bramkę wyjątków (WYJ-GATE, `shared/MOD-WYJATEK-GATE.md` 2.1), cztery zamiatania S1–S4. Zamiatasz policzalny zakres, nie „szukasz wyjątku". ⛔ S3 zamyka się dopiero po ZAPISANIU OBU OSI: b1 strona chroniona, b2 działalność regulowana (F-170). ⛔ S4 obejmuje także akt przesuwający wyłącznie DATĘ STOSOWANIA aktu głównego — taki akt nie ujawnia się przy odczycie samej normy, więc datę stosowania czytaj w brzmieniu AKTUALNYM, nie pierwotnym (F-171).
- **Reguła 12b — norma centralna:** rozstrzygasz cokolwiek → wykonaj CN-GATE (`shared/MOD-CN-GATE.md`) PRZED OŚ-GATE i WYJ-GATE. Wskazujesz JEDNĄ jednostkę per oś sporu i sprawdzasz trzy zakresy: czasowy, podmiotowy, przedmiotowy. Wynik „NIE" jest blokujący — poprawnie odczytany przepis bez zastosowania jest groźniejszy niż przepis niezweryfikowany, bo cała dalsza analiza wygląda na rzetelną.
- **Reguła 12c — środek naprawczy:** oddajesz cokolwiek → wykonaj REM-GATE (`shared/MOD-REM-GATE.md`) przed HYBRID-VALIDATION. Oddalenie bez sparowanej alternatywy, ⬛ bez rozstrzygnięcia warunkowego oraz argument stłumiony znacznikiem źródła to trzy osobne tryby awarii — bramka zamyka wszystkie trzy.
- **Reguła 12d — próba przed znacznikiem (REM-0):** ⛔ ZANIM oznaczysz powołanie ⚠️ [NIEWERYFIKOWANE] — spróbuj je pobrać, DWUKANAŁOWO: `bash_tool`/`curl` ORAZ `web_search`→`web_fetch`. Kanały mają różne listy dozwolonych domen, więc HTTP 403 w jednym nie dowodzi niczego o drugim (`ohchr.org`: curl 403, web_fetch pełny tekst RZĘDU 1). Znacznik dopuszczalny wyłącznie po porażce w OBU kanałach, zapisanej z kanałem i kodem — „brak dostępu" bez kodu nie jest zapisem porażki, tylko zapisem, że nie wiadomo, czy próbowano. Trzecie wystąpienie tej klasy błędu w tym systemie (F-151, F-162, F-164).
- **Reguła 14 — ślad weryfikacji:** wykonaj `shared/WERYFIKACJA-SLAD.md`.
- **Reguła 14a — forma znacznika ✅ (AF-7):** znacznik `✅ [VER]` bez trzech pól — kanału odczytu, identyfikatora aktu lub orzeczenia oraz daty odczytu W TEJ turze — jest NIEWAŻNY i czyta się go jak `⚠️ [NIEWERYFIKOWANE]`. Reguła jest składniowa i sprawdzalna z zewnątrz bez dostępu do logów. Zmierzone: w arkuszu testowym 24 gołe „✅ [VER]", z pięciu sprawdzonych dwa fałszywe (F-169).
- **Reguła 15 — sygnatury:** wykonaj `shared/SYGNATURY.md` oraz standard istnienia orzeczenia
  (statusy ✅ ISTNIEJE + TREŚĆ / 🟧 ISTNIEJE, TREŚĆ NIEODCZYTANA / ⚠️ NIEPOTWIERDZONE, zakaz łączenia
  sygnatury i daty z różnych rekordów): `view prawny-router-v3/references/HARD-GATES-ORZECZNICTWO.md`.
- **Reguła 16 — disclaimer:** wykonaj KROK 7.

### Reguły wykonawcze 17–27

- **Reguła 17 — V10:** przy analizie pisma przeciwnika wczytaj
  `pisma-procesowe-v3/references/engines/contradiction-intelligence-engine-v10.md`.
  Lista silników obowiązkowych i HARD GATE odpowiedzi na pismo przeciwnika:
  `view prawny-router-v3/references/ROUTING-OPPONENT-ANALYSIS-V9.md` (słabości, riposta) oraz
  `view prawny-router-v3/references/ROUTING-CONTRADICTION-INTELLIGENCE-V10.md` (sprzeczności, przyznania).
- **Reguła 18 — PRE-W2:** przed W2 każdego pisma wczytaj
  `shared/PRE-W2-VERIFICATION-GATE.md`; zweryfikuj online sąd, organ i podmioty.
- **Reguła 19 — strategia:** dla pisma z ≥2 ścieżkami lub anomalią podmiotową wczytaj
  `shared/MOD-STRATEGIA-WYBOR.md` przed W1.3.
- **Reguła 20 — checkpointy:** wykonuj `shared/CP-GATE.md`; po STOP zakończ turę.
- **Reguła 20a — status pisma:** DRAFT/FINAL i checkpointy pisma prowadzi `pisma-procesowe-v3`.
- **Reguła 21 — zlecenie złożone:** przypisz PRIMARY osobno każdemu komponentowi i nie
  omijaj checkpointu jednego komponentu z powodu równoległego wykonania innych.
- **Reguła 22 — świadek:** frazy „pytania do świadka”, „przesłuchanie”,
  „kontrprzesłuchanie” lub ich synonimy wymagają przed odpowiedzią odczytu
  `przesluchanie-swiadkow-v2-min90/SKILL.md` i wejścia od PRE-W1a.
- **Reguła 23 — re-check każdej tury:** jeżeli odpowiedź wspomina, potwierdza, koryguje
  albo ocenia przepis, sygnaturę lub kwalifikację, ponownie wykonaj HARD GATE
  dla każdego powołania w tej turze.
- **Reguła 24 — VER-GRAIN:** przed wysłaniem zinwentaryzuj osobno każdą jednostkę
  redakcyjną, wartość liczbową, datę, status i sygnaturę; każda pozycja musi
  mieć własne pokrycie źródłowe albo własny znacznik `⚠️ [NIEWERYFIKOWANE]`.
  Rozbieżność źródeł wymaga kontroli temporalnej z
  `shared/TEMPORAL-LAW-CHECK.md`.
- **Reguła 25 — cudzy materiał:** kategoria [11] i
  `references/AUDYT-KLUCZA-ODPOWIEDZI.md`; materiał nie jest źródłem prawa.
- **Reguła 26 — skill nie jest źródłem:** moduł wskazuje, który przepis sprawdzić, ale nie
  zastępuje świeżego odczytu źródła.
- **Reguła 27 — audyt klucza:** werdykt „PEŁNA ZGODNOŚĆ” jest dozwolony wyłącznie przy
  `P=N`, `O=0`, `U=0` i rachunku `P + O + U = N`.

---

## SELF-CHECK (przed każdą odpowiedzią)

Wykonaj w całości: `view prawny-router-v3/references/SELF-CHECK.md`.

Bramki blokujące:

- anonimizacja zamknięta;
- PRIMARY faktycznie wczytany i ślad KROKU 3A zgodny z wywołaniami;
- każdy URL ma znacznik RZĄD;
- każde powołanie ma świeżą weryfikację lub własne `⚠️ [NIEWERYFIKOWANE]`;
- każdy znacznik `✅ [VER]` niesie kanał, identyfikator i datę odczytu (AF-7);
- VER-GRAIN i właściwe reguły warunkowe wykonane;
- aktywne checkpointy, PRE-W2, RPK i ST-FINAL zamknięte;
- przy ≥2 datach w stanie faktycznym blok OŚ-GATE jest WIDOCZNY w odpowiedzi przed konkluzją;
- disclaimer jest ostatnim elementem odpowiedzi prawnej.

Niespełnienie któregokolwiek punktu → STOP; wykonaj brakujący krok albo uruchom
jawny TRYB ZDEGRADOWANY.

## RENDEROWANIE WIDGETÓW

> Pliki `.jsx` przez `present_files` NIE renderują się w claude.ai.
> Jedyna poprawna metoda inline: `show_widget` z HTML (vanilla JS).
> Pliki .docx / .pdf → present_files (dokumenty do pobrania — tu zasada nie dotyczy).

**Anonimizer — aktualny standard:**
`view prawny-router-v3/anonimizer/anonimizer-skill.md`

---

## POKRYCIE DZIEDZINOWE (wczytuj tylko gdy potrzebne)

```text
view prawny-router-v3/references/pokrycie-dziedzinowe.md
```

Tylko gdy: pytanie o dostępność modułu, audyt systemu, budowanie kombinacji multi-skill.

Mosty dziedzinowe (8 skrótów do kanonu DR/shared): rejestr w `references/pokrycie-dziedzinowe.md`,
sekcja MOSTY.
