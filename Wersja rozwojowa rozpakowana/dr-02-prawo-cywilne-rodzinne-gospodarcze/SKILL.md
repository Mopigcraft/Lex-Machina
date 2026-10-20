---
name: dr-02-prawo-cywilne-rodzinne-gospodarcze
version: "3.95"
description: "Prawo cywilne, rodzinne i gospodarcze: KC, KPC, spadki, rodzina, spółki, upadłość, restrukturyzacja, windykacja i odpowiedzialność kontraktowa/deliktowa."
dependencies:
  requires:
    - shared
  # 2026-09-27e: jawna zależność (każdy skill systemu korzysta z `shared`); pole czytane przy imporcie z marketplace
---

> **Universal runtime:** przed wykonaniem zastosuj kanoniczny `shared/UNIVERSAL-RUNTIME-ADAPTER.md` z osobnego skilla `shared`. Lokalna sekcja adaptera poniżej jedynie go doprecyzowuje.


## ADAPTER RUNTIME — PORTABILITY (ChatGPT / Claude / inne hosty)

Ta sekcja zmienia wyłącznie wykonanie operacji technicznych. Merytoryka dziedzinowa, mapy aktów, hard gate’y, kolejność modułów i kryteria jakości tego DR-skilla pozostają bez zmian.

1. `view dr-02-prawo-cywilne-rodzinne-gospodarcze/<plik>` oraz `view modules/...` / `view references/...` oznaczają świeży odczyt odpowiedniego lokalnego pliku tego skilla. Literalna ścieżka `/mnt/skills/user` nie jest wymagana.
2. `view shared/<plik>` oznacza świeży odczyt z osobnego, kanonicznego skilla `shared`. NIE kopiuj `shared` do tej paczki. Brak obowiązkowego zasobu shared = fail-closed, nie substytucja pamięcią modelu.
3. `view <inny-skill>/<plik>` oznacza aktywację/odczyt wskazanego osobnego skilla. Nie vendoryzuj innych skilli do tego ZIP-a.
4. `web_search` / `web_fetch` i podobne nazwy oznaczają świeże wyszukanie/odczyt online przez równoważną funkcję hosta. Zachowaj wymagane źródła oficjalne, statusy weryfikacji i zakaz cytowania prawa z pamięci.
5. `show_widget`, `visualize:read_me`, `present_files`, `create_file`, shell/Python i podobne operacje są nazwami semantycznymi. Jeśli host nie ma literalnego narzędzia, użyj równoważnej funkcji natywnej bez omijania bramek jakości.
6. `/mnt/user-data/...` oznacza rzeczywiste załączniki użytkownika dostępne w bieżącym hoście; wymagany ponowny odczyt ma być faktycznym odczytem źródła.

**Zasada nadrzędna:** instrukcje, które są już zrozumiałe i wykonalne w bieżącym hoście, wykonuj bez konwersji. Adapter działa wyłącznie na granicy runtime.


# DR-02 — Prawo Cywilne, Rodzinne i Gospodarcze

## ⛔ HARD GATE — ZAKAZ CYTOWANIA Z PAMIĘCI

**PRZED każdym powołaniem przepisu, artykułu, terminu lub sygnatury:**
1. Zweryfikuj brzmienie i Dz.U. w `ELI (RZĄD 1)`
2. Zweryfikuj orzeczenie w `orzeczenia.ms.gov.pl` / `nsa.gov.pl` / `sn.pl`
3. **NIGDY** nie podawaj artykułu, terminu, kary ani sygnatury wyłącznie z pamięci modelu.

> Procedura szczegółowa (warstwa strukturalna SAOS/MCP, kontrakt sygnatur,
> gradient weryfikacji cytatu): `view shared/PRAWO-HARDGATE.md` — wczytaj
> PRZED pierwszym przepisem w każdej odpowiedzi. Integruje się z
> `shared/ISAP-AUDIT-PROTOCOL.md`.


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

## Upadłość i restrukturyzacja — wejście operacyjne

