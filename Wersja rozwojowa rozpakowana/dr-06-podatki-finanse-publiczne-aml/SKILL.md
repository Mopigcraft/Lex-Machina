---
name: dr-06-podatki-finanse-publiczne-aml
version: "3.99"
description: "Podatki, finanse publiczne i AML: Ordynacja podatkowa, PIT, CIT, VAT, akcyza, cło, KAS, finanse publiczne i obowiązki przeciwdziałania praniu pieniędzy."
dependencies:
  requires:
    - shared
  # 2026-09-27e: jawna zależność (każdy skill systemu korzysta z `shared`); pole czytane przy imporcie z marketplace
---

> **Universal runtime:** przed wykonaniem zastosuj kanoniczny `shared/UNIVERSAL-RUNTIME-ADAPTER.md` z osobnego skilla `shared`. Lokalna sekcja adaptera poniżej jedynie go doprecyzowuje.


## ADAPTER RUNTIME — PORTABILITY (ChatGPT / Claude / inne hosty)

Ta sekcja zmienia wyłącznie wykonanie operacji technicznych. Merytoryka dziedzinowa, mapy aktów, hard gate’y, kolejność modułów i kryteria jakości tego DR-skilla pozostają bez zmian.

1. `view dr-06-podatki-finanse-publiczne-aml/<plik>` oraz `view modules/...` / `view references/...` oznaczają świeży odczyt odpowiedniego lokalnego pliku tego skilla. Literalna ścieżka `/mnt/skills/user` nie jest wymagana.
2. `view shared/<plik>` oznacza świeży odczyt z osobnego, kanonicznego skilla `shared`. NIE kopiuj `shared` do tej paczki. Brak obowiązkowego zasobu shared = fail-closed, nie substytucja pamięcią modelu.
3. `view <inny-skill>/<plik>` oznacza aktywację/odczyt wskazanego osobnego skilla. Nie vendoryzuj innych skilli do tego ZIP-a.
4. `web_search` / `web_fetch` i podobne nazwy oznaczają świeże wyszukanie/odczyt online przez równoważną funkcję hosta. Zachowaj wymagane źródła oficjalne, statusy weryfikacji i zakaz cytowania prawa z pamięci.
5. `show_widget`, `visualize:read_me`, `present_files`, `create_file`, shell/Python i podobne operacje są nazwami semantycznymi. Jeśli host nie ma literalnego narzędzia, użyj równoważnej funkcji natywnej bez omijania bramek jakości.
6. `/mnt/user-data/...` oznacza rzeczywiste załączniki użytkownika dostępne w bieżącym hoście; wymagany ponowny odczyt ma być faktycznym odczytem źródła.

**Zasada nadrzędna:** instrukcje, które są już zrozumiałe i wykonalne w bieżącym hoście, wykonuj bez konwersji. Adapter działa wyłącznie na granicy runtime.


# DR-06 — Podatki, Finanse Publiczne, AML

## ⛔ HARD GATE — ZAKAZ CYTOWANIA Z PAMIĘCI

**PRZED każdym powołaniem przepisu podatkowego, stawki, progu, kwoty, terminu, sankcji, interpretacji, objaśnienia, WIS/WIA/WIP albo sygnatury orzeczenia:**
1. Zweryfikuj aktualne brzmienie aktu, tekst jednolity i nowelizacje w `ELI (RZĄD 1)`.
2. Zweryfikuj interpretacje, objaśnienia podatkowe oraz informacje MF/KIS w oficjalnym serwisie `podatki.gov.pl`, w szczególności w systemie **EUREKA**: `podatki.gov.pl/narzedzia/eureka/`.
3. Zweryfikuj orzecznictwo podatkowe w `orzeczenia.nsa.gov.pl`; dla spraw powszechnych pomocniczo także `orzeczenia.ms.gov.pl` / `sn.pl`.
4. **NIGDY** nie podawaj artykułu, stawki, progu, kwoty, terminu, sankcji, interpretacji ani tezy orzeczenia wyłącznie z pamięci modelu.

**Prawo podatkowe, stawki, progi, formularze, obowiązki raportowe, KSeF/JPK oraz praktyka interpretacyjna MF/KIS zmieniają się wielokrotnie w ciągu roku.**
W sprawach podatkowych sama treść modułu lokalnego jest tylko punktem startu; rozstrzygające jest aktualne brzmienie aktu i aktualna linia interpretacyjna/orzecznicza zweryfikowana online.


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
- **Zakaz cytowania przepisów z pamięci modelu podczas sesji — każde brzmienie weryfikuj w ELI (RZĄD 1)**
- **Stawki podatkowe, kwoty wolne, progi — ZAWSZE weryfikuj przed podaniem (zmieniane co roku!)**
- Źródło podstawowe: ELI (RZĄD 1); ISAP — adres dla człowieka; LEX/Legalis, potem ArsLege — gdy aktu nie da się pobrać z RZĘDU 1 (awaria serwera, timeout, blokada) (kanon E-1…E-5: `shared/HIERARCHIA-ZRODEL.md`)

