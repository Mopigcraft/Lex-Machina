# BLOK I — Import / Eksport raportu (wczytaj przed KROK 4)

## BLOK I — Import / Eksport raportu

```
I0. MOD-WIDGET-IO (OBOWIĄZKOWE — wczytaj przed wygenerowaniem dashboardu):
    view /mnt/skills/user/shared/MOD-WIDGET-IO.md
    → wbuduj pasek IO w nagłówek dashboardu (powyżej zakładek)
    → IO_SKILL_ID='analizator-dowodow-v3', IO_CASE_ID=CASE_ID
    → matryca: Export JSON ✅ MD ✅ CSV ✅ | Import JSON ✅
    → ioGetState(): { evidence, contradictions, persons, nazewnictwo,
                      dis_items, coverage_data, gaps, recs, lapsus }
    → ioSetState(s): odtwórz dashboard z wczytanego JSON (wszystkie zakładki)

I1. Dashboard wygenerowany (B1=TAK i KROK 4 wykonany)?
    TAK → dodaj przyciski eksportu do dashboardu:

    EKSPORT-JSON: serializacja tablic evidence[], contradictions[], persons[], nazewnictwo[],
                  dis_items[], coverage_data[], gaps[], recs[] do pliku .json
                  → Blob + URL.createObjectURL + link.click()

    EKSPORT-MD:   generowanie raportu Markdown z sekcjami:
                  # Analiza dowodów — [sygnatura] — [data]
                  ## Strony i świadkowie
                  ## Rejestr dowodów
                  ## Sprzeczności INTRA / CROSS / IDENT
                  ## Nazewnictwo procesowe
                  ## Kwestie sporne DIS
                  ## Pokrycie przesłanek i luki
                  ## Rekomendacje procesowe
                  Każdy przepis → ⚠ [WYMAGA WERYFIKACJI RZĄD 1]

    EKSPORT-CSV:  tabela evidence[] jako CSV (id, nazwa, typ, poziom, score, alerty, opis)

    Pozycja przycisków: pasek eksportu w nagłówku dashboardu (obok przycisku "Sporządź pismo")
    Ikony: JSON=💾  MD=📄  CSV=📊
```
