# ETAP W3: bloki A-E, macierz, scoring, rekomendacje

> Plik obowiązkowy przy budowie bloków pytań W3. Treść przeniesiona dosłownie z SKILL.md (refaktor 2026-10-20); SKILL.md zawiera nagłówki i streszczenia.

### BLOK A — Pytania identyfikujące i wiarygodnościowe

Cel: ustalenie relacji świadka ze sprawą, stronami, podstawy wiedzy, ewentualnego interesu.

Zawsze na początku. Ilość: 3–6 pytań (min. 4, gdy aktywny FUNDAMENT-A — niżej).
Model domyślny dla tego bloku: PEACE (Engage).

```
⛔ FUNDAMENT-A — CZTERY ELEMENTY OBOWIĄZKOWE (dodane 2026-08-23g, flaga F-122)

Blok A NIE JEST listą przykładów do wyboru. Cztery poniższe elementy generuje
się ZAWSZE, bez czekania na to, aż użytkownik o nie poprosi w prompcie —
brak któregokolwiek jest brakiem produktu, nie stylem redakcyjnym.

  A-1  RELACJA ZE STRONAMI
       Zależność służbowa / rodzinna / osobista / ekonomiczna — dziś ORAZ
       w dacie zdarzenia (relacje zmieniają się między zdarzeniem a rozprawą,
       a zmiana sama w sobie jest materiałem).
  A-2  INTERES W WYNIKU SPRAWY
       Finansowy, reputacyjny, karny (własna odpowiedzialność świadka),
       pracowniczy. Także interes NEGATYWNY — czego świadek uniknie,
       jeżeli sprawa skończy się w określony sposób.
  A-3  ŹRÓDŁO WIEDZY — per twierdzenie, nie zbiorczo dla świadka
       BEZPOŚREDNIE (widział/słyszał sam) · Z RELACJI (kto? kiedy? w jakich
       słowach?) · WNIOSKOWANE (świadek wyciąga wniosek) · DOMYSŁ (sam
       zaznacza niepewność). Zapis kategorii przy każdym twierdzeniu W-xxx.
  A-4  WARUNKI OBSERWACJI — obowiązkowe dla świadka typu 2 (naoczny),
       fakultatywne dla pozostałych
       Odległość, oświetlenie, czas trwania obserwacji, przeszkody w polu
       widzenia, wady wzroku/słuchu, stan świadka (zmęczenie, substancje),
       czas od zdarzenia do pierwszej relacji.

⛔ ŹRÓDŁO TREŚCI — ODESŁANIE, NIE DRUGA KOPIA:
   view shared/MOD-ATAK-NA-SWIADKA.md
     § FAZA 1 SW-P1 — dane formalne i relacja ze stronami        → A-1
     § FAZA 2 SW-A1 — konflikt interesu / stronniczość           → A-2
     § FAZA 1 SW-P3 — kategorie źródła wiedzy                    → A-3
     § FAZA 2 SW-A6 — upływ czasu, zawodność pamięci             → A-4
   Kategorie A-3 MUSZĄ być tożsame z SW-P3 (BEZPOŚREDNIE / Z RELACJI /
   WNIOSKOWANE / DOMYSŁ) — dwie różne siatki pojęć w jednym systemie
   uniemożliwiłyby przeniesienie wyniku W3 do wektorów ataku SW-A3/SW-A4.
   ⛔ NIE kopiuj treści tamtego modułu tutaj (CHECKLIST-DEDUP): przy zmianie
   brzmienia powstałaby druga, cicho rozjeżdżająca się wersja — dokładnie ten
   dryf, który F-115 udokumentowała na self-checku ANTY-FASADA.

⛔ RÓŻNICA KIERUNKU — czytaj zanim sięgniesz do shared/:
   MOD-ATAK-NA-SWIADKA analizuje zeznanie JUŻ ZŁOŻONE (materiał zastany,
   protokół). BLOK A buduje pytania PRZED zeznaniem. Ta sama siatka pojęć,
   przeciwny kierunek: tam „które twierdzenie podważyć", tu „o co zapytać,
   żeby kategoria w ogóle dała się ustalić". Nie przenoś gotowych formuł
   pisma procesowego (SW-A1 „Technika pisma") do listy pytań — pytanie do
   świadka nie zawiera tezy, którą ma potwierdzić (por. QUESTION-ADMISSIBILITY-GATE,
   zakaz pytań sugestywnych).

⛔ KONTROLA NA WYJŚCIU (przed wydaniem W3 użytkownikowi):
   Dla KAŻDEGO świadka wypisz cztery znaczniki:
     A-1 ✔/✖ · A-2 ✔/✖ · A-3 ✔/✖ · A-4 ✔/✖/n.d. (n.d. = świadek nie jest typu 2)
   Znacznik ✖ wymaga JEDNOZDANIOWEJ przyczyny w wyniku — np. „A-2 ✖: brak
   danych o sytuacji zawodowej świadka w materiale, pytanie ogólne w W3 poz. 4".
   ⚠️ Ta kontrola jest SAMO-RAPORTUJĄCA — ✔ dowodzi, że model zadeklarował
   pokrycie, nie że pytanie faktycznie stoi w liście. Weryfikacja skuteczności
   dopiero testem z grupą kontrolną (F-113 w audyt-systemu-v4).
```

