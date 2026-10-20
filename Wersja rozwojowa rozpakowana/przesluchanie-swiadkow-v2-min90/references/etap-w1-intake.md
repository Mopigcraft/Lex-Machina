# ETAP W1: intake

> Plik obowiązkowy dla ETAP W1 i jego bramek. Treść przeniesiona dosłownie z SKILL.md (refaktor 2026-10-20); SKILL.md zawiera nagłówki i streszczenia.

## ETAP W1 — INTAKE

### Cel etapu

Zebranie danych wejściowych o świadku z dwóch źródeł:
1. **Materiały dostarczone przez użytkownika** (akta, protokół, zeznania, dokumenty) — dane ekstrahujesz samodzielnie.
2. **Pytania do użytkownika** — tylko dla danych krytycznych, których nie możesz uzyskać z materiałów.

### Zasada ekstrakcji

> Jeśli użytkownik dostarczył dokumenty, zawsze najpierw czytaj i ekstrahuj z nich dane.
> Pytaj tylko o to, czego dokumenty nie zawierają lub co jest niejednoznaczne.
> Nie pytaj o informacje dostępne w materiale źródłowym.

---

### WARSTWA A — dane wspólne (każdy świadek)

Ekstrahuj z materiałów lub pytaj, jeśli brak:

| Pole | Źródło | Pytanie jeśli brak |
|---|---|---|
| Imię / inicjały | materiały | „Jak mam oznaczyć świadka?" |
| Strona powołująca | materiały / opis | „Kto powołuje świadka — Państwo czy strona przeciwna?" |
| Typ postępowania | materiały | „Jaki to rodzaj postępowania — cywilne, karne, pracownicze, administracyjne?" |
| Okoliczność dowodowa | opis / teza | „Na jaką konkretną okoliczność jest powoływany świadek?" |
| Typ relacji ze sprawą | materiały | — |
| Wcześniejsze zeznania? | materiały / opis | „Czy świadek składał już zeznania lub deklarację pisemną?" |

---

### TEZY-DOWODY-SWIADEK-GATE (dodane w audycie 3.6) ⚠️ OBOWIĄZKOWA

> Cel: nie budować pytań na milczącym domyśle co do tego, kim jest świadek,
> czego dotyczy jego zeznanie i czym to jest poparte — jeśli te trzy rzeczy
> nie wynikają JEDNOZNACZNIE z dostarczonych materiałów, trzeba o nie zapytać
> wprost, zanim powstanie choćby jedno pytanie.

```
Przed przejściem do W2, sprawdź czy z dostarczonych materiałów wynika
JEDNOZNACZNIE (nie przez domysł czy prawdopodobieństwo) odpowiedź na TRZY
poniższe punkty. Dla każdego punktu, który NIE wynika wprost z dokumentów —
zadaj pytanie użytkownikowi. Nie zgaduj i nie zakładaj milcząco.

1. TEZY DO WYKAZANIA (maks. 3, jednozdaniowe):
   "Jakie są maksymalnie trzy główne tezy/fakty, które to przesłuchanie ma
   wykazać lub obalić?"
   → Jeśli użytkownik już to podał wcześniej w rozmowie lub wynika to
     jasno z kontekstu sprawy (np. z KROK 0) — nie pytaj ponownie, tylko
     potwierdź jednym zdaniem: "Rozumiem, że tezy to: [...] — potwierdza Pan?"

2. POSIADANE DOWODY:
   "Jakimi konkretnie dowodami dysponuje Pan już teraz na poparcie tych
   tez (dokumenty, maile, zeznania innych osób, nagrania, metadane)?"
   → Ekstrahuj samodzielnie z już wgranych dokumentów w tej rozmowie;
     pytaj tylko o dowody, których nie widziałeś, a na które użytkownik
     się powołuje.
   → Brak dowodu kontrolnego dla danej tezy → ta teza NIE otrzymuje
     pytań typu impeachment/pułapka w W3, tylko SAFE-Q lub trafia do
     luk dowodowych w CHECKPOINT-W2.

3. KIM JEST ŚWIADEK I JAKĄ PEŁNI ROLĘ:
   "Kim dokładnie jest ten świadek względem obu stron — jakie stanowisko
   zajmował/zajmuje, czy jest stroną, pracownikiem, osobą postronną, i w
   jakim charakterze ma zeznawać (naoczny, ze słyszenia, biegły)?"
   → Jeśli rola i stanowisko wynikają wprost z dostarczonych dokumentów
     (np. z podpisu na piśmie, z nagłówka maila, z wcześniejszych ustaleń
     w tej samej rozmowie) — NIE pytaj, tylko zrekonstruuj to jednym
     zdaniem i poproś o potwierdzenie zamiast otwartego pytania.

REGUŁA NADRZĘDNA: to nie jest formularz do wypełnienia w każdej sesji od
zera. Jeśli którykolwiek z trzech punktów już padł explicite w tej samej
rozmowie (np. przy okazji wcześniejszego dokumentu) — nie powtarzaj pytania,
tylko przywołaj ustalenie i poproś o samo potwierdzenie ("czy to nadal
aktualne?"). Pytaj tylko o to, czego naprawdę brakuje.
```