Upadłość: `modules/mod-PrUpad-zrodla-i-wersje.md`.
Restrukturyzacja: `modules/mod-PrRestr-zrodla-i-wersje.md`.
Pełne korpusy: `references/prup/`, `references/prrestr/`.
Katalog każdego nagłówka: `references/insolvency/katalog.md`.
Wersje i przepisy przejściowe: `references/insolvency/wersje-i-przepisy-przejsciowe.md`.
`scripts/insolvency.py coverage` sprawdza integralność i pełność routingu.
Testy: `scripts/test_prup.py`, `scripts/test_insolvency.py` (`python3 -m unittest test_prup test_insolvency` z katalogu `scripts/`; integralność źródła, granice artykułów, wersje i routing — nie poprawność rozstrzygnięć).
Dostęp do całego tekstu i procedur nie jest deklaracją pełnego komentarza
orzeczniczego; dobierz prawo do dat i faktów konkretnej sprawy.

## Zasada architektoniczna
- Jeden moduł = jeden akt prawny (tekst jednolity Dz.U.)
- Wyjątek: wydzielone rozdziały jednej ustawy mogą mieć osobny moduł (z adnotacją)
- Ten sam akt NIE może pokrywać dwóch różnych DR-skills
- **Zakaz cytowania przepisów z pamięci modelu podczas sesji — każde brzmienie weryfikuj w ELI (RZĄD 1)**
- Źródło podstawowe: ELI (RZĄD 1); ISAP — adres dla człowieka; LEX/Legalis, potem ArsLege — gdy aktu nie da się pobrać z RZĘDU 1 (awaria serwera, timeout, blokada) (kanon E-1…E-5: `shared/HIERARCHIA-ZRODEL.md`)

## DEFINICJE — shared/definicje/ (bezpośrednie, lazy loading per temat)

- `definicje/DEF-PODMIOTY-WLASNOSC.md` — osoba fizyczna/prawna, przedsiębiorca,
  konsument, nieruchomość, posiadanie, własność, "rzecz" (art. 45 KC)
- `definicje/DEF-ODPOWIEDZIALNOSC-SZKODA.md` — szkoda (damnum emergens/lucrum
  cessans), odpowiedzialność cywilna, odszkodowanie; ⚠️ NOWE: siła wyższa
  (brak def. ustawowej, 3 przesłanki SN) + rebus sic stantibus / art. 357¹ KC
  (4 przesłanki nieostre, tryb wyłącznie powództwem, granice modyfikacji umowy)
- `definicje/DEF-PROCEDURA.md` — termin zawity vs przedawnienie vs instrukcyjny,
  strona postępowania
- `definicje/DEF-CYWILNE-WYKLADNIA.md` — rękojmia vs gwarancja (reforma 2023)

- `definicje/DEF-INTERES-WLASNY-WYLACZENIA.md` — ⚠️ NOWE: czynność prawna
  ukryta/pozorna (art. 83 KC — symulacja, dysymulacja, ochrona osoby trzeciej
  w dobrej wierze), wyłączenie sędziego/biegłego z powodu interesu własnego
  (art. 48-49/281 KPC + TK P 10/19), świadek i jego interes (art. 233/261 KPC)

## ORKA-BAS — Definicje wspomagające (shared/ORKA-BAS-LEKSYKON.md)

Przy sprawach z tej dziedziny rozważ doładowanie (`view`) definicji:
- BAS-112 Faktyczne wspólne pożycie (art. 115 §11 KK — osoba najbliższa)
- BAS-119 Przedsiębiorca (Prawo przedsiębiorców art. 4)
- BAS-126 Zasiedzenie nieruchomości (art. 172 KC — przesłanki, dobra/zła wiara)
- BAS-127 Hipoteka (akcesoryjność, pierwszeństwo, wpis do KW)
- BAS-128 Bezpodstawne wzbogacenie (art. 405 KC — 4 przesłanki)
- BAS-W13 Niezgodność towaru z umową B2C (od 01.01.2023 — u.p.k. art. 43a-43n)
- BAS-W26 Szkoda / damnum emergens / lucrum cessans (art. 361 §2 KC)
- BAS-W27 Termin zawity vs przedawnienie vs instrukcyjny (KRYTYCZNE rozróżnienie)
- BAS-W28 Nadużycie prawa (art. 5 KC — zasada "czystych rąk")
- BAS-W30 Moc dowodowa dokumentu urzędowego vs prywatnego (art. 243-245 KPC)
- BAS-W31 Właściwość miejscowa sądu (ogólna, przemienna, wyłączna)
- BAS-W32 Przedawnienie po reformie 2018 (6 lat ogólny, terminy szczególne)
- BAS-W33 Kara umowna — miarkowanie (art. 484 §2 KC)
- BAS-W34 Odsetki: kapitałowe vs za opóźnienie vs handlowe (różne stopy!)
- BAS-W35 Nakaz zapłaty: sprzeciw vs zarzuty vs EPU (różne terminy/skutki)

