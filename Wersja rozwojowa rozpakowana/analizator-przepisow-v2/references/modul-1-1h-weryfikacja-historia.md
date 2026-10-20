# Moduł 1 (weryfikacja i pobranie przepisu) i Moduł 1H (stan prawny na datę) — analizator-przepisow-v2

> Plik przeniesiony ze SKILL.md bez zmian treści (progressive disclosure). Wczytaj w całości przed wykonaniem odpowiedniego kroku.

## MODUŁ 1 — WERYFIKACJA I POBRANIE PRZEPISU

### Hierarchia źródeł (RZĄD 1 / RZĄD 2 / RZĄD 3)

> ⛔ **KANONICZNA LOKALIZACJA (od 2026-07-15):** pełna treść tej hierarchii
> (definicje RZĄD 1/2A/2B/3, listy domen, zakaz mieszania rzędów, znaczniki
> obowiązkowe, procedura H-1→H-4) przeniesiona do
> `view shared/HIERARCHIA-ZRODEL.md` — plik jest teraz
> współdzielony przez `shared/PRAWO-HARDGATE.md`, `shared/WERYFIKACJA-SLAD.md`
> i każdy inny skill podający linki źródłowe, nie tylko ten moduł.
> Wczytaj ten plik PRZED podaniem jakiegokolwiek linku/URL w analizie
> przepisu — kategoryzacja RZĄD jest OBOWIĄZKOWA dla każdego źródła,
> nie tylko dla brzmienia przepisu.
>
> Powód wydzielenia: kategoryzacja obowiązywała dotąd wyłącznie lokalnie
> w tym skillu i nie była wymuszana przy linkach/kotwicach generowanych
> poza kontekstem analizy przepisu (np. w odpowiedziach opartych na
> `shared/WERYFIKACJA-SLAD.md` bez wczytania tego modułu) — zgłoszone przez
> użytkownika i naprawione przeniesieniem do `shared/`.

### Procedura weryfikacji (OBOWIĄZKOWA)

```
1. E-1 ELI: api.sejm.gov.pl/eli/acts/search?title=[nazwa aktu] → aktualny t.j.
   (rok/poz.), metryka /eli/acts/DU/{rok}/{poz} — kanałem kodu (curl/skrypt);
   host bez kanału kodu → B-1 web_search „eli.gov.pl DU {rok} {poz}” → B-2 web_fetch
2. Odczyt treści: /eli/acts/DU/{rok}/{poz}/text.pdf (t.j.; pułapka /text.html
   — B-T1…B-T3 PRAWO-HARDGATE). Link ISAP dopisz dla czytelnika (E-2).
   Aktu nie da się pobrać z RZĘDU 1 (ELI ani ISAP — awaria serwera, timeout,
   blokada; zapisz próby) → obowiązkowo E-3 LEX/Legalis → E-4 ArsLege.
3. Zlokalizuj dokładny przepis (artykuł / paragraf / ustęp / punkt)
4. Z treści obwieszczenia o t.j. wypisz nowelizacje JUŻ UWZGLĘDNIONE
   (obwieszczenia standardowo wymieniają: „uwzględnia zmiany wprowadzone
   ustawami z dnia..."). To jest punkt wyjścia — te zmiany są już wliczone,
   nie trzeba ich szukać ponownie w kroku 4A.
4A. ⛔ KROK 2C shared/PRAWO-HARDGATE.md — OSOBNE zapytanie o WSZYSTKIE
    akty zmieniające OPUBLIKOWANE PO dacie t.j. z kroku 1-2 (skorygowano
    2026-08-23f, po pytaniu użytkownika — NIE zatrzymuj się na pierwszej
    znalezionej nowelizacji; między t.j. a dziś mogło wejść w życie
    kilka kolejnych zmian tego samego przepisu). To NIE jest to samo
    zapytanie co krok 1 — krok 1 szuka t.j., krok 4A szuka WSZYSTKICH
    nowelizacji OGŁOSZONYCH PO nim, w całym przedziale od daty t.j. do
    dziś. Zapisz PEŁNĄ LISTĘ chronologiczną wyników zawsze, także gdy
    pusta (pole „Sprawdzono po t.j." w Karcie Przepisu niżej). Gdy
    nowelizacji więcej niż jedna — ustal, które brzmienie obowiązuje
    NA DATĘ ANALIZY (kolejność wejścia w życie, ewentualne vacatio
    legis), nie zakładaj że najnowsza znaleziona = aktualna. Obowiązkowe
    dla przepisów NIOSĄCYCH ROZSTRZYGNIĘCIE, opcjonalne dla przywołań
    kontekstowych.
5. Sprawdź czy przepis nie został uchylony lub zmieniony
6. Zapisz DOSŁOWNĄ treść z oficjalnego źródła
```

### Karta Przepisu

```
KARTA PRZEPISU
Akt prawny:         [pełna nazwa + rok + Dz.U.]
Numer przepisu:     [art./§/ust./pkt]
Tekst jednolity z:  [Dz.U. RRRR poz. NNN — z metryki ELI]
Nowelizacje w t.j.: [lista ustaw zmieniających już uwzględnionych w t.j.,
                     z treści obwieszczenia]
Nowelizacje po t.j.:[TAK: pełna lista chronologiczna / brak — patrz KROK
                     2C — / NIE sprawdzono]
Status:             Obowiązuje / Zmieniony / Uchylony
Data analizy:       [data stanu prawnego]
Źródło URL:         [link ELI (odczyt) + link ISAP (dla człowieka); inne źródło tylko wg E-3/E-4]

PEŁNA TREŚĆ PRZEPISU:
[tekst dosłownie z oficjalnego źródła]
```

---

## MODUŁ 1H — STAN PRAWNY NA WYBRANĄ DATĘ

Stosuj gdy użytkownik chce zbadać przepis w stanie na konkretną datę przeszłą.

```
1. Ustal datę docelową: [DD.MM.RRRR]
2. W ELI ustal historię aktu: /eli/acts/DU/{rok}/{poz}/references (zmiany,
   teksty jednolite) — ISAP tylko jako link dla czytelnika
3. Zidentyfikuj tekst jednolity obowiązujący W DNIU docelowym
4. Pobierz historyczną wersję przepisu
5. Oznacz wyraźnie: "STAN NA [data]" we wszystkich wynikach
```

### Raport historyczny

```
ANALIZA ZMIAN PRZEPISU W CZASIE
Przepis:          [identyfikator]
Data docelowa:    [DD.MM.RRRR]

Chronologia zmian:
┌──────────────┬─────────────────────┬────────────────────────┐
│ Data zmiany  │ Nowelizacja (Dz.U.) │ Co się zmieniło        │
├──────────────┼─────────────────────┼────────────────────────┤
│ [data]       │ Dz.U. [rok] poz.[n] │ [opis zmiany]          │
└──────────────┴─────────────────────┴────────────────────────┘

Wersja na [datę docelową]: [treść — dosłownie]
Wersja aktualna:           [treść dziś — dosłownie]
Różnice procesowo istotne: [co się zmieniło i jak wpływa]
```