---

### WITNESS-SCOPE-LOCK (dodane w audycie 3.14) ⛔ OBOWIĄZKOWA

> Cel: materiał dowodowy sprawy niemal zawsze wspomina więcej niż jedną osobę
> po stronie przeciwnej (np. dwóch reprezentantów spółki, kilku sygnatariuszy
> pism). Sam fakt, że dana osoba pojawia się w dokumentach, NIE oznacza, że
> użytkownik chce przygotowywać pytania także do niej. Domyślne rozszerzanie
> zakresu świadków ponad to, co użytkownik faktycznie wskazał, jest błędem
> tego samego rodzaju co pomijanie TEZY-DOWODY-SWIADEK-GATE — to zgadywanie
> zamiast ustalania.

```
KROK 1 — USTAL ZAMKNIĘTĄ LISTĘ ŚWIADKÓW PRZED W2/W3:
  a) Czy użytkownik wprost nazwał świadka (imię/nazwisko, "ta osoba",
     "świadek, który podpisał X") → TA osoba i TYLKO ta osoba wchodzi na
     listę. Inne osoby wymienione w tych samych dokumentach (współpracownicy,
     inni sygnatariusze, inni reprezentanci strony przeciwnej) NIE wchodzą
     automatycznie na listę, nawet jeśli są równie dobrze udokumentowane.
  b) Czy z kontekstu rozmowy (np. "kto będzie przesłuchiwany", ustalenia
     wcześniejsze w tej samej sesji) wynika JEDNOZNACZNIE, kto jest
     przesłuchiwanym świadkiem → potwierdź to jednym zdaniem zamiast pytać
     od nowa (zgodnie z REGUŁĄ NADRZĘDNĄ wyżej).
  c) Jeśli ani (a) ani (b) nie rozstrzyga jednoznacznie, kto konkretnie ma
     być przesłuchiwany, a materiały wspominają więcej niż jedną możliwą
     osobę → ZAPYTAJ WPROST, zanim powstanie choćby jedno pytanie:
     "Widzę w materiałach kilka osób powiązanych z pozwaną stroną: [lista
     z rolami]. Które z nich mają być przesłuchiwane jako świadkowie w tym
     zestawie pytań?"

KROK 2 — ZAKAZ ROZSZERZANIA BEZ POTWIERDZENIA:
  ⛔ Nie generuj pytań ani tez dla żadnej osoby spoza zamkniętej listy z
     KROKU 1 — nawet jeśli ta osoba pełni analogiczną funkcję (np. drugi
     członek zarządu, współsygnatariusz tego samego pisma) i nawet jeśli
     dodanie jej "dla kompletności" wydaje się pomocne.
  ⛔ Chęć bycia wyczerpującym nie jest wyjątkiem od tej zasady — dodanie
     niezamówionego świadka to nie dodatkowa wartość, tylko rozmycie
     zakresu ustalonego przez użytkownika.
  → Jeśli podczas przygotowania W2/W3 pojawi się materiał sugerujący, że
    warto byłoby przesłuchać dodatkową osobę — zasygnalizuj to jako
    REKOMENDACJĘ na końcu odpowiedzi ("czy rozszerzyć zestaw pytań o
    [osoba], która też widnieje w [dokument]?"), nie jako gotowy blok pytań.

KROK 3 — PRZY WIELU ŚWIADKACH JEDNOCZEŚNIE:
  Jeśli użytkownik potwierdzi więcej niż jednego świadka — każdy świadek
  dostaje osobny, wyraźnie nagłówkowany blok W1→W3 (osobny profil, osobne
  tezy, osobne pytania). Nie mieszaj pytań do różnych świadków w jednej
  wspólnej liście.
```

**Test regresyjny (patrz `tests/REGRESSION-CASES.md`):** sprawa pracownicza,
w materiałach występuje dwóch reprezentantów pozwanej spółki (np. prezes
zarządu i dyrektor generalna), obaj podpisani pod różnymi pismami; użytkownik
prosi ogólnie o "pytania do świadka" bez podania nazwiska, ale z wcześniejszej
rozmowy jasno wynika, że przesłuchiwana będzie tylko jedna konkretna osoba
(np. autorka najbardziej spornego, świeżego pisma) → oczekiwany wynik: pytania
WYŁĄCZNIE do tej jednej osoby; błędem jest dołączenie drugiego reprezentanta
"na wszelki wypadek".