## DEFINICJE — shared/definicje/ (bezpośrednie, lazy loading per temat)

- `definicje/DEF-PODATKOWE.md` — dochód/przychód/koszty (wykładnia MF),
  koszty uzyskania ZPCh, definicje podatkowe ustawowe

- `definicje/DEF-INTERES-WLASNY-WYLACZENIA.md` — ⚠️ NOWE: rzeczywisty
  beneficjent/UBO (AML art. 2 ust. 2 pkt 1, próg 25%, CRBR, kara do 1 mln zł)
  + alert: 3 RÓŻNE definicje "rzeczywistego właściciela" (AML/CIT-WHT art.4a
  pkt29/KSH art.4§1pkt4) — nie mylić

## ORKA-BAS — Definicje wspomagające (shared/ORKA-BAS-LEKSYKON.md)

Przy sprawach z tej dziedziny rozważ doładowanie (`view`) definicji:
- BAS-011 Cel mieszkaniowy (PIT — ulgi)
- BAS-074/099/100 Podatek / VAT / PIT — definicje podstawowe
- BAS-104 Stałe miejsce prowadzenia działalności VAT (TSUE C-605/12, C-547/18)
- BAS-W06 "Zajęcie na DG" — podatek od nieruchomości (MF interp. 37882/2023)
- BAS-W07 "Grunty zajęte na DG" — upol (NSA III FSK 530/23)
- BAS-W08 Podatek katastralny — brak planów (MF interp. 4662/2024)
- BAS-W14 ⚠️ ALERT: reforma upol od 01.01.2025 — nowe definicje budynek/budowla
  (Dz.U. 2024 poz. 1757, TK SK 14/21)
- BAS-022/023/045/050/053/054/059/061/070/071/073/076/081-084/086/087/090/092/
  096-098 — pełny katalog finansów publicznych JST (budżet, WPF, subwencje,
  dochody własne, dług SP, poręczenia/gwarancje — wszystkie z podstawą UFP)
  ⚠️ ALERT: ustawa z 27.02.2026 r. o zmianie UFP — zmiany w art. 11-15, 23-28
  (jednostki budżetowe, IGB, fundusze celowe, klasyfikacja budżetowa) —
  weryfikuj aktualną treść tych rekordów przy sprawach JST
- BAS-110 Absolwent CIS (ustawa o zatrudnieniu socjalnym, zmiana 2024)
- BAS-125 ⚠️ CRU JSFP — Centralny Rejestr Umów (wejście 01.07.2026, brak progu kwotowego!)
- BAS-W08 ⚠️⚠️ Podatek katastralny — NOWY projekt poselski Lewicy w Sejmie
  (20.03.2026): ≥3 lokale, stawka 0,5%→1,5% wartości. Stan: złożony, brak
  pierwszego czytania (06.2026). MF: brak prac rządowych, ale Sejm pracuje.
- BAS-W32 ⚠️ Przedawnienie podatkowe — Ordynacja podatkowa ma ODRĘBNY reżim
  od KC. ⛔ Twierdzenie „nowelizacja znosi «wieczne przedawnienie» + ugoda
  podatkowa od 01.10.2026" NIEPOTWIERDZONE: `Dz.U. 2026 poz. 846` (w życie
  1.10.2026) nie zmienia art. 70 i nie zna ugody; art. 70 § 6 pkt 1 w mocy
  (✅ [VER] RZĄD 1 2026-09-16). Opis zamiaru legislacyjnego, nie stanu prawa —
  przed powołaniem wskaż pozycję Dz.U. z odczytu treści

## Moduły (47 łącznie — ✓ 47 OK, ☐ 0 STUB)

Opisy zakresu i historia zmian modułów (wieloliniowe opisy wpisów, adnotacje NAPRAWA/Aktualizacja) są w `dr-06-podatki-finanse-publiczne-aml/references/moduly-opisy-i-historia.md` — `view` tego pliku, gdy potrzebny jest zakres lub historia konkretnego modułu (routing do modułów działa wyłącznie z listy poniżej).


