# BLOK-ATAK-NA-DOWOD, BLOK-NEGACJA, BLOK-PROWENIENCJA — szczegóły

> **Trigger:** gdy w sprawie są dowody przeciwnika (MP5 perspektywa = TAK)
>   LUB gdy BLOK-PROWENIENCJA wykrył P! (alert autentyczności/custody)
> **Plik kanoniczny:** `view /mnt/skills/user/shared/MOD-ATAK-NA-DOWOD.md`
> **Cel:** systematyczna analiza 12 wektorów ataku na dowody przeciwnika
>   + procedura obrony własnych dowodów przed tymi samymi atakami.

```
12 WEKTORÓW ATAKU (AD-1..AD-12) — skrót (szczegóły w MOD-ATAK-NA-DOWOD.md):
  [AD-1]  Autentyczność: metadane, podpis, fałszerstwo, deepfake
  [AD-2]  Łańcuch przechowywania (custody): przerwy, dostęp, integralność
  [AD-3]  Relewantność: fakt bez znaczenia / już udowodniony (art. 227 KPC)
  [AD-4]  Forma: kopia bez oryginału / bez poświadczenia (art. 129 §1 KPC)
  [AD-5]  Zakaz ustawowy: nagrania (art. 168a KPK), tajemnica, RODO, art. 174 KPK
  [AD-6]  Wiarygodność treści: retrospektywne, interes autora, sprzeczność
  [AD-7]  Zakres wniosku: nieokreślony, nieprzydatny (art. 235¹ KPC)
  [AD-8]  Prekluzja: spóźniony (art. 235² KPC / art. 170 §1 pkt 5-6 KPK)
  [AD-9]  Kontrdowód aktywny: KD-1 dokument, KD-2 biegły, KD-3 świadek...
  [AD-10] Dowody elektroniczne: brak metadanych, hash, kontekst, AI/deepfake
  [AD-11] Jednostronny ex parte: wytworzony przez stronę na potrzeby sporu
  [AD-12] Systemowy: sprzeczność, cherry-picking, koordynacja, luki

PROCEDURA ADIS (ofensywna — atakowanie dowodów przeciwnika):
  ADIS-1 → inwentaryzacja dowodów przeciwnika
  ADIS-2 → screening AD-1..AD-12 per dowód
  ADIS-3 → priorytety 🔴/🟠/🟡/🟢
  ADIS-4 → instrument procesowy (wniosek o oddalenie / biegły / oryginał)
  ADIS-5 → sekcja w piśmie "ZARZUTY CO DO MATERIAŁU DOWODOWEGO"

PROCEDURA SHIELD (obronna — szczepienie własnych dowodów):
  S Secure → oryginał + metadane + hash
  H Harden → triangulacja ≥2 klas (P+ z MOD-PROWENIENCJA)
  I Integrate → każdy dowód = konkretna przesłanka art. X §Y
  E Enumerate → wszystkie dowody w pozwie / odpowiedzi (prekluzja)
  L Link → chronologia MP3 + wyjaśnienie pozornych sprzeczności
  D Document → proweniencja per dowód (MOD-PROWENIENCJA §PR1)

INTEGRACJA:
  P! z BLOK-PROWENIENCJA → automatycznie AD-1 + AD-2
  [ZAW] proweniencja → AD-11 + AD-12 SY-3
  MP5 §5.2 "typ: dowodowe" → rozwiń na AD-X z siłą N/10
```

> **Trigger:** ZAWSZE — automatyczny dla każdej sprawy z ≥1 dowodem i ≥1 tezą.
> **Plik kanoniczny:** `view /mnt/skills/user/shared/MOD-NEGACJA-DOWODOW.md`
> **Cel:** ocenić siłę każdego dowodu wobec technik negacji przeciwnika,
> zidentyfikować milczące przyznania i zbudować odporne pismo.