---

### PRIOR-TESTIMONY-GATE ⚠️

**Jeśli świadek składał już zeznania (protokół przesłuchania, deklaracja, zeznania w innym postępowaniu):**

```
⚠️ GATE: Świadek z wcześniejszymi zeznaniami.

Wymagam wprowadzenia dokumentu z poprzedniego przesłuchania.
Proszę wgrać protokół / zeznania / deklarację pisemną.

Bez tego dokumentu nie przejdę do W2 — analiza sprzeczności
i technika loopingu wymagają materiału źródłowego.
```

Jeśli użytkownik nie może dostarczyć dokumentu, odnotuj brak i zredukuj zakres W3
(blok D — pytania na sprzeczności — będzie niedostępny; zaznacz to w W2).


Po otrzymaniu dokumentu z zeznaniami: ekstrahuj z niego samodzielnie:
- kluczowe twierdzenia faktyczne,
- daty, miejsca, osoby, sekwencje,
- sformułowania potencjalnie rozbieżne z innymi dowodami,
- wszelkie zastrzeżenia, niepewności, braki odpowiedzi świadka.

---

### WARSTWA B — uzupełnienie zależne od typu świadka

Po identyfikacji typu z materiałów — ekstrahuj z dokumentów, pytaj tylko o luki.

#### TYP 1 — Świadek pracownik / współpracownik

Wymagane dane:

| Pole | Źródło | Pytanie jeśli brak |
|---|---|---|
| Stanowisko i zakres obowiązków | akta / umowy / dokumenty HR | „Jakie były jego/jej obowiązki w spornym okresie?" |
| Dostęp do spornych dokumentów / decyzji | materiały | „Czy miał bezpośredni dostęp do [dokument / decyzja]?" |
| Czas zatrudnienia / współpracy | akta | — |
| Stosunek do stron po rozstaniu | opis sytuacji | „Czy po zakończeniu zatrudnienia relacje były konfliktem, neutralne, czy pozytywne?" |
| Czy podpisał dokumenty sporne? | materiały | — |

#### TYP 2 — Świadek naoczny / „ze zdarzenia"

Wymagane dane:

| Pole | Źródło | Pytanie jeśli brak |
|---|---|---|
| Pora dnia zdarzenia | protokół / akta | „O której godzinie doszło do zdarzenia?" |
| Warunki oświetlenia | opis / protokół | „Jakie było oświetlenie — dzień, noc, sztuczne światło?" |
| Warunki atmosferyczne | opis / dokumenty | „Jaka była pogoda — mgła, deszcz, śnieg, dobre warunki?" |
| Odległość od zdarzenia | protokół / szkic | „W jakiej odległości od zdarzenia znajdował się świadek?" |
| Kąt i pole widzenia | opis / szkic | „Czy miał bezpośrednią linię wzroku, czy patrzył przez przeszkodę?" |
| Wady wzroku / słuchu | wcześniejsze zeznania | „Czy świadek nosi okulary lub ma inne wady zmysłów istotne dla obserwacji?" |
| Stan psychofizyczny świadka | opis | „Czy świadek był w normalnym stanie — bez wpływu alkoholu, silnych emocji, zmęczenia?" |
| Czas od zdarzenia do pierwszej relacji | protokół / data | — |

#### TYP 3 — Świadek ze słyszenia

Wymagane dane:

| Pole | Pytanie jeśli brak |
|---|---|
| Kto przekazał informację | „Od kogo świadek dowiedział się o zdarzeniu?" |
| Kiedy i w jakich okolicznościach | „Kiedy i gdzie doszło do tego przekazu?" |
| Czy istnieje możliwość weryfikacji pośrednika | „Czy pośrednik jest dostępny jako świadek lub czy istnieje pisemny ślad?" |

#### TYP 4 — Ekspert / biegły

Wymagane dane:

| Pole | Pytanie jeśli brak |
|---|---|
| Metodologia opinii | „Jaką metodologią posłużył się biegły?" |
| Zleceniodawca opinii | „Kto zlecił opinię — sąd, strona, prokuratura?" |
| Wcześniejsze opinie w podobnych sprawach | „Czy biegły wydawał wcześniej opinie w podobnych sprawach?" |
| Ewentualne powiązania ze stronami | „Czy biegły jest powiązany zawodowo lub osobiście z którąś ze stron?" |

#### TYP 5 — Świadek charakteru

Wymagane dane:

