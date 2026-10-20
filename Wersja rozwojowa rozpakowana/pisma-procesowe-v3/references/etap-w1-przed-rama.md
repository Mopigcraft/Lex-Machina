# W1.2a — W1.2b: CLAIM-VALIDATION, ELIMINACJA TEZ, KARTY/ŁAŃCUCHY/MACIERZ, FSL-D, STRATEGIA-WYBOR (pełna treść)

### W1.2a — CLAIM-VALIDATION (przed mapą przesłanek)

> ⛔ OBOWIĄZKOWE — wykonaj przed W1.3. Pomiń tylko gdy pismo nie zawiera
> żadnych twierdzeń faktycznych strony (praktycznie: nigdy).
> Wywołaj: `view shared/CLAIM-VALIDATION.md`

Przed zbudowaniem mapy przesłanka → dowód wykonaj weryfikację twierdzeń strony:

- Dla każdego twierdzenia faktycznego z opisu sprawy i dostarczonych dokumentów
  wykonaj kroki C1–C4 z MOD-CLAIM-VALIDATION.
- Twierdzenie `[⛔ SPRZECZNE]` → zastąp twierdzeniem wynikającym z materiału; poinformuj użytkownika.
- Twierdzenie `[⛔ NIEUDOWODNIONE]` → oznacz jako lukę; nie buduj na nim przesłanki;
  wpisz do W1.5 jako ⬛ BRAK ISTOTNY lub BRAK KRYTYCZNY zależnie od wagi.
- Wyświetl Raport Walidacji Twierdzeń jeśli wykryto błędy.

> Engines specjalistyczne — wywołaj PRZED W1.2 gdy aktywne (patrz MODUŁY-MAPA):
> ```
> view references/engines/pleading-engine-v8.md          (każde pismo złożone — matryca roszczenia)
> view references/engines/theory-of-case-engine.md      (≥2 roszczenia / apelacja)
> view references/engines/appellate-engine-v8.md        (⛔ obowiązkowy przy apelacji)
> view references/engines/rebuttal-drafting-engine-v9.md (riposta / odpowiedź)
> view references/engines/prosecution-complaint-engine-v8.md (⛔ obowiązkowy: zażalenie do prokuratury)
> view references/engines/opponent-pleading-attack-engine-v9.md (analiza pisma przeciwnika)
> ```

### W1.2a-POST — ELIMINACJA TEZ I WERYFIKACJA PRZEPISÓW (obowiązkowe po CLAIM-VALIDATION)

> ⛔ OBOWIĄZKOWE — wykonaj po CLAIM-VALIDATION (W1.2a) per każde żądanie.
> Wypełnia lukę systemową: CLAIM-VALIDATION sprawdza twierdzenia vs fakty;
> PRAWO-HARDGATE sprawdza przepis przed cytowaniem;
> TEN KROK sprawdza czy przepis DOTYCZY tej sytuacji i czy żądanie ma podstawę.

```
KROK ET: Eliminacja tez i weryfikacja przepisów
  view modules/MOD-ELIMINACJA-TEZ.md

  Per każde żądanie z petitum:
  → ET-Q1: Czy istnieje przepis który to żądanie PRZEWIDUJE? (ELI — RZĄD 1)
  → ET-Q2: Czy PRZESŁANKI przepisu są spełnione przez fakty F-nn?
           (subsumpcja — per każda przesłanka osobno)
  → ET-Q3: Czy przepisy z materiału dowodowego są PRAWIDŁOWE?
           (nie przepisuj — weryfikuj samodzielnie)
  → Raport ET-4: ZATWIERDZONE / EWENTUALNE / WYELIMINOWANE

  WYNIK:
  ✅ ZATWIERDZONE → wchodzą do W1.3 i petitum
  ⚠️ EWENTUALNE  → wchodzą jako "ewentualnie" + CV-ALT
  ⛔ WYELIMINOWANE → NIE wchodzą do petitum ani uzasadnienia
```

