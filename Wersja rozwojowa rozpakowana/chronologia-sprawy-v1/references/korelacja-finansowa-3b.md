# 3B. Korelacja finansowa między dokumentami

> Plik obowiązkowy dla KROK-FIN-GATE i KROK-FIN-1..4. Treść przeniesiona dosłownie z SKILL.md (refaktor 2026-10-20); SKILL.md zawiera nagłówki i streszczenia.

## 3B. KORELACJA FINANSOWA MIĘDZY DOKUMENTAMI (OBOWIĄZKOWA, v1.2)

> ⛔ KROK-FIN-GATE — HARD GATE. Nie wolno zamknąć FAZY EKSTRAKCJI (KROK A4/A6)
> jeśli w materiale występuje ≥1 wzmianka o kwocie pieniężnej, a rekord FINANSE
> nie został wypełniony i skorelowany z pozostałymi dokumentami. Pominięcie tego
> kroku jest traktowane tak samo jak pominięcie ekstrakcji daty — jako niepełna
> analiza, nie jako pominięcie nieistotnego szczegółu.

### Dlaczego to osobna bramka, a nie część ogólnej ekstrakcji zdarzeń

Data i opis zdarzenia odpowiadają na pytanie "co i kiedy się stało". Kwota
odpowiada na trzy DODATKOWE pytania, które model pomija, jeśli kwotę potraktuje
się jako zwykły szczegół zdarzenia: **komu**, **ile dokładnie** i **czy/kiedy
rozliczono**. Te trzy pytania rzadko mają odpowiedź w jednym dokumencie —
odpowiedź składa się z fragmentów rozproszonych po wielu źródłach (arkusz +
korespondencja + zeznanie), więc wymaga jawnego, osobnego kroku korelacji, a nie
tylko ekstrakcji.

### Rekord FINANSE — pola obowiązkowe

```
Dla KAŻDEJ wzmianki o kwocie wypełnij:

kwota:            liczba + waluta (np. "700 zł", "1200 PLN") — nigdy w przybliżeniu,
                  jeśli dokument podaje kwotę dokładną
tytul:            za co (opłata za pozwolenie na pracę, zwrot, kara umowna, …)
plator:           kto płaci / kto ma zapłacić (imię, nazwa, lub "NIEZIDENTYFIKOWANY")
odbiorca:         kto otrzymuje / ma otrzymać
termin:           data lub warunek płatności, jeśli wskazany w dokumencie
                  ("po 1 miesiącu", "do 10. dnia następnego miesiąca") — jeśli brak
                  terminu w dokumencie, pole = null, NIE domyślaj się terminu
status:           ZAPŁACONE / DO_ZAPŁATY / ZALEGŁE / SPORNE_CZY_ZWRÓCONE / NIEZNANY
dok_id:           źródło (jak w proweniencji zdarzeń)
strona_dok:       lokalizacja w dokumencie
powiazane_osoby:  lista identyfikatorów osób/podmiotów, których kwota dotyczy
                  (nawet jeśli w danym dokumencie występują tylko pod pseudonimem,
                  numerem telefonu lub inicjałem — patrz KROK-FIN-3 niżej)
```

### KROK-FIN-1 — Inwentaryzacja kwot per dokument

Dla każdego DOK-XX zawierającego kwotę: wypełnij rekord FINANSE jak wyżej.
Rób to RÓWNOLEGLE z inwentaryzacją dat — nie jako odrębny, późniejszy przebieg,
żeby uniknąć sytuacji, w której dokument bez daty procesowej (np. zrzut czatu,
arkusz kalkulacyjny) zostaje uznany za "niekwalifikujący się" do analizy.

### KROK-FIN-2 — Zestawienie krzyżowe (tabela rekoncyliacji)

Zbuduj tabelę: wiersz = jedna relacja płatnicza (jedna osoba/podmiot ↔ jedna
kwota), kolumny = wszystkie DOK-XX, w których ta relacja występuje. Dla każdej
pary dokumentów dotyczących tej samej osoby/kwoty sprawdź:

```
CZY kwota z DOK-A zgadza się z kwotą z DOK-B?
  TAK → oznacz jako potwierdzoną (podnieś pewność zdarzenia o jeden poziom,
        jeśli wcześniej było [WYDEDUKOWANE])
  NIE → SPRZECZNOŚĆ-[N], TYP: KWOTA (nowy podtyp — patrz references/sprzecznosci-dat.md
        → KATEGORIA D) — nie uśredniaj ani nie wybieraj kwoty "bardziej prawdopodobnej"
        bez jawnego uzasadnienia hierarchią źródeł

CZY status (zapłacone/do zapłaty) jest spójny w czasie?
  Zbuduj mini-oś: kwota zgłoszona jako należna (data X) → kwota potwierdzona
  jako zapłacona (data Y, jeśli istnieje) → jeśli status "do zapłaty"/"zaległe"
  utrzymuje się w najpóźniejszym chronologicznie dokumencie → oznacz jako
  [NIEROZLICZONE NA DZIEŃ NAJPÓŹNIEJSZEGO DOKUMENTU], nie milcz na ten temat
```

### KROK-FIN-3 — Identyfikacja osób przy danych szczątkowych

Dokumenty finansowe nieformalne (czat, WhatsApp, SMS) często identyfikują
osoby przez numer telefonu, pseudonim czy samo imię, bez nazwiska. Nie wolno:
(a) milcząco pominąć takiej kwoty, bo "nie wiadomo czyja", ani
(b) domyślnie przypisać jej do strony postępowania bez wskazania podstawy.

```
JEŻELI tożsamość płatnika/odbiorcy nie jest jednoznaczna z samego dokumentu:
  → oznacz osobę jako [OSOBA-NIEZIDENTYFIKOWANA-N] (numeruj kolejno w obrębie sprawy)
  → wskaż wszystkie poszlaki dostępne w materiale, które mogłyby pomóc w identyfikacji
    (numer telefonu, kontekst rozmowy, zbieżność kwoty z innym, w pełni
    zidentyfikowanym dokumentem)
  → NIE zgaduj tożsamości bez jawnego zaznaczenia, że to dedukcja z przypisaną
    skalą pewności (patrz [WYDEDUKOWANE], sekcja 3 wyżej)
```

### KROK-FIN-4 — Eksport

W eksporcie do pisma (sekcja "Rekoncyliacja finansowa", dodatkowa wobec sekcji
A–D z rozdziału EKSPORT DO PISMA PROCESOWEGO) każda relacja płatnicza ma osobny
akapit z kwotą, tytułem, stronami, terminem, statusem i źródłem — w kolejności
chronologicznej rozliczenia, nie w kolejności występowania w aktach.

### SELF-CHECK (uzupełnienie do sekcji SELF-CHECK głównej)

```
□ Czy KAŻDA wzmianka o kwocie w KAŻDYM dostarczonym dokumencie (w tym w plikach
  nieformalnych — czat, arkusz, SMS) ma wypełniony rekord FINANSE?
□ Czy zbudowano tabelę rekoncyliacji krzyżowej (KROK-FIN-2) zamiast wypisania
  kwot osobno per dokument bez zestawienia ich ze sobą?
□ Czy każda kwota o niejasnym statusie rozliczenia (zapłacone/zaległe) na dzień
  najpóźniejszego dostępnego dokumentu została jawnie oznaczona jako
  NIEROZLICZONE, a nie pominięta milczeniem?
□ Czy tożsamości niepełne (telefon/pseudonim) oznaczono jako
  [OSOBA-NIEZIDENTYFIKOWANA-N] zamiast pominięcia lub domysłu bez zastrzeżenia?
```
