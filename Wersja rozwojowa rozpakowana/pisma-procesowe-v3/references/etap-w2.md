# PRE-W2-VERIFICATION-GATE, W2.1 moduły przed redakcją, W2.4 MOD-ATAK-NA-DRAFT (pełna treść)

> **Wywołaj:** `view shared/PRE-W2-VERIFICATION-GATE.md`
>
> ⛔ HARD GATE — BEZWZGLĘDNY. Wykonaj PO zatwierdzeniu W1 przez użytkownika,
> PRZED W2.1. NIE można pominąć. NIE ma wyjątków (nawet "prosta sprawa",
> "mam to z pamięci", "użytkownik podał dane", "dane są w aktach sprawy").
> Dane z akt sprawy NIE są weryfikacją online. Dane z pamięci modelu NIE są.
> ⛔ WERYFIKACJA [POV-B][POV-C]: web_search/web_fetch dla SĄDU i POZWANEGO
>    musi być wywołany fizycznie w tej odpowiedzi — patrz SELF-CHECK-PISMA.md blok PRE-W2.
>
> **Co weryfikuje:**
> - PRE-W2.B: adres i wydział sądu/organu — web_search OBOWIĄZKOWY
> - PRE-W2.C: dane rejestrowe pozwanego — KRS/NIP/adres z rejestru
> - PRE-W2.D: każdy numer KRS/NIP z akt — do której spółki należy?
>             Rozbieżność KRS ≠ NIP w tym samym dokumencie → STOP, wyjaśnij
>
> **Efekt:** Raport PRE-W2 (widoczny użytkownikowi) z danymi zweryfikowanymi.
> W2.1 używa WYŁĄCZNIE danych z raportu PRE-W2, nie z pamięci modelu.
>
> ⛔ ZAKAZ-PRE-W2: NIE wstawiaj do W2 żadnego adresu sądu, KRS, NIP, REGON,
> adresu pozwanego bez uprzedniej weryfikacji w PRE-W2. Naruszenie = błąd
> krytyczny — powróć do PRE-W2 i wykonaj retroaktywnie.
>
> **Przykłady błędów wyeliminowanych przez ten gate:**
> - SR Katowice-Zachód VII Wydział Pracy: ul. Warszawska 45 (nie ul. Lompy 14)
> - KRS [KRS-A] = [SPÓŁKA-A] sp. z o.o.; [SPÓŁKA-B] ma KRS [KRS-B] — bez
>   sprawdzenia rejestru model błędnie zbudował argument "ten sam KRS"