## Moduły (85 łącznie — rejestracja w SKILL.md; głębokość w MAPA-POKRYCIA)

Opisy zakresu i historia zmian modułów (wieloliniowe opisy wpisów, adnotacje NAPRAWA/Aktualizacja) są w `dr-02-prawo-cywilne-rodzinne-gospodarcze/references/moduly-opisy-i-historia.md` — `view` tego pliku, gdy potrzebny jest zakres lub historia konkretnego modułu (routing do modułów działa wyłącznie z listy poniżej).


  [✓] OK    mod-KC-current-state-COV
  [✓] OK    mod-KPC-current-state-COV
  [✓] OK    mod-Prawo-przedsiebiorcow-current-state-COV
  [✓] OK    mod-ustawa-zastaw-rejestrowy

```
  [✓] OK    mod-transakcje-handlowe-opoznienia
              (F-108/46: rdzeń cywilny B; gałęzie administracyjne/historyczne częściowe)
  [✓] NOWY  mod-prawo-przedsiebiorcow
              (F-108/51: dedykowany moduł B, pełna mapa rozdziałów; RZĄD 1 ELI)
  [✓] NOWY  mod-KSH-uzupelnienie-pokrycia-2026
              (pozostałe tytuły KSH: ogólne, partnerska/SKA, sp. z o.o., PSA, S.A., transgraniczne i karne)
  [✓] NOWY  mod-ustawa-ubezpieczenia-obowiazkowe-UFG-PBUK
              (F-108/41: osobny akt, Dz.U. 2026 poz. 783 t.j.; poziom B, UFG/PBUK/OC)
  [✓] NOWY  mod-ustawa-fundacja-rodzinna
              (F-108/52: ustawa o fundacji rodzinnej; poziom B, mapa 16 rozdziałów)
  [✓] OK    mod-KPC-art162-zastrzezenie-protokol
              (art. 162 KPC oraz powiązania z art. 172 § 2¹ i art. 380)
  [✓] NOWY  mod-KPC-uzupelnienie-pokrycia-2026
              (krytyczne luki audytu KPC: orzeczenia, postępowania odrębne, nieproces, egzekucja, jurysdykcja)
  [✓] OK    mod-kaucja-najem-lokalu
              (kaucja przy najmie zwykłym i okazjonalnym)
  [✓] NOWY  mod-KRO-opieka-i-kuratela
  [✓] NOWY  mod-ustawa-ochrona-praw-lokatorow-najem-eksmisja
  [✓] NOWY  mod-KW-ksiega-wieczysta-zakup-nieruchomosci
  [✓] NOWY  mod-ustawa-frankowa-2026-procedura
  [✓] NOWY  mod-sklad-sadu-liczba-sedziow
  [✓] NOWY  mod-liczba-pelnomocnikow-strona-samodzielna
  [✓] NOWY  mod-parabanki-chwilowki-lombardy-lichwa
  [✓] NOWY  mod-pies-droga-rowerowa-odpowiedzialnosc
  [✓] NOWY  mod-ustawa-kredyt-konsumencki-SKD
  [✓] OK    mod-KC-cywilne-zobowiazania-odpowiedzialnosc
  [✓] OK    mod-KC-spadki
  [✓] NOWY  mod-KC-spadki-zachowek-dzial-rozrzadzenia
  [✓] NOWY  mod-KC-spadki-dlugi-umowy-transgraniczne
  [✓] OK    mod-KC-konsumenckie
  [✓] OK    mod-KC-ubezpieczenia
  [✓] NOWY  mod-KC-kredyty-frankowe
  [✓] OK    mod-KRO-rodzinne
  [✓] OK    mod-ubezwlasnowolnienie-opieka-kuratela
  [✓] OK    mod-KRO-zawarcie-malzenstwa-bigamia-transgraniczne
  [✓] OK    mod-KRO-przysposobienie-adopcja-miedzynarodowa
  [✓] OK    mod-piecza-zastepcza-rodzina-zastepcza
  [✓] OK    mod-KSH-spolki-handlowe
  [✓] NOWY  mod-KSH-organy-spolki-zoo
  [✓] OK    mod-reklama-wobec-nieletnich
              (nadrobienie zaległości w SKILL.md — moduł już istniał)
  [✓] OK    mod-prawo-wekslowe-czekowe
  [✓] OK    mod-wekslowe-kontrola-przedsiebiorcy-koncesje
  [✓] OK    mod-KSH-wrogie-przejecie-obrona-bialy-rycerz
  [✓] NOWY  mod-KSH-spolki-osobowe-rada-nadzorcza
  [✓] OK    mod-PrRestr-zrodla-i-wersje
              (Prawo restrukturyzacyjne — pełny korpus i sposób użycia)
  [✓] OK    mod-PrRestr-wejscie-plan-test
              (Restrukturyzacja — kwalifikacja sprawy, plan i test zaspokojenia)
  [✓] OK    mod-PrRestr-pzu
              (Postępowanie o zatwierdzenie układu — pełny przebieg)
  [✓] OK    mod-PrRestr-ppu-pu
              (Przyspieszone postępowanie układowe i postępowanie układowe)
  [✓] OK    mod-PrRestr-sanacja
              (Sanacja — zarząd, działania sanacyjne i układ)
  [✓] OK    mod-PrRestr-procedura-zakonczenie
              (Restrukturyzacja — procedura wspólna, zakończenie i upadłość)
  [✓] OK    mod-PrRestr-odrebne-miedzynarodowe
              (Restrukturyzacja — transgraniczne, odrębne, karne i przejściowe)
  [✓] OK    mod-PrUpad-wniosek-ogloszenie
              (Upadłość — przesłanki, wniosek, zabezpieczenie i pre-pack)
  [✓] OK    mod-PrUpad-skutki-masa-bezskutecznosc
              (Upadłość — masa, umowy, bezskuteczność i procesy)
  [✓] OK    mod-PrUpad-organy-procedura
              (Upadłość — organy, wierzyciele i wspólna procedura)
  [✓] OK    mod-PrUpad-zakonczenie-zakaz-karne
              (Upadłość — zakończenie, oddłużenie przedsiębiorcy, zakaz i przepisy końcowe)
  [✓] OK    mod-PrUpad-zrodla-i-wersje
              (Prawo upadłościowe — pełny tekst, wersje i nawigacja; źródło i procedura, fresh/temporal gate)
  [✓] OK    mod-PrUpad-wierzytelnosci-235-266
              (PrUp — zgłoszenia, sprawdzanie i lista wierzytelności; źródło i procedura, fresh/temporal gate)
  [✓] OK    mod-PrUpad-podzial-335-360
              (PrUp — fundusze masy, kategorie i plan podziału; źródło i procedura, fresh/temporal gate)
  [✓] OK    mod-PrUpad-syndyk-likwidacja
              (PrUp — czynności syndyka, sprawozdawczość i likwidacja; źródło i procedura, fresh/temporal gate)
  [✓] OK    mod-PrUpad-konsument-workflow
              (PrUp — upadłość konsumencka w pracy syndyka; źródło i procedura, fresh/temporal gate)
  [✓] OK    mod-PrUpad-upadlosc-restrukturyzacja
              (Upadłość i restrukturyzacja — kwalifikacja i nawigacja; źródło i procedura, fresh/temporal gate)
  [✓] OK    mod-PrUpad-uklad-likwidacja-zakonczenie
              (Układ w upadłości i powiązanie z likwidacją; źródło i procedura, fresh/temporal gate)
  [✓] OK    mod-PrUp-PrRestr-uzupelnienie-pokrycia-2026
              (Prawo upadłościowe i restrukturyzacyjne — wspólna nawigacja; źródło i procedura, fresh/temporal gate)
  [✓] OK    mod-PrUpad-postepowania-odrebne-426-491-38
              (Prawo upadłościowe — postępowania odrębne od art. 426 do art. 491^38; źródło i procedura, fresh/temporal gate)
  [✓] OK    mod-PrUpad-likwidacja-miedzynarodowe-szczegolne
              (Prawo upadłościowe — dalsza likwidacja, postępowanie międzynarodowe i odrębne; źródło i procedura, fresh/temporal gate)
  [✓] OK    mod-PrRestr-dzial-III-nadzorca-zarzadca
              (Nadzorca i zarządca — kompetencje, kontrola i wynagrodzenie; źródło i procedura, fresh/temporal gate)
  [✓] OK    mod-PrRestr-dzial-IV-uczestnicy-wierzyciele
              (Restrukturyzacja — uczestnicy, spis, zgromadzenie i rada; źródło i procedura, fresh/temporal gate)
  [✓] OK    mod-PrRestr-dzial-V-pomoc-publiczna
              (Restrukturyzacja — pomoc publiczna i test prywatnego wierzyciela; źródło i procedura, fresh/temporal gate)
  [✓] NOWY  mod-ustawa-pomoc-ratowanie-restrukturyzacja-przedsiebiorcow
  [✓] OK    mod-PrRestr-dzial-VII-uklad-czesciowy
              (Układ częściowy — wybór wierzycieli, ochrona i głosowanie; źródło i procedura, fresh/temporal gate)
  [✓] OK    mod-PrRestr-dzial-VI-uklad
              (Układ — zakres, propozycje, głosowanie, zatwierdzenie i wykonanie; źródło i procedura, fresh/temporal gate)
  [✓] NOWY  mod-ustawa-doradca-restrukturyzacyjny-zawod
  [✓] OK    mod-KPC-egzekucja-windykacja
  [✓] NOWY  mod-KPC-nieproces-czesc-ogolna
  [✓] NOWY  mod-KPC-prawomocnosc-granice-apelacji
  [✓] OK    mod-ustawa-prawa-konsumenta
  [✓] OK    mod-ustawa-UZNK-nieuczciwa-konkurencja
  [✓] OK    mod-ustawa-UOKIK-antymonopolowe
  [✓] OK    mod-ustawa-monopole-panstwowe
  [✓] OK    mod-rzeczy-znalezione-zasiedzenie
  [✓] OK    mod-ustawa-deweloperska
  [✓] OK    mod-ustawa-KRS-rejestr-sadowy
  [✓] OK    mod-ustawa-fundacje-stowarzyszenia
  [✓] NOWY  mod-prawo-spoldzielcze
              (F-108/13 P3: wydzielony akt, poziom B, Dz.U. 2026 poz. 521)
  [✓] NOWY  mod-ustawa-spoldzielnie-mieszkaniowe
              (F-108/34 P3: wydzielony akt, poziom B+, Dz.U. 2026 poz. 889)
  [✓] OK    mod-ustawa-spoldzielnie-wlasnosc-lokali
  [✓] OK    mod-KP-art943-mobbing-dyskryminacja
  [✓] OK    mod-ustawa-cudzoziemcy
  [✓] OK    mod-ustawa-timeshare-zastaw-rejestrowy
```

