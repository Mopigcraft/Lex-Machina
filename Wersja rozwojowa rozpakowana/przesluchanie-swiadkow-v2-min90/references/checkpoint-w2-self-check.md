# CHECKPOINT-W2 i SELF-CHECK-PRZED-W3

> Plik obowiązkowy dla CHECKPOINT-W2 i dla startu wiadomości z W3. Treść przeniesiona dosłownie z SKILL.md (refaktor 2026-10-20); SKILL.md zawiera nagłówki i streszczenia.

## CHECKPOINT-W2 — OBOWIĄZKOWA PAUZA PRZED W3

> ⛔ REGUŁA DWÓCH WIADOMOŚCI — system zatrzymuje się tutaj.
> Po dostarczeniu W2 (tez, profilu, modelu, scoringu) system CZEKA.
> Pytania W3 generowane są w OSOBNEJ wiadomości, dopiero po uwagach użytkownika.

```
WIADOMOŚĆ 1 (ta wiadomość):
  Zawiera: PRE-W1 profil + mapa wiedzy + KROK 0 + W1 intake + W2 tezy/model/scoring
  Kończy się pytaniem do użytkownika.

WIADOMOŚĆ 2 (następna wiadomość, po odpowiedzi użytkownika):
  Zawiera: W3 pytania (kompletny zestaw z FPW + macierz + scoring finalny + rekomendacje)
```

### Treść CHECKPOINT-W2

Po dostarczeniu W2 system prezentuje podsumowanie i zadaje jedno pytanie:

```
═══════════════════════════════════════════════════════════
CHECKPOINT W2 — WERYFIKACJA PRZED GENEROWANIEM PYTAŃ
═══════════════════════════════════════════════════════════

ŚWIADEK:        [oznaczenie]
TYP:            [typ 1/2/3/4/5]
SCORING W2:     [X]/10 — [kwalifikacja]
MODEL:          [PEACE / LEJEK / ONE-FACT / CHRONOLOGICZNY]
ALTERNATYWA:    [model zapasowy]

TEZY (do wykazania):
  T1: [treść] — przepis kandydujący: ⚠️ [art. X]
  T2: ...

TEZY DO OBALENIA (jeśli cross):
  T_OB1: [treść]

SPRZECZNOŚCI DOSTĘPNE: [n] — kluczowe: [lista]

TEMATY ZAKAZANE (BLOK E):
  [lista z uzasadnieniem]

LUKI DOWODOWE:
  [tematy bez dowodu kontrolnego → SAFE-Q wymagane]

CHRONOLOGIA ZDARZEŃ (do zatwierdzenia):
  [lista zdarzeń/dat istotnych dla tez powyżej — jeśli chronologia jest
  złożona lub sporna, wypisz ją tu w skrócie; jeśli nie ustalono jeszcze
  chronologii, napisz to wprost: "⚠️ chronologia nie została jeszcze
  ustalona/zatwierdzona — wymagana przed W3"]

══════════════════════════════════════════════════════════
Czy tezy, model I CHRONOLOGIA są właściwe? Czy chcesz coś zmienić lub
uzupełnić zanim przejdę do generowania pytań?
(Możesz odpowiedzieć "OK" aby kontynuować lub wskazać zmiany)
══════════════════════════════════════════════════════════
```

**Reguła CHECKPOINT-W2 (poprawiona w audycie 3.16 — USUNIĘTO WYJĄTEK):**
System nie generuje ŻADNEGO pytania z W3 bez wyraźnego, oddzielnego
potwierdzenia użytkownika obejmującego JEDNOCZEŚNIE (a) tezy i model
oraz (b) chronologię zdarzeń. Potwierdzenie musi paść jako osobna
wiadomość użytkownika PO wiadomości z W2 — nie w tej samej wiadomości,
w której podano materiał źródłowy.

⛔ BEZ WYJĄTKÓW. Poprzednia treść tej reguły przewidywała wyjątek dla
sytuacji, gdy użytkownik w pierwotnym poleceniu wprost zażądał pytań
("przygotuj od razu pytania") — ten wyjątek został USUNIĘTY (audyt 3.16),
ponieważ w praktyce prowadził do pomijania weryfikacji chronologii i tez
nawet wtedy, gdy użytkownik nie miał jeszcze szansy ich zobaczyć. Nawet
przy wyraźnym żądaniu natychmiastowych pytań, system:
  1. dostarcza W2 (tezy + model + chronologia) w jednej wiadomości,
  2. kończy tę wiadomość pytaniem o akceptację,
  3. CZEKA na odpowiedź — nie generuje W3 w tej samej turze pod żadnym pozorem.

---

<!-- lex:wczytaj-gdy: KOLEJNA-TURA -->
## SELF-CHECK-PRZED-W3 — OBOWIĄZKOWE PONOWNE WCZYTANIE (dodane w audycie 3.16)

> ⛔ Ta sekcja uruchamia się NA STARCIE wiadomości zawierającej W3 (pytania),
> czyli w wiadomości NASTĘPUJĄCEJ PO akceptacji CHECKPOINT-W2 przez
> użytkownika — niezależnie od tego, ile innych tematów pojawiło się w
> międzyczasie w rozmowie (np. prośba o naprawę innego skilla). Zanim
> powstanie choćby jedno pytanie W3, potwierdź w tej samej wiadomości,
> krótko, każdy z poniższych punktów:

