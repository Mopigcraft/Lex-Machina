# ZASADY 11-15, ZASADY KRYTYCZNE 7-14 i STRUKTURA KATALOGU (przeniesione ze SKILL.md, treść bez zmian)

# ZASADY 11-15 audytu (przeniesione ze SKILL.md, treść bez zmian)

> ⚙️ **ZASADA 11 (2026-07-10, STAŁA — nie precedens):** Zakres audytu obejmuje
> **wszystkie skille prawne w systemie**, nie tylko mapę Dz.U. i skille DR-01
> do DR-16. Obejmuje to również skille proceduralne (np. `pisma-procesowe-v3`,
> `przesluchanie-swiadkow-v2-min90`, `analizator-dowodow-v3`,
> `chronologia-sprawy-v1`), gdzie przedmiotem audytu nie jest poprawność
> numeru aktu prawnego, lecz **poprawność i domyślne (nie tylko na żądanie)
> stosowanie wbudowanych bramek jakości** (np. zakazy pytań sugestywnych,
> wymóg rekonstrukcji tezy, wymóg jawnego potwierdzenia ról/dowodów/tez przed
> generowaniem treści). Wpis dokumentujący taki audyt trafia do tego samego
> `AUDIT-JOURNAL.md`, z jawnym wskazaniem w tytule sekcji, że dotyczy skilla
> proceduralnego, a nie mapy Dz.U. — żeby FAZA 3 (Dz.U.) nie myliła kontekstów.
> Ta zasada nie jest jednorazowym wyjątkiem — obowiązuje dla każdego kolejnego
> audytu, dowolnego skilla w ``.

---

> ⚙️ **ZASADA 12 (2026-07-16, STAŁA — nie precedens):** Audyt map Dz.U.
> (FAZA 3A–3D) i audyt treści merytorycznej modułów (FAZA 3E,
> `MOD-TRESC-MERYTORYCZNA.md`) to **dwa odrębne zakresy kontroli, oba
> obowiązkowe**. Aktualizacja numeru/statusu tekstu jednolitego w
> `mapa_dzu`/`MAPA-AKTOW.md` (np. `OK` → `PREV`, dodanie nowego wiersza
> `TJ`) **nie jest równoznaczna** ze sprawdzeniem, czy opisowa treść
> modułu `dr-XX/modules/mod-*.md` (progi, terminy, definicje, przesłanki)
> nadal odpowiada aktualnemu stanowi prawnemu. FAZA 3E uruchamia się
> automatycznie po każdej sesji FAZA 3, w której wykryto zmianę statusu
> aktu — nie jest opcjonalna i nie wymaga osobnego wywołania. Naruszenie
> (zamknięcie FAZA 3 bez FAZA 3E mimo wykrytej zmiany) = **CRIT**.

---

> ⚙️ **ZASADA 13 (2026-07-17, STAŁA — nie precedens):** Ponowna weryfikacja
> oznaczeń/skrótów prawnych + wytrwałość wyszukiwania + oznaczanie przy
> każdym użyciu. Pełna treść i uzasadnienie: `shared/PRAWO-HARDGATE.md`
> wersja 2.4. Skrót operacyjny na potrzeby audytu:
> 1. Każde niepotwierdzone źródłowo oznaczenie/skrót prawny, gdy pojawia
>    się PONOWNIE w dalszej części rozmowy jako podstawa wniosku, wymaga
>    NOWEJ weryfikacji — przywołanie z pamięci wcześniejszej hipotezy
>    (nawet własnej) NIE wystarcza i nie podnosi jej do statusu ustalonego
>    faktu.
> 2. Pierwsze wyszukiwanie bez jednoznacznego potwierdzenia z aktu
>    źródłowego NIE kończy weryfikacji — kontynuuj różnymi zapytaniami
>    (pełna nazwa instytucji/rejestru, synonimy, szersze/węższe ujęcie)
>    zamiast zatrzymywać się na hipotezie prawdopodobieństwa.
> 3. ⚠️ [NIEWERYFIKOWANE] musi towarzyszyć KAŻDEMU wystąpieniu
>    niepotwierdzonego oznaczenia w odpowiedzi/dokumencie, nie tylko
>    pierwszemu wprowadzeniu.
>
> Przy audycie treści merytorycznej (FAZA 3E) i przy każdym audycie
> skilli operujących na sygnaturach/repertoriach/oznaczeniach
> instytucjonalnych — sprawdź zgodność z tą zasadą jako osobny punkt.
> Naruszenie (powtórne użycie niepotwierdzonego oznaczenia bez ponownej
> weryfikacji lub bez powtórzonego ⚠️ [NIEWERYFIKOWANE]) = **CRIT**.

---

