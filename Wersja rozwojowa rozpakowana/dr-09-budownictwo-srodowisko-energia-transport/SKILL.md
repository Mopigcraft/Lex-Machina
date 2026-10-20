---
name: dr-09-budownictwo-srodowisko-energia-transport
version: "3.48"
description: "Budownictwo, środowisko, energia i transport: prawo budowlane, planowanie, odpady, ochrona środowiska, energetyka, drogi i regulacje transportowe."
dependencies:
  requires:
    - shared
  # 2026-09-27e: jawna zależność (każdy skill systemu korzysta z `shared`); pole czytane przy imporcie z marketplace
---

> **Universal runtime:** przed wykonaniem zastosuj kanoniczny `shared/UNIVERSAL-RUNTIME-ADAPTER.md` z osobnego skilla `shared`. Lokalna sekcja adaptera poniżej jedynie go doprecyzowuje.


## ADAPTER RUNTIME — PORTABILITY (ChatGPT / Claude / inne hosty)

Ta sekcja zmienia wyłącznie wykonanie operacji technicznych. Merytoryka dziedzinowa, mapy aktów, hard gate’y, kolejność modułów i kryteria jakości tego DR-skilla pozostają bez zmian.

1. `view dr-09-budownictwo-srodowisko-energia-transport/<plik>` oraz `view modules/...` / `view references/...` oznaczają świeży odczyt odpowiedniego lokalnego pliku tego skilla. Literalna ścieżka `/mnt/skills/user` nie jest wymagana.
2. `view shared/<plik>` oznacza świeży odczyt z osobnego, kanonicznego skilla `shared`. NIE kopiuj `shared` do tej paczki. Brak obowiązkowego zasobu shared = fail-closed, nie substytucja pamięcią modelu.
3. `view <inny-skill>/<plik>` oznacza aktywację/odczyt wskazanego osobnego skilla. Nie vendoryzuj innych skilli do tego ZIP-a.
4. `web_search` / `web_fetch` i podobne nazwy oznaczają świeże wyszukanie/odczyt online przez równoważną funkcję hosta. Zachowaj wymagane źródła oficjalne, statusy weryfikacji i zakaz cytowania prawa z pamięci.
5. `show_widget`, `visualize:read_me`, `present_files`, `create_file`, shell/Python i podobne operacje są nazwami semantycznymi. Jeśli host nie ma literalnego narzędzia, użyj równoważnej funkcji natywnej bez omijania bramek jakości.
6. `/mnt/user-data/...` oznacza rzeczywiste załączniki użytkownika dostępne w bieżącym hoście; wymagany ponowny odczyt ma być faktycznym odczytem źródła.

**Zasada nadrzędna:** instrukcje, które są już zrozumiałe i wykonalne w bieżącym hoście, wykonuj bez konwersji. Adapter działa wyłącznie na granicy runtime.


# DR-09 — Budownictwo, Środowisko, Energia, Transport

## ⛔ HARD GATE — ZAKAZ CYTOWANIA Z PAMIĘCI

**PRZED każdym powołaniem przepisu lub sygnatury:**
1. Zweryfikuj brzmienie i Dz.U. w `ELI (RZĄD 1)`
2. Zweryfikuj orzeczenie w `orzeczenia.ms.gov.pl` / `nsa.gov.pl` / `sn.pl`
3. **NIGDY** nie podawaj artykułu, kary, terminu ani sygnatury wyłącznie z pamięci modelu.

Akty DR-09 (zwłaszcza Prawo budowlane, POŚ, Prawo wodne) są **bardzo często nowelizowane** —
tekst sprzed 6 miesięcy może być już nieaktualny. Zawsze pobieraj aktualny t.j. przed użyciem.


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
- **Zakaz cytowania przepisów z pamięci — każde brzmienie weryfikuj w ELI (RZĄD 1)**
- **Dz.U. DR-09 zmieniają się bardzo często — przed każdym powołaniem weryfikuj t.j.**

---

## DEFINICJE — shared/definicje/ (bezpośrednie, lazy loading per temat)

- `definicje/DEF-BUDOWLANE-DROGOWE.md` — obiekt liniowy (kable w kanalizacji
  ≠ obiekt budowlany), samowola budowlana, decyzja WZ, definicje ministerialne
  prawa budowlanego (H.2) — PLIK GŁÓWNY dla tej dziedziny

