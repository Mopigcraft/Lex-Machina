# Reguły ekstrakcji, protokół sprzeczności, eksport do pisma

> Plik obowiązkowy dla reguł ekstrakcji, obsługi sprzeczności i eksportu do pisma. Treść przeniesiona dosłownie z SKILL.md (refaktor 2026-10-20); SKILL.md zawiera nagłówki i streszczenia.

## REGUŁY EKSTRAKCJI

### Co traktować jako zdarzenie

```
✓ Złożenie pisma / doręczenie (data z prezentatą lub potwierdzeniem)
✓ Zawarcie umowy / aneksu
✓ Zwolnienie / wypowiedzenie / rozwiązanie stosunku
✓ Wyrok / postanowienie / decyzja administracyjna
✓ Przekroczenie terminu
✓ Płatność / brak płatności / wezwanie do zapłaty
✓ Zdarzenie faktyczne (wypadek, incydent, spotkanie)
✓ Zawiadomienie organów (policja, prokuratura, PIP, UOKiK)
✓ Upływ terminu zawitego
✓ Zmiana stanu prawnego lub faktycznego strony
```

### Czego NIE traktować jako zdarzenie

```
✗ Daty pisania pisma procesowego (chyba że = data zdarzenia)
✗ Daty powołanych przepisów (wejście w życie ustaw) — chyba że kluczowe
✗ Daty orzeczeń powoływanych jako precedens
✗ Daty hipotetyczne / warunkowe ("gdyby doszło do...")
```

### Priorytety wiarygodności źródeł

```
1. Dokumenty urzędowe z pieczęcią / prezentata sądu
2. Wyroki i postanowienia z sygnaturą
3. Korespondencja z potwierdzeniem odbioru
4. Zeznania potwierdzone przez ≥2 świadków
5. Korespondencja e-mail / SMS z metadanymi
6. Zeznania jednostronne
7. Twierdzenia w pismach procesowych (bez dowodu)
```

---

## SPRZECZNOŚCI — PROTOKÓŁ OBSŁUGI

Indeks obejmuje dwa typy sprzeczności — obsługuj oba identyczną ścieżką.

### Typy sprzeczności

```
TYP: DATA
  Definicja: różne źródła podają różne daty dla tego samego zdarzenia
  Wykrywanie: porównaj pole `data` dla zdarzeń o tym samym opisie
  Przykłady:
    • Pracodawca datuje wypowiedzenie 10.04, pracownik zeznaje że otrzymał 15.04
    • Wyrok podaje datę zdarzenia 03.03, zeznanie świadka wskazuje 05.03
  Odesłanie do katalogu: references/sprzecznosci-dat.md → kategoria A/B/C

TYP: OPIS
  Definicja: źródła zgodnie (lub w przybliżeniu) co do daty, ale różnią się
             w opisie przebiegu, sprawcy, skutku lub okoliczności zdarzenia
  Wykrywanie: porównaj treść opisów zdarzeń o tej samej lub zbliżonej dacie
  Przykłady:
    • Świadek A zeznaje: "krzyczał wulgarnie", świadek B: "mówił podniesionym głosem"
    • Pozew: "pracownik odmówił wykonania polecenia", protokół: "pracownik poprosił
      o pisemne potwierdzenie polecenia"
    • DOK-01 (umowa): "termin płatności 30 dni", DOK-03 (faktura): "termin 14 dni"
    • Zeznanie pokrzywdzonego: "uderzył mnie", zeznanie świadka: "popchnął go"
  Odesłanie do katalogu: references/sprzecznosci-dat.md → analogicznie kategoria A/B/C

TYP: DATA_I_OPIS
  Definicja: źródła różnią się zarówno datą, jak i opisem — traktuj jako dwie
             sprzeczności wpisane w jeden rekord SPRZECZNOŚĆ-[N]

TYP: IDENT
  Definicja: dokument dowodowy (podpis, pokwitowanie, formularz) zawiera zapis
             imienia/nazwiska/nazwy podmiotu, który różni się od danych tej samej
             osoby/strony/świadka używanych w pismach procesowych
  Wykrywanie: porównaj zapisy imion/nazwisk/nazw dla osób w tej samej roli procesowej
             (strona, świadek, podpisujący) między dokumentem dowodowym a pismami
  Przykłady:
    • Strona w pozwie: "Jan Nowakowski"; pokwitowanie z 9.10.2024: podpis "Michał Nowak"
    • Świadek w piśmie: "Bishal Poudel"; pokwitowanie z 5.12.2024: "Bishal Paudel"
  Nie zakładaj automatycznie zgodności ani niezgodności — oznacz [SPORNE] i wymagaj
  wyjaśnienia. Jeśli żadna ze stron nigdy nie odniosła się do rozbieżności, podnieś
  kategorię do A-KRYTYCZNA (zob. references/ekstrakcja-zdarzen.md → A-O5).
```