```
BLOK N1 — CIĘŻAR DOWODU (per teza T-X):
  KR1: kto wywodzi skutki z faktu? → ten ma ciężar (art. 6 KC)
  KR2: czy istnieje przepis odwracający ciężar?
       OD-1 mobbing | OD-2 dyskryminacja | OD-3 dyscyplinarne
       OD-4 wypowiedzenie | OD-5 wypadek | OD-6 probatio diabolica
  KR3: czy fakt jest negatywny? → rozważ art. 231 KPC
  KR4: co wystarczy do SPEŁNIENIA ciężaru przez nas?
  KR5: co wystarczy przeciwnikowi do ZNIWECZENIA?

BLOK N2 — ODPORNOŚĆ DOWODÓW (per klasa A-G):
  A (urz.) → obalenie: wymaga klasy A lub G + dowód błędu/fałszu
  B (pryw.) → obalenie: żądanie oryginału + twierdzenie o przeróbce
  C (koresp.) → obalenie: zaprzeczenie + wniosek o metadane
  D (świad. bezp.) → obalenie: motyw stronniczości + zeznanie przeciwne
  E (świad. pośr.) → samo wskazanie pośredniości obniża do 1/10
  F (strona) → zaprzeczenie strony p. rodzi sprzeczność (art. 233 §1)
  G (biegły) → obalenie: atak na metodologię + wniosek o 2. biegłego

12 TECHNIK NEGACJI (N1-N12) — pełna taksonomia w MOD-NEGACJA-DOWODOW.md:
  [N1]  Gołosłowne zaprzeczenie
  [N2]  Twierdzenie o nieistnieniu faktu pozytywnego
  [N3]  Twierdzenie o nieistnieniu elementu prawnego
  [N4]  Ogólnikowe zaprzeczenie "wszystkiemu"
  [N5]  Atak na autentyczność dokumentu
  [N6]  Odmowa przedłożenia dokumentu (art. 233 §2 KPC)
  [N7]  Zarzut braku formy / wadliwości formalnej
  [N8]  Atak na wiarygodność świadka
  [N9]  Zarzut prekluzji dowodowej
  [N10] Cherry-picking — selektywne cytowanie (MAN-05)
  [N11] Antycypacja zarzutu / immunizacja twierdzenia
  [N12] Zniszczenie lub ukrycie dowodu (spoliation / art. 233 §2)

BLOK N4 — MILCZENIE JAKO PRZYZNANIE:
  Per każde kluczowe twierdzenie faktyczne:
    M1: czy pismo przeciwnika odnosi się wprost? → NIE → M2
    M2: czy objęte ogólnym zaprzeczeniem? → jeśli nie → PRZYZ-MIL
    M3: waga: H (kluczowe) / M (istotne) / L (poboczne)
    M4: formularz: "T-X pozostaje niezaprzeczone. Art. 230 KPC."
  Rejestr [PRZYZ-MIL-H/M/L] → sekcja "Fakty bezsporne" pisma.

PROCEDURA NG1-NG6:
  NG1 mapowanie ciężaru → NG2 odporność → NG3 prognoza N1-N12
  → NG4 milczenie → NG5 raport BLOK-NEGACJA → NG6 integracja pipeline
```

> **Trigger OBOWIĄZKOWY:**
>   ≥3 dowodów klasy C lub D (korespondencja, zeznania)
>   LUB ≥2 świadkowie z tego samego miejsca pracy / działu
>   LUB DTA-ID-MODE aktywny (≥5 plików)
> **Trigger na żądanie:** "sprawdź czy z jednego systemu", "czy zeznania skoordynowane",
>   "skąd pochodzi", "czy ten sam autor", "proweniencja"
> **Plik kanoniczny:** `view /mnt/skills/user/shared/MOD-PROWENIENCJA-DOWODOW.md`
> **Cel:** wykryć wspólne źródło ≥2 pozornie niezależnych dowodów i ocenić konsekwencje.

```
7 TYPÓW PROWENIENCJI (pełna taksonomia w MOD-PROWENIENCJA-DOWODOW.md):

  [SYS]   Wspólny system IT  — format/numeracja/metadane systemowe identyczne
  [KOM]   Wspólny komunikator — ten sam nadawca/odbiorca/wątek/kanał
  [ZAW]   Wspólne środowisko zawodowe — ten sam pracodawca/dział/przełożony
  [AUT]   Wspólny autor — metadane, nawyki typograficzne, identyczne błędy
  [URZ]   Wspólne urządzenie — EXIF, adres IP, artefakty skanera
  [LIN]   Podobieństwo tekstu — identyczne zdania, schematy, błędy merytoryczne
  [CHAIN] Wspólny custody — stemple, braki numeracji, kolejność skanowania

4 KLASY KONSEKWENCJI:

  P+  Wzmacniająca: wspólne niezależne źródło → fakt awansuje do BEZSPORNE/PEWNE
  P-  Osłabiająca:  pozorna niezależność → oba dokumenty traktuj jak jeden
  P0  Neutralna:    wspólne źródło znane obu stronom, bez wpływu na siłę
  P!  Alert:        nieoczekiwane wspólne źródło → [H-PROW] + wniosek dowodowy

PROCEDURA (szczegółowa w MOD-PROWENIENCJA-DOWODOW.md §PR1-PR5):
  PR1 Inwentaryzacja proweniencyjna (autor/system/kanał per dowód)
  PR2 Skan par (Di, Dj) pod wszystkie 7 typów
  PR3 Klasyfikacja P+/P-/P0/P!
  PR4 Raport proweniencji (klastry + fakty awansowane/zdegradowane + alerty P!)
  PR5 Integracja: → DTA-ID-MODE → macierz D×T → BLOK-KONSEKWENCJE

INTEGRACJA Z PIPELINE:
  Fakty awansowane P+ → BEZSPORNE w BLOK-KONSEKWENCJE C-X.1
  Alerty P! → wnioski dowodowe art. 248 KPC / biegły art. 278 KPC
  Obniżona wiarygodność P- → RS (ryzyko sporności) w macierzy D×T
  Hipotezy [H-PROW] → MP6-sledczy §6.12 lista pytań śledczych
```