### W1.2c-PRE — KARTY DOWODOWE I ŁAŃCUCHY (gdy ≥2 dokumenty dostarczone)

> ⛔ OBOWIĄZKOWE gdy użytkownik dostarczył ≥2 dokumenty.
> Wykonaj PO SD-SKAN, PRZED W1.2b i PRZED W1.3.
>
> DIAGNOZA DLACZEGO ŁAŃCUCHY NIE BYŁY UŻYWANE (naprawione 2026-06-25):
> MOD-LANCUCH-DOWODOWY istniał ale nie był wywołany w pipeline.
> Brak MOD-KARTA-DOWODU powodował że system produkował LISTY, nie GRAFY.

### W1.2c-FSL-D — FACT-SOURCE-LOCK DOKUMENTÓW (⛔ OBOWIĄZKOWE — wykonaj PRZED KROK KD)

> ⛔ HARD GATE — wykonaj natychmiast po SD-VER = KOMPLET, PRZED jakąkolwiek
> pracą na macierzy lub kartach dowodowych.
>
> DIAGNOZA DLACZEGO FSL-D JEST KONIECZNE (sprawa [SYGN-SPRAWY], 2026-06-27):
> Po SD-VER (wszystkie pliki odczytane ✅) model budował macierz D×T z PAMIĘCI
> zamiast z per-teza przeszukania SD-FAKTY. Skutek: teza gotowości do pracy
> miała 1 dowód zamiast 4. Teza pracodawcy faktycznego — argumenty ogólne
> zamiast konkretnych wierszy XLSX i zrzutów ekranu. Nazwa pliku (Szef.odt,
> Zatrudnienie.odt) myląca — model pomijał pliki bo „intuicyjnie nie pasowały".
>
> FSL-D WYMUSZA: per każdą tezę → przeszukanie WSZYSTKICH D[id] z SD-REJ →
> każde twierdzenie atomowe musi mieć D[id] + lokalizację z SD-FAKTY (nie z pamięci).

```
⛔ KROK FSL-D: Fact-Source-Lock Dokumentów
  view shared/MOD-FSL-DOKUMENTY.md

  Sekwencja FSL-D (wykonaj w tej kolejności):

  FSL-D-INIT:
    1. Pobierz listę tez T1..Tn z CLAIM-VALIDATION (W1.2a)
    2. Pobierz SD-REJ (D01..D[N]) z MOD-SKAN-DOWODOW-KOMPLETNY
    3. Zbuduj pustą FSL-D-MACIERZ: T[n] × twierdzenia atomowe

  FSL-D-SCAN (per KAŻDA teza T[n], po kolei):
    A. Rozłóż T[n] na twierdzenia atomowe TC[n,1]..TC[n,k]
    B. Per KAŻDE TC[n,k]: przeszukaj WSZYSTKIE D[id] z SD-REJ
       ⛔ ZAKAZ CYTOWANIA Z PAMIĘCI: wracaj do SD-FAKTY[D[id]], nie do
          odtworzenia z kontekstu konwersacji
       ⛔ ZAKAZ WNIOSKOWANIA Z NAZWY PLIKU: przeszukuj każdy D[id]
          niezależnie od tego czy jego nazwa „pasuje" do tezy
    C. Klasyfikuj: ✅ POTWIERDZONE / ⚠️ POŚREDNIE / ⬛ FSL-D-LUKA (🔴/🟠/🟡)
    D. Wpisz do FSL-D-MACIERZ: TC[n,k] → D[id], lok.[strona/zakładka/obraz/godz.],
       treść wyekstrahowana z SD-FAKTY (nie parafrazowana z pamięci)

  FSL-D-ORPHAN:
    Po skanowaniu wszystkich T[n]: czy jest D[id] z 0 przypisań do tez?
    → TAK: sprawdź czy zawiera fakty na nową tezę T_new → zaproponuj użytkownikowi
    → NIE: FSL-D-NEUTRALNY

  FSL-D-REPORT:
    Wyświetl raport z FSL-D-MACIERZ (wg formatu z MOD-FSL-DOKUMENTY.md)
    Policz: ✅ potwierdzone / ⚠️ pośrednie / ⬛ luki per klasa (🔴/🟠/🟡)

  Rozgałęzienie:
    ⬛ FSL-D-LUKA 🔴 → ⛔ STOP: zadaj PYTANIA FSL-D; czekaj na decyzję a/b/c/d
    ⬛ FSL-D-LUKA 🟠 → kontynuuj, ale w piśmie: żądanie ewentualne + UWAGI REDAKCYJNE
    ⬛ FSL-D-LUKA 🟡 → notacja w raporcie; nie blokuje
    brak luk 🔴/🟠 → przejdź do KROK KD (karty dowodowe)

  ⛔ ZAKAZ-FSL-D: NIE przystępuj do KROK KD ani KROK ŁD ani KROK MT
     dopóki FSL-D-REPORT nie jest wyświetlony i luki 🔴 nie są rozwiązane.
     Naruszenie = błąd krytyczny pipeline — równoważny pominięciu CLAIM-VALIDATION.
```

