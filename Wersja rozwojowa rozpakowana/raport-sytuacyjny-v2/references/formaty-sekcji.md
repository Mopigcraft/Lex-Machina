# Formaty sekcji raportu (przeniesione ze SKILL.md, treść bez zmian)

## STATUS ŹRÓDEŁ — KLASYFIKACJA

Każde ustalenie faktyczne musi otrzymać jeden z pięciu statusów:

| Status | Znaczenie | Zasada |
|---|---|---|
| `A — źródło bezpośrednie` | dokument, nagranie, e-mail, decyzja, pismo, akt | mocne ustalenie |
| `B — źródło pośrednie` | relacja, opis, streszczenie, odpowiedź strony | wymaga ostrożności |
| `C — twierdzenie strony` | informacja wyłącznie od użytkownika lub przeciwnika | nie traktować jako udowodnione |
| `D — luka dowodowa` | brak dokumentu lub brak potwierdzenia | oznaczyć jako ryzyko |
| `E — sprzeczność` | dwa źródła mówią co innego | skierować do bloku sprzeczności |

Zakaz mieszania ustaleń kategorii A z twierdzeniami kategorii C bez oznaczenia statusu.

---

## MAPA RYZYK — FORMAT

```json
{
  "ryzyko": "opis",
  "kategoria": "dowodowe|prawne|terminowe|formalne|strategiczne|kosztowe|reputacyjne",
  "prawdopodobieństwo": "niskie|średnie|wysokie",
  "wpływ": "niski|średni|wysoki|krytyczny",
  "podstawa": "z czego wynika ryzyko",
  "działanie_mitygujące": "konkretna czynność",
  "priorytet": "P1|P2|P3"
}
```

Priorytety:
- `P1` — może przesądzić o wyniku lub terminie; działanie natychmiastowe.
- `P2` — istotne, nie blokuje biegu sprawy.
- `P3` — porządkowe lub strategiczne.

Kolorowanie w widgecie:
- P1: `border-left: 3px solid var(--color-border-danger)` + `background: var(--color-background-danger)`
- P2: `border-left: 3px solid var(--color-border-warning)` + `background: var(--color-background-warning)`
- P3: `border-left: 3px solid var(--color-border-tertiary)` + `background: var(--color-background-secondary)`

---

## SPRZECZNOŚCI I LUKI — FORMAT

```json
{
  "punkt": "czego dotyczy sprzeczność",
  "wersja_1": "opis + źródło",
  "wersja_2": "opis + źródło",
  "znaczenie": "wysokie|średnie|niskie",
  "rekomendacja": "jak usunąć sprzeczność"
}
```

Wykrywaj obligatoryjnie: sprzeczne daty, sprzeczne kwoty, sprzeczne wersje zdarzeń, brak dokumentu potwierdzającego kluczową tezę, brak dowodu doręczenia, nieustaloną właściwość sądu, nieustalony termin.

Jeśli nie wykryto sprzeczności i materiał był wystarczający → `"Nie wykryto sprzeczności w dostarczonym materiale"`.
Jeśli materiał niewystarczający → `"Brak wystarczających danych do oceny sprzeczności"`.

---

## ZAKŁADKA RYZYKA — ROZSZERZENIE (priorytety aspektów)

Jeśli `priorytetyAspektow.aspekty_glowne` lub `aspekty_poboczne` niepuste —
dodaj w zakładce Ryzyka osobny blok PONAD mapą ryzyk P1/P2/P3:

```
SEKCJA "PRIORYTETY SPRAWY":
  ROSZCZENIA GŁÓWNE:
    [lista aspektów_glowne — każdy z odnośnikiem do powiązanego ryzyka
     w risk_map, jeśli istnieje]
  KWESTIE POBOCZNE:
    [lista aspektów_poboczne]
  METODY BADAWCZE ZASTOSOWANE:
    [metody_wybrane — per aspekt, format "ASP-X: MET-XXX (opis funkcjonalny
     z shared/MOD-METODY-BADAWCZE.md §5 — wersja LAIK/PRAWNIK wg detekcji
     persony)"]
```

Wizualnie: dwie kolumny (główne/poboczne) analogicznie do checklisty z
`shared/MOD-PRIORYTETY-ASPEKTOW.md` — ale tu w trybie tylko-odczyt
(edycja odbywa się w checklist, nie w raporcie).

Jeśli `priorytetyAspektow.aspekty_glowne` i `aspekty_poboczne` oba puste —
pomiń tę sekcję bez komunikatu (sprawa jednowątkowa, checklist nie była
wywoływana — zgodnie z `MOD-PRIORYTETY-ASPEKTOW.md` §3.4).

---

## ZAKŁADKA HISTORIA STRATEGII

Renderuj jako oś czasu wersji (najnowsza na górze), na podstawie
`historiaStrategii.wersje[]` (schema: `shared/MOD-HISTORIA-STRATEGII.md` §2).

```
DLA KAŻDEJ WERSJI:
  Nagłówek: "Wersja [n] — [timestamp]"
  Lista wariantów (warianty_pozwu[]):
    [nazwa] — Ryzyko: [P1/P2/P3] | Styl: [styl_sugerowany]
    [oznacz wybrany wariant (pole "wybor") wizualnie — np. ramka/badge "WYBRANY"]
    [jeśli powod_odrzucenia zawiera wpis dla tego wariantu — pokaż jako
     "Odrzucony: [powód]"]
  Przyciski:
    "Porównaj z aktualną wersją" — pokazuje diff wariantów między wersją
    historyczną i najnowszą (tylko jeśli ≥2 wersje)
    "Wróć do tego wariantu" → sendPrompt('Wróć do wariantu [nazwa] z wersji [n]')

GDY historiaStrategii.wersje jest puste:
  Komunikat: "Brak zapisanej historii strategii dla tej sprawy. Historia
  zapisywana jest automatycznie po wyborze wariantu pozwu w W1
  (pisma-procesowe-v3)."

GDY historiaStrategii.tryb === "A":
  Dodaj baner informacyjny (np. var(--color-background-warning)):
  "⚠️ Historia zapisana w trybie sesyjnym (Artifacts) — może nie przetrwać
  zamknięcia tej konwersacji. Dla trwałej historii skonfiguruj integrację
  z portalem (TRYB B w MOD-HISTORIA-STRATEGII)."
```

---

## REKOMENDACJE PROCESOWE — FORMAT

```json
{
  "działanie": "konkretna czynność",
  "cel": "co ma osiągnąć",
  "podstawa": "fakt/ryzyko/luka, z którego wynika",
  "termin": "data albo tryb: natychmiast / przed kolejnym pismem / przed rozprawą",
  "priorytet": "P1|P2|P3",
  "eskalacja_do_skilla": "nazwa skilla albo null"
}
```

Eskalacje (przyciski sendPrompt w zakładce Rekomendacje):

| Sytuacja | Eskalacja |
|---|---|
| Brak osi czasu | `chronologia-sprawy-v1` |
| Brak oceny dowodów | `analizator-dowodow-v3` |
| Potrzeba pisma | `pisma-procesowe-v3` |
| Pytania do świadka | `przesluchanie-swiadkow-v2-min90` |
| Problem z podstawą prawną | `analizator-przepisow-v2` |
| Potrzeba orzecznictwa | `orzeczenia-sadowe-v2` |
