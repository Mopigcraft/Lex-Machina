# KROK 0a / 0b / 0c — szczegóły (tryb MODE, skan kompletności, rejestr kroków)

## KROK 0a — WYKRYCIE TRYBU PRACY (MODE) — addytywny, auto-detect

```
Analizuj materiał i ustal MODE przed uruchomieniem routera.
MODE jest addytywny — może rozszerzyć się w trakcie sesji.

──────────────────────────────────────────────────────────────
SYGNAŁY TRYBU — sprawdzaj w tej kolejności:
──────────────────────────────────────────────────────────────

SYGNAŁ A — tryb porównawczy jednej strony:
  → ≥2 pisma procesowe TEGO SAMEGO autora / tej samej strony z różnych dat
  → słowa kluczowe: "odpowiedź na pozew" + "pismo procesowe" od tego samego pełnomocnika
  → wynik: MODE=A (obligatoryjne: Nazewnictwo, Historia narracji, INTRA)
  → LAPSUS szczególnie istotny: błędy autorskie wynikające z wielokrotnego pisania

SYGNAŁ B — tryb dwustronny:
  → pisma od CO NAJMNIEJ dwóch różnych stron procesowych
  → słowa kluczowe: "pozew" + "odpowiedź", "apelacja" + "odpowiedź na apelację"
  → wynik: MODE=B (obligatoryjne: DIS, Fakty bezsporne, CROSS)

SYGNAŁ C — tryb przygotowawczy:
  → dokumenty źródłowe BEZ pism procesowych drugiej strony
  → słowa kluczowe: "przygotowuję pozew", "piszę wezwanie", "co mam do dyspozycji"
  → wynik: MODE=C (obligatoryjne: Scoring dowodów, Przesłanki i luki, Roszczenia)

TRYBY WIELOKROTNE — addytywność:
  → Materiał może spełniać kilka sygnałów jednocześnie → ustaw wszystkie aktywne tryby
  → Inicjalnie ustaw tryb dominujący; przy dołączeniu nowych pism auto-rozszerz
  → MODE=A+B: jest materiał jednej strony (kilka pism) + odpowiedź drugiej
  → MODE=B+C: jest pozew własny + odpowiedź pozwanej → pełna analiza dwustronna
    z planowaniem dalszych kroków
  → Nigdy nie kasuj danych przy rozszerzeniu MODE — tablice są addytywne

BRAK SYGNAŁU:
  → Uruchom widget-kreator STEP 1.5 — zapytaj użytkownika
  → Zaproponuj tryb na podstawie opisu sprawy

──────────────────────────────────────────────────────────────
ZAKŁADKI OBLIGATORYJNE PER TRYB:
──────────────────────────────────────────────────────────────

| Zakładka dashboardu          | MODE A | MODE B | MODE C |
|------------------------------|--------|--------|--------|
| Strony i świadkowie          |  ✅    |  ✅    |  ✅    |
| Tożsamość IDENT              |  ✅    |  ✅    |  ✅    |
| Lapsusy autorskie [LAPSUS]   |  ✅    |  ✅    |  🔷    |
| Nazewnictwo procesowe        |  ✅    |  🔷    |  ❌    |
| Historia narracji [A-only]   |  ✅    |  ❌    |  ❌    |
| Sprzeczności INTRA           |  ✅    |  🔷    |  ❌    |
| Sprzeczności CROSS           |  ❌    |  ✅    |  ❌    |
| Kwestie sporne DIS           |  ❌    |  ✅    |  ❌    |
| Fakty bezsporne              |  ❌    |  ✅    |  ❌    |
| Rejestr dowodów / scoring    |  🔷    |  🔷    |  ✅    |
| Roszczenia i podstawy [C]    |  ❌    |  ❌    |  ✅    |
| Przesłanki i luki            |  🔷    |  ✅    |  ✅    |
| Terminy procesowe            |  🔷    |  🔷    |  🔷    |
| Raport + Eksport             |  ✅    |  ✅    |  ✅    |

✅ = obligatoryjna  🔷 = opcjonalna (jeśli materiał zawiera)  ❌ = nieaktywna

──────────────────────────────────────────────────────────────
BADGE TRYBU W DASHBOARDZIE:
──────────────────────────────────────────────────────────────
Nagłówek dashboardu zawiera badge aktywnego trybu:
  [MODE A: Analiza jednej strony] [MODE B: Dwustronny] [MODE C: Przygotowanie]
  lub kombinacje: [MODE A+B] [MODE B+C]
Przycisk: "＋ Dodaj pisma drugiej strony →" gdy MODE=A → auto-rozszerz do A+B
Przycisk: "＋ Dodaj własne pisma →" gdy MODE=B → auto-rozszerz do A+B
```

## KROK 0b — SKAN KOMPLETNOŚCI PLIKÓW ⛔ HARD GATE

