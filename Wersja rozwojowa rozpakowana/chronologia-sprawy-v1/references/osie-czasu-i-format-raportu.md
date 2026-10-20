# Osie czasu per wątek, struktura zdarzenia, format raportu (TRYB A)

> Plik obowiązkowy dla budowy osi czasu i KROK A6. Treść przeniesiona dosłownie z SKILL.md (refaktor 2026-10-20); SKILL.md zawiera nagłówki i streszczenia.

## OSIE CZASU PER WĄTEK PRAWNY

### Zasada wątków

```
KROK W1 — Identyfikuj wątki prawne przed budową chronologii:
  Przykłady:
  • Sprawa pracownicza: [W1] Stosunek pracy, [W2] Wypowiedzenie, [W3] Mobbing, [W4] ZUS
  • Sprawa cywilna:     [W1] Umowa, [W2] Naruszenie, [W3] Szkoda, [W4] Postępowanie sądowe
  • Sprawa karna:       [W1] Czyn, [W2] Postępowanie przygotowawcze, [W3] Sąd I inst.

KROK W2 — Przypisz każde zdarzenie do wątku (lub kilku — węzeł wspólny):
  zdarzenie.watki = ["W1", "W2"]  ← pojawia się na obu osiach z oznaczeniem [WSPÓLNY]

KROK W3 — Buduj osobną oś czasu per wątek:
  Każda oś: tylko zdarzenia należące do danego wątku
  Węzły wspólne: wyróżnione wizualnie, z odesłaniem do innych wątków

KROK W4 — Generuj widok zbiorczy (CROSS-WĄTEK):
  Wszystkie zdarzenia razem — do wykrywania sprzeczności MIĘDZY wątkami
```

### Struktura zdarzenia (v1.1)

```
ZDARZENIE:
  id:                [Z-001, Z-002, … — od v1.13; ten sam ID w grafie przyczynowym i w MP13 (pole fakt_m1)]
  data:              [dd.mm.rrrr lub zakres lub ~miesiąc.rrrr lub "MIĘDZY X a Y"]
  pewnosc:           [BEZSPORNE / PEWNE / WYDEDUKOWANE / SPORNE]
  dedukacja:         [null / opis rozumowania + podstawa + przedział czasowy]
  opis:              [co się wydarzyło — 1 zdanie, faktycznie, bez ocen]
  strona:            [kto działał: powód / pozwany / sąd / organ / osoba trzecia]

  proweniencja:
    typ_zrodla:      [DOKUMENT_URZEDOWY / DOKUMENT_PRYWATNY / ZEZNANIE /
                      KORESPONDENCJA / DEDUKCJA / TWIERDZENIE_STRONY]
    dok_id:          [DOK-01 / DOK-02 / … — identyfikator z inwentaryzacji]
    strona_dok:      [numer strony / akapit / §X / nagłówek / "str. 3, ust. 2"]
    autor_twierdzenia: [powód / pozwany / sąd / biegły / organ / obie_strony]

  watki:             ["W1", "W3"]  — lista wątków prawnych
  wezel_wspolny:     [true / false]
  znaczenie:         [KLUCZOWE / ISTOTNE / TŁO]
  kolizja_id:        [null / "SPRZECZNOŚĆ-01" — odesłanie do Indeksu Sprzeczności]
  typ_kolizji:       [null / DATA / OPIS / DATA_I_OPIS]
  przyczyny:         [od v1.13, opcjonalnie — [{ "od": "Z-003", "typ": "WYWOLUJE", "dowod": "KORELACJA" }];
                      tylko gdy materiał mówi coś o MECHANIZMIE; sama kolejność dat to nie przyczyna
                      (post hoc) — pełna analiza w TRYBIE C]
```

---

## FORMAT RAPORTU CHRONOLOGICZNEGO (TRYB A)