> ⚙️ **ZASADA 14 (2026-07-26, STAŁA — nie precedens):** Gradacja źródeł
> przy weryfikacji merytorycznej (FAZA 3E) — obowiązkowe stosowanie
> `shared/HIERARCHIA-ZRODEL.md` (Rząd 1/2A/2B/3), nie tylko przy
> podawaniu linków użytkownikowi, ale RÓWNIEŻ jako metodologia SAMEJ
> weryfikacji przy audycie. Ustalone po dwóch transzach FAZA 3E
> (AUDYT-2026-07-26h/i), na wyraźne polecenie użytkownika.
>
> **Procedura, w kolejności:**
> 1. **Rząd 1 — ELI, próba pierwsza, zawsze (kanon E-1…E-5,
>    `shared/HIERARCHIA-ZRODEL.md`, od audytu 6.125).** Brzmienie i stan
>    aktu z `api.sejm.gov.pl/eli` kanałem kodu (`text.pdf` t.j.,
>    `/references` dla zmian), host bez kanału kodu — B-1 → B-2 na
>    `eli.gov.pl`. ISAP (`isap.sejm.gov.pl`) wyłącznie jako link dla
>    człowieka; jego blokada to stan normalny, nie powód do zejścia rzędu.
> 2. **Rząd 2A/2B jako główne potwierdzenie** wyłącznie, gdy ELI zawiódł
>    i ISAP (akt niepobieralny z RZĘDU 1 — awaria, timeout, blokada; wynik
>    zapisany): LEX/Legalis, potem lexlege.pl,
>    arslege.pl, prawo.pl i analogiczne z rejestru
>    `HIERARCHIA-ZRODEL.md`/`PORTALE-BRANZOWE-RZAD-2B.md`. Traktuj jako
>    wiarygodne dla BRZMIENIA przepisu, ale NIGDY nie zaznaczaj wyniku
>    jako ✅ [VER] tak jakby to był Rząd 1 — użyj oznaczenia zgodnego z
>    `shared/WERYFIKACJA-SLAD.md` odpowiedniego dla źródła Rządu 2.
> 3. **Rząd 3 (blogi kancelaryjne) — WYŁĄCZNIE jako dodatkowe
>    potwierdzenie zbieżności, NIGDY jako jedyne źródło.** Wysoka liczba
>    zgodnych źródeł Rządu 3 (5+) wokół tego samego brzmienia ZWIĘKSZA
>    pewność, ale nie zastępuje braku Rządu 1/2 — jeśli WSZYSTKIE
>    dostępne źródła to Rząd 3, oznacz wynik jako potwierdzony z
>    zastrzeżeniem niższej kategorii źródła, nie jako pełne ✅.
> 4. **Próg potwierdzenia:** minimum 2-3 źródła NIEZALEŻNE (różne domeny,
>    różni wydawcy) zgodne ze sobą, zanim twierdzenie modułu zostanie
>    oznaczone jako sprawdzone. Rozbieżność między źródłami = sygnał do
>    DALSZEGO wyszukiwania (inne zapytanie, inny kąt), nie do wyboru
>    jednego źródła arbitralnie (patrz ZASADA 13, pkt 2 — wytrwałość
>    wyszukiwania stosuje się też tutaj).
> 5. **Każdy wynik weryfikacji FAZA 3E w AUDIT-JOURNAL.md wskazuje
>    WYRAŹNIE, z jakiego Rzędu pochodziło potwierdzenie** (nie tylko
>    nazwy domen) — np. "potwierdzone w lexlege.pl (Rząd 2B) oraz 5
>    źródłach Rządu 3" — żeby czytelnik dziennika mógł ocenić siłę
>    dowodową ustalenia bez ponownego sprawdzania.
>
> Naruszenie (oznaczenie twierdzenia jako "zweryfikowane" na podstawie
> WYŁĄCZNIE jednego źródła Rządu 3, lub bez wskazania Rzędu w ogóle) =
> **WARN**, nie CRIT — to zasada jakości dowodu, nie zakaz absolutny jak
> PRAWO-HARDGATE, ale traktuj ją jako obowiązkową praktykę FAZA 3E.

> ⚙️ **ZASADA 15 (2026-08-20z4, STAŁA — nie precedens; na wyraźne polecenie
> użytkownika):** **Historia zmian KAŻDEGO skilla mieszka wyłącznie w osobnym
> pliku `references/CHANGELOG.md`.** W SKILL.md nie ma sekcji `## CHANGELOG`
> z wpisami — dopuszczalne jest wyłącznie odesłanie do pliku; pole `changelog:`
> w YAML pozostaje krótkim skrótem bieżącej wersji (do ~15 linii), nigdy pełną
> listą wpisów.
>
> Uzasadnienie nie jest porządkowe, tylko funkcjonalne: rozproszenie historii
> między trzy lokalizacje (korpus SKILL.md, frontmatter, `references/`) było
> BEZPOŚREDNIĄ przyczyną fałszywych wyników testu T12 w sesji 2026-08-20z3 —
> test szukał wpisów w `references/`, nie znajdował ich (bo leżały w SKILL.md)
> i raportował luki, których nie było. W `pisma-procesowe-v3` groziło to
> dopisaniem pięciu zmyślonych wpisów. Jedna lokalizacja kanoniczna usuwa całą
> tę klasę błędu — i ten sam argument dotyczy każdego przyszłego narzędzia,
> które będzie czytać historię automatycznie.
>
> Egzekwowanie: test **T12** (`scripts/check_wersje_changelog.py`) zgłasza
> sekcję z wpisami w korpusie jako ⛔, a pole `changelog:` dłuższe niż 15 linii
> jako ⚠️. Nowy skill BEZ `references/CHANGELOG.md` jest dopuszczalny tylko
> dopóki nie ma historii — przy pierwszym wpisie plik zakłada się od razu.
>