```
  [✓] OK    mod-interpretacje-definicje-podatkowe
  [✓] NOWY  mod-PKWiU-klasyfikacje-statystyczne
  [✓] OK    mod-OP-ordynacja-podatkowa
  [✓] NOWY  mod-OP-dzial-IV-rozdzial-11-dowody
  [✓] NOWY  mod-OP-uzupelnienie-pokrycia-2026
              (pozostałe działy OP: organy, zobowiązania, następstwo, STIR, procedura, tryby nadzwyczajne, tajemnica i zaświadczenia)
  [✓] OK    mod-OP-kontrola-podatkowa-dzial-VI
  [✓] NOWY  mod-OP-czynnosci-sprawdzajace-dzial-V
  [✓] NOWY  mod-OP-ulgi-w-splacie-dzial-III-rozdzial-7a
  [✓] OK    mod-KAS-kontrola-celno-skarbowa
  [✓] OK    mod-PIT-podatek-dochodowy-fizyczne
  [✓] OK    mod-CIT-podatek-dochodowy-prawne
  [✓] NOWY  mod-VAT-import-towarow-i-zwolnienia-importowe
  [✓] NOWY  mod-VAT-WIS-tryb-i-ochrona
  [✓] NOWY  mod-VAT-kursy-walut-rachunek-VAT-tax-free
  [✓] NOWY  mod-VAT-rejestracja-zaplata-metoda-kasowa-likwidacja
  [✓] NOWY  mod-VAT-platnicy-egzekucja-kasy-trojstronne
  [✓] OK    mod-VAT-podatek-od-towarow-i-uslug
  [✓] OK    mod-VAT-transakcje-fakturowanie
  [✓] OK    mod-VAT-miejsce-swiadczenia-zwolnienia
  [✓] OK    mod-VAT-obowiazek-podstawa-zwolnienia-nieruchomosci
  [✓] OK    mod-VAT-sankcje-bony-odliczenia
  [✓] OK    mod-VAT-ewidencja-deklaracje
  [✓] OK    mod-odliczenia-uzytek-mieszany-firma-prywatny-KUP
  [✓] OK    mod-podatki-sektorowe-bankowy-gry-tonazowy-cukrowy-detaliczny
  [✓] OK    mod-ustawa-ryczalt-przychody
  [✓] OK    mod-VAT-klasyfikacja-produktow-baza-niejednoznacznosci
  [✓] OK    mod-ustawa-PCC-i-podatek-spadkow-darowizn
  [✓] OK    mod-ustawa-podatek-nieruchomosci-i-lokalne
  [✓] NOWY  mod-ustawa-oplata-skarbowa
  [✓] NOWY  mod-ustawa-podatek-wydobycie-kopalin
  [✓] OK    mod-UFP-finanse-publiczne-NIK-RIO
  [✓] OK    mod-ustawa-akcyzowa-i-clo-UCC
  [✓] OK    mod-alkohol-tyton-regulacja-sprzedazy
  [✓] NOWY  mod-UCC-clo-taryfa-celna
  [✓] OK    mod-clo-podroznych-limity-towary-zabronione
  [✓] OK    mod-limit-platnosci-gotowkowych
  [✓] OK    mod-ustawa-rachunkowosci
  [✓] OK    mod-rachunkowosc-budzetowa-JSFP
  [✓] OK    mod-JPK-ksiegi-elektroniczne-e-sprawozdania
  [✓] OK    mod-PKPiR-ewidencje-uproszczone
  [✓] OK    mod-kasy-rejestrujace-fiskalizacja
  [✓] OK    mod-ustawa-AML-instytucje-obowiazkowe
  [✓] OK    mod-prawo-bankowe-KNF-BFG
  [✓] OK    mod-ustawa-rynek-kapitalowy-fundusze
  [✓] OK    mod-ustawa-uslugi-platnicze
  [✓] NOWY  mod-ustawa-biegli-rewidenci-zawod
  [✓] NOWY  mod-ustawa-doradcy-podatkowi-zawod
```

## Jak wywołać

```
view dr-06-podatki-finanse-publiczne-aml/modules/[nazwa-modulu].md
```

## Lokalna mapa aktów prawnych

```
view dr-06-podatki-finanse-publiczne-aml/MAPA-AKTOW.md
```

Bazy aktów (rejestry pomocnicze — kierunek, nie weryfikacja; KROK 2C
`shared/PRAWO-HARDGATE.md` obowiązuje przy każdym użyciu):

```
view dr-06-podatki-finanse-publiczne-aml/references/BAZA-AKTOW-OKOLOPODATKOWYCH.md   (akty podatkowe i okołopodatkowe)
view dr-06-podatki-finanse-publiczne-aml/references/BAZA-AKTOW-OKOLOAKCYZOWYCH.md   (akcyza + mapa KKS wg czasownika czynu)
```

## Mapa pokrycia treściowego (planowanie rozwoju skilla)

Rejestr informacyjny — NIE krok obowiązkowy przy obsłudze konkretnej sprawy.
Przydatny przy planowaniu, które luki uzupełnić w pierwszej kolejności
(F-83, zasilony 2026-08-22 z audytu źródłowego 2026-08-13; obejmuje na
razie wyłącznie Ordynację podatkową):

```
view dr-06-podatki-finanse-publiczne-aml/MAPA-POKRYCIA.md
```

## Powiązania zewnętrzne
- Wchodzi z: `prawo-polskie-v2` → `ROUTING-MAP.md` → ten skill
- KPA (postępowanie adm.): `dr-05` → `mod-KPA-postepowanie-administracyjne`
- Wychodzi do: `pisma-procesowe-v3` / `analiza-sadowa-v6` / `orzeczenia-sadowe-v2`
- Weryfikacja prawa: ELI (RZĄD 1)
- Interpretacje / objaśnienia / WIS-WIA-WIP: podatki.gov.pl/narzedzia/eureka/ oraz interpretacje.podatki.gov.pl
- Orzecznictwo NSA: orzeczenia.nsa.gov.pl

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