## ORKA-BAS — Definicje wspomagające (shared/ORKA-BAS-LEKSYKON.md)

Przy sprawach z tej dziedziny rozważ doładowanie (`view`) definicji:
- BAS-007 Gospodarstwo rolne
- BAS-105 Zabudowa zagrodowa na gruntach leśnych (ORKA-REG-05 — def. techniczna
  nie tworzy prawa do zabudowy)
- BAS-108 Odbiorca wrażliwy energii (PE art. 3 pkt 13c + zmiana dyr. 2024/1711)
- BAS-109 Względy techniczne — podatek od nieruchomości (art. 1a ust. 1 pkt 3 upol)
- BAS-111 Strona postępowania w sprawach WZ
- BAS-115 Wolnostojące ogniwa fotowoltaiczne (kwalifikacja: zgłoszenie vs pozwolenie)
- BAS-W09 Samowola budowlana po nowelizacji 2023 (abolicja, brak przedawnienia)
- BAS-W10 Obiekt liniowy (art. 3 pkt 3a PrBud — kable w kanalizacji ≠ obiekt!)
- BAS-W14 ⚠️ Reforma upol 2025 — nowe definicje budynek/budowla (dot. też DR-06)

## Moduły (36 łącznie — ✓ 36 OK, ☐ 0 STUB)

Opisy zakresu i historia zmian modułów (wieloliniowe opisy wpisów, adnotacje NAPRAWA/Aktualizacja) są w `dr-09-budownictwo-srodowisko-energia-transport/references/moduly-opisy-i-historia.md` — `view` tego pliku, gdy potrzebny jest zakres lub historia konkretnego modułu (routing do modułów działa wyłącznie z listy poniżej).


```
BUDOWNICTWO:
  [✓] NOWY  mod-ochrona-zabytkow-obiekty-uzytecznosci-publicznej
  [✓] OK    mod-PrBud-prawo-budowlane
  [✓] NOWY  mod-PrBud-uzupelnienie-pokrycia-2026
  [✓] OK    mod-UGN-gospodarka-nieruchomosciami
              (deweloper, MRP, DFG, WM, najem, zasiedzenie, KW, służebności)
  [✓] OK    mod-PrGeodezyjne-kartografia-wywlaszczenia
              (ewidencja gruntów, podziały, wywłaszczenie, ZRID, specustawy)
  [✓] OK    mod-ustawa-planowanie-przestrzenne
              (Plan Ogólny Gminy, MPZP, WZ, ZPI — reforma 2023)
  [✓] NOWY  mod-ustawa-architekci-inzynierowie-budownictwa-zawod

ŚRODOWISKO:
  [✓] OK    mod-POS-prawo-ochrony-srodowiska
              (POŚ, pozwolenia, IPPC, emisje, kary WIOŚ, KK 181-188a)
  [✓] OK    mod-inspekcja-ochrony-srodowiska-GIOS-WIOS
  [✓] OK    mod-formy-ochrony-przyrody-obszary-chronione
  [✓] OK    mod-POS-prawo-ochrony-srodowiska-szczegoly
  [✓] OK    mod-ustawa-OOS-oceny-srodowiskowe
              (DŚU, OOŚ, RDOŚ/GDOŚ, udział społeczeństwa, organy)
  [✓] OK    mod-ustawa-odpadach-gospodarka-komunalna
              (BDO, zezwolenia, kary, nielegalne składowanie, rekultywacja)
  [✓] OK    mod-ustawa-lesna-lowiecka-ochrona-przyrody
  [✓] OK    mod-lowiectwo-klusownictwo
  [✓] OK    mod-PrBud-patodeweloperka-uzytkowanie-male-obiekty-ograniczenia
  [✓] OK    mod-srodowisko-wycinka-odpady-niebezpieczne-rekultywacja
  [✓] OK    mod-UE-PPWR-EUDR-rozporzadzenia-srodowiskowe
  [✓] OK    mod-system-kaucyjny-opakowania
  [✓] NOWY  mod-szkody-lowieckie-szacowanie-odszkodowanie
  [✓] NOWY  mod-lowieckie-obwody-dzierzawa-odszkodowania
  [✓] NOWY  mod-lowieckie-wykonywanie-polowania-uprawnienia
  [✓] NOWY  mod-lowieckie-odpowiedzialnosc-dyscyplinarna-PZL
  [✓] NOWY  mod-lowieckie-PZL-kola-nadzor-ministra
  [✓] NOWY  mod-lowieckie-straz-lowiecka-PSL-uprawnienia
  [✓] NOWY  mod-lowieckie-zasady-gospodarki-lowieckiej-plany
  [✓] NOWY  mod-lowieckie-przepisy-ogolne-organy-administracji
  [✓] NOWY  mod-lowieckie-dzialalnosc-gospodarcza-turystyka-obrot
  [✓] NOWY  mod-lowieckie-przepisy-przejsciowe-koncowe-derogacja
  ⚠️ UWAGA: szkody od gatunków CHRONIONYCH (żubr, wilk, ryś, niedźwiedź,
     bóbr) to INNY REŻIM — art. 126 ustawy o ochronie przyrody →
     mod-formy-ochrony-przyrody-obszary-chronione
              (ochrona przyrody, Natura 2000, wycinka)

ENERGIA I ZASOBY:
  [✓] OK    mod-PrEnergetyczne-URE-OZE
              (koncesje, taryfy, przyłączenia, prosument, OZE, gaz, URE)
  [✓] OK    mod-ustawa-charakterystyka-energetyczna
              (certyfikaty energetyczne, EPBD recast 2024, NZEB)
  [✓] OK    mod-PrWodne-gospodarka-sciekowa
              (Prawo wodne, Wody Polskie, pozwolenia wodnoprawne, opłaty)
  [✓] OK    mod-prawo-geologiczne-gornicze
              (koncesje wydobywcze, opłaty eksploatacyjne, WUG)

TRANSPORT:
  [✓] OK    mod-ustawa-transport-drogowy-kolejowy-lotniczy-morski
  [✓] OK    mod-GDDKiA-specustawa-drogowa-ZRID
  [✓] OK    mod-ustawa-prawo-gazowe
              (Prawo energetyczne — część gazowa, URE, TGE, odbiorca wrażliwy)
```