```
## CHRONOLOGIA SPRAWY — [tytuł sprawy lub opis]
Wygenerowano: [data]  |  Dokumentów: N  |  Wątków: W  |  Zdarzeń: M  |  Sprzeczności: K

### INWENTARYZACJA DOKUMENTÓW
DOK-01: [nazwa / typ / data pisma / autor]
DOK-02: …

### OŚ CZASU — WĄTEK [W1]: [nazwa wątku]

[data]  ✓✓ [BEZSPORNE]
        [opis zdarzenia]
        Strona: [kto] | Prow.: DOK-01, str. 3 | Autor twierdzenia: obie strony
        Wątki: W1

[data]  ✓ [PEWNE]
        [opis zdarzenia]
        Strona: [kto] | Prow.: DOK-02, str. 1, nagłówek | Autor: powód

[data]  ~ [WYDEDUKOWANE / pewność: 8/10]
        [opis zdarzenia]
        Dedukuję: DOK-01 (str. 4) potwierdza X, DOK-03 (str. 2) potwierdza Y
        Wniosek: zdarzenie nastąpiło MIĘDZY 12.03.2023 a 15.04.2023
        Strona: [kto] | Wątki: W1, W2 ← [WSPÓLNY]

[data]  ⚠ [SPORNE] → zob. SPRZECZNOŚĆ-01
        [opis zdarzenia]
        Prow.: DOK-02 str. 5 (powód) vs DOK-04 str. 1 (pozwany)

### OŚ CZASU — WĄTEK [W2]: [nazwa wątku]
…

### OŚ CZASU — WIDOK ZBIORCZY (CROSS-WĄTEK)
[wszystkie zdarzenia posortowane chronologicznie, z oznaczeniem wątku]

### FAKTY BEZSPORNE
✓✓ [lista zdarzeń klasy BEZSPORNE — do prezentacji w piśmie bez dowodzenia]

### INDEKS SPRZECZNOŚCI

Rejestr obejmuje WSZYSTKIE wykryte rozbieżności — zarówno dotyczące dat,
jak i opisów zdarzeń (co się stało, w jaki sposób, kto był sprawcą, jaki był przebieg).

SPRZECZNOŚĆ-[N]:
  Typ:         [DATA / OPIS / DATA_I_OPIS / IDENT]
  Zdarzenie:   [opis zdarzenia którego dotyczy sprzeczność]
  Wątek:       [W1 / W2 / …]

  ── jeśli Typ = DATA lub DATA_I_OPIS ──
  Data wg A:   [data1] | DOK-[XX], str. [N] | Autor: [powód / pozwany / sąd / …]
  Data wg B:   [data2] | DOK-[YY], str. [M] | Autor: [powód / pozwany / sąd / …]
  Różnica:     [N dni]

  ── jeśli Typ = OPIS lub DATA_I_OPIS ──
  Opis wg A:   "[dosłowny opis lub cytat]" | DOK-[XX], str. [N] | Autor: [powód / …]
  Opis wg B:   "[dosłowny opis lub cytat]" | DOK-[YY], str. [M] | Autor: [pozwany / …]
  Rozbieżność: [co dokładnie się różni — przebieg / sprawca / skutek / okoliczności]

  ── jeśli Typ = IDENT ──
  Osoba wg sprawy:     [imię/nazwisko jak w pismach procesowych] | DOK-[XX]
  Osoba wg dokumentu:  [zapis na podpisie/dokumencie] | DOK-[YY], str. [M]
  Rozbieżność:         [literówka / inna osoba / błąd OCR / niewyjaśnione]

  ── wspólne dla wszystkich typów ──
  Common ground: [null lub opis tego, co OBIE strony przyznają w tej kwestii —
                   element niesporny mimo istnienia sprzeczności]
  Kategoria:   [A-KRYTYCZNA / B-ISTOTNA / C-MARGINALNA]
  Wpływ:       [opis konsekwencji procesowych]
  Rekomendacja: [które źródło wiarygodniejsze i dlaczego / co wyjaśnić]

### ZDARZENIA WYDEDUKOWANE — REJESTR
[lista wszystkich zdarzeń WYDEDUKOWANE z pełnym opisem rozumowania i przedziałem czasowym]

### LUKI CZASOWE
  📌 Wątek [W1]: Brak dokumentów z okresu [od] → [do] ([N dni])
     Potencjalnie istotne: [co mogło się wydarzyć]

### ZDARZENIA NIEUSTALONE CHRONOLOGICZNIE
  ? [opis] — brak daty, wzmiankowane w: DOK-XX, str. N

### REKOMENDACJE DO PISMA
  → Fakty bezsporne (nie wymagają dowodzenia): [lista]
  → Fakty pewne kluczowe dla uzasadnienia: [lista]
  → Fakty wydedukowane — rozwinąć łańcuch logiczny: [lista]
  → Daty wymagające weryfikacji lub wyjaśnienia sprzeczności: [lista]
  → Sugerowana kolejność w uzasadnieniu faktycznym: [numerowana lista]
```