| Pole | Pytanie jeśli brak |
|---|---|
| Czas znajomości | „Od jak dawna świadek zna stronę?" |
| Częstotliwość kontaktów | „Jak często się kontaktowali w spornym okresie?" |
| Podstawa oceny charakteru | „Skąd świadek czerpie wiedzę o charakterze / wiarygodności strony?" |

---

### INTAKE-COMPLETENESS-GATE

Po zebraniu danych W1 wykonaj kontrolę:

```
POLA KRYTYCZNE — bez nich NIE przechodzę do W2:
  □ Strona powołująca
  □ Okoliczność dowodowa
  □ Typ świadka
  □ Dane z Warstwy B (min. 3 z 4+ wymaganych dla danego typu)

POLA UZUPEŁNIAJĄCE — brak → zaznacz ⬛ i kontynuuj:
  □ Szczegóły warunków obserwacji (typ 2)
  □ Stosunek do stron (typ 1)
  □ Wcześniejsze opinie (typ 4)
```

Jeśli brakuje pól krytycznych — zadaj 1–3 pytania uzupełniające, jedno na wiadomość.
Jeśli wszystkie pola krytyczne są uzupełnione — przejdź do W2 bez dodatkowych pytań.

---

### IMPORTED-QUESTIONS-GATE (dodane w audycie 3.6)

> Aktywacja: użytkownik dostarcza **gotowy blok pytań** (np. z poprzedniej
> sesji, notatek własnych, projektu innej osoby) zamiast budować pytania
> od zera przez W1→W2→W3.

```
Dla KAŻDEGO dostarczonego pytania, przed jego oceną, poprawą lub włączeniem
do finalnej listy:

1. Zrekonstruuj tezę jednym zdaniem: "To pytanie ma wykazać, że...".
2. Jeśli teza nie daje się zrekonstruować w jednym zdaniu z materiału
   dostarczonego przez użytkownika → pytanie jest strukturalnie podejrzane
   (fishing expedition albo pytanie poboczne) → oznacz do BLOKU E lub zapytaj
   użytkownika o cel.
3. Dopiero po rekonstrukcji tezy zastosuj normalny QUESTION-ADMISSIBILITY-GATE
   (FPW-1/2/3, WHY-GATE, SAFE-Q) do TREŚCI pytania.

Nie wolno oceniać samej poprawności gramatyczno-taktycznej pytania
(otwarte/zamknięte, sugestywne/nie) bez wykonania kroku 1-2 — inaczej pytania
poboczne przechodzą bramkę mimo braku uzasadnienia procesowego.
```

---

### REVISION-DIFF-CHECK (dodane w audycie 3.7)

> Aktywacja: użytkownik przesyła **pełną, zaktualizowaną wersję** zestawu
> pytań, który był już wcześniej w tej rozmowie oceniany lub poprawiany.

```
Zamiast pełnej, od-zera analizy każdego pytania:

1. Zestaw nadesłaną wersję z ostatnią wersją zaakceptowaną/poprawioną przez
   ten skill w tej samej rozmowie.
2. Wskaż jawnie, w trzech kategoriach:
   - NAPRAWIONE: które z wcześniej zgłoszonych problemów zostały usunięte.
   - REGRESJA: które z wcześniej zgłoszonych problemów WRÓCIŁY nienaprawione
     lub w zmodyfikowanej, ale nadal wadliwej formie.
   - NOWE: pytania lub zmiany nieobecne w poprzedniej wersji, wymagające
     pełnej oceny wg standardowych bramek.
3. Priorytet uwagi: REGRESJA > NOWE > przypomnienie NAPRAWIONYCH (te ostatnie
   wystarczy wymienić jednym zdaniem, bez powtarzania pełnego uzasadnienia).

Cel: uniknięcie sytuacji, w której ten sam problem jest wykrywany od nowa
przy każdej kolejnej rundzie, bo ocena zaczyna się od zera zamiast od
różnicy względem stanu poprzedniego.
```

### AUTO-RENUMBER-OFFER (dodane w audycie 3.7)

> Aktywacja: wykryto duplikującą się numerację pytań w obrębie jednego
> zestawu (ten sam numer użyty w dwóch różnych sekcjach/blokach).

```
Nie poprzestawaj na samym zasygnalizowaniu problemu numeracji. Razem z
sygnałem zaproponuj i — jeśli użytkownik nie zastrzeże inaczej — wykonaj
od razu przenumerowanie całego zestawu na jedną, ciągłą sekwencję (1, 2,
3... przez wszystkie bloki), zachowując przypisanie pytań do bloków
tematycznych w treści, ale z unikalnym numerem globalnym dla każdego.
```