# ZASADY KRYTYCZNE 7-14 (przeniesione ze SKILL.md, treść bez zmian)


   Każda naprawa pliku (CRIT lub WARN) musi być dostarczona jako **kompletny skill**
   zawierający WSZYSTKIE pliki i podfoldery danego skilla, nie tylko zmieniony plik.
   Naruszenie tej zasady (dostarczenie samego pliku zamiast pełnego skilla) jest błędem
   krytycznym równoważnym CRIT i musi być odnotowane w AUDIT-JOURNAL.

   > 🔴 **PRE-DELIVERY-COMPLETENESS-CHECK — procedura przenośna.** Najpierw
   > rozwiąż trzy lokalizacje przez adapter hosta: `SKILL_SOURCE` (pełne
   > źródło skilla), `WORK_COPY` (zapisywalna kopia robocza) i `ARCHIVE`
   > (plik wynikowy). Żadna z nich nie może być ścieżką założoną dla jednego
   > hosta.
   >
   > ⛔ **`SKILL_SOURCE` = repozytorium (`main`), NIGDY kopia zainstalowana
   > w hoście (F-221/F-223, od 6.158).** claude.ai przy imporcie z marketplace
   > serializuje frontmatter `SKILL.md` ponownie: usuwa komentarze YAML, zdejmuje
   > wcięcia list, zamienia skalary blokowe na ciągi z literalnym `\n`. Pozostałe
   > pliki są bajtowo zgodne z `main`. Wydanie 6.157 zbudowane z takiej kopii
   > straciło 181 linii frontmatteru audytu i podniosło T22 na `main` z 6 do 113
   > rozjazdów. Gdy repozytorium nie jest dostępne, a kopia zainstalowana tak —
   > pobierz `SKILL.md` z `main` (raw GitHub) i nanieś zmiany na niego.
   > `dostarcz_skill.sh` odmawia spakowania skilla, który nie przechodzi T22.
   > Audyt prowadzony NA kopii zainstalowanej: T21 i T22 przełączają się same
   > w tryb kopii (układ `plugin:skill`); `SKILL.md` weryfikuje wtedy wyłącznie
   > T21 z `--repo-ref <katalog skilli repozytorium>` (od 6.159).
   >
   > ```bash
   > # 1. Stan wejściowy
   > find "$SKILL_SOURCE" -type f | sort > before.files
   >
   > # 2. Pełna kopia; edycje wykonuj wyłącznie w WORK_COPY
   > cp -R "$SKILL_SOURCE" "$WORK_COPY"
   >
   > # 3. Stan wyjściowy — różnicę liczby plików trzeba jawnie uzasadnić
   > find "$WORK_COPY" -type f | sort > after.files
   >
   > # 4. Jeden pełny pakiet na jeden skill
   > zip -r "$ARCHIVE" "$WORK_COPY"
   >
   > # 5. Rozpakuj do świeżego VERIFY_COPY i porównaj bajtowo
   > diff -rq "$VERIFY_COPY" "$WORK_COPY"
   > ```
   >
   > Przed wydaniem pokaż liczbę plików przed/po oraz listę zamierzonych
   > różnic. `diff` archiwum po rozpakowaniu z `WORK_COPY` musi być pusty.
   > Dodatkowy `diff` względem `SKILL_SOURCE` ma zawierać wyłącznie zmiany
   > tej tury. Przy wielu skillach wykonaj procedurę osobno dla każdego;
   > zakaz pakietu zbiorczego i zakaz dostarczania pojedynczego `SKILL.md`.
   > Sposób udostępnienia (`present_files`, instalacja skilla lub równoważna
   > funkcja hosta) nie zmienia wymogu kompletności.
   >
   > ⛔ **Pliki kanału pluginów NIE wchodzą do paczki skilla (F-230, od 6.187).**
   > `.claude-plugin/` i `.mcp.json` w korzeniu skilla służą wyłącznie instalacji
   > z marketplace (repozytorium, T38); claude.ai odrzuca wgrywany skill z
   > manifestem pluginu („Umiejętność nie może zawierać manifestu wtyczki”).
   > Kompletny skill do wgrania = wszystkie pliki skilla bez tych dwóch pozycji;
   > `CHECKSUMS.sha256` ich nie wymienia (T21 i tak pomija pliki ukryte).
   > `dostarcz_skill.sh`, `repack_development_archives.py` i T34 liczą pliki
   > przed/po bez nich; T34 i weryfikator paczek zgłaszają plik pluginu w ZIP-ie.