---

## Jak wywołać

```
view dr-09-budownictwo-srodowisko-energia-transport/modules/[nazwa-modulu].md
```

## Lokalna mapa aktów prawnych

```
view dr-09-budownictwo-srodowisko-energia-transport/MAPA-AKTOW.md
```

## Mapa pokrycia treściowego (planowanie rozwoju skilla)

Rejestr informacyjny — NIE krok obowiązkowy przy obsłudze konkretnej sprawy.
Jedyne bieżące źródło statusu pokrycia tego DR (por. `prawny-router-v3/references/pokrycie-dziedzinowe.md`);
przy nowelizacji pokazuje, czy dotknięty fragment ma treść do zaktualizowania:

```
view dr-09-budownictwo-srodowisko-energia-transport/MAPA-POKRYCIA.md
```

---

## Powiązania zewnętrzne
- Wchodzi z: `prawo-polskie-v2` → `ROUTING-MAP.md` → ten skill
- Planowanie przestrzenne (MPZP, WZ) → też `dr-08` → `mod-MPZP-WZ-planowanie-przestrzenne`
  ⛔ Brzmienie samego planu/uchwały bierz z publikatora: `dziennikiurzedowe.gov.pl`
  (RZĄD 1) wg ŚCIEŻKI B-L w `shared/PRAWO-HARDGATE.md`. MPZP, plan ogólny i WZ
  opierają się na aktach prawa miejscowego, których NIE MA w ISAP ani w API ELI
  (dodane 2026-09-01g, F-154).
- Podatek od nieruchomości (reforma 2025) → `dr-06`
- Zamówienia publiczne (budowlane) → `dr-07`
- Samorząd terytorialny (MPZP, gospodarka komunalna) → `dr-08`
- Wychodzi do: `pisma-procesowe-v3` / `analiza-sadowa-v6` / `orzeczenia-sadowe-v2`
- Weryfikacja: ELI (RZĄD 1) | orzeczenia.nsa.gov.pl | sn.pl | kio.gov.pl (zamówienia budowlane)

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
