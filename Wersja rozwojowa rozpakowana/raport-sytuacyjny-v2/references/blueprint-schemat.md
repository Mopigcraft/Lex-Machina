# Blueprint JSON — schemat danych (przeniesione ze SKILL.md, treść bez zmian)

## BLUEPRINT JSON — SCHEMAT DANYCH

```json
{
  "tryb": "A|B|C",
  "przepis": "art. X KP/KK/...",
  "czyn": "opis roszczenia / czynu",
  "etap": "przedsądowy|I instancja|apelacja|kasacja|egzekucja",
  "dziedzina": "karne|cywilne|pracownicze|admin|rodzinne|spadkowe|gospodarcze",
  "sygnatura": null,
  "termin": null,
  "pilnosc": "natychmiastowa|wysoka|normalna|niska",
  "confidence": 0,
  "uwagi_pewnosci": "tekst",
  "s1rola": "powód|oskarżony|wnioskodawca|...",
  "s1opis": "opis strony 1",
  "s2rola": "pozwany|oskarżyciel|...",
  "s2opis": "opis strony 2",
  "zdarzenie": "1–3 zdania stanu faktycznego",
  "skutki": null,
  "p1lbl": "wygranie|skazanie|...",
  "p1pct": 0,
  "p1opis": null,
  "p2lbl": null,
  "p2pct": 0,
  "p2war": null,
  "sources": [
    {"status": "A|B|C|D|E", "type": "dokument|...", "name": "opis",
     "impact": "wysoki|średni|niski", "ryzyko": null}
  ],
  "dowody": [
    {"opis": "...", "poziom": "A|B|C|D", "typ": "...",
     "zrodlo": "...", "ryzyko": null}
  ],
  "risk_map": [
    {"level": "P1|P2|P3", "name": "...", "probability": "...",
     "wplyw": "...", "mitigation": "..."}
  ],
  "conflicts": [
    {"type": "...", "opis": "...", "znaczenie": "...", "rekomendacja": "..."}
  ],
  "chronologia": [
    {"data": "YYYY-MM-DD|null", "zdarzenie": "...", "zrodlo": "...",
     "status_zrodla": "zweryfikowane|częściowe|twierdzenie strony|brak źródła",
     "znaczenie_procesowe": "wysokie|średnie|niskie", "ryzyko": null}
  ],
  "procedural_recommendations": [
    {"text": "...", "deadline": "..."}
  ],
  "nastepnyKrok": null
}
```

**Reguła antyhalucynacyjna:** Pola bez podstawy w materiale → `null`. Nie wymyślaj dat, kwot, sygnatur ani stron. Jeśli data nie wynika z materiału → `null`.

**Pole `chronologia[]`:** Jeśli w historii rozmowy istnieje blok "DANE CHRONOLOGICZNE DLA RAPORTU SYTUACYJNEGO" wygenerowany przez chronologia-sprawy-v1 — wyciągnij go i użyj jako wartości tego pola.

```javascript
// Logika auto-zasilania chronologii w widgecie HTML:
const chronSource = window._chronologiaData || null;
if (chronSource && blueprint.chronologia.length === 0) {
  blueprint.chronologia = chronSource;
}
```

**Pola rozszerzone blueprintu** (wbuduj obok schematu głównego w widgecie):

```json
{
  "ustaleniaZeStatusemZrodla": [],
  "mapaRyzyk": [],
  "sprzecznosciILuki": [],
  "rekomendacjeProcesowe": [],
  "poziomPewnosciRaportu": 0,
  "ograniczeniaRaportu": [],
  "priorytetyAspektow": {
    "aspekty_glowne": [],
    "aspekty_poboczne": [],
    "metody_wybrane": {}
  },
  "historiaStrategii": {
    "tryb": "A|B|null",
    "wersje": []
  }
}
```

**Pole `priorytetyAspektow`:** jeśli w historii rozmowy wystąpił wynik
`shared/MOD-PRIORYTETY-ASPEKTOW.md` (checklist klasyfikacji), wyciągnij go i
użyj jako wartości tego pola. Aspekty główne i poboczne renderowane są jako
dwie listy w zakładce Ryzyka (patrz §"ZAKŁADKA RYZYKA — ROZSZERZENIE").

**Pole `historiaStrategii`:** jeśli `shared/MOD-HISTORIA-STRATEGII.md` zwróciło
wpisy (TRYB A — window.storage, lub TRYB B — eksport z portalu), wyciągnij
listę wersji jako `wersje[]` (wg schematu §2 tego modułu) i ustaw `tryb`.
Jeśli brak wpisów → `wersje: []`, `tryb: null` — zakładka "Historia strategii"
renderowana jest, ale z komunikatem "Brak zapisanej historii dla tej sprawy".

`poziomPewnosciRaportu` 0–10: zakaz 9–10 przy braku źródeł dla kluczowych faktów.
