---
name: dr-03-prawo-karne-wykroczenia-egzekucja
version: "3.64"
description: "Prawo karne, wykroczenia i egzekucja: KK, KPK, KKW, KW, KPW, KKS, kwalifikacja karnomaterialna, tryby ścigania i wykonanie orzeczeń."
dependencies:
  requires:
    - shared
  # 2026-09-27e: jawna zależność (każdy skill systemu korzysta z `shared`); pole czytane przy imporcie z marketplace
---

> **Universal runtime:** przed wykonaniem zastosuj kanoniczny `shared/UNIVERSAL-RUNTIME-ADAPTER.md` z osobnego skilla `shared`. Lokalna sekcja adaptera poniżej jedynie go doprecyzowuje.


## ADAPTER RUNTIME — PORTABILITY (ChatGPT / Claude / inne hosty)

Ta sekcja zmienia wyłącznie wykonanie operacji technicznych. Merytoryka dziedzinowa, mapy aktów, hard gate’y, kolejność modułów i kryteria jakości tego DR-skilla pozostają bez zmian.

1. `view dr-03-prawo-karne-wykroczenia-egzekucja/<plik>` oraz `view modules/...` / `view references/...` oznaczają świeży odczyt odpowiedniego lokalnego pliku tego skilla. Literalna ścieżka `/mnt/skills/user` nie jest wymagana.
2. `view shared/<plik>` oznacza świeży odczyt z osobnego, kanonicznego skilla `shared`. NIE kopiuj `shared` do tej paczki. Brak obowiązkowego zasobu shared = fail-closed, nie substytucja pamięcią modelu.
3. `view <inny-skill>/<plik>` oznacza aktywację/odczyt wskazanego osobnego skilla. Nie vendoryzuj innych skilli do tego ZIP-a.
4. `web_search` / `web_fetch` i podobne nazwy oznaczają świeże wyszukanie/odczyt online przez równoważną funkcję hosta. Zachowaj wymagane źródła oficjalne, statusy weryfikacji i zakaz cytowania prawa z pamięci.
5. `show_widget`, `visualize:read_me`, `present_files`, `create_file`, shell/Python i podobne operacje są nazwami semantycznymi. Jeśli host nie ma literalnego narzędzia, użyj równoważnej funkcji natywnej bez omijania bramek jakości.
6. `/mnt/user-data/...` oznacza rzeczywiste załączniki użytkownika dostępne w bieżącym hoście; wymagany ponowny odczyt ma być faktycznym odczytem źródła.

**Zasada nadrzędna:** instrukcje, które są już zrozumiałe i wykonalne w bieżącym hoście, wykonuj bez konwersji. Adapter działa wyłącznie na granicy runtime.


# DR-03 — Prawo Karne, Wykroczenia, Egzekucja

## ⛔ OBOWIĄZKOWY KWALIFIKATOR — dla każdej sprawy karnej/wykroczeniowej