```
□ Czy użytkownik potwierdził W2 (tezy + model) ORAZ chronologię w
  OSOBNEJ, wcześniejszej wiadomości? Jeśli NIE — STOP, wróć do CHECKPOINT-W2.
□ Czy lista świadków jest zamknięta i potwierdzona (WITNESS-SCOPE-LOCK
  KROK 1)? Jeśli świadek wynika z dokumentu/protokołu (np. postanowienie
  sądu o wezwaniu), przywołaj to źródło jednym zdaniem zamiast pytać od nowa.
□ Czy teza dowodowa dla TEGO świadka w TYM postępowaniu została ustalona
  (TEZA-DOWODOWA-SCOPE-GATE)? Jeśli nie wynika z materiałów — pytanie do
  użytkownika, nie zgadywanie.
□ Czy rejestr kroków (MOD-STEP-TRACKER) jest aktualny? Każdy etap
  pominięty od ostatniej wiadomości → raportuj TERAZ, na tej samej
  zasadzie jak w pisma-procesowe-v3 (FAZA 2 MOD-STEP-TRACKER): wypisz
  wprost co zrobiono i co pominięto, nie milcz i nie odkładaj raportu
  do końca pracy.
```

Wynik tego self-checku pokazujesz użytkownikowi jako krótki nagłówek
przed właściwymi pytaniami W3 (2–4 linijki, nie rozbudowany raport) —
np.: "Potwierdzone: tezy+chronologia (Twoja wiadomość z [opis]), świadek:
[ŚWIADEK-K] (postanowienie sądu z 8.07.2026). Pominięte etapy: brak."
Jeśli coś pominięto — wpisz to zamiast "brak".

---


> 🔴 Sąd uchyla pytania wykraczające poza zatwierdzoną tezę dowodową
> NATYCHMIAST i BEZ WZGLĘDU na ich merytoryczną siłę — najlepiej
> skonstruowane pytanie jest bezwartościowe, jeśli dotyczy okoliczności,
> na którą świadek nie został dopuszczony.

```
Przed przejściem do ETAP W3 w KONKRETNYM postępowaniu sądowym:

1. Sprawdź, czy w dostępnych materiałach (protokoły, postanowienia sądu)
   jest zapis USTALONEJ/ZATWIERDZONEJ tezy dowodowej dla tego świadka
   w TYM konkretnym postępowaniu (sygn. akt).
   - Jeśli TAK → wypisz tę tezę dosłownie, jako ramę, w której muszą
     zmieścić się wszystkie pytania W3.
   - Jeśli NIE (brak takiej informacji w materiałach) → zapytaj
     użytkownika wprost o zakres zatwierdzonej tezy PRZED wygenerowaniem
     pytań, zamiast zakładać, że każdy wątek merytoryczny jest dopuszczalny.

2. Dla KAŻDEGO pytania z W3 — oznacz zgodność z tezą:
   ✅ W RAMACH TEZY / ⚠️ GRANICZNE (może wymagać wniosku o rozszerzenie
   tezy przed rozprawą) / 🔴 POZA TEZĄ (wysokie ryzyko uchylenia — sąd
   może odrzucić natychmiast, niezależnie od jakości pytania).

3. Pytania oznaczone 🔴 POZA TEZĄ nie trafiają do finalnego zestawu bez
   wyraźnego ostrzeżenia użytkownika i/lub rekomendacji złożenia
   wcześniejszego wniosku o rozszerzenie tezy dowodowej.

4. Jeśli sąd już wcześniej (w tym samym lub powiązanym postępowaniu)
   uchylał pytania określonego typu z uzasadnieniem "poza tezą" —
   traktuj to jako precedens dla tego konkretnego sądu/sprawy i ostrzegaj
   z wyższym priorytetem.

Przykład z praktyki: sąd w postępowaniu o wynagrodzenie/świadectwo pracy
systematycznie uchylał pytania o treść i procedurę wydania upomnienia/kary
porządkowej, wskazując wprost "nie jest to przedmiotem tego postępowania"
— mimo że merytorycznie pytania były dobrze skonstruowane. Zestaw pytań
przygotowany bez sprawdzenia tezy dowodowej danego postępowania może więc
być w dużej części nieadmisyjny, niezależnie od jakości analitycznej.
```

### PROCEEDING-DISAMBIGUATION-TABLE (dodane w audycie 3.10)

> 🔴 Aktywacja: sprawa użytkownika obejmuje więcej niż jedno równolegle
> toczące się postępowanie (różne sygnatury, sądy, przedmiotowe zakresy).

```
Prowadź i aktualizuj tabelę:

| Sygnatura | Sąd | Przedmiot postępowania | Zatwierdzona teza dowodowa (jeśli znana) | Status |
|---|---|---|---|---|

Każdy przygotowywany zestaw pytań musi być jawnie oznaczony, do którego
konkretnego postępowania (sygnatury) jest przeznaczony — pytania właściwe
w jednym postępowaniu (np. o odszkodowanie za mobbing) mogą być całkowicie
nieadmisyjne w innym, równoległym postępowaniu tej samej osoby (np. o samo
wynagrodzenie i świadectwo pracy), nawet dotyczącym tych samych stron.
```

---
