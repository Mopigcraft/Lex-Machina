# KROK 2 — CENTRALNY ROUTER: BLOK A, B, B5, C, D0, D, E, F, G (tryb minimalny)

### BLOK A — Charakter materiału

```
A1. Materiał zawiera dowody do oceny (dokumenty, nagrania, maile, zeznania)?
    TAK → dodaj: MD1, MD2

A2. Materiał zawiera pisma procesowe, akta lub narrację stron?
    TAK → dodaj: MP0, MP1

A3. Tylko pytanie o termin procesowy (bez analizy dowodów)?
    TAK → dodaj: MD5 · STOP (pomiń pozostałe bloki)
```

---

### BLOK B — Liczba i typ dokumentów

```
B1. Liczba dokumentów ≥ 3 LUB sprawa złożona wielowątkowa?
    TAK → dodaj: FAZA2-dashboard

B2. Liczba dokumentów ≥ 2?
    TAK → dodaj: MD3c (sprzeczności między dokumentami) [obowiązkowy]
        → wykonaj też MD3a KROK 0 (skan błędów dat i nazw) jako pierwszy krok
          analizy, niezależnie od tego czy B4=TAK — MD3a KROK 0 jest lekki
          (kilka punktów kontrolnych) i zapobiega błędom propagowanym dalej

B3. Materiał zawiera nagranie LUB wątpliwość co do legalności dowodu?
    TAK → dodaj: MD3b (walidacja prawna, zakazy dowodowe, art. 267 KK)

B4. Dokument może mieć wady formalne (kopia bez poświadczenia, brak pieczęci,
    brak podpisu, skan bez oryginału)?
    TAK → dodaj: MD3a (pełna walidacja formalna, wszystkie punkty)
```

---

### BLOK B5 — PORCJOWANIE (⛔ HARD GATE gdy materiał duży)

```
Po SD-VER (KROK 0b) — PRZED MD1-ekstrakcją:
  view /mnt/skills/user/shared/MOD-PORCJOWANIE-DOWODOW.md → wykonaj PD0.

  STATUS BEZPIECZNY  (≤5 plików i ≤100 KB):
    → kontynuuj BLOK C i MD1 normalnie bez podziału.

  STATUS OSTRZEŻENIE (6–15 plików lub 100–400 KB):
    → PD1 (podział na partie) → PD2 (plan dla użytkownika) → STOP.
    → Czekaj na zatwierdzenie planu przed analizą.

  STATUS WYMAGANE    (≥16 plików lub >400 KB):
    → ⛔ HARD GATE — nie rozpoczynaj MD1 bez zatwierdzonego planu partii.
    → PD1 → PD2 → STOP → po zatwierdzeniu: MD1/MD2/MD3 per partia.

  STATUS KRYTYCZNE   (≥30 plików lub >800 KB):
    → ⛔ HARD GATE BEZWZGLĘDNY — max 3–4 pliki per partia.
    → Każda partia kończy się PD4 (checkpoint) → present_files.
    → Użytkownik wznawia przez wgranie checkpointu (PD5).

  Trigger wznawiania: plik "# CHECKPOINT ANALIZY" wgrany przez użytkownika
    → PD5 (parsuj checkpoint, odtwórz stan) → kontynuuj od właściwej partii.

  W każdej partii: kroki MD1/MD2/MD3 wykonuj per plik z bieżącej partii.
  Akumuluj wyniki w STAN_PARTII (PD3.3 z MOD-PORCJOWANIE-DOWODOW).
  Po ostatniej partii: PD6 (synteza finalna) → zasilenie MD4/MD5/MD6.
```

---

### BLOK C — Zakres analizy dowodowej

```
C1. Użytkownik pyta o luki w materiale / brakujące dowody / pokrycie przesłanek?
    TAK → dodaj: MD4

C2. W materiale pada data doręczenia, ogłoszenia wyroku lub inna data krytyczna?
    TAK → dodaj: MD5

C3. Potrzebny raport końcowy / podsumowanie dowodowe?
    TAK → dodaj: MD6
    DOMYŚLNY format wyjścia = dashboard interaktywny (FAZA 2 / KROK 4).
    Dashboard jest wzorcowym formatem raportu — generuj go zawsze gdy B1=TAK,
    bez pytania o format.

C4. Użytkownik prosi WYRAŹNIE o wersję szczegółową / dokument / plik / "jak
    LexAlpha" / ciągły tekst z nawigacją po sekcjach LUB chce przekazać analizę
    osobie trzeciej jako dokument?
    TAK → dodaj: MD-NARR jako DODATEK do dashboardu (nie zamiast).
    MD-NARR to wersja szczegółowa — generowana TYLKO na wyraźne żądanie,
    nigdy domyślnie. Jeśli C3=TAK i C4=NIE → tylko dashboard.
    Jeśli C4=TAK → wygeneruj dashboard (jeśli jeszcze nie istnieje w tej
    rozmowie) + MD-NARR, w tej kolejności.
```

---

### BLOK D0 — TEZA-GATE (obowiązkowe, PRZED D1-D6 — naprawa F-7/ZASADA 11)

