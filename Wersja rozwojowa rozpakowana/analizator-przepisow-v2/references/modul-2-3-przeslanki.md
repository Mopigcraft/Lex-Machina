# Moduł 2 (dekompozycja przesłanek) i Moduł 3 (analiza spełnienia) — analizator-przepisow-v2

> Plik przeniesiony ze SKILL.md bez zmian treści (progressive disclosure). Wczytaj w całości przed wykonaniem odpowiedniego kroku.

## MODUŁ 2 — DEKOMPOZYCJA PRZESŁANEK

### Klasyfikacja struktury logicznej

| Typ         | Symbol        | Opis                          |
|-------------|---------------|-------------------------------|
| Koniunkcja  | A i B i C     | Wszystkie przesłanki łącznie  |
| Alternatywa | A lub B lub C | Wystarczy jedna               |
| Warunkowa   | A → B         | Warunek konieczny             |
| Mieszana    | (A i B) lub C | Grupy przesłanek              |

### Drzewo Przesłanek

> ⚠️ **DRZEWO-LIMIT — przeczytaj przed wygenerowaniem:**
> Drzewo przesłanek jest modelem analitycznym opartym na tekście przepisu pobranego
> z ELI (RZĄD 1). NIE jest oficjalną wykładnią prawa ani opinią prawną.
> Struktura logiczna (koniunkcja / alternatywa) wynika z literalnej analizy językowej
> przepisu — może odbiegać od wykładni przyjętej w orzecznictwie.
>
> **ZAKAZ-DRZEWO:** Nie prezentuj wyniku drzewa jako definitywnego rozstrzygnięcia
> bez weryfikacji w Module 7A (orzecznictwo). Jeśli linia orzecznicza jest niejednolita
> lub pojęcia są nieostre — wynik drzewa jest ZAWSZE `?` (niejednoznaczny), niezależnie
> od literalnej struktury logicznej przepisu. Dla laika: dodaj obligatoryjnie sekcję
> 7D z zaznaczeniem ograniczeń analizy.

```
DRZEWO PRZESŁANEK — [numer przepisu]
Skutek prawny: [co wynika z przepisu]
Typ logiczny:  [koniunkcja / alternatywa / mieszany]

P1: [nazwa przesłanki]
    Definicja ustawowa: [jeśli istnieje]
    Treść: [opis]
    Charakter: Konieczna / Alternatywna
    Pojęcia nieostre: [jeśli są → Krok 2.3]

P2: [j.w.]
Pn: [j.w.]

LOGIKA: Wszystkie P1–Pn lacznie / Wystarczy jedna / Wystarczy: [opis]
```

### Weryfikacja pojęć nieostrych

```
POJĘCIE: "[słowo/fraza]"
Definicja ustawowa (ten sam akt): [artykuł + treść]
Definicja ustawowa (inny akt):    [akt + artykuł + treść]
Pojęcie nieostre → wykładnia orzecznicza (Moduł 7)
Pojęcie techniczne → znaczenie branżowe: [źródło]
```

### Wykładnia orzecznicza pojęć nieostrych

Przeszukaj w kolejności:
1. https://www.sn.pl/pl/wyszukiwarka-orzeczen — Sąd Najwyższy (link = karta `?orzeczenie=ID`)
2. https://orzeczenia.nsa.gov.pl — NSA / WSA
3. https://orzeczenia.ms.gov.pl — sądy powszechne
4. https://www.trybunal.gov.pl/orzeczenia — Trybunał Konstytucyjny
5. https://saos.org.pl — agregator orzeczeń

Uzupełniająco (POMOCNICZO, nie zamiast powyższego): sprawdź też komentarze
doktrynalne na dużych, uznanych portalach RZĘDU 3 (prawo.pl, LEX, Legalis,
rp.pl, gofin.pl i pozostałe duże portale — patrz "Hierarchia źródeł" w
Module 1) i oznacz je znacznikiem 📚 [ŹRÓDŁO POMOCNICZE — RZĄD 2: ...].
Strony indywidualnych prawników/kancelarii/blogów (Rząd 3) traktuj z
dodatkową ostrożnością wg zasad Rzędu 3. Gdy komentarz i orzecznictwo się różnią —
priorytet ma orzecznictwo, odnotuj rozbieżność.

---

## MODUŁ 3 — ANALIZA SPEŁNIENIA PRZESŁANEK

### Matryca oceny

```
MATRYCA OCENY PRZESŁANEK
Przepis:             [identyfikator]
Stan prawny na:      [data analizy]
Materiały wejściowe: [lista dokumentów / faktów]

┌─────┬──────────────────────┬────────┬──────────────────────┬─────────┐
│ Nr  │ Przesłanka           │ Status │ Uzasadnienie          │ Pewność │
├─────┼──────────────────────┼────────┼──────────────────────┼─────────┤
│ P1  │ [nazwa]              │ T/N/?  │ [dowód / brak]       │ 85%     │
│ P2  │ [nazwa]              │ T/N/?  │ [dowód / brak]       │ 60%     │
└─────┴──────────────────────┴────────┴──────────────────────┴─────────┘
Legenda: T = Spełniona  N = Niespełniona  ? = Wątpliwa
```

### Analiza szczegółowa przesłanki N lub ?

```
PRZESŁANKA [Pn] — SZCZEGÓŁOWO
Treść:                [cytat z przepisu]
Co musi być wykazane: [fakty 1, 2...]
Na spełnienie (+):    [dokument/fakt → powiązanie]
Przeciw spełnieniu(-): [dokument/fakt → powiązanie]
Braki dowodowe (?):   [czego brak]
Ocena:    spełniona / niespełniona / wątpliwa
Pewność:  [%] — wysoka 80+ / średnia 50-79 / niska <50
```

### Wynik logiczny

```
WYNIK LOGICZNY
Koniunkcja: P1(T) i P2(N) i P3(T) = N — NIE STOSUJE SIĘ
  Blokuje: P2 — [wyjaśnienie]

Alternatywa: P1(N) lub P2(T) = T — STOSUJE SIĘ
  Podstawa: P2 — [wyjaśnienie]

KONKLUZJA:
  T — PRZEPIS STOSUJE SIĘ
  N — PRZEPIS NIE STOSUJE SIĘ
  ? — WYNIK NIEJEDNOZNACZNY — [co go warunkuje]
```
