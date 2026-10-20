# Przejście I (mapowanie faktyczne) i Przejście II (kwalifikacja prawna) — analiza-sadowa-v6

> Plik przeniesiony ze SKILL.md bez zmian treści (progressive disclosure). Wczytaj w całości przed wykonaniem odpowiedniego kroku.

### PRZEJŚCIE I — MAPOWANIE FAKTYCZNE
**Cel: Wyłącznie bezsporny stan faktyczny. Zero oceny. Zero prawa.**

> **CLAIM-VALIDATION przed mapowaniem:**
> `view shared/CLAIM-VALIDATION.md`
> Twierdzenia strony nieznajdujące oparcia w dostarczonych dokumentach → oznacz
> `[⛔ NIEUDOWODNIONE]`; nie wpisuj do Mapy Faktycznej jako faktów.
> Twierdzenia strony sprzeczne z dokumentami → oznacz `[⛔ SPRZECZNE]`;
> wpisz do Mapy to co faktycznie wynika z materiału (nie wersję strony).

Rejestruj WYŁĄCZNIE:
- daty zdarzeń (chronologia bezwzględna — co do dnia)
- kwoty, liczby, okresy (co do grosza, co do dnia)
- podmioty i ich role (kto, w jakiej roli, w jakim momencie)
- treść dokumentów (co dokument stwierdza dosłownie — nie co znaczy)
- sekwencję czynności (kto co zrobił, kiedy, w jakiej kolejności)

ZAKAZ w Przejściu I:
- oceniania wiarygodności stron
- interpretowania intencji lub motywów
- stosowania przepisów prawa
- formułowania wniosków prawnych
- używania słów: naruszył, bezprawnie, celowo, oszukał

Format wyniku:
```
MAPA FAKTYCZNA
CHRONOLOGIA: [DD.MM.RRRR] → [zdarzenie dosłowne] → [podmiot] → [dokument/strona]
PODMIOTY:    [nazwa] → [rola] → [relacja procesowa]
KWOTY/DATY:  [pozycja] → [kwota lub data] → [dokument źródłowy]
DOKUMENTY:   [nazwa] → [data] → [autor] → [treść kluczowa dosłownie]
```

PUNKT STOP przed Przejściem II:
Czy Mapa Faktyczna zawiera ocenę prawną lub interpretację intencji?
TAK → usuń, zastąp suchym opisem. NIE → przejdź dalej.

> ⚑ KONIEC WIADOMOŚCI 1 — wyślij tę wiadomość. Przejście II w kolejnej wiadomości.


### PRZEJŚCIE II — KWALIFIKACJA PRAWNA
**Cel: Przypisanie faktów z Mapy Faktycznej do norm prawnych. Żadne nowe fakty nie powstają.**

> ⚠️ REGUŁA BEZWZGLĘDNA — WERYFIKACJA w ELI (RZĄD 1) PRZED MACIERZĄ:
> Przed wpisaniem JAKIEJKOLWIEK normy do macierzy fakt-norma Claude MUSI:
> 1. Wywołać web_search z zapytaniem o treść konkretnego przepisu (eli.gov.pl / lexlege.pl / arslege.pl)
> 2. Odczytać aktualną treść przepisu z wyników
> 3. Dopiero wtedy wpisać normę do macierzy
>
> ZAKAZ: Pisanie norm z pamięci bez uprzedniego web_search jest bezwzględnie zakazane.
> Każdy przepis w macierzy musi mieć potwierdzenie z live-search w tej samej sesji.
> Jeśli web_search nie zwróci treści przepisu — oznaczyć jako NIEWERYFIKOWALNY i nie stosować.
>
> MINIMUM: Dla każdej ustawy (KP, KC, KPC, KK, KPK) — co najmniej jeden web_search
> przed pierwszą normą z tej ustawy. Przy kolejnych przepisach z tej samej ustawy
> wystarczy web_search jeśli zachodzi wątpliwość co do brzmienia lub aktualności.

Sekwencja obowiązkowa:
1. Pobierz fakty WYŁĄCZNIE z Mapy Faktycznej (Przejście I)
2. Dla każdego faktu: web_search → odczytaj przepis → wpisz do macierzy
3. Każde znamię ustawowe = osobna linia
4. Oznacz: SPEŁNIONE / NIESPEŁNIONE / WĄTPLIWE / BRAK DANYCH
5. Macierz fakt-norma (format poniżej)
6. Fakty bez normy → "procesowo neutralne"
7. Dwie wykluczające się kwalifikacje tej samej kwoty → uruchom MOD-D

Format macierzy:
```
MACIERZ FAKT-NORMA
Fakt nr | Norma (art. X ustawy Y) [zweryfikowano: URL] | Znamię | Status | Uwaga

ZNAMIONA SPORNE:    [znamię] → [co jest potrzebne do wykazania]
ZNAMIONA NIESPORNE: [znamię] → [dokument potwierdzający]
FAKTY NEUTRALNE:    [fakt] → [dlaczego bez normy]
```

PUNKT STOP przed Przejściem III:
Czy każda norma pochodzi z ELI (RZĄD 1, kanon E-1…E-5) / oficjalnego źródła ZWERYFIKOWANEGO web_search w tej sesji?
Czy żaden wniosek nie opiera się na fakcie spoza Mapy Faktycznej?
TAK do obu → przejdź dalej. NIE → uzupełnij brakujące web_search przed przejściem dalej.

> ⚑ KONIEC WIADOMOŚCI 2 — wyślij tę wiadomość. Przejście III w kolejnej wiadomości.