> Dodano: 2026-07-06 (utrwalenie preferencji użytkownika "Karne:
> +kwalifikator"). UWAGA DEDUP: zasada i pełne drzewo decyzyjne JUŻ
> istnieją jako `prawny-router-v3` UP-3 (sekcja "PREFERENCJE UŻYTKOWNIKA")
> + moduł kanoniczny poniżej — ten wpis to tylko punkt wejścia z poziomu
> DR-03, NIE nowa treść (nie duplikować dalej).

Dla KAŻDEJ sprawy karnej/wykroczeniowej (nie tylko na wyraźne żądanie
użytkownika) obowiązkowe jest przejście przez drzewo decyzyjne kwalifikacji
przed podaniem jakiejkolwiek analizy lub pisma:

```
view dr-03-prawo-karne-wykroczenia-egzekucja/modules/mod-KK-kwalifikator-karnomaterialny.md
```

Zasada naczelna modułu (skrót): nigdy nie kwalifikuj czynu bez przejścia
przez drzewo; kwalifikacja oparta na chronologii faktów, nie na pierwszym
pasującym przepisie; każdy przepis weryfikowany w ELI (RZĄD 1) przed użyciem
(zgodnie z zasadą 2 `prawo-polskie-v2/SKILL.md` / UP-2 routera). Jeśli czyn
wyczerpuje znamiona więcej niż jednego przepisu — kwalifikacja kumulatywna
(art. 11 § 2 KK), nie wybór arbitralny.

⚡ **STRUKTURA 2026-08-20 (F-78):** powyższy plik to teraz LEKKI INDEKSATOR
(104 linie) z tabelą nawigacyjną — treść merytoryczna 8 bloków tematycznych
znajduje się w podkatalogu `modules/kwalifikator-karnomaterialny/`. Wczytaj
najpierw indeks, potem WYŁĄCZNIE właściwy plik części wg tabeli. Ścieżka
`view` powyżej NIE wymagała zmiany — to zamierzona korzyść tej struktury.

## ⛔ HARD GATE — ZAKAZ CYTOWANIA Z PAMIĘCI

**PRZED każdym powołaniem przepisu, artykułu, terminu lub sygnatury:**
1. Zweryfikuj brzmienie i Dz.U. w `ELI (RZĄD 1)`
2. Zweryfikuj orzeczenie w `orzeczenia.ms.gov.pl` / `nsa.gov.pl` / `sn.pl`
3. **NIGDY** nie podawaj artykułu, terminu, kary ani sygnatury wyłącznie z pamięci modelu.


> ⛔ **SELF-CHECK ANTY-FASADA — obowiązkowy przed wysłaniem odpowiedzi/pisma**
> (podłączone 2026-08-24, flaga F-115 P3 — zamknięcie zakresu 16 skilli DR):
>
> ```
> view shared/SELF-CHECK-ANTY-FASADA.md
> ```
>
> Sprawdza dwie rzeczy: (1) czy w tekście stoi „zweryfikowano", data weryfikacji
> albo URL przy przepisie, dla którego NIE wywołano narzędzia W TEJ ODPOWIEDZI;
> (2) czy znacznik statusu nie został nadany treści WYGENEROWANEJ w tej odpowiedzi
> (AF-6). Treść listy jest w module, nie tutaj — celowo, żeby nie powstało kolejne
> miejsce dryfu (7 wcześniejszych kopii rozjechało się ze źródłem przy pierwszej
> zmianie brzmienia).
>
> ⛔ Wyzwalaczem jest BRAK WYWOŁANIA NARZĘDZIA dla danego twierdzenia w danej
> odpowiedzi — nie brak narzędzi w sesji. Niedostępność ELI (oba kanały) nie zwalnia z
> oznaczenia, tylko je wymusza; niedostępność ISAP to stan normalny.

---

## Zasada architektoniczna
- Jeden moduł = jeden akt prawny (tekst jednolity Dz.U.)
- Wyjątek: wydzielone rozdziały jednej ustawy mogą mieć osobny moduł (z adnotacją)
- Ten sam akt NIE może pokrywać dwóch różnych DR-skills

## DEFINICJE — shared/definicje/ (bezpośrednie, lazy loading per temat)

- `definicje/DEF-PROCEDURA.md` — termin zawity vs przedawnienie vs instrukcyjny
  (KRYTYCZNE: terminy zawite w KPK — apelacje, zażalenia 14 dni)
- `definicje/DEF-PRACA.md` — niealimentacja (art. 209 KK) — sekcja dolna pliku

- `definicje/DEF-INTERES-WLASNY-WYLACZENIA.md` — ⚠️ NOWE: świadek a interes
  własny (KPK art. 182-186 — prawo odmowy zeznań/odpowiedzi, "osoba najbliższa"
  z faktycznym wspólnym pożyciem — BAS-112)

## ORKA-BAS — Definicje wspomagające (shared/ORKA-BAS-LEKSYKON.md)

Przy sprawach z tej dziedziny rozważ doładowanie (`view`) definicji:
- BAS-013 Treści pornograficzne (art. 202 KK — brak definicji legalnej, ocenne)
- BAS-103 Uprawdopodobnienie (≠ udowodnienie — ORKA-REG-02)
- BAS-114 Mobbing a prawo karne (zbieg z art. 190/191/216/217/218 KK)
- BAS-118 Mowa nienawiści (art. 256-257 KK — brak definicji + zmiana 2024/2025)
- BAS-121 Handel ludźmi (art. 115 §22 KK — zgoda ofiary irrelewantna)
- BAS-129 Recydywa szczególna i multirecydywa (art. 64 KK — przesłanki łączne)
- BAS-130 Warunkowe umorzenie (art. 66 KK — 6 przesłanek + wykluczenia)
- BAS-134 Środki karne + zatarcie skazania (→ mod-prawa-obywatelskie-srodki-karne.md)
- BAS-W22 Czyn ciągły / "z góry powzięty zamiar" (art. 12 KK)
- BAS-W23 Mienie znacznej/wielkiej wartości (art. 115 §5-6 KK — progi zamrożone od 2010!)
- BAS-W24 Nieznaczna ilość narkotyku (art. 62a ustawy PN — brak definicji)
- BAS-131/132/133 Niewidomy / niepełnosprawność intelektualna / głuchota —
  obrona obligatoryjna art. 79 §1 pkt 2-4 KPK (→ mod-niewidomy-prawa-prawne.md,
  mod-niepelnosprawnosc-intelektualna-gluchota.md)

## Moduły (71 łącznie — ✓ 71 OK, ☐ 0 STUB; 1 przeniesiony do shared/)

Opisy zakresu i historia zmian modułów (wieloliniowe opisy wpisów, adnotacje NAPRAWA/Aktualizacja) są w `dr-03-prawo-karne-wykroczenia-egzekucja/references/moduly-opisy-i-historia.md` — `view` tego pliku, gdy potrzebny jest zakres lub historia konkretnego modułu (routing do modułów działa wyłącznie z listy poniżej).


  [✓] OK    mod-KK-current-state-COV
  [✓] OK    mod-KKW-current-state-COV
  [✓] OK    mod-KPK-current-state-COV
  [✓] OK    mod-KW-current-state-COV
  [✓] OK    mod-KPW-kodeks-postepowania-w-sprawach-o-wykroczenia
  [✓] OK    mod-narkomania-current-state-COV

```
  [✓] OK    mod-nielegalny-pobor-mediow
              (kwalifikacja karna nielegalnego poboru energii i innych mediów)
  [✓] OK    mod-KK-KPK-framework-karne
  [✓] OK    mod-KK-KPK-framework-szczegolowy
  [✓] OK    mod-KKW-kodeks-karny-wykonawczy
              (Kodeks karny wykonawczy — warunkowe przedterminowe zwolnienie (159-163), odroczenie/przerwa (150-158a), dozór elektroniczny (43a-43zf); ZAREJESTROWANY 2026-08-14e (F-77 rozszerzona) — moduł istniał od naprawy F-75, bez wpisu w checkliście)
  [✓] NOWY  mod-KKW-uzupelnienie-pokrycia-2026
              (pozostałe części KKW: ogólna, penitencjarna, ograniczenie wolności, zwolnienie, środki i część wojskowa)
  [✓] NOWY  mod-ustawa-oplaty-w-sprawach-karnych
              (F-108/8: ustawa z 23.06.1973 r.; poziom B+, pełna mapa art. 1–23 i aktualne stawki z Rządu 1)
  [✓] OK    mod-przerobki-modyfikacje-pojazdow
              (v1.1.0 — dopuszczalne modyfikacje pojazdów, homologacja, motocykle, tachografy; ⚠️ zawiera flagę F-14 (projekt ws. UTO/hulajnóg); ZAREJESTROWANY 2026-08-14e (F-77 rozszerzona))
  [✓] OK    mod-podmiana-czesci-naprawa-oszustwo
              (Podmiana części przy naprawie jako oszustwo; ⚠️ wątek przywłaszczenia oryginalnej części (284 KK) — punkt otwarty w F-26; ZAREJESTROWANY 2026-08-14e (F-77 rozszerzona))
  [✓] OK    mod-lincz-ochrona-swiadkow-lowcy-pedofili
              (Samosąd/lincz, ochrona świadków, tzw. „łowcy pedofilów” — granice legalności działań obywatelskich; ZAREJESTROWANY 2026-08-14e (F-77 rozszerzona))
  [✓] OK    mod-KK-art190a-stalking
  [✓] OK    mod-KK-art207-przemoc-domowa
  [✓] OK    mod-KK-art267-269c-cyberprzestepstwa
  [✓] OK    mod-KK-cyberprzestepstwa-szczegolowy
  [✓] OK    mod-KK-kodeks-karny
  [✓] OK    mod-KK-kwalifikator-karnomaterialny
  [✓] OK    mod-czynny-zal-KK-KKS-samooskarzenie
  [✓] OK    mod-dobrowolne-poddanie-sie-karze-KPK
  [✓] OK    mod-KK-art18-22-formy-popelnienia
  [✓] OK    mod-KK-art10-odpowiedzialnosc-nieletnich
  [✓] OK    mod-KK-art64-recydywa
  [✓] OK    mod-KK-art69-84-warunkowe-zawieszenie-zwolnienie
  [✓] OK    mod-KK-art101-105-przedawnienie-karalnosci
  [✓] OK    mod-KK-art148-162-przeciwko-zyciu-zdrowiu
  [✓] OK    mod-KK-art212-216-przeciwko-czci
  [✓] OK    mod-KK-art222-226-ochrona-funkcjonariusza
  [✓] OK    mod-KK-art228-231-korupcja-urzednicza
  [✓] OK    mod-KK-art250a-korupcja-wyborcza
  [✓] OK    mod-KK-art255b-patostreaming
              (nadrobienie 2026-07-21, dodany 2026-07-18)
  [✓] OK    mod-KK-art270-310-falszerstwa-dokumentow
  [✓] NOWY  mod-KK-art278-295-przestepstwa-przeciwko-mieniu
  [✓] OK    mod-KK-art296-naduzycie-zaufania
  [✓] OK    mod-KK-art296a-korupcja-sektor-prywatny
  [✓] OK    mod-KK-art305-zmowa-przetargowa-karna
  [✓] OK    mod-KK-przemoc-domowa-szczegolowy
  [✓] OK    mod-KKS-karny-skarbowy-i-AML
  [✓] NAPRAWIONY 2026-08-14 (F-75)
  [✓] OK    mod-KPK-tryby-scigania
  [✓] NOWY  mod-tajemnica-zawodowa-poufnosc
  [✓] NOWY  mod-przymusowe-leczenie-odwykowe
  [✓] NOWY  mod-KPK-wspolpraca-miedzynarodowa-karna
  [✓] OK    mod-KW-KPW-framework-szczegolowy
  [✓] OK    mod-KW-kodeks-wykroczen
  [✓] OK    mod-KW-art1-48-czesc-ogolna
  [✓] OK    mod-KW-art119-131-przeciwko-mieniu
  [✓] OK    mod-KW-art49-64-porzadek-publiczny
  [✓] OK    mod-KW-art65-69-instytucje
               (dodany 2026-08-28: Rozdz. IX KW — usuwa ostatnią lukę numeracyjną między art. 64 i 70; art. 65/65a, 66/66a-66c, 67-69; verified current-state ELI)
  [✓] OK    mod-KK-art127-139-przeciwko-RP
  [✓] OK    mod-KK-art163-172-bezpieczenstwo-powszechne
  [✓] OK    mod-KK-art181-188a-przeciwko-srodowisku
  [✓] OK    mod-KW-art70-118-bezpieczenstwo-osoba-zdrowie
  [✓] OK    mod-KW-art132-166-pozostale-rozdzialy
  [✓] OK    mod-grzywny-mandaty-szczegolowe
  [✓] OK    mod-PRD-prawo-jazdy-punkty-karne
  [✓] OK    mod-PRD-nowe-przestepstwa-drogowe-BRD
  [✓] OK    mod-KK-art291-pranie-pieniedzy
  [✓] OK    mod-swiadek-koronny-duzy-maly
  [✓] OK    mod-ustawa-fundusz-pomocy-pokrzywdzonym
              (dopisany do listy 2026-07-15, plik istniał wcześniej)
  [✓] OK    mod-ustawa-narkomania
  [✓] OK    mod-KPK-mediacja-sprawiedliwosc-naprawcza
  [✓] OK    mod-ustawa-odpowiedzialnosc-podmiotow-zbiorowych
  [✓] OK    mod-KK-art233-244b-przeciwko-wymiarowi-sprawiedliwosci
  [✓] OK    mod-KK-slupy-fikcyjna-reprezentacja-spolki
  [✓] OK    mod-poreczenie-majatkowe-kaucja-karna
  [✓] NOWY  mod-KPK-srodki-zapobiegawcze-tymczasowe-aresztowanie
  [✓] NOWY  mod-KPK-podstawy-odwolawcze-przeslanki-zarzuty-biegli
  [✓] OK    mod-KK-art263-bron-nielegalna
```

> **Przeniesiony do shared/ (2026-07-12):** `mod-KK-stalking-szczegolowy` był
> bajt-w-bajt identyczny z dawną kopią routera `stalking-nekanie`
> (wykryte przez `ci_check_shared.py`; obecny plik routera jest wyłącznie bridge’em). Scalony pod jedną kanoniczną lokalizacją:
> `view shared/STALKING-NEKANIE.md`. Ładuj stamtąd bezpośrednio —
> `mod-KK-art190a-stalking.md` zawiera odesłanie. Pełny opis:
> `audyt-systemu-v4/references/CHECKLIST-DEDUP.md` NOTA-12.

## Jak wywołać

```
view dr-03-prawo-karne-wykroczenia-egzekucja/modules/[nazwa-modulu].md
```

## Lokalna mapa aktów prawnych

```
view dr-03-prawo-karne-wykroczenia-egzekucja/MAPA-AKTOW.md
```

## Mapa pokrycia treściowego (planowanie rozwoju skilla)

Rejestr informacyjny — NIE krok obowiązkowy przy obsłudze konkretnej sprawy.
Przydatny przy planowaniu, które luki uzupełnić w pierwszej kolejności
(F-83, zasilony 2026-08-22 z audytu źródłowego 2026-08-13):

```
view dr-03-prawo-karne-wykroczenia-egzekucja/MAPA-POKRYCIA.md
```

## Powiązania zewnętrzne
- Wchodzi z: `prawo-polskie-v2` → `ROUTING-MAP.md` → ten skill
- Wychodzi do: `pisma-procesowe-v3` / `analiza-sadowa-v6` / `orzeczenia-sadowe-v2`
- Weryfikacja prawa: ELI (RZĄD 1)
- Orzecznictwo: orzeczenia.ms.gov.pl, sn.pl, nsa.gov.pl

## ⚖️ DISCLAIMER (obowiązkowy)

Po zakończeniu analizy lub przed oddaniem odpowiedzi zawierającej ocenę prawną:

```text
view shared/DISCLAIMER.md
```

Wybierz wariant odpowiedni do trybu:
- **PRAWNIK / kancelaria** → wariant techniczny (art. 4 Prawa o adwokaturze / art. 6 u.r.p.)
- **LAIK / pro se** → wariant uproszczony (informacja ≠ porada prawna)

Disclaimer musi być **ostatnim elementem** każdej odpowiedzi zawierającej analizę prawną,
ocenę szans, kwalifikację prawną lub interpretację przepisu.
