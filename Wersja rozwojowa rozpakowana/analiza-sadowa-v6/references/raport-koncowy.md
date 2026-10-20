# Format raportu końcowego i sekwencja end-to-end po raporcie — analiza-sadowa-v6

> Plik przeniesiony ze SKILL.md bez zmian treści (progressive disclosure). Wczytaj w całości przed wykonaniem odpowiedniego kroku.

## FORMAT RAPORTU KOŃCOWEGO

```
RAPORT ANALITYCZNY — [Sygnatura / Sprawa]
Data: [DD.MM.RRRR] | Postępowanie: [rodzaj] | Etap: [etap]

EXECUTIVE SUMMARY
[3 zdania: prognoza + kluczowy czynnik decydujący + główna rekomendacja]

─── WYNIKI MODELU CZTEROPRZEBIEGOWEGO ─────────────────────────────────

PRZEJŚCIE I — MAPA FAKTYCZNA
  Chronologia: [zdarzenia z datami i dokumentami]
  Podmioty: [lista z rolami]
  Kwoty/daty: [rejestr]

PRZEJŚCIE II — MACIERZ FAKT-NORMA
  [tabela: fakt → norma (ELI) → znamię → status]
  Sporne: [...] | Niesporne: [...]

PRZEJŚCIE III — RAPORT ADVERSARIALNY
  Perspektywa sędziego: [...]
  Perspektywa przeciwnika: [...]
  Perspektywa własna: [...]
  V10 Sprzeczności: [lista]
  V10 Przyznania: [lista z wagą]
  WERYFIKACJA PIERWSZA: [korekty / STATUS: UKOŃCZONA]

PRZEJŚCIE IV — AUTOKOREKTA
  P1 ✓/✗ | P2 ✓/✗ | P3 ✓/✗ | P4 ✓/✗ | P5 ✓/✗
  WERYFIKACJA OSTATECZNA: [korekty / STATUS: UKOŃCZONA]
  GATE: ZATWIERDZONE TAK

─── RAPORT §1-§11 ──────────────────────────────────────────────────────

§1.  KWALIFIKACJA PRAWNA I ZNAMIONA
     Przepis: [pełna treść z ELI (RZĄD 1)]
     Znamiona: [każde oddzielnie — sporne vs niesporne]

§2.  ORZECZNICTWO
     [Sąd, DD.MM.RRRR, sygnatura, URL] — [teza max 14 słów]
     [max 3 orzeczenia, zweryfikowane oficjalnie]

§3.  STRONA PODMIOTOWA
     Zamiar: [z min. 3 elementów materiału]
     Forma winy: [zamiar bezpośredni/ewentualny/kierunkowy/nieumyślność]
     Alternatywne wyjaśnienie: [TAK/NIE + uzasadnienie]

§4.  OCENA MATERIAŁU DOWODOWEGO
     Poziom A: [...] | B: [...] | C: [...] | D: [...]
     Siła łączna: [0-10] | Luki: [...]

§5.  SŁABOŚCI STRON
     Powód/Oskarżyciel: [twierdzenia bez dowodu, sprzeczności, interes]
     Pozwany/Obrona:    [milczenie, sprzeczności z dokumentami]

§6.  TEST IN DUBIO
     Znamię 1 [nazwa]: PEWNE / WĄTPLIWE / NIEPEWNE → [skutek]
     [każde znamię osobno]
     Konkluzja: [wynik]

§7.  SYGNAŁY PROCEDURALNE
     [sygnał]: Interpretacja A [...] | Interpretacja B [...]

§8.  MODUŁY SPECJALISTYCZNE (tylko aktywne)
     [Moduł X]: [ustalenia kluczowe]

§9.  PREDYKCJA ROZSTRZYGNIĘCIA
     Wariant główny:       [wynik] [%] — [uzasadnienie] — pewność: [PEWNE/PRAWDOPODOBNE]
     Wariant alternatywny: [wynik] [%] — [warunek zmiany]
     Kluczowy czynnik:     [co zdecyduje]

§10. REKOMENDACJE PROCESOWE
     1. [działanie + podstawa prawna + pilność]
     2. [...] 3. [...]

§11. AUTOKOREKTA (skrót z Przejścia IV)
     P1 ✓ | P2 ✓ | P3 ✓ | P4 ✓ | P5 ✓
     Weryfikacja Pierwsza:    UKOŃCZONA
     Weryfikacja Ostateczna:  UKOŃCZONA
     GATE:                    ZATWIERDZONE TAK
```

---


## SEKWENCJA END-TO-END — PO RAPORCIE KOŃCOWYM

> KOLEJNOŚĆ JEST BEZWZGLĘDNA. Każdy krok w osobnej wiadomości.

```
WIADOMOŚĆ 6 — WIDGET RAPORTU SYTUACYJNEGO [OBOWIĄZKOWY]

Wykonaj natychmiast po §11 raportu końcowego, bez pytania o zgodę.

SEKWENCJA:
  1. view shared/raport-sytuacyjny-integracja.md
     (tylko jeśli nie wczytano w tej sesji)

  2. Zbuduj blueprint JSON ze schematu w raport-sytuacyjny-v2/SKILL.md
     → dane wyłącznie z rozmowy / dokumentów; pola nieznane → null
     → tryb: "A" (po pełnej analizie)

  3. show_widget(path="raport-sytuacyjny-v2/assets/widget-raport-sytuacyjny.html",
                 data=BLUEPRINT) — bez kodu; host wstawia dane i pasek IO.
     Host bez pola `data`: raport-sytuacyjny-v2/SKILL.md § WIDGET — WYKONANIE BEZ POLA `data`.

  Poprzedź widgetem komunikat:
  "Poniżej aktualny raport sytuacyjny sprawy —
   możesz uzupełnić brakujące dane lub skorygować automatycznie rozpoznane informacje."

WYJĄTEK: pomiń wiadomość 6 tylko gdy użytkownik zadał jedno pytanie
         bez dokumentów i bez stanu faktycznego sprawy.

---

WIADOMOŚĆ 7 — OFERTA PISMA PROCESOWEGO

Po widgecie (lub gdy wyjątek powyżej — bezpośrednio po raporcie):

  LAIK:    "Czy chcesz żebym napisał pismo na podstawie tej analizy?"
  PRAWNIK: "Czy wygenerować dokument procesowy? (.docx / .pdf)"
  → TAK → prawny-router-v3 → pisma-procesowe-v3 lub pisma-proste-v2
```