```
view pisma-procesowe-v3/modules/MOD-SZABLONY.md   (zawsze)
view pisma-procesowe-v3/modules/MOD-DOWODY.md     (gdy są dowody)
view pisma-procesowe-v3/modules/MOD-OBAL.md       (gdy riposta/odpowiedź)
view pisma-procesowe-v3/modules/MOD-OPLATY.md     (gdy pismo wszczynające)
view pisma-procesowe-v3/modules/MOD-ADMIN.md      (gdy sprawa adm./KPA/WSA)
view shared/ZAZALENIE-ADRESAT-GATE.md             (⛔ OBOWIĄZKOWE gdy pismo to
                                                                     zażalenie/odwołanie/sprzeciw/
                                                                     zarzuty/skarga — ustal adresata
                                                                     PRZED redakcją nagłówka pisma,
                                                                     nie zakładaj domyślnie instancji
                                                                     wyższej)
view shared/MOD-TIMING.md                         (gdy timing złożenia jest istotny:
                                                                     pierwsza rozprawa <14 dni /
                                                                     wniosek dowodowy grożący prekluzją /
                                                                     korzystne postanowienie do utrwalenia)
view modules/MOD-DOKTRYNA.md                       (gdy uzasadnienie powołuje
                                                                     komentarze lub literaturę —
                                                                     hierarchia: orzeczenie > doktryna)
⛔ UWAGA: MOD-MACIERZ-DOWOD-TEZA (KROK MT) wykonany już w W1.2c.
          W2 używa gotowej macierzy z W1.2c:
          • wnioski dowodowe formułuj PER TEZA: "Na okoliczność Tn: dowód D[x], D[y]"
          • dowody [W] powołuj RAZ z listą tez, nie per teza oddzielnie
          • tabela D×T z MT4 wchodzi do treści pisma jako sekcja widoczna dla sądu
          • MT5-MANDATE-ALL-EVIDENCE: sprawdź N_pismo ≥ 0.7 × N_macierzy po redakcji W2
view shared/MOD-IDENTYFIKACJA-STRONY-UMOWY.md
                                                                    (⛔ OBOWIĄZKOWE gdy: rozbieżne
                                                                     identyfikatory stron w dokumentach
                                                                     (różne KRS/NIP/nazwa); błędny PESEL;
                                                                     faktura z błędnym NIP — wykonaj
                                                                     ISU-1→ISU-5 przed W1.3;
                                                                     ⛔ gdy PESEL w aktach i znana data
                                                                     ur. lub płeć — wykonaj ISU-PESEL P1→P6)
view pisma-procesowe-v3/modules/MOD-PRACODAWCA-RZECZYWISTY.md
                                                                    (⛔ OBOWIĄZKOWE gdy: w materiale
                                                                     widoczne są ≥2 podmioty / różne KRS
                                                                     na umowach / zmiana nazwy pracodawcy /
                                                                     argument o tożsamości pracodawcy —
                                                                     wykonaj NAJPIERW ISU, potem PR1→PR4)
view modules/MOD-BUDOWA-ARGUMENTU.md               (⛔ OBOWIĄZKOWE — zawsze przed W2.2:
                                                                     schemat 7-elementowy każdego bloku,
                                                                     klasyfikacja A/B/C/D, kolejność tez,
                                                                     zamknięcie furtki, wniosek cząstkowy)
view modules/MOD-KOSZT-ODPOWIEDZI.md               (⛔ OBOWIĄZKOWE — zawsze przed W2.2:
                                                                     szablon KO-2 dla twierdzeń o dokumentach
                                                                     pozwanego, numerowanie KO-4, audit KO-3
                                                                     uruchamiany po W2 przed AUDYT-KOŃCOWY)
view modules/MOD-SKUTEK-PROCESOWY.md               (⛔ OBOWIĄZKOWE — zawsze przed W2.2:
                                                                     SP-1: blok skutku po każdej podstawie
                                                                     prawnej; SP-3: 4 pytania kontrolne;
                                                                     SP-5: pozycja w schemacie 7-el.)
view modules/MOD-MIKROPODSUMOWANIA.md               (⛔ OBOWIĄZKOWE — zawsze przed W2.2:
                                                                     MK-1: 3-4 zdania po każdym rozdziale;
                                                                     MK-2: zasady redakcji; BLOKADA gdy brak)
view modules/MOD-STRESS-TEST.md                     (⛔ OBOWIĄZKOWE — po W2, przed W3:
                                                                     ST-1: symulacja odpowiedzi pełnomocnika;
                                                                     ST-2: raport do wyświetlenia;
                                                                     ST-3: fix dla argumentów 🔴;
                                                                     BLOKADA .docx bez PASS)
view shared/STRATEGIA-PROCESOWA.md                (⛔ OBOWIĄZKOWE — zawsze przed W2.2:
                                                                     klasyfikacja A/B/C/D twierdzeń,
                                                                     kolejność bloków uzasadnienia,
                                                                     zasada niezależności tez)
```

> ⛔⛔⛔ HARD GATE W2.4 — BEZWZGLĘDNY, BEZ WYJĄTKU ⛔⛔⛔
> Ten krok jest OBLIGATORYJNY. Nie ma warunku aktywacji. Każdy draft przez niego przechodzi.
> NIE WOLNO przejść do W3 bez wykonania W2.4 i wyświetlenia RAPORTU D.
> NIE WOLNO wygenerować .docx bez zamkniętego W2.4.
> Pośpiech użytkownika, prosta sprawa, brak prośby — ŻADNE z nich nie jest wyjątkiem.

> Wywołaj: `view shared/MOD-ATAK-NA-DRAFT.md`
> (plik istnieje od v1.0.0 2026-06-21; jeśli view() zwróci błąd — zatrzymaj się
> i poinformuj użytkownika o brakującym pliku zamiast cicho pomijać krok)

**Sekwencja W2.4 (wykonaj w tej kolejności):**

1. `view shared/MOD-ATAK-NA-DRAFT.md`
2. D1 — skan zdań kategorycznych → naprawa redakcyjna samodzielnie
3. D2 — test pełnomocnika akapit po akapicie → naprawa redakcyjna dla 🟡/🟢;
         dla 🔴/🟠 bez pokrycia dowodowego → oznacz jako ⬛ LUKA D4
4. D3 — skan sprzeczności międzyakapitowych → naprawa redakcyjna samodzielnie
5. D5 — analiza własnych słabości i ryzyk (RP prawne / RD dowodowe / RPC procesowe)
         → 🔴/🟠: zdanie ubezpieczające lub zmiana konstrukcji; 🟡: notacja w RAPORCIE D
6. D4 — weryfikacja luk dowodowych → jeśli ⬛ LUKA D4 klasy 🔴/🟠: STOP
7. Wyświetl RAPORT D (obligatoryjny — nawet gdy wynik ✅)

**Rozgałęzienie po RAPORCIE D:**
- ATAK-OK / ATAK-UWAGI → przejdź do W3 automatycznie
- ATAK-STOP (⬛ LUKA D4 🔴/🟠) → STOP; zadaj pytania użytkownikowi;
  czekaj na odpowiedź; dopiero po niej uzupełnij draft i przejdź do W3

⛔ ZAKAZ-9 (nowy): NIE przechodzij do W3 bez wyświetlonego RAPORTU D z W2.4.
   Naruszenie = błąd krytyczny pipeline — powróć do W2.4 i wykonaj go retroaktywnie.