8. ⛔ **ZASADA WERYFIKACJI NUMERU NIEZALEŻNIE OD NAZWY (dodana 2026-07-02s,
   na wyraźny nakaz użytkownika) — "jeśli nazwy różnią się choć trochę,
   sprawdzaj w ISAP" (od 6.125 czytaj: w RZĘDZIE 1 — najpierw ELI).**

   Zgodność NAZWY aktu między dwoma źródłami (np. między MAPA-AKTOW.md a
   treścią modułu) NIE jest dowodem poprawności numeru Dz.U. Odkryty
   przypadek referencyjny (dr-10, ustawa o medycynie laboratoryjnej): moduł
   poprawnie nazwał akt, ale podał numer Dz.U. należący do INNEGO,
   zastąpionego aktu o pokrewnej tematyce (2022.2162 zamiast 2022.2280).
   Zasada praktyczna: przy każdej weryfikacji TRYB DZU sprawdzaj NUMER
   niezależnie od tego, czy NAZWA aktu w mapie/module wygląda poprawnie —
   zwłaszcza gdy w tej samej dziedzinie istnieje stary i nowy akt o
   zbliżonym temacie (typowy wzorzec ryzyka: reformy zawodowe/regulacyjne,
   gdzie nowa ustawa zastępuje starą pod inną nazwą lub tym samym tytułem).
   Kanał (od 6.125): numer Dz.U. sprawdzaj w ELI —
   `api.sejm.gov.pl/eli/acts/DU/{rok}/{poz}` zwraca tytuł aktu, więc
   rozbieżność numeru i nazwy widać wprost. Kanał maszynowy ISAP jest
   martwy; `web_search` z numerem Dz.U. (fragmenty ISAP, dziennikustaw.gov.pl,
   sip.lex.pl, gofin.pl) tylko pomocniczo, gdy aktu nie da się pobrać z RZĘDU 1.
   Dostarczanie wyłącznie zmodyfikowanego pliku bez reszty struktury grozi nieodwracalną
   utratą danych przy wgraniu (nadpisanie katalogu bez pozostałych plików).

   ⛔ **Limit i relikty (od 6.153):** skill ma mieć < 200 plików (T41). Instalację wydania
   wykonuje się przez ZASTĄPIENIE katalogu skilla w całości, nie nałożenie paczki na stary katalog —
   nałożenie wskrzesza pliki usunięte w poprzednich wydaniach (zmierzone: 6 plików z 6.146 i 30 z 6.149
   w jednej instalacji; AUDYT-2026-09-29c). Plik zgłoszony przez T21 jako „BRAK WPISU” najpierw
   sprawdź w CHANGELOG — dopisanie mu sumy legalizuje relikt.

   **Reguła:** po każdej naprawie → `find <skill>/ -not -path "*/archive/*"` →
   skopiuj WSZYSTKIE pliki do `/home/claude/<skill>/` z zachowaniem podfolderów →
   `zip -r <skill>.zip <skill>/` → skopiuj ZIP do `/mnt/user-data/outputs/` →
   `present_files` pliku ZIP. Nigdy nie dostarcza się luźnych plików .md.

   **Wyjątek dozwolony:** wyłącznie gdy deweloper **explicite** potwierdził w tej sesji,
   że chce tylko diff/patch i rozumie ryzyko. Bez takiego potwierdzenia — zawsze pełna struktura.

9. ⛔ **ZASADA PRZEGLĄDU OKRESOWEGO WARN (dodana 2026-07-07, po sesji w której
   WARN-12 i WARN-24 pozostały otwarte przez wiele kolejnych wpisów dziennika
   bez zamknięcia i bez ponownego odnotowania).**

   Flagi drugorzędne (priorytet "niski/średni", bez oznaczenia PILNY) mogą
   zostać zgubione w długich, wielokrokowych sesjach, gdy kolejne wpisy
   dziennika koncentrują się na głównym wątku bieżącej sesji i nie powtarzają
   pełnej listy historycznie otwartych WARN. Wynik: flaga pozostaje formalnie
   otwarta, ale nikt jej już nie widzi w bieżącym kontekście.

   **Reguła:** co najmniej raz na ~10 wpisów dziennika (liczonych od
   ostatniego pełnego przeglądu) — lub natychmiast, gdy użytkownik pyta
   wprost "czy wszystkie WARN są zamknięte" / podobnie — wykonaj:
   `grep -noE "WARN-[0-9]+" AUDIT-JOURNAL.md | sort -t- -k2 -n -u`, a następnie
   dla każdego numeru sprawdź kontekst NAJNOWSZEGO (najniższy numer linii)
   wystąpienia, by potwierdzić status. Nie polegaj wyłącznie na podsumowaniach
   "WARN nadal otwarte: ..." z pojedynczej sesji — mogą być niekompletne,
   jeśli odnoszą się tylko do WARN otwartych w ramach tej jednej sesji, a nie
   do całej historii. Wynik przeglądu odnotuj w dzienniku jako osobny wpis
   (jak ten), nawet jeśli nie znaleziono nowych otwartych flag.