Przykładowe sformułowania (dobierz do danych z W1 — to warstwa redakcyjna
NAD czterema elementami obowiązkowymi, nie zamiast nich):
- Skąd świadek zna okoliczności sprawy?                       [A-3]
- Jak długo i w jaki sposób pozostawał w kontakcie ze stronami? [A-1]
- Czy posiada interes osobisty lub finansowy w wyniku sprawy?  [A-2]
- Czy był wcześniej przesłuchiwany w tej lub powiązanej sprawie?
- W jakiej odległości i przez jaki czas obserwował zdarzenie?  [A-4]

---

### BLOK B — Pytania główne (tezy z W2)

Cel: udowodnienie tez dowodowych zidentyfikowanych w W2.

Ilość: min. 2 pytania na tezę.
Model: zgodnie z rekomendacją z W2.

Przy modelu PEACE: pytania otwarte narracyjne → uszczegóławiające.
Przy modelu LEJEK: szerokie → wąskie.
Przy modelu ONE-FACT: zamknięte, jedno zdanie, jeden fakt.

---

### BLOK C — Pytania kontrolne i zabezpieczające

Cel: potwierdzenie kluczowych faktów alternatywnymi sformułowaniami,
zabezpieczenie ustępstw przed wycofaniem.

Ilość: 3–8 pytań.
Technika: looping dla ustępstw uzyskanych w Bloku B.

**SYGNAŁY STOP — oznacz przy każdej grupie pytań w tym bloku:**

```
STOP-1: USTĘPSTWO UZYSKANE
  Świadek potwierdził kluczowy fakt → natychmiast przejdź dalej.
  Nie pytaj o przyczynę, nie eksploruj — looping w BLOKU C, potem STOP.

STOP-2: ODPOWIEDŹ ROZSZERZONA SZKODLIWA
  Świadek zaczął narrację korzystną dla siebie → nie kontynuuj linii.
  Wróć do pytania zamkniętego z innego obszaru lub zmień blok.

STOP-3: ŚWIADEK ZMIENIŁ POSTAWĘ
  Świadek odpowiada inaczej niż prognozowano w W2 → aktywuj model awaryjny
  z REKOMENDACJI KOŃCOWYCH. Nie improwizuj otwartymi pytaniami.

STOP-4: CEL ROZDZIAŁU OSIĄGNIĘTY
  Cel procesowy bloku/rozdziału zrealizowany → zakończ blok bez "jednego pytania za dużo".
```

---

### BLOK D — Pytania na sprzeczności
*(dostępny TYLKO jeśli dostarczono dokument z wcześniejszymi zeznaniami)*

Cel: ujawnienie rozbieżności między obecnymi zeznaniami a wcześniejszymi.

Dla każdej sprzeczności zidentyfikowanej w W2:
- Przytoczyć wcześniejsze sformułowanie (bez cytowania wprost — parafrazą lub przez pytanie).
- Pytanie stwierdzające aktualną wersję.
- Pytanie konfrontacyjne ujawniające rozbieżność.
- Pytanie o przyczynę zmiany zeznań.

Jeśli dokument zeznań nie został dostarczony:
```
⬛ BLOK D: niedostępny — brak dokumentu z wcześniejszymi zeznaniami.
   Aby odblokować: dostarcz protokół przesłuchania / deklarację pisemną.
```

---

### BLOK E — Pytania ryzykowne i niedopuszczalne

Dla każdego pytania ryzykownego lub niedopuszczalnego podaj:
- treść pytania,
- dlaczego jest ryzykowne / niedopuszczalne,
- alternatywę bezpieczną lub rezygnację.

Kategorie:
- **Niedopuszczalne**: sugestywne w przesłuchaniu bezpośrednim, naruszające zakazy dowodowe,
  dotyczące faktów nieobjętych tezą dowodową.
- **Ryzykowne**: otwarte na odpowiedź szkodliwą, mogące wzmocnić zeznania świadka,
  pytania bez dowodu kontrolnego.

---

### MACIERZ FINALNA

Format tabeli:

| # | Pytanie (skrót) | Blok | Cel | Teza | Dowód kontrolny | Ryzyko |
|---|---|---|---|---|---|---|

Uwzględnij wszystkie pytania z Bloków A–D.

---

### SCORING FINALNY

Zaktualizowany scoring 0–10 po analizie pytań ryzykownych.

Format:
```
SCORING FINALNY: [X]/10 — [słaby / umiarkowany / istotny / kluczowy]

Uzasadnienie:
- Bezpośredniość wiedzy: [ocena]
- Interes w wyniku: [ocena]
- Spójność z dokumentami: [ocena]
- Odporność na kontrpytania: [ocena]
- Znaczenie dla ciężaru dowodu: [ocena]
- Warunki obserwacji (jeśli typ 2): [ocena]

Zmiana względem W2: [bez zmiany / podniesiony / obniżony + powód]
```

---

### REKOMENDACJE KOŃCOWE

- Kolejność bloków na sali (jeśli odmienna od A→B→C→D).
- Kwestie do monitorowania podczas przesłuchania.
- Pytania rezerwowe na wypadek nieoczekiwanej odpowiedzi.
- Rekomendacja co do modelu awaryjnego (jeśli świadek zmieni postawę).