```
KROK KD: Wypełnij karty dowodowe i rejestr faktów
  view shared/MOD-KARTA-DOWODU.md
  → Per każdy D[nn] ze SD-FAKTY: wypełnij KD-1 (karta dowodowa)
  → Zbuduj KD-2 (rejestr faktów F-nn z pewnością i źródłem)
  → Narysuj KD-3 (graf relacji dowód→fakt→teza per teza)

KROK ŁD: Zbuduj łańcuchy dowodowe z kart
  view shared/MOD-LANCUCH-DOWODOWY.md
  → Per każda teza T-X: wykonaj ŁD-1..ŁD-7
  → Ogniwa łańcucha = fakty F-nn z rejestru (nie lista plików)
  → BRAMKA EQG (ŁB-5): wyklucz ogniwa szkodliwe
  → Scoring ★-★★★★★ per teza główna
  → OUTPUT łańcucha ŁD-XX → wejście do W1.3

KROK MT: Macierz Dowód × Teza (⛔ OBOWIĄZKOWE gdy ≥2 dowody i ≥2 tezy)
  view shared/MOD-MACIERZ-DOWOD-TEZA.md
  → MT1: inwentaryzacja — lista T1..Tn z przesłankami + lista D1..Dm z kategorią A/B/C/D
  → MT2: skan dwukierunkowy (A: każdy dowód → wszystkie tezy; B: każda teza → pokrycie przesłanek)
  → MT3: klasyfikacja powiązań: [K] KLUCZOWY / [W] WIELOFUNKCYJNY / [R] REDUNDANTNY / [RK] RYZYKOWNY
  → MT4: raport — tabela D×T, pokrycie tez (%), luki KRYTYCZNE/ISTOTNE, decyzje RK
  → MT5: zasilenie pipeline:
       • luki KRYTYCZNE z MT4 → W1.5 jako ⬛ BRAK KRYTYCZNY
       • luki ISTOTNE z MT4   → W1.5 jako ⬛ BRAK ISTOTNY
       • dowody [W] (wielofunkcyjne) → powołuj RAZ w sekcji "Na dowód" z listą tez
       • po W2: MT5-MANDATE-ALL-EVIDENCE (cross-check N_pismo ≥ 0.7 × N_macierzy)

  ⛔ POZYCJA: ten krok jest TUTAJ (W1.2c), NIE w W2.
     Macierz musi powstać PRZED mapą przesłanka→dowód (W1.3).
     Tworzenie macierzy w W2 = błąd architektoniczny: pismo redagowane
     bez wiedzy o lukach i wielofunkcyjności dowodów.

  ⛔ WBUDOWANIE W PISMO: tabela D×T z MT4 WCHODZI do treści pisma
     jako osobna sekcja (przed lub po uzasadnieniu, zależnie od konwencji sądu).
     Macierz nie jest tylko krokiem wewnętrznym — jest widoczna dla sądu,
     bo art. 227 i 232 k.p.c. wymagają wskazania jakie fakty mają być wykazane
     jakim dowodem. Wnioski dowodowe formułowane są PER TEZA (nie jako lista en bloc).

  ⛔ FORMAT SĄDOWY — ZAKAZ SYMBOLI:
     Tabela w piśmie procesowym NIE używa symboli wewnętrznych (●●●, ★, [K], [W], RK).
     Te oznaczenia służą wyłącznie wewnętrznemu pipeline'owi (MT1–MT5).
     Tabela dla sędziego ma WYŁĄCZNIE kolumny czytelne dla prawnika:
       Lp. | Dowód (nazwa i opis) | Lokalizacja w aktach (str./zał./godz.) |
       Roszczenie (T1/T2/... lub pełna nazwa) | Na okoliczność (opis faktów)
     Dla dokumentów z protokołu: obowiązkowe wskazanie strony protokołu i godziny.
     Dla załączników: numer załącznika.
     Klasyfikacje wewnętrzne (siła dowodu, ryzyka krzyżowe) — tylko do użytku
     wewnętrznego modelu; nie trafiają do pisma.

⛔ Generator pisma nie pyta "jakie dowody mam?"
   Pyta: "jakie FAKTY F-nn prowadzą do TEZY T-X i w jakim łańcuchu?"
⛔ ZAKAZ: sekcja "Na dowód" bez powiązania z F-nn z rejestru.
⛔ ZAKAZ: W1.3 bez gotowych łańcuchów ŁD-XX dla tez głównych.
⛔ ZAKAZ: W1.3 bez gotowej macierzy D×T (gdy ≥2 dowody i ≥2 tezy).
⛔ ZAKAZ: wnioski dowodowe jako lista en bloc — każdy wniosek wskazuje tezę Tn.
```