10. ⛔ **ZASADA ROZDZIAŁU OTWARTE/ZAMKNIĘTE (dodana 2026-07-07, na wyraźne
    polecenie użytkownika) — "wydziel do otwartych warnów osobny dziennik,
    a zamknięte utrzymuj w aktualnym".**

    `AUDIT-JOURNAL.md` i `references/WARN-OTWARTE.md` mają rozłączne role:
    - **`WARN-OTWARTE.md`** — WYŁĄCZNIE aktualnie otwarte flagi (WARN
      numerowane + flagi strukturalne F-N). Krótki, żywy rejestr — to jest
      TODO systemu, nie archiwum. Nie zawiera narracji, dat naprawy ani
      historii — tylko to, co jeszcze czeka.
    - **`AUDIT-JOURNAL.md`** — pełna historia chronologiczna, w tym
      zamknięcia z pełnym opisem naprawy. Nic z niego nigdy nie jest
      usuwane.

    **Reguła operacyjna:**
    - Nowa flaga (WARN lub strukturalna) odkryta w sesji → dodaj wiersz do
      `WARN-OTWARTE.md` ORAZ krótki wpis o odkryciu w `AUDIT-JOURNAL.md`.
    - Flaga zamknięta → USUŃ jej wiersz z `WARN-OTWARTE.md` ORAZ dodaj pełny
      wpis o naprawie w `AUDIT-JOURNAL.md` (jak dotychczas).
    - ⛔ **Naprawa CZĘŚCIOWA (dodane 2026-08-15w, po porządkowaniu rejestru,
      który urósł do 489 linii / ~96 KB): SKRÓĆ wiersz flagi do tego, co
      ZOSTAŁO — NIE dopisuj do niego opisu tego, co właśnie zrobiono.**
      Opis wykonanej części należy WYŁĄCZNIE do `AUDIT-JOURNAL.md`; w
      wierszu flagi zostaje co najwyżej odesłanie do wpisu dziennika.
      Dopisywanie bloków „✅ CZĘŚCIOWO ZAMKNIĘTE …" do komórki opisu było
      JEDYNĄ przyczyną rozrostu rejestru i doprowadziło do sklejenia
      czterech struktur wierszowych w jednym wierszu (F-86) oraz do
      sytuacji, w której odczyt „co mam zrobić" wymagał przeczytania
      opisu tego, co już zrobione.
    - Pytanie "co jest otwarte" / "czy wszystko zamknięte" → czytaj
      NAJPIERW `WARN-OTWARTE.md`. Grep całego `AUDIT-JOURNAL.md` (ZASADA 9)
      pozostaje jako kontrola co ~10 wpisów, żeby wykryć rozjazd między
      dwoma plikami — nie jako podstawowy sposób odpowiadania na bieżąco.
    - Ten sam skill (`audyt-systemu-v4`) z niepustym `WARN-OTWARTE.md`
      NIE jest blokowany (WARN nie blokuje, ZASADA 5) — plik służy
      wyłącznie widoczności, nie jest bramką.

