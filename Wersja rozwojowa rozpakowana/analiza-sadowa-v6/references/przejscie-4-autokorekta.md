# Przejście IV (autokorekta + weryfikacja ostateczna) — analiza-sadowa-v6

> Plik przeniesiony ze SKILL.md bez zmian treści (progressive disclosure). Wczytaj w całości przed wykonaniem odpowiedniego kroku.

### PRZEJŚCIE IV — AUTOKOREKTA + WERYFIKACJA OSTATECZNA
**Cel: Spójność I-III + drugie i ostatnie obowiązkowe przeczytanie weryfikacyjne.**

#### 4A. Pięć pytań autokorekty P1-P5

```
P1. ZAKORZENIENIE
    Czy każdy wniosek prawny z II wynika z konkretnego faktu z I?
    NIE → usuń lub wskaż lukę dowodową.

P2. IZOLACJA
    Czy ocena prawna z II nie zanieczyszcza ustaleń faktycznych z I?
    TAK (zanieczyszczenie) → wróć do I i oczyść mapę.

P3. SYMETRIA
    Czy w III przeanalizowano słabości OBU stron z równą starannością?
    NIE → uzupełnij słabiej opracowaną stronę.

P4. SPÓJNOŚĆ NARRACYJNA
    Czy teoria sprawy z III jest spójna z chronologią z I?
    NIE → zidentyfikuj punkt sprzeczności, wyjaśnij lub skoryguj.

P5. POZIOMY PEWNOŚCI
    Czy każdy wniosek ma oznaczony poziom: PEWNE/PRAWDOPODOBNE/WĄTPLIWE/SPEKULATYWNE?
    NIE → dodaj oznaczenia przed raportem.

P6. IZOLACJA DZIEDZINOWA  (DOMAIN-LOCK, dodane 2026-08-23 — F-109)
    Czy w raporcie jest kwalifikacja spoza dziedziny wiodącej sprawy?
    TAK → czy opiera się na KONKRETNYM fakcie z PRZEJŚCIA I, a nie na
          skojarzeniu tematycznym (dług→oszustwo, konflikt→znęcanie)?
    NIE → ⛔ usuń kwalifikację. Sygnalizacja wątku bez podstawy faktycznej
          wyłącznie opisowo, BEZ numeru artykułu (DL-5).
    → view shared/DOMAIN-LOCK.md

P7. KOMPLETNOŚĆ SZEREGU  (RATE-COMPLETENESS, dodane 2026-08-23 — F-109)
    Czy predykcja §9 lub wyliczenie roszczenia opiera się na odsetkach /
    waloryzacji / wskaźniku zmiennym w czasie?
    TAK → czy szereg podokresów pokrywa cały przedział BEZ LUK, z rozdzielonym
          reżimem i znacznikiem na każdym wierszu?
    NIE → ⛔ nie podawaj kwoty łącznej; tabela z jawnymi ⬛.
    → view shared/RATE-COMPLETENESS.md
```

#### 4B. WERYFIKACJA OSTATECZNA — ponowne przeczytanie dokumentów

> To jest DRUGIE i ostatnie obowiązkowe przeczytanie weryfikacyjne.
> Cel: niezależna kontrola raportu końcowego przed jego wydaniem.
> Różnica od Weryfikacji Pierwszej: skupia się na kompletności i spójności
> całego raportu, nie tylko poszczególnych ustaleń.

> ⚠️ REGUŁA BEZWZGLĘDNA — MECHANIZM PONOWNEGO CZYTANIA:
> Identyczna reguła jak w Weryfikacji Pierwszej — obowiązkowe wywołanie view.
>
> PRZED krokiem O1: wywołaj view na każdy dokument zawierający dowód
>   wpływający na predykcję §9 raportu końcowego — dla każdego wariantu
>   predykcji osobno (wariant główny + alternatywny).
> PRZED krokiem O2: wywołaj view na fragmenty pism procesowych zawierające
>   każde przyznanie V10-2 o wadze KRYTYCZNA — sprawdź pełny akapit.
>
> ZAKAZ: Opisywanie "ponownego przeczytania" bez uprzedniego wywołania view
>   jest bezwzględnie zakazane. Identyczne konsekwencje jak w Weryfikacji Pierwszej.
>
> FORMAT OBOWIĄZKOWY przed każdym krokiem O:
>   [view: {katalog załączników hosta}/{plik}, strony {X}-{Y}]
>   (claude.ai: /mnt/user-data/uploads/; UNIVERSAL-RUNTIME-ADAPTER §4)
>   → co odczytano / potwierdzono / skorygowano

```
WERYFIKACJA OSTATECZNA — PROTOKÓŁ

Krok O1: Dowody kluczowe — view + drugie przeczytanie
  OBOWIĄZEK: view na dokumenty zawierające dowody wpływające na predykcję §9
  [ ] Wróć do każdego dowodu wpływającego na predykcję (§9 raportu)
  [ ] Czy dowód odczytany w pełnym kontekście dokumentu?
  [ ] Czy nie istnieje fragment tego samego dokumentu przeczący ustaleniu
      — pominięty w Przejściu I?

Krok O2: Pisma procesowe — view + drugie przeczytanie
  OBOWIĄZEK: view na akapity zawierające przyznania KRYTYCZNE (V10-2)
  [ ] Wróć do każdego pisma, z którego pochodzi ustalenie kluczowe
  [ ] Czy nie pominięto fragmentów pasujących do sprzeczności V10?
  [ ] Czy każde przyznanie V10-2 odczytane w pełnym akapicie (nie wyrwane)?

Krok O3: Spójność raportu
  [ ] Czy Executive Summary zgodne z §1-§11?
  [ ] Czy predykcja §9 zakorzeniona w faktach z I (nie interpretacjach z III)?
  [ ] Czy rekomendacje §10 wynikają z §4-§6?

Krok O4: Luki i braki
  [ ] Jakich dokumentów/dowodów brakuje?
  [ ] Jakie fakty pozostają niewyjaśnione po obu weryfikacjach?
  [ ] Czy braki wpływają na predykcję?

Krok O5: Lista korekt:
  [nr] → [korekta] → [wpływ na raport]

STATUS WERYFIKACJI OSTATECZNEJ: UKOŃCZONA / WYMAGA UZUPEŁNIENIA
```

Format wyniku Przejścia IV:
```
AUTOKOREKTA + WERYFIKACJA OSTATECZNA
P1 ✓/✗ | P2 ✓/✗ | P3 ✓/✗ | P4 ✓/✗ | P5 ✓/✗
WERYFIKACJA OSTATECZNA: [korekty O1-O4 / STATUS]
Luki nierozwiązane:     [lista lub "brak"]
GATE: RAPORT KOŃCOWY ZATWIERDZONY: TAK / NIE [blokada jeśli NIE]
```

> HARD GATE: Raport końcowy §1-§11 można wygenerować WYŁĄCZNIE po:
> (1) ukończeniu Weryfikacji Pierwszej (Przejście III) i
> (2) ukończeniu Weryfikacji Ostatecznej (Przejście IV) z GATE: ZATWIERDZONE TAK.

> ⚑ KONIEC WIADOMOŚCI 4 — wyślij tę wiadomość. Raport końcowy §1-§11 w kolejnej wiadomości.