```
⛔ Zanim odpowiesz na pytania D1-D6, zrekonstruuj JEDNYM ZDANIEM per strona
tezę centralną wynikającą z materiału: czego strona żąda/twierdzi i na
jakiej podstawie. Zapisz to jawnie w odpowiedzi — nie tylko w rozumowaniu
wewnętrznym.

Powód: bez tego punktu odniesienia ocena mocnych/słabych stron (D2), analiza
prawna per roszczenie (D4) czy raport końcowy (D5) mogą oceniać argumenty
w oderwaniu od tego, co pismo FAKTYCZNIE twierdzi — ryzykując ocenę
powierzchowną (np. na podstawie tonu czy objętości argumentacji, nie jej
rzeczywistego związku z tezą) lub pominięcie, że pismo broni innej tezy niż
się wydaje z pierwszego wrażenia.

Jeśli materiał zawiera kilka wątków/roszczeń → osobna teza per wątek, nie
jedna uśredniona. Jeśli strony są >1 (spór dwustronny) → teza każdej strony
osobno, nawet jeśli są sprzeczne.

To nie zastępuje D1 (kolizje narracyjne) ani MP2 (ocena prawna) — to punkt
odniesienia, do którego D1-D6 się odnoszą.
```

---

### BLOK D — Zakres analizy pism (tylko jeśli A2=TAK)

```
D1. Materiał zawiera twierdzenia stron, narrację, sprzeczne wersje zdarzeń?
    TAK → dodaj: MP3 (kolizje i sprzeczności narracyjne)

D2. Użytkownik pyta o mocne/słabe strony, pozycję procesową, szanse?
    TAK → dodaj: MP4

D3. Użytkownik pyta o strategię ataku / obrony / riposty LUB sprawa
    ma wyraźnego przeciwnika procesowego?
    TAK → dodaj: MP5

D4. Potrzebna ocena prawna per roszczenie/zarzut, ciężar dowodu, znamiona?
    TAK → dodaj: MP2
    (UWAGA: MP2 zawiera katalog dziedzinowy — wczytaj MX przed MP2)

D5. Potrzebny raport końcowy z predykcją i rekomendacjami?
    TAK → dodaj: MP7

D6. Potrzebna matryca dowodowa (admissibility, chain of custody)?
    TAK → dodaj: MP8
```

---

### BLOK E — Moduły specjalistyczne (wczytuj TYLKO gdy sygnał obecny)

```
E1. Pytanie o „logikę zdarzeń" / „co z czego wynika" / „narrację procesową"
    / „powiązanie faktów" / łańcuchy przyczynowe LUB sprawa złożona ≥2 dok.?
    TAK → dodaj: MP13 (synteza faktyczna — 442 linie, wczytuj świadomie)
    + gdy łańcuchy się rozgałęziają/zbiegają, jest przyczynienie, kilku sprawców, wzajemny wpływ
      albo pytanie „co jeśli” → MP13 §13.2a → shared/MOD-GRAF-PRZYCZYNOWY.md (od 5.16.18)

E2. Podejrzenie manipulacji, ukrytych motywacji, kłamstwa, zaplanowanego działania
    LUB sprawa karna LUB użytkownik pyta o profilowanie / zachowanie stron?
    TAK → dodaj: MP6 (techniki śledcze — 457 linii, wczytuj świadomie)

E3. Materiał dotyczy RODO, monitoringu pracownika, danych osobowych,
    dostępu do kont/urządzeń, art. 267 KK?
    TAK → dodaj: MP11

E4. Użytkownik pyta o koszty sądowe, opłacalność postępowania, próg ekonomiczny?
    TAK → dodaj: MP10

E5. W materiale pada wiele dat krytycznych / terminów sądowych do śledzenia?
    TAK → dodaj: MP12

E6. Konieczna kontrola jakości / audyt antyhalucynacyjny analizy?
    TAK → dodaj: MP9
```

---

### BLOK F — Wykrywanie dziedzin prawa

```
F1. Analiza dotyczy oceny prawnej (D4=TAK) LUB sprawa obejmuje wiele reżimów
    prawnych LUB użytkownik pyta o dziedziny prawa?
    TAK → wczytaj MX przed MP2
         view /mnt/skills/user/analizator-dowodow-v3/modules/MX-dziedziny.md
         Wynik MX uzupełni moduły specjalistyczne (np. MP11 dla RODO/CYBER,
         MP6 dla [KARNE-ZN], MD3b dla [PRAC-ROZW]).

F2. MX wykrył dziedzinę karną [KARNE-ZN]?
    TAK → aktywuj kwalifikator: prawo-polskie-v2 (rozbicie na znamiona)
```

---

### BLOK G — Tryb minimalny (kiedy NIE wczytywać modułów P)

```
Jeśli użytkownik zadaje JEDNO konkretne pytanie (np. „czy ten dowód jest silny",
„ile mam czasu na apelację", „co znaczy ten zapis") i NIE prosi o pełną analizę:
→ odpowiedz inline bez wczytywania modułów
→ wczytaj maksymalnie 1–2 moduły jeśli niezbędne do precyzyjnej odpowiedzi
→ NIE uruchamiaj dashboardu ani MP7/MD6

```