11. ⛔ **ZASADA TREŚĆ-PO-MAPIE (dodana 2026-07-16, ZASADA 12 w nagłówku
    pliku, tu jako pozycja 11 listy operacyjnej) — audyt aktualności
    numeru Dz.U. i audyt aktualności treści merytorycznej modułu to
    dwie różne kontrole.**

    Zamknięcie FAZA 3 (dowolny podtryb) z wykrytą zmianą statusu aktu
    (nowy `TJ`, `✅ WSZEDŁ`, lub WARN z 3C potwierdzony jako "jest nowszy
    akt") **bez uruchomienia FAZA 3E** (`modules/MOD-TRESC-MERYTORYCZNA.md`)
    jest błędem krytycznym równoważnym CRIT — analogicznie do ZASADY 7
    dla kompletności dostarczenia. Aktualizacja samego wiersza w
    `mapa_dzu`/`MAPA-AKTOW.md` nie jest dowodem, że treść modułu została
    sprawdzona pod kątem tego, co konkretnie zmieniła nowelizacja.

12. ⛔ **ZASADA GRADACJI ŹRÓDEŁ PRZY WERYFIKACJI (dodana 2026-07-26,
    ZASADA 14 w nagłówku pliku, tu jako pozycja 12 listy operacyjnej) —
    FAZA 3E stosuje `shared/HIERARCHIA-ZRODEL.md` jako metodologię, nie
    tylko jako zasadę oznaczania linków.**

    Kolejność: kanon E-1…E-5 — Rząd 1 ELI (próba zawsze pierwsza; ISAP
    tylko link dla człowieka) → Rząd 2A LEX/Legalis → Rząd 2B (lexlege.pl,
    arslege.pl, prawo.pl — gdy aktu nie da się pobrać z RZĘDU 1) → Rząd 3 (blogi kancelaryjne — WYŁĄCZNIE jako dodatkowe
    potwierdzenie zbieżności, nigdy jako jedyne źródło). Minimum 2-3
    źródła niezależne zgodne ze sobą przed oznaczeniem twierdzenia jako
    sprawdzonego. Każdy wpis w AUDIT-JOURNAL.md wskazuje Rząd źródła
    potwierdzenia, nie tylko nazwę domeny. Naruszenie (oznaczenie
    "zweryfikowane" na podstawie wyłącznie 1 źródła Rządu 3, lub bez
    wskazania Rzędu) = **WARN**.

13. ⛔ **ZASADA LIMITU DŁUGOŚCI MODUŁU (dodana 2026-08-14, na żądanie
    użytkownika) — moduł przekraczający 1000 linii MUSI zostać
    podzielony wg rozdziałów aktu, który opisuje.**

    **Kiedy sprawdzać:** (a) po KAŻDYM utworzeniu nowego modułu (budowa wg
    `shared/MOD-GENERATOR-AKTU.md` G-1…G-8) — `wc -l`
    na plik zaraz po `create_file`, PRZED rejestracją w SKILL.md/mapie/
    ROUTING-MAP; (b) po KAŻDYM rozbudowaniu istniejącego modułu (kolejna
    sesja FAZA 3E, dopisanie nowego rozdziału/artykułów) — sprawdzić
    długość PO edycji, nie tylko przy tworzeniu; (c) okresowo przy
    audytach kompletności (np. razem z `check_rejestracja_modulow.py`)
    jako dodatkowa kontrola dla modułów rozrastających się iteracyjnie
    przez wiele sesji.

    **Próg:** **1000 linii** (`wc -l`). Moduł ≤1000 linii — bez zmian,
    zostaje jednym plikiem. Moduł >1000 linii — PODZIEL wg rozdziałów
    aktu (nie wg arbitralnego przecięcia w połowie treści), analogicznie
    do wzorca już stosowanego w systemie dla dużych kodeksów (np.
    `mod-KW-art49-64-...`, `mod-KW-art70-118-...`,
    `mod-KW-art119-131-...`, `mod-KK-art127-139-...` — każdy moduł
    obejmuje spójny zakres rozdziałów/artykułów, nie cały kodeks
    naraz).

    **Zakres stosowania (doprecyzowane 2026-08-15n, po pełnym skanie
    systemu ujawniającym pliki >1000 linii POZA katalogami `modules/`):**
    - **OBJĘTE:** wszystkie pliki `modules/mod-*.md` w DR-01…DR-16 oraz
      pliki merytoryczne w `shared/` opisujące jeden akt/jedną dziedzinę
      (precedens: `ORKA-BAS-LEKSYKON.md`, `PORTALE-BRANZOWE-RZAD-2B.md`
      już figurują w F-78).
    - **DO ROZSTRZYGNIĘCIA (nie egzekwować bez decyzji użytkownika):**
      pliki `SKILL.md` skilli-orchestratorów (`przesluchanie-swiadkow-v2-min90`
      1809, `analizator-dowodow-v3` 1203, `audyt-systemu-v4` 1170 —
      stan 2026-08-15n). Podział wg „rozdziałów aktu" nie ma tu
      zastosowania (nie opisują aktu prawnego), a `SKILL.md` musi
      pozostać JEDNYM plikiem wejściowym skilla — ewentualny zabieg to
      wydzielenie sekcji do `modules/`, nie podział pliku.
    - **WYŁĄCZONE TRWALE:** `references/AUDIT-JOURNAL.md` (40 483 linii
      na 2026-08-15n) — dziennik przyrostowy, append-only, z definicji
      rosnący; nie ma rozdziałów aktu, a podział zerwałby chronologię
      i odesłania `AUDYT-YYYY-MM-DD` używane w całym systemie.
      Analogicznie pozostałe rejestry historyczne (`mapa_dzu_*.md`).

    **Jak dzielić:** (1) zidentyfikuj naturalne granice rozdziałów w
    obrębie modułu (np. "Rozdział I", "Rozdział II" aktu źródłowego);
    (2) pogrupuj rozdziały w 2+ nowe moduły tak, by każdy mieścił się
    wygodnie poniżej progu, zachowując spójność tematyczną (nie dziel
    W ŚRODKU pojedynczego rozdziału/artykułu); (3) każdy nowy plik
    dostaje nazwę wzorowaną na istniejącej konwencji
    (`mod-<KODEKS>-art<OD>-<DO>-<krotki-opis>.md`); (4) w PIERWSZYM
    (najniższe numery artykułów) module dodaj sekcję "PODZIAŁ MODUŁU"
    wskazującą pozostałe części i ich zakres; (5) zarejestruj WSZYSTKIE
    nowe pliki osobno w SKILL.md/mapie/ROUTING-MAP (Reguła 2/3
    HARDGATE) — podział zwiększa liczbę zarejestrowanych modułów, co
    jest zamierzoną, uzasadnioną zmianą liczby plików w Regule 6/
    ZASADA 7 KROK 1/4; (6) usuń oryginalny, zbyt długi plik dopiero PO
    potwierdzeniu, że wszystkie nowe pliki poprawnie zastępują jego
    treść (nic nie zgubione) — porównaj sumę linii nowych plików z
    linią bazową oryginału jako grubą kontrolę kompletności.

    **Uzasadnienie:** moduły >1000 linii utrudniają nawigację przy
    `view` (truncation przy dużych plikach), zwiększają ryzyko
    przypadkowego nadpisania fragmentu przy `str_replace` (niejednoznaczne
    dopasowanie w długim pliku) i utrudniają utrzymanie spójności przy
    częściowych aktualizacjach (łatwiej przeoczyć fragment do
    zaktualizowania w rozdziale odległym od miejsca edycji).

    Naruszenie (dostarczenie/pozostawienie modułu >1000 linii bez próby
    podziału, lub podział w niewłaściwym miejscu przecinający rozdział)
    = **WARN**, odnotować w WARN-OTWARTE.md z docelowym podziałem do
    wykonania.

14. ⛔ **ZASADA BRAMKI WYJŚCIOWEJ ZGŁOSZENIA (AUDIT-CLAIM-GATE, dodana
    2026-08-23g, flaga F-121) — skill audytowy stosuje wobec własnych
    zgłoszeń dokładnie ten kontrakt weryfikacyjny, którego pilnuje u
    innych.**

    **Przesłanka (TEST1 §5.2):** trzy diagnozy samoaudytu zostały obalone
    przez recenzenta zewnętrznego, bo powstały bez weryfikacji w źródle —
    termin „30 dni" zgłoszony jako prawdopodobna halucynacja (podczas gdy
    termin ten ma podstawę ustawową i wymagał tylko sprawdzenia zakresu
    zastosowania), status niedzieli opisany jako jednoznaczny mimo że nie
    jest, oraz `ROBOTS_DISALLOWED` zakwalifikowany jako „błąd krytyczny
    infrastruktury" cudzego systemu. **Fałszywy alarm audytu kosztuje tyle
    samo, co błąd przeoczony** — kieruje sesję naprawczą na nieistniejący
    problem i podważa zaufanie do pozostałych zgłoszeń w tym samym
    raporcie, w tym tych trafnych.

    **Reguła:** żadne zgłoszenie audytowe (wiersz w `WARN-OTWARTE.md`,
    punkt raportu, akapit w `AUDIT-JOURNAL.md`, wiersz raportu różnic) NIE
    opuszcza skilla w postaci TWIERDZENIA, jeśli nie niesie łącznie trzech
    pól:

    ```
    (1) STATUS  — wg rejestru statusów w shared/PRAWO-HARDGATE.md:
        ✅ [VER: źródło, data]        — potwierdzone w Rzędzie 1
        🟨 [KOTWICA-URZĘDOWA]         — potwierdzone kotwicą urzędową
        ⚠️ [NIEWERYFIKOWANE — HIPOTEZA] — NIEpotwierdzone; wolno zgłosić
                                         WYŁĄCZNIE z tym oznaczeniem
        (F-116 ANULOWANA — brak osobnej karty statusów, rejestr jest
        i pozostaje w shared/PRAWO-HARDGATE.md)
    (2) IDENTYFIKATOR ŹRÓDŁA — plik + numer linii, albo numer Dz.U. +
        artykuł, albo URL z datą odczytu. „Widziałem gdzieś w systemie"
        NIE jest identyfikatorem.
    (3) REPRODUKCJA — polecenie lub sekwencja, którą czytelnik odtworzy
        zgłoszenie samodzielnie (`grep -n …`, `python3 scripts/…`, „otwórz
        plik X w. N"). Zgłoszenie nieodtwarzalne przez drugą osobę jest
        opinią, nie ustaleniem audytowym.
    ```

    **Zakaz szczególny — KWALIFIKACJA CUDZEGO BŁĘDU:** określenia „błąd
    krytyczny", „halucynacja", „awaria infrastruktury" opisują PRZYCZYNĘ,
    a przyczyna prawie nigdy nie jest obserwowalna z zewnątrz. Zgłaszaj
    OBJAW (co dokładnie zwróciło narzędzie, czego zabrakło w odpowiedzi) i
    dopiero po nim — osobno oznaczoną — hipotezę przyczyny. `ROBOTS_DISALLOWED`
    to zaobserwowany objaw; „krytyczna awaria serwisu X" to hipoteza.

    **Egzekwowanie:** `references/FORMAT-RAPORTU-ROZNIC.md` § 4 wymusza te
    trzy pola w raporcie różnic. Dla pozostałych wyjść bramka jest ręczna —
    przed zamknięciem sesji przejrzyj każde NOWE zgłoszenie i sprawdź
    obecność (1)(2)(3). Naruszenie = **WARN** (nie CRIT: zgłoszenie bez
    pól nie niszczy danych, tylko wprowadza w błąd), odnotowywane jak
    każda inna flaga.

    ⚠️ **Ograniczenie znane i jawne:** ta bramka, jak każda bramka
    samo-raportująca (por. F-119, `KROK 3A` w `prawny-router-v3`), jest
    wiarygodna tylko wtedy, gdy pole (2) da się sprawdzić NIEZALEŻNIE.
    Sama deklaracja „zweryfikowano" bez identyfikatora, który druga osoba
    otworzy, jest fasadą tej samej klasy co usterka z TEST2. Skuteczność
    bramki mierzy dopiero test z grupą kontrolną z **F-113** — do jej
    zamknięcia obecność ZASADY 14 w pliku dowodzi wyłącznie obecności
    reguły, nie zmiany zachowania.