```
Wykonaj PRZED KROK 1. Mechanizm współdzielony z pisma-procesowe-v3 i analiza-sadowa-v6.

view /mnt/skills/user/shared/MOD-SKAN-DOWODOW-KOMPLETNY.md → wykonaj sekwencję:

SD-GATE-0: Czy w wiadomości wzmianka o załącznikach/dowodach/aktach BEZ wgranego pliku?
  TAK → ⛔ STOP. Wyświetl: "Wskazujesz na dokumenty, ale nie wykryłem żadnego pliku.
         Wgraj materiały przed analizą." Czekaj. Nie przechodzij do KROK 1.

SD-INW: Zinwentaryzuj WSZYSTKIE pliki (ZIP = zawartość, nie kontener).
  Zbuduj SD-REJ z każdym plikiem D[id] i liczbą stron/zakładek.

SD-READ: Per każdy D[id] — właściwa metoda per typ:
  PDF-skan    → pdftoppm -r 120 per KAŻDA strona → view
  PDF-tekst   → pdftotext; jeśli pusty → rasteryzacja
  XLSX        → openpyxl: KAŻDA zakładka
  ODT-obrazy  → zipfile Pictures/* → view per obraz
  JPG/PNG     → view bezpośrednio
  DOCX        → zipfile word/document.xml
  ⛔ ZAKAZ POMINIĘCIA STRONY / ZAKŁADKI / OBRAZU

SD-VER: Wszystkie D[id] = ✅ ODCZYTANE?
  NIE → wróć do SD-READ. Nie przechodzij do KROK 1.

Wyniki SD-READ → SD-FAKTY[D[id]] zasilają BLOK A i BLOK B.
Protokoły sądowe: KAŻDE zdanie zeznań świadka → osobny wpis SD-FAKTY.

⛔ BLOK-C-FSL: PO SD-VER, PRZED KROK 1 — gdy ≥1 teza dowodowa:
  view /mnt/skills/user/shared/MOD-FSL-DOKUMENTY.md
  → FSL-D-INIT (macierz T[n])
  → FSL-D-SCAN per każda teza: rozłóż na twierdzenia atomowe TC[n,k];
    per każde TC: przeszukaj WSZYSTKIE D[id] z SD-FAKTY (zakaz wnioskowania z nazwy pliku);
    klasyfikuj ✅/⚠️/⬛ (🔴/🟠/🟡)
  → FSL-D-ORPHAN: D[id] z 0 przypisań = kandydaci na nowe tezy
  → FSL-D-REPORT: macierz + luki per klasa
  → Luka 🔴 = STOP (decyzja a/b/c/d); luka 🟠 = kontynuuj z żądaniem ewentualnym
  ⛔ ZAKAZ przejścia do MD1/BLOK-A bez FSL-D-REPORT
```

## KROK 0c — ST-INIT: REJESTR KROKÓW (MOD-STEP-TRACKER) ⛔ OBOWIĄZKOWE

> Dodano w audycie 5.13.0. Przyczyna: skill miał już poprawnie wpiętą bramkę
> DOWODOWĄ (SD-VER w KROK 0b), ale brakowało mu bramki PROCEDURALNEJ —
> żaden mechanizm nie raportował użytkownikowi, gdy w wieloetapowym routerze
> (KROK 2 → BLOK A-J → KROK 3) pominięto blok, który powinien być obowiązkowy
> (np. BLOK G/J przy A2=TAK). Ten sam typ luki naprawiono już wcześniej w
> `pisma-procesowe-v3` i `przesluchanie-swiadkow-v2-min90` (audyt 3.13) —
> tutaj stosujemy identyczny mechanizm.

```
Wykonaj PO KROK 0b (SD-VER = KOMPLET), PRZED KROK 1.

ST-INIT: view /mnt/skills/user/shared/MOD-STEP-TRACKER.md (jeśli REJESTR
jeszcze nie zainicjowany w tej sesji) → zainicjuj z pozycjami dedykowanymi
temu skillowi:

  "AD-KROK0"  — KROK 0 blokada wstępna (przekierowanie do analizator-umow?)
  "AD-KROK0a" — KROK 0a wykrycie trybu MODE (A/B/C)
  "AD-KROK0b" — KROK 0b SD-VER skan kompletności plików (już HARD GATE)
  "AD-KROK1"  — KROK 1 intake i widget-kreator
  "AD-KROK2"  — KROK 2 centralny router (BLOK A-F diagnostyka)
  "AD-BLOKG"  — BLOK G rejestr stron/świadków (OBOWIĄZKOWY gdy A2=TAK)
  "AD-BLOKJ"  — BLOK J lapsusy autorskie [LAPSUS] (OBOWIĄZKOWY gdy A2=TAK)
  "AD-BLOKH"  — BLOK H kwestie sporne DIS (gdy D3=TAK lub D4=TAK)
  "AD-KROK3"  — KROK 3 wykonanie modułów MD/MP z listy KROK 2
  "AD-KROK4"  — KROK 4 dashboard (gdy B1=TAK)

Każdy krok/BLOK oznaczony jako obowiązkowy w KROK 2 (np. "TAK → dodaj: X"),
który ostatecznie nie zostanie wykonany, musi zmienić status na
"⚠️ POMINIĘTY" z powodem — NIE wolno cicho pominąć bloku diagnostycznie
wymaganego i przejść dalej bez odnotowania.

ST-REPORT: przed KROK 4 (dashboard) lub przed dostarczeniem raportu MD-NARR
— jeśli REJESTR zawiera ≥1 "⚠️ POMINIĘTY" — wyświetl raport pominięć
(format z shared/MOD-STEP-TRACKER.md FAZA 2) i czekaj na decyzję użytkownika
(a: kontynuuj mimo braków / b: wykonaj brakujące kroki), zanim wywołasz
show_widget/present_files.

⛔ ZAKAZ: generowanie dashboardu lub raportu końcowego bez wyświetlenia
stanu REJESTRU (pełny ✅ lub z jawnym ⚠️ POMINIĘTY) — patrz FAZA 3
ST-FINAL w shared/MOD-STEP-TRACKER.md.
```