### Protokół obsługi (wspólny dla obu typów)

```
GDY wykryjesz sprzeczność:
1. Nadaj numer: SPRZECZNOŚĆ-[N] — numeruj sekwencyjnie w obrębie sprawy
2. Określ TYP: DATA / OPIS / DATA_I_OPIS
3. Zapisz obie wersje z pełną proweniencją (dok_id, strona_dok, autor_twierdzenia)
4. Oceń WPŁYW PROCESOWY:
   - KRYTYCZNY:
       DATA:  sprzeczność dotyczy terminu zawitego / przedawnienia / skuteczności doręczenia
       OPIS:  sprzeczność zmienia kwalifikację czynu lub zasadność roszczenia głównego
   - ISTOTNY:
       DATA:  sprzeczność zmienia sekwencję przyczynową
       OPIS:  sprzeczność osłabia lub wzmacnia wiarygodność kluczowego świadka / strony
   - MARGINALNY:
       DATA:  różnica nie wpływa na rozstrzygnięcie
       OPIS:  różnica stylistyczna / subiektywna ocena bez wpływu na ustalenia faktyczne
5. Zaproponuj rekomendację:
   DATA:  które źródło wiarygodniejsze (hierarchia z REGUŁY EKSTRAKCJI pkt 7) i dlaczego
   OPIS:  co wyjaśnić, jaki dowód rozstrzygnąłby sprzeczność (konfrontacja, biegły, dokument)
6. Jeśli wpływ KRYTYCZNY → STOP i poinformuj użytkownika przed kontynuacją analizy
7. Oznacz oba (lub wszystkie) zdarzenia flagą: kolizja_id = "SPRZECZNOŚĆ-[N]"
```

---

## EKSPORT DO PISMA PROCESOWEGO

```
Na żądanie "eksportuj do pisma" / "uzasadnienie faktyczne" / "sekcja faktów":

FORMAT EKSPORTU — SEKCJA A: FAKTY BEZSPORNE
"Niespornym jest, że:
[Numer]. W dniu [data] [podmiot] [zdarzenie]. [brak wskazania dowodu — fakt bezsporny]"

FORMAT EKSPORTU — SEKCJA B: FAKTY UDOWODNIONE
"[Numer]. W dniu [data] [podmiot] [zdarzenie opisane w czasie przeszłym,
bezosobowo, bez ocen]. [Dowód: DOK-XX — nazwa dokumentu, str. N]."

FORMAT EKSPORTU — SEKCJA C: FAKTY WYDEDUKOWANE
"[Numer]. Z materiału dowodowego wynika, że [zdarzenie].
[Dowód pośredni: DOK-XX (str. N) oraz DOK-YY (str. M) — rozumowanie: ...]"

FORMAT EKSPORTU — SEKCJA D: FAKTY SPORNE
"[Numer]. Powód twierdzi, że [wersja A]. Pozwany kwestionuje tę okoliczność,
wskazując, że [wersja B]. [Dowód strony powodowej: DOK-XX. Dowód strony pozwanej: DOK-YY]."

ZASADY:
✓ Każde zdarzenie = osobny akapit z numerem
✓ Sekcja A (BEZSPORNE) zawsze pierwsza — skraca pismo i skupia uwagę sądu
✓ Tylko zdarzenia [BEZSPORNE], [PEWNE] lub [WYDEDUKOWANE z adnotacją] w sekcjach A–C
✓ Zdarzenia [SPORNE] → wyłącznie sekcja D
✓ Kolejność: ścisła chronologiczna (od najstarszego) w obrębie każdej sekcji
✓ Styl: bezosobowy, faktyczny, bez ocen prawnych
✓ Proweniencja (dok_id + strona) → przy każdym fakcie w sekcjach B i C
```