# STRUKTURA KATALOGU (przeniesione ze SKILL.md, treść bez zmian)

> ⛔ **KOREKTA 2026-08-20y — drzewo było nieaktualne o 15 plików.** Wymieniało
> 4 pliki `references/` (stan sprzed F-80) i pomijało CAŁY folder `scripts/`,
> mimo że YAML `references:`/`scripts:` naprawiono 2026-08-15h. Podawało też
> „460 wierszy" mapy Dz.U. przy faktycznych 509. **Przy każdej zmianie liczby
> plików aktualizuj OBA miejsca — YAML i to drzewo** (rozjazd jednego z drugim
> to ten sam wzorzec luki, który wykrywa `check_rejestracja_modulow.py`).

> ⚡ **2026-09-27m:** +`.mcp.json` (serwery MCP pluginu) i +`mcp-servers/` (74 pliki: źródła 9 serwerów z CBOSA,
> `dist/lex-mcp.mjs`, manifest rozszerzenia MCPB, instalator, skrypt budowy, README) — łącznie **192 pliki** (6.144: +`mcp-servers/LICENSE`). Drzewo niżej nie
> rozpisuje `mcp-servers/` — opis w `mcp-servers/README.md`. Licznik w pierwszej linii drzewa jest
> historyczny (stan 2026-09-09b).
> ⚡ **2026-10-04e:** +`scripts/check_mapy_aktow.py` (T45) — **189 plików**.
> ⚡ **2026-10-04d:** +`scripts/check_osiagalnosc_shared.py` (T44) — **188 plików**.
> ⚡ **2026-10-04b:** usunięte 40 reliktów (30 `mcp-servers/*-example/*`, 2 `.pyc`, 6 `references/` z 6.146, raporty pokrycia KPK/KRO), dodany `scripts/check_sieroty.py` (T43) — **187 plików**.
> ⚡ **2026-09-27s:** `mcp-servers/` scalony — wspólne `package.json`/`package-lock.json` i jeden `test_protokol.mjs` zamiast 10 kopii; 11 serwerów (+`wl-example`). Liczba plików skilla: `find . -type f | wc -l` (limit wydania 200).

