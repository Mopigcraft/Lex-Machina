# KROK 2 — BLOK G (rejestr stron), BLOK J (lapsusy), BLOK H (DIS)

## BLOK G — Rejestr stron, świadków i osób trzecich (ZAWSZE przy A2=TAK)

```
G1. Materiał zawiera pisma procesowe, akta lub dokumenty z udziałem osób?
    TAK → wykonaj BLOK-STRONY przed MD3c:

    BLOK-STRONY — dla każdej osoby/podmiotu utwórz kartę:
    - Imię i nazwisko / nazwa (DOSŁOWNIE jak w dokumencie — nie normalizuj)
    - Rola procesowa: Powód / Pozwany / Pełnomocnik / Świadek / Biegły / Osoba trzecia / Organ
    - Status procesowy: strona czynna / bierna / świadek wnioskowany / świadek wzywany / organ
    - Umocowanie: pełnomocnictwo (data, zakres) / organ statutowy / brak danych
    - Dane kontaktowe / adres doręczeń (jeśli znane z materiału)
    - Alerty IDENT: jeśli ta sama osoba pojawia się pod różnymi zapisami → od razu
      przekaż do MD3c jako kandydat [DOUBT][IDENT] / [CROSS][IDENT]
    - Znaczenie dla sprawy: kluczowe / pomocnicze / tło

    Format karty w dashboardzie: zakładka "Strony i świadkowie"
    Kategorie kolorystyczne: Powód (niebieski) / Pozwana (bursztynowy) / Świadek (fioletowy) / Inne (szary)

G2. Materiał zawiera pisma jednej strony (analiza wyłącznie pism Pozwanej lub Powoda)?
    TAK → dodaj: BLOK-NAZW (kontrola nazewnictwa procesowego)

    Wczytaj tabelę nazewnictwa dla trybu sprawy:
    view /mnt/skills/user/shared/NAZEWNICTWO-STRON.md
    → Tabela T1 (cywilne procesowe), T2 (nieprocesowe), T3 (karne), T4 (wykroczenia)
       T5 (KPA), T6 (PPSA/WSA), T7 (pracownicze), T8 (egzekucja), T9 (zabezpieczenie)
       T10 (rodzinne)
    → Wymogi formalne: W1-W7 (art. 126 KPC, 187 KPC, 511 KPC, 57 PPSA i in.)
    → Wzory nagłówków: N1-N7 (pozew, odpowiedź, wniosek, skarga WSA, zawiadomienie, wezwanie)
    → Reguły C1 (test rodzaju gramatycznego) i C2 (test kompletności podmiotów)

    BLOK-NAZW — sprawdź konsekwentność nazewnictwa w pismach:
    [ ] Czy autor pisma konsekwentnie używa "Powód" / "Pozwany" / "Pozwana" (odpowiedni rodzaj)?
    [ ] Czy przez zamienne użycie zaimków ("on", "ona") podmiot zdania może być niejednoznaczny?
    [ ] Czy kwalifikacje prawne tej samej osoby/kwoty są spójne między pismami (np. "zaliczka"
        vs "nienależnie pobrane" to dwie różne kwalifikacje tej samej kwoty — wzajemnie sprzeczne)?
    [ ] Czy autor pisma odpiera twierdzenie, które strona przeciwna nigdy nie postawiła
        (sygnalizując tym Sądowi argument, który chce zneutralizować)?
    [ ] Czy wniosek o przesłuchanie / pominięcie dotyczy właściwej osoby / właściwej roli procesowej?
    [ ] Czy strona pozwana jest konsekwentnie opisywana jako spółka / osoba fizyczna zgodnie z KRS?

    Format alertów: NZ-1, NZ-2... z cytatem, problemem, skutkiem i rekomendacją
    Renderuj w dashboardzie jako zakładka "Nazewnictwo procesowe"
```

---

## BLOK J — Lapsusy autorskie [LAPSUS] (ZAWSZE przy A2=TAK, gdy autor pisma znany)

```
Wczytaj moduł przed wykonaniem:
view /mnt/skills/user/analizator-dowodow-v3/modules/MOD-LAPSUS-AUDYT.md
    view /mnt/skills/user/shared/NAZEWNICTWO-STRON.md
    (tabele T1-T10 wymagane dla KROK L0 i KROK L1 w MOD-LAPSUS-AUDYT)

Moduł zawiera pełny protokół L0-L5 + 22 typy lapsusów w 4 kategoriach:
  Kategoria I  — Podmiot: [LA-RODZAJ][LA-PODMIOT][LA-PODMIOT-POWTORZONY]
                           [LA-NAZWA-PODMIOT][LA-OSOBA-MYLONA]
  Kategoria II — Kwalifikacja: [LA-KWALIF][LA-KWALIFIKACJA-PRAWNA]
                                [LA-KWALIFIKACJA-TECHNICZNA][LA-LEGAL][LA-BRAK-KONKRETYZACJI]
  Kategoria III— Logika: [INTRA-SAMOOBALA][LA-PRZYZNANIE-KORZYSTNE][LA-TEZA-DOWODOWA]
                          [LA-INTENCJA][LA-NARR][LA-ZAKRES-DOWODOWY]
  Kategoria IV — Dokument: [LA-KOSZTY][LA-DATA][LA-DATA-PRZYSZLA][LA-KWOTA]
                             [LA-KWOTA-SLOWNIE-CYFRAMI][LA-ODRECZNIE][LA-CHRONOLOGIA]
                             [LA-MIESIAC][LA-PODMIOT-ROLA][LA-SYGNATURA]

Pole wzorzec karty LA: SZABLON | JEDNOSTKOWY | SYSTEMOWY
  SYSTEMOWY → KROK L5: tabela wzorca dla Sądu (gdy ≥2 błędy tego samego typu)

Wynik → tablica lapsusy[] w KROK 4 (dashboard, zakładka "Lapsusy")
Eksport: JSON + MD + CSV
```

---

## BLOK H — Kwestie sporne DIS z drill-down (gdy D4=TAK lub D3=TAK)

```
H1. Sprawa zawiera zidentyfikowane roszczenia / zarzuty / przedmioty sporu?
    TAK → wykonaj BLOK-DIS dla każdej kwestii spornej:

    BLOK-DIS — dla każdej kwestii spornej (DIS01, DIS02...) utwórz rekord:
    - Tytuł kwestii
    - Fakty bezsporne / common ground (co obie strony de facto przyznają)
    - Stanowisko Powoda (z materiału lub "nieznane — brak pisma Powoda")
    - Stanowisko Pozwanej
    - Stosowne przepisy prawne:
      ⛔ HARDGATE: każdy przepis musi mieć etykietę "wymaga weryfikacji w ELI (RZĄD 1)"
      Nie cytuj treści przepisu z pamięci — tylko art. + ustawa + oznaczenie HARDGATE
    - Rekomendacje procesowe: konkretne wnioski, żądania, argumenty
    - Przycisk drill-down: "Głębsza analiza DIS-XX ↗" → sendPrompt

    Format w dashboardzie: zakładka "Kwestie sporne DIS" z accordion (kliknij → rozwiń)
    Priorytet kwestii: KRYTYCZNA (blokuje główne roszczenie) / ISTOTNA / POBOCZNA
```
