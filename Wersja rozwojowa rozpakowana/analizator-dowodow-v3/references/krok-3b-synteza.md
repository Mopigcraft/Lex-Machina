# KROK 3B — SYNTEZA: ASPEKTY -> PRZEPISY -> SELEKCJA DOWODÓW (szczegóły)

> ⛔ Ten krok istniał wcześniej pod nazwą „KROK 4a" (z podkrokami 4a.1–4a.6),
> zanim analizator-dowodow-v3 został przebudowany na router KROK 2/3/4
> (MD/MP-moduły). Nazwa „KROK 4a" **nie istnieje już w tym pliku**, ale
> pozostała rozsiana po innych skillach (`przesluchanie-swiadkow-v2-min90`,
> `pisma-procesowe-v3/references/W1-SZCZEGOLY.md`, `shared/MOD-KONTEKST-SESJI.md`,
> `shared/MOD-MAPA-PRZEPISOW.md`, `shared/MOD-SELEKCJA-DOWODOW.md`,
> `shared/MOD-PRIORYTETY-ASPEKTOW.md`, `prawny-router-v3/SKILL.md`,
> `audyt-systemu-v4/references/CHECKLIST-DEDUP.md`) jako odwołanie do
> punktu, który przestał istnieć pod tą nazwą. **KROK 3B to ten sam punkt
> integracji, odtworzony pod nazwą zgodną z aktualną strukturą** —
> wykonywany PO zakończeniu KROK 3 (a w nim: po MD6/MP7), PRZED KROK 4
> (dashboard), niezależnie od tego czy B1=TAK (dashboard jest opcjonalny,
> KROK 3B nie jest).

```
KROK 3B.1 — ASPEKTY GŁÓWNE/POBOCZNE:
  view /mnt/skills/user/shared/MOD-PRIORYTETY-ASPEKTOW.md
  Wykonaj checklistę klasyfikacji/priorytetyzacji na podstawie wyniku KROK 3
  (w tym MD6/MP7) → wynik: aspekty_glowne[], aspekty_poboczne[]

KROK 3B.2 — MAPOWANIE NA PRZEPISY (dawne "KROK 4a.3"):
  view /mnt/skills/user/shared/MOD-MAPA-PRZEPISOW.md
  Zmapuj aspekty z KROK 3B.1 na przepisy kandydujące (oznaczenia
  ⚠️ [akt] art. [X] (NIEWERYFIKOWANE) — bez wywoływania ELI/ISAP na tym etapie)
  → wynik: mapa_przepisow{}

KROK 3B.3 — SELEKCJA DOWODÓW (dawne "KROK 4a.5"):
  view /mnt/skills/user/shared/MOD-SELEKCJA-DOWODOW.md
  Na podstawie mapa_przepisow{} z KROK 3B.2 dobierz dowody do każdej tezy,
  oznacz ryzyko krzyżowe (HARDGATE-SD-01/02 z tego modułu obowiązują)
  → wynik: selekcja_dowodow{}, ostrzezenia_krzyzowe[]

KROK 3B.4 — EKSPORT PAKIETU KONTEKSTU:
  Złóż wynik w jeden obiekt do przekazania dalej (do pisma-procesowe-v3 W1.3,
  przesluchanie-swiadkow-v2-min90 KROK 0, MOD-KONTEKST-SESJI EXPORT):
    kontekst_sprawy = {
      aspekty_glowne, aspekty_poboczne,   ← KROK 3B.1
      mapa_przepisow,                       ← KROK 3B.2
      selekcja_dowodow,                     ← KROK 3B.3
      ostrzezenia_krzyzowe,                 ← KROK 3B.3
      wyniki_metod,                         ← BLOK E2a-j / MD-moduły metod (streszczenia)
      chronologia_wstepna                   ← TYLKO jeśli chronologia-sprawy-v1 wykonana osobno
    }
```

**Uwaga zgodności wstecznej:** wszystkie zewnętrzne odwołania do „KROK 4a" /
„KROK 4a.3" / „KROK 4a.5" w innych skillach zostały w tym samym audycie
zaktualizowane odpowiednio do „KROK 3B" / „KROK 3B.2" / „KROK 3B.3" — patrz
`audyt-systemu-v4/references/AUDIT-JOURNAL.md`, wpis AUDYT-2026-07-12c.
