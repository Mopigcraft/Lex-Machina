# Walidacja kompletności blueprintu i funkcje widgetu (przeniesione ze SKILL.md, treść bez zmian)

## WALIDACJA KOMPLETNOŚCI BLUEPRINTU

Wykonaj przed renderowaniem widgetu:

```
POLA OBOWIĄZKOWE:
  □ dziedzina         → null?  → ⬛ [UZUPEŁNIJ: cywilne/karne/pracownicze/admin/inne]
  □ etap              → null?  → ⬛ [UZUPEŁNIJ: przedsądowy/I instancja/apelacja/...]
  □ s1rola + s1opis   → null?  → ⬛ [UZUPEŁNIJ: kim jest strona 1]
  □ s2rola + s2opis   → null?  → ⬛ [UZUPEŁNIJ: kim jest strona 2]
  □ zdarzenie         → null?  → ⬛ [UZUPEŁNIJ: stan faktyczny 1–3 zdania]
  □ p1lbl + p1pct     → null?  → ⬛ [UZUPEŁNIJ: scenariusz główny i prawdopodobieństwo]

POLA OSTRZEGAWCZE:
  □ sources[]         → pusta? → ⚠️ brak rejestru źródeł
  □ risk_map[]        → pusta? → ⚠️ brak mapy ryzyk
  □ chronologia[]     → pusta? → ⚠️ brak osi czasu — rozważ chronologia-sprawy-v1

WYNIK:
  0 pól ⬛ → GOTOWY    → renderuj widget
  1–2 ⬛  → CZĘŚCIOWY → renderuj widget z banerem "⚠️ Raport częściowy — uzupełnij pola [lista]"
  ≥3 ⬛   → ROBOCZY   → renderuj widget z banerem "⛔ Wersja robocza — brak kluczowych danych"
                        + wyświetl listę brakujących pól przed widgetem
```

Baner statusu w widgecie (sekcja Sprawa):

| Status | Kolor | Tekst |
|---|---|---|
| GOTOWY | `var(--color-background-success)` | `✅ Raport kompletny` |
| CZĘŚCIOWY | `var(--color-background-warning)` | `⚠️ Raport częściowy — uzupełnij pola [lista]` |
| ROBOCZY | `var(--color-background-danger)` | `⛔ Wersja robocza — brak kluczowych danych` |


## FUNKCJE WIDGETU

- **7 zakładek:** Sprawa | Chronologia | Źródła | Ryzyka | Luki i sprzeczności | Rekomendacje | Historia strategii
- **Baner statusu** (GOTOWY / CZĘŚCIOWY / ROBOCZY) w zakładce Sprawa
- **Auto-fill** — dane z rozmowy wyciągane automatycznie przy każdym otwarciu; brak Anthropic API
- **Detekcja trybu** — widget wykrywa [A]/[B]/[C] i pokazuje go w badge
- **Edycja inline** — metadane, strony, stan faktyczny, dowody, predykcja
- **Oznaczanie zmian** — niebieski kontur + badge "zmienione" na każdym edytowanym elemencie
- **Oznaczanie dowodów** — każdy dowód zmieniony względem auto-fill jest oznaczony
- **Historia zmian** — pełny log z godziną, cofanie Ctrl+Z, ponawianie Ctrl+Y
- **Resetuj** — powrót do stanu auto-fill jednym kliknięciem
- **Graceful fallback** — przy błędzie renderowania widget otwiera się w trybie ręcznym
  z amber-barem i komunikatem błędu; użytkownik uzupełnia pola ręcznie
- **Historia snapshota** — tryb ręczny zapisuje się jako "Tryb ręczny — brak auto-fill" w historii
- **Retry ×2 z backoffem** — przy błędzie: próba 1 natychmiast, próba 2 po 500 ms, próba 3 po 1000 ms
- **Timeout 15s** — AbortController przerywa fetch po 15 sekundach; nie blokuje widgetu
- **📄 Eksportuj PDF** — pełny raport: metadane, strony, stan faktyczny, rejestr dowodów,
  predykcja, chronologia, ryzyka, rekomendacje, historia zmian; otwiera dialog drukowania
- **Kontynuuj ↗** — sendPrompt do dalszej pracy z Claude
- **Przyciski sendPrompt** w zakładce Rekomendacje dla kolejnych kroków akcji

### Integracja z analizatorem umów v1.8

Gdy raport generowany po analizie umowy — dodaj sekcję RYZYKA KONTRAKTOWE w zakładce Ryzyka:

```
TRIGGER: sprawa zawiera umowę / kontrakt / OWU / regulamin

SEKCJA KONTRAKTOWA (lazy — tylko gdy analiza umowy była wcześniej):
  □ Ekspozycja finansowa klauzul → wynik z mod-shared-economic.md
  □ Brakujące klauzule TOP 3    → wynik z mod-shared-missing-clause.md
  □ Aktywne regulacje UE        → wynik z mod-shared-regulatory-horizon.md
  □ Kluczowe orzecznictwo       → wynik z mod-shared-orzecznictwo-umow.md

Format w zakładce Ryzyka (dodaj jako osobny blok):
  | Klauzula | Ryzyko finansowe | Poziom A/B/C/D | Regulacja |
  Rekomendacja: [playbook FL z mod-shared-fallback-library.md]
```