## Jak wywołać

```
view dr-02-prawo-cywilne-rodzinne-gospodarcze/modules/[nazwa-modulu].md
```

## Lokalna mapa aktów prawnych

```
view dr-02-prawo-cywilne-rodzinne-gospodarcze/MAPA-AKTOW.md
```

## Mapa pokrycia treściowego (planowanie rozwoju skilla)

Rejestr informacyjny — NIE krok obowiązkowy przy obsłudze konkretnej sprawy.
Przydatny przy planowaniu, które luki uzupełnić w pierwszej kolejności, oraz
przy nowelizacjach — pokazuje od razu czy dotknięty fragment ma treść do
zaktualizowania. (F-83, zasilony 2026-08-22 z KSH i PrUp/PrRestr; KPC
świadomie pominięty jako częściowo przestarzały względem stanu po F-65):

```
view dr-02-prawo-cywilne-rodzinne-gospodarcze/MAPA-POKRYCIA.md
```

## Powiązania zewnętrzne
- Wchodzi z: `prawo-polskie-v2` → `ROUTING-MAP.md` → ten skill
- Wychodzi do: `pisma-procesowe-v3` / `analiza-sadowa-v6` / `orzeczenia-sadowe-v2` / `analizator-umow-v1`
- mod-KRO-rodzinne (sprawy rozwodowe, świadkowie) → `shared/MOD-ATAK-NA-SWIADKA.md` (kanoniczne techniki
  ataku/obrony wiarygodności świadka) oraz `przesluchanie-swiadkow-v2-min90` (przygotowanie przesłuchania)
- Weryfikacja prawa: ELI (RZĄD 1)
- Orzecznictwo: orzeczenia.ms.gov.pl, sn.pl

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