```
audyt-systemu-v4/                               ← 89 plików (stan 2026-09-09b; licznik sprawdzony
│                                                  `find . -type f`, bez __pycache__. ⚡ Drzewo podawało
│                                                  82 przy 84 faktycznych PRZED tą turą — trzeci z rzędu
│                                                  rozjazd tego licznika (F-147: 71 przy 81). Ta tura
│                                                  dokłada 2 pliki: check_domeny_allowlist.py i
│                                                  F-152-pomiar-domen-2026-09-04.md)
├── SKILL.md                                    ← orchestrator (ten plik)
├── README.md                                   ← opis skilla dla czytelnika ludzkiego (NIE wczytywany
│                                                  przez żadną fazę; dopisany do drzewa 2026-08-23g)
├── modules/                                    ← 5 modułów, pełna lista w YAML `modules:`
│   ├── MOD-INTERLINIE.md                       ← zbędne puste linie (FAZA 2D-1)
│   ├── MOD-WSTAWKI.md                          ← wstawki opisowe (FAZA 2D-2)
│   ├── MOD-DESCRIPTION.md                      ← description, profil ≤200 (FAZA 2C)
│   ├── MOD-TRESC-MERYTORYCZNA.md               ← FAZA 3E, treść modułów DR po zmianie przepisu
│   └── MOD-PROPAGACJA-NOWELIZACJI.md           ← propagacja nowelizacji przez CAŁY system
├── widgets/
│   └── WIDGET-MENU.md                          ← menu interaktywne (FAZA 0B; 14 pozycji, poz. 14 → FAZA 0E)
├── scripts/                                    ← 47 plików (stan 2026-09-27e): testy T1-T4, T8, T9, T11-T36, T38,
│   │                                             orkiestrator, ci_check_shared (T6/T7),
│   │                                             check_rejestracja_modulow, sync ELI (3 pliki),
│   │                                             2 skrypty .sh, README.md — pełna lista w YAML
│   └── …                                         `scripts:`
└── references/                                 ← 44 pliki (31 w katalogu głównym + 13 w podfolderze)
    ├── AUDIT-JOURNAL.md                        ← dziennik audytów (kilka MB; nie wczytywać w całości — FAZA 0)
    ├── WARN-OTWARTE.md                         ← rejestr żywy otwartych flag (ZASADA 10)
    ├── CHANGELOG.md                            ← historia wersji orkiestratora (F-78)
    ├── CHECKLIST-DEDUP.md                      ← mapa pojęć → lokalizacje kanoniczne
    ├── REGRESSION-TEST-PLAN.md                 ← testy T1-T17
    ├── PORTALE-ORZECZNICZE-API.md              ← dostęp maszynowy do orzecznictwa/interpretacji
    ├── F-171-pomiar-domen-2026-09-09.md        ← surowy wynik T25 (52 sondy), 4 regresje — F-171
    ├── F-152-pomiar-domen-2026-09-04.md        ← surowy wynik T25 (40 sond), dowód zamknięcia F-152
    ├── SYNC-DZU-AUTOMATYCZNY.md                ← + HARMONOGRAM-CRON.md, FORMAT-RAPORTU-ROZNIC.md
    ├── SCHEDULED-TASK-COWORK.md                ← POZYCJA 11 menu (FAZA 0C)
    ├── PAMIEC-TRWALA-ROUTER.md                 ← POZYCJA 13 menu (FAZA 0D)
    ├── F-108-lista-MS-egzamin-2026.md          ← benchmark F-108 (52 akty MS; 52/52 B+/COV, 0 FULL)
    ├── mapa_dzu_2026-10-04.md                  ← mapa Dz.U. AKTUALNA (AUDYT-2026-10-04, 2026/1161)
    ├── mapa_dzu_2026-08-28.md                  ← generacja poprzednia; dane test_f108_consistency.py
    │                                             (starsze generacje usunięte w 6.208 — historia w Git)
    └── raporty-pokrycia-2026-08-13/            ← 12 raportów + indeks = 13 plików
```