### W1.2b — MOD-STRATEGIA-WYBOR (obligatoryjna ocena i ranking ścieżek)

> ⛔ HARD GATE W1.2b — dla każdego pisma złożonego gdy ≥2 ścieżki prawne
> lub anomalia podmiotowa w materiale dowodowym.
>
> Wywołaj: `view shared/MOD-STRATEGIA-WYBOR.md`
>
> Moduł jest NADRZĘDNY wobec MOD-WARIANTY-POZWU — wywołuje go wewnętrznie
> jako generator kart. Nie wywołuj MOD-WARIANTY-POZWU samodzielnie.

Jeśli warunek aktywacji spełniony:
1. S1 — zidentyfikuj WSZYSTKIE ścieżki (w tym anomalie podmiotowe: różne KRS/NIP)
2. S2 — oceń każdą ścieżkę pod kątem ataku przeciwnika (OCENA-A/B/C)
3. S3 — wygeneruj ranking z rekomendacją; ścieżka z atakiem 🔴 bez kontrargumentu
         → PORZUĆ lub EWENTUALNA — nigdy GŁÓWNA
4. S4 — wybierz strukturę pisma (Scenariusz 1/2/3)
5. S5 — wyświetl RAPORT STRATEGII użytkownikowi; czekaj na zatwierdzenie
6. Po zatwierdzeniu: zaktualizuj W1.2 (teza centralna) jeśli zmienił się wybór;
   zapisz wynik do MOD-HISTORIA-STRATEGII PRZED W1.3

⛔ ZASADA BEZWZGLĘDNA: Ścieżka z atakiem 🔴 bez kontrargumentu NIE może być
ścieżką główną. System OBLIGATORYJNIE rekomenduje ścieżkę silniejszą — użytkownik
może to zmienić, ale decyzja musi być explicite, nie domyślna.

Jeśli warunek aktywacji NIE jest spełniony — pomiń ten krok, przejdź do W1.3.
