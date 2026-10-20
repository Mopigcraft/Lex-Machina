# FAZA 3 (3-PULL, 3A-3D), 3E oraz FAZA 4-7 (przeniesione ze SKILL.md, treść bez zmian)

# FAZA 3 (mapa Dz.U.: 3-PULL, 3A-3D) i FAZA 3E (treść merytoryczna) (przeniesione ze SKILL.md, treść bez zmian)


Wczytaj `AKTUALNA_MAPA_DZU` ustaloną w FAZIE 0. Nie wybieraj mapy na podstawie
daty zapamiętanej w tym pliku.

### 3-PULL — Synchronizacja DR-MAPA-AKTOW → ROUTING-MAP → mapa_dzu

> ⚙️ **Protokół pull** — wykonaj PRZED 3A gdy zakres audytu obejmuje TRYB DZU lub pełny audyt.
> Cel: mapa_dzu musi być spójna z tym co faktycznie mają DR-skills.

**Krok 1 — Skan DR-MAPA-AKTOW:**

```bash
# Zebranie wszystkich Dz.U. z lokalnych map DR
grep -h "Dz\.U\." dr-*/MAPA-AKTOW.md | \
  grep -oP "Dz\.U\. \d{4} poz\. \d+" | sort -u
```

**Krok 2 — Porównanie z ROUTING-MAP.md:**

```bash
# Znalezienie Dz.U. w MAPA-AKTOW które nie są w ROUTING-MAP
# (wykonuj manualnie: porównaj output Kroku 1 z ROUTING-MAP.md)
view prawo-polskie-v2/ROUTING-MAP.md
# od 2026-10-20 ROUTING-MAP.md to indeks: tabele aktów w prawo-polskie-v2/routing/DR-01.md … DR-16.md
```

**Krok 3 — Porównanie z mapa_dzu:**

```bash
# Znalezienie Dz.U. w ROUTING-MAP których brak w mapa_dzu
# Każdy akt w ROUTING-MAP z Dz.U. powinien mieć wpis w mapa_dzu
```

**Krok 4 — Wykrywanie MONITORING ze wszystkich źródeł:**

```bash
# Znajdź akty z vacatio legis w DR-MAPA-AKTOW
grep -h "OCZEKUJE\|WCHODZI\|vacatio\|wchodzi w życie" \
  dr-*/MAPA-AKTOW.md | sort -u
```

Każdy wynik Kroku 4 → **sprawdź czy jest wpisany do sekcji MONITORING** w:
- `mapa_dzu_*.md` (tabela MONITORING)
- `ROUTING-MAP.md` (sekcja MONITORING)

Jeśli brakuje → **dodaj do obu plików** jako `⏳ OCZEKUJE`.

---

### 3A — Nowe t.j. od ostatniego audytu

Sprawdź w ELI (`api.sejm.gov.pl/eli/acts/search`, RZĄD 1; ISAP tylko jako link dla człowieka) czy pojawiły się nowe teksty jednolite dla kluczowych aktów:
- KC, KPC, KPK, KRO, KP, KSH, KPA, PB, PrFarm, PIT, CIT, OrdPod, PrNotariat
- Sprawdź Dz.U. poz. > max_poz z ostatniego audytu (aktualnie: > 1079 z 2026 — najwyższa pozycja odnotowana w sesji 2026-08-21)

### 3B — Aktualizacja statusów

Jeśli znaleziono nowe t.j.:
- Zmień status starego wpisu: `OK` → `PREV`
- Dodaj nowy wiersz do tabeli z: rok, poz., akt, typ=TJ, status=OK, skille (wg mapy), uwagi

### 3D — Akty oczekujące na wejście w życie (MONITORING)

> ⛔ **UZUPEŁNIENIE LEGENDY 2026-08-15p — brakujący znacznik ⚠️ ALERT.**
> Prompt zadania cyklicznego (`references/SCHEDULED-TASK-COWORK.md`, § 2B krok 4)
> każe priorytetyzować „wszelkie ⚠️ ALERT z poprzednich audytów". Kontrola
> wykazała **0 wystąpień** tego znacznika zarówno w SKILL.md, jak i w mapie
> Dz.U. — krok 4 promptu odsyłał do konwencji, której nigdy nie wprowadzono,
> więc sesja wykonawcza nie miała czego szukać.
>
> **Definicja (od 2026-08-15p):** `⚠️ ALERT` oznacza w kolumnie uwag mapy akt,
> którego numer **okazał się błędny lub sporny** i został skorygowany — czyli
> pozycję o podwyższonym ryzyku nawrotu, wymagającą sprawdzenia w KAŻDYM
> kolejnym przebiegu, niezależnie od rotacji. Znaczniki `⏳ OCZEKUJE`
> i `⚡ WCHODZI-90DNI` dotyczą PRZYSZŁOŚCI aktu (vacatio legis); `⚠️ ALERT`
> dotyczy PRZESZŁOŚCI rejestru (już raz się pomylił).
>
> Pierwsze pozycje kwalifikujące się do oznaczenia: Kodeks morski (F-82 —
> numer należał do innej ustawy), PIT/CIT/KC (F-84 — stary t.j. nieziejący
> statusu PREV), KPSW (błędna „poprawka" z 2026-07-02q, patrz wpis 08-15d).

Po weryfikacji nowych t.j. (3A–3B) sprawdź i zaktualizuj tabelę aktów opublikowanych, które **nie weszły jeszcze w całości w życie** lub wchodzą etapami.

Dla każdego aktu z tabeli MONITORING wykonaj:
1. Sprawdź w ELI (metryka `entryIntoForce` + przepis o wejściu w życie — DOSTEP-MASZYNOWY-API §2) czy data wejścia w życie minęła lub zbliża się (horyzont: 90 dni).
2. Jeśli akt wszedł w życie → przenieś do tabeli głównej mapy Dz.U. (zmień typ `OCZEKUJE` → `TJ` lub `NOV`), usuń z MONITORING.
3. Jeśli data jeszcze nie minęła → zaktualizuj uwagi, potwierdź termin.
4. Jeśli akt zastępuje inny → odnotuj w kolumnie `Zastępuje` (nazwa aktu + stary Dz.U.).

**Format tabeli MONITORING** (prowadzonej w `mapa_dzu_YYYY-MM-DD.md`, sekcja osobna na końcu pliku):

| Akt | Dz.U. opubl. | Data wejścia w życie | Zastępuje / zmienia | Moduł DR | Status |
|---|---|---|---|---|---|
| Prawo budowlane art. 1 pkt 1 lit. a i c, pkt 3 *(przykład formatu — historyczny; w mocy od 20.09.2026, źródło zmiany: 2025/1847, nie t.j. 2026/524 — F-195)* | Dz.U. 2025 poz. 1847 | 20.09.2026 | — (przepis nowy) | dr-09/mod-PrBud-* | ✅ WSZEDŁ |
| Ordynacja podatkowa (część przepisów z Dz.U. 2025 poz. 1235) | Dz.U. 2026 poz. 622 | ~4 mies. od ogłoszenia | — (nowelizacja OP) | dr-06/mod-OP-* | ⏳ OCZEKUJE |
| Obrona cywilna zm. | Dz.U. 2026 poz. 646 | 29.05.2026 (ELI 2026-10-12) | Dz.U. 2024 poz. 1907 (część) | dr-13/mod-ustawa-zarzadzanie-kryzysowe-* | ✅ WSZEDŁ |
| Zarządzanie kryzysowe zm. (+ obrona cywilna art. 27, obrona Ojczyzny art. 23) | Dz.U. 2026 poz. 815 | 4.07.2026 (art. 73: 14 dni od ogłoszenia 19.06.2026) | Dz.U. 2026 poz. 574 t.j. (uchyla art. 5–6d, dodaje rozdz. 2–16); Dz.U. 2024 poz. 1907 (art. 5, 15, 38, 40, 44) | dr-01/mod-stany-nadzwyczajne-*, dr-08/mod-ustawa-zarzadzanie-kryzysowe, dr-13/mod-ustawa-zarzadzanie-kryzysowe-*, dr-13/mod-ustawa-obrona-ojczyzny-* | ✅ WSZEDŁ |

**Reguły statusów MONITORING:**

| Status | Znaczenie |
|---|---|
| ⏳ OCZEKUJE | Opublikowany, vacatio legis w toku — nie stosuj do zdarzeń wcześniejszych |
| ⚡ WCHODZI-90DNI | Data wejścia w ciągu 90 dni — zaktualizuj moduł przed tą datą |
| ✅ WSZEDŁ | Wszedł w życie — przesuń do tabeli głównej, usuń z MONITORING |
| ❌ UCHYLONY | Uchylony przed wejściem — usuń z MONITORING, odnotuj w AUDIT-JOURNAL |

**Przy wpisie do raportu (Faza 6)** dodaj sekcję `### 4B. MONITORING — akty oczekujące` z aktualnym stanem tabeli.

**Przy aktualizacji mapa_dzu (Faza 7B)** — tabela MONITORING jest aktualizowana razem z tabelą główną, na końcu pliku.

---

### 3C — Rozporządzenia "do weryfikacji"

Otwarte WARN z poprzednich audytów:
- WARN-4: Rozp. RM 2020.2437 (progi PZP) — dr-07
- WARN-5b: Rozp. MS 2015.1800 (stawki komornicze) — analizator-dowodow-v3
- WARN-6: Rozp. RM 2008.1656 (prace uciążliwe) — dr-16

Dla każdego: sprawdź online czy istnieje nowszy akt. Jeśli tak → CRIT. Jeśli nie → zamknij WARN jako "zweryfikowane, bez zmian".

---

## FAZA 3E — WERYFIKACJA TREŚCI MERYTORYCZNEJ MODUŁÓW (ZASADA 12)

> Odpowiada na pytanie: skoro FAZA 3A–3D wykryła zmianę numeru/statusu
> aktu — czy **treść** modułu DR, która o tym akcie coś twierdzi (progi,
> terminy, definicje, przesłanki), nadal jest zgodna z aktualnym stanem
> prawnym? To zakres inny niż poprawność numeru Dz.U. w mapie.

Pełna procedura: `modules/MOD-TRESC-MERYTORYCZNA.md` — wczytaj przed wykonaniem:

```
view audyt-systemu-v4/modules/MOD-TRESC-MERYTORYCZNA.md
```

> ⭐ **Mechanizm uzupełniający (dodany 2026-07-26):** gdy transza FAZA 3E
> ujawni, że MODUŁ SAM ostrzegał o nowelizacji, ale nie zastosował jej do
> własnej treści (wzorzec z AUDYT-2026-07-26l) — uruchom
> `modules/MOD-PROPAGACJA-NOWELIZACJI.md`, żeby sprawdzić, czy TA SAMA
> nieaktualność występuje też w INNYCH plikach systemu (nie tylko w
> module "domowym" dla danego aktu). Jedna naprawa punktowa nie
> gwarantuje, że problem nie powtarza się gdzie indziej.

**Uruchamia się automatycznie**, gdy FAZA 3 (dowolny podtryb) zakończyła
się co najmniej jedną zmianą: nowy `TJ` (3A/3B), pozycja `✅ WSZEDŁ` z
MONITORING (3D), lub WARN z 3C zamknięty jako "jest nowszy akt".

> ⭐ **Tryb NA ŻĄDANIE (dodane 2026-07-26):** FAZA 3E może być też
> wywołana samodzielnie, bez poprzedzającej zmiany Dz.U. — użytkownik
> wskazuje konkretny moduł/dziedzinę do pogłębionej weryfikacji
> merytorycznej ("sprawdź treść modułu X", "kontynuuj audyt
> merytoryczny"). W tym trybie KROK 1 (identyfikacja modułu) jest
> zastąpiony wskazaniem użytkownika lub wyborem audytora wg priorytetu
> (np. najnowsze/najmniej sprawdzone moduły) — reszta procedury
> identyczna. Każda taka transza to jeden fragment jednego pliku, nie
> cały system naraz — traktuj jako iteracyjne, nie jednorazowe zadanie.

Skrót procedury:
1. Zidentyfikuj moduł(y) DR opisujące dotknięty akt (kolumna `Moduł` w `MAPA-AKTOW.md`).
2. Ustal w ELI (`text.pdf` aktu zmieniającego) zakres zmiany — które artykuły dodano/zmieniono/uchylono (zakaz cytowania z pamięci — PRAWO-HARDGATE).
3. Skonfrontuj wyłącznie te twierdzenia modułu, które dotyczą zmienionych artykułów (nie cały moduł).
4. Sklasyfikuj: ✅ ZGODNE / ⚠️ WARN-TREŚĆ / ❌ CRIT-TREŚĆ.
5. CRIT-TREŚĆ → napraw treść modułu w tej samej sesji (str_replace na kopii), z adnotacją źródła i datą weryfikacji.

> ⚙️ Przy KROKU 2/3 stosuj ZASADĘ 14 (gradacja źródeł, patrz sekcja
> ZASADY KRYTYCZNE pkt 12 i `shared/HIERARCHIA-ZRODEL.md`) — Rząd 1
> pierwsza próba, Rząd 2B główne potwierdzenie gdy Rząd 1 niedostępny
> wprost, Rząd 3 wyłącznie jako dodatkowe potwierdzenie zbieżności.

Brak zmian Dz.U. w sesji → FAZA 3E pomijana, odnotuj wprost:
`FAZA 3E: pominięta — brak zmian Dz.U. w tej sesji` (NIE dotyczy trybu
NA ŻĄDANIE, który działa niezależnie od FAZA 3A-3D).

Wynik trafia do raportu jako `### 4C. TREŚĆ MERYTORYCZNA MODUŁÓW` (FAZA 6)
oraz — dla CRIT-TREŚĆ naprawionych — do `AUDIT-JOURNAL.md` z jawnym
odróżnieniem od poprawek czysto numeracyjnych (analogicznie do ZASADY 11
dla skilli proceduralnych).

# FAZA 4-7: testy antyhalucynacyjne, scoring, raport, aktualizacja references (przeniesione ze SKILL.md, treść bez zmian)


### 4A — Zakaz cytowania z pamięci

```bash
grep -r "Dz\.U\. [0-9]\{4\} poz\." "${LEX_MACHINA_SKILLS_ROOT:?}" \
  --include="*.md" | grep -v "isap\|weryfikuj\|MAPA\|mapa_dzu\|references\|archive" | head -30
```

Hardkodowane Dz.U. bez kontekstu weryfikacji = **WARN**.

### 4B — PRAWO-HARDGATE obecny

```bash
grep -r "PRAWO-HARDGATE" "${LEX_MACHINA_SKILLS_ROOT:?}" \
  --include="*.md" | grep -v archive | head -10
```

Brak HARDGATE w routerze = **CRIT**.

---

## FAZA 5 — SCORING

Dla każdego skilla generuj wynik 0–10:

| Kryterium | Waga | Punkty |
|-----------|------|--------|
| Brak błędów CRIT | 40% | 0–4 |
| Spójność zależności (ścieżki, wersje) | 25% | 0–2.5 |
| Description w limicie | 10% | 0–1 |
| Czystość kodu (interlinie + wstawki) | 15% | 0–1.5 |
| HARDGATE obecny (router) | 10% | 0–1 |

**Wynik < 6.0** = skill wymaga naprawy przed użyciem.
**Wynik ≥ 8.0** = skill zielony.

---

## FAZA 6 — RAPORT AUDYTU

Generuj raport wg szablonu z AUDIT-JOURNAL.md (sekcja "SZABLON NOWEGO WPISU").

Struktura wymaganego raportu:

```
## AUDYT-YYYY-MM-DD

### 1. STATUS OGÓLNY
### 2. NAPRAWY WYKONANE (CRIT)
### 3. OSTRZEŻENIA (WARN)
### 4. WERYFIKACJA Dz.U.
### 4C. TREŚĆ MERYTORYCZNA MODUŁÓW (FAZA 3E — patrz MOD-TRESC-MERYTORYCZNA.md)
### 5. STRUKTURA SYSTEMU — SNAPSHOT
### 6. WNIOSKI I ZALECENIA
```

---

## FAZA 7 — AKTUALIZACJA PLIKÓW REFERENCES ← OBOWIĄZKOWE

Po zakończeniu audytu **ZAWSZE** zaktualizuj pliki references (7A obowiązkowo,
7B i 7C warunkowo — wg opisu każdej podfazy):

### 7A — Aktualizacja AUDIT-JOURNAL.md

> ⛔ **KOREKTA 2026-08-15p — reguła doprowadzona do zgodności ze stanem faktycznym.**
> Ta sekcja nakazywała dotąd dopisywanie wpisu „na początku listy" i aktualizację
> stopki. Kontrola pliku wykazała, że **przez co najmniej 15 kolejnych sesji
> (wpisy 08-15a … 08-15o) wpisy były dopisywane na KOŃCU**, a stopka
> `*Ostatnia aktualizacja:*` nie była ruszana od **2026-06-09** i tkwi w połowie
> pliku (ok. w. 18383). Kolejność wpisów w pliku jest dziś mieszana (24 przejścia
> rosnące i 24 malejące na 698 wpisów) — nie jest ani chronologiczna, ani odwrotna.
>
> **Reguła z 2026-08-15p (nakazywała dopisywanie na KOŃCU PLIKU) — zastąpiona
> praktyką od 2026-10-04h.** Od wpisu AUDYT-2026-10-04h kolejne wpisy tworzą na
> końcu pliku blok w kolejności **od najnowszego** (10-10a, 10-09h, 10-09g, …,
> 10-04h); stan zmierzony 2026-10-10.
>
> **Stopki NIE reanimujemy jako pola do ręcznej aktualizacji** — była martwa
> przez ponad dwa miesiące, co dowodzi, że nikt jej nie utrzymuje. Datę ostatniego
> audytu odczytuje się z **najwyższego identyfikatora wpisu** (nie z pozycji
> w pliku). Istniejącą stopkę w połowie pliku pozostawiono jako artefakt
> historyczny z adnotacją.
>
> ⚠️ **Historyczne warianty (nieaktualne, zachowane dla zrozumienia starych wpisów):**
> wpisy sprzed sierpnia 2026 były wstawiane na początku listy; od 2026-08-15p do
> 2026-10-04g — na końcu pliku.

**Reguła kanoniczna (od 2026-10-04h):** nowy wpis `## AUDYT-YYYY-MM-DD[litera]`
wstaw **bezpośrednio PRZED dotychczas najnowszym wpisem** (najwyższy identyfikator;
dziś pierwszy wpis bloku malejącego przy końcu pliku), bez separatora `---`.
Litera po dacie rozróżnia kilka sesji tego samego dnia (a, b, c…). Nie oglądaj
całego pliku — wystarczą numery linii:

```bash
J=audyt-systemu-v4/references/AUDIT-JOURNAL.md
grep -n "^## AUDYT-$(date +%Y-%m-%d)" "$J"                     # wolna litera
N=$(grep -n '^## AUDYT-[0-9]' "$J" | LC_ALL=C sort -t' ' -k2,2 | tail -1 | cut -d: -f1)
sed -n "${N},$((N+15))p" "$J"                                  # kontrola miejsca
# nowy_wpis.md: treść wpisu zakończona jedną pustą linią
python3 - "$J" nowy_wpis.md "$N" <<'PY'
import sys
j, w, n = sys.argv[1], sys.argv[2], int(sys.argv[3])
linie = open(j, encoding="utf-8").read().split("\n")
nowe = open(w, encoding="utf-8").read().rstrip("\n").split("\n") + [""]
assert linie[n - 1].startswith("## AUDYT-"), "linia N nie jest nagłówkiem wpisu"
open(j, "w", encoding="utf-8").write("\n".join(linie[:n - 1] + nowe + linie[n - 1:]))
PY
grep -n '^## AUDYT-[0-9]' "$J" | LC_ALL=C sort -t' ' -k2,2 | tail -2   # nowy wpis = najwyższy
```
⛔ Nie wstawiaj wpisu na początku pliku, w środku ani za ostatnim wpisem bloku
malejącego. Nie używaj `str_replace` na całym pliku (ryzyko REGUŁY 5).

### 7B — Aktualizacja mapa_dzu_YYYY-MM-DD.md

Jeśli znaleziono nowe t.j. lub zmiany statusów Dz.U.:

> ⛔ **KOREKTA 2026-08-20y/2026-08-26 — ta sekcja kopiowała mapę ARCHIWALNĄ.**
> Polecenie wcześniej wskazywało datę na stałe, więc stawało się błędne przy
> każdej nowej generacji. Wykonanie
> FAZY 7B literalnie cofnęłoby mapę o **trzy generacje** (06-14 → 07-02 → 07-04 →
> 07-15), kasując ~250 wierszy ustaleń, i to bez żadnego sygnału błędu — nowy plik
> powstałby poprawnie, tylko z przestarzałą treścią. To DRUGIE wystąpienie tej samej
> klasy usterki: identyczną naprawę wykonano w 4.4 (2026-06-14g, „12 miejsc w SKILL.md,
> w tym FAZA 7B"). **Reguła stała: przy każdej zmianie mapy aktualnej sprawdź
> `grep -n mapa_dzu SKILL.md` i popraw WSZYSTKIE wystąpienia, nie tylko `references:`.**

1. Utwórz nową wersję pliku z datą bieżącą. Źródłem jest wyłącznie
   `AKTUALNA_MAPA_DZU` ustalona dynamicznie w FAZIE 0:
```bash
cp "$AKTUALNA_MAPA_DZU" \
   audyt-systemu-v4/references/mapa_dzu_YYYY-MM-DD.md
```

2. Zaktualizuj w nowym pliku:
   - Nagłówek: `**Data weryfikacji:** YYYY-MM-DD`
   - Zmień statusy `OK` → `PREV` dla zastąpionych t.j.
   - Dodaj nowe wiersze do tabeli (na początku, sortuj malejąco po roku/poz.)

3. Zaktualizuj wpis mapy aktualnej w `references:`. Procedura FAZY 0 i FAZY 3
   pozostaje dynamiczna — nie wolno dopisywać tam nowej daty na stałe.

Jeśli **brak zmian Dz.U.** — plik mapy pozostaje bez zmian, odnotuj w AUDIT-JOURNAL.md:
```
Dz.U.: brak nowych t.j. — mapa bez zmian (ostatnia: [nazwa AKTUALNA_MAPA_DZU])
```

### 7C — Aktualizacja WARN-OTWARTE.md (ZASADA 10)

> ⛔ **ZMIANA 2026-08-20y — ta sekcja była MARTWA od 2026-06-14g.** Nakazywała
> aktualizację pliku `SKILLS-MAP-AND-FIXES`, USUNIĘTEGO w wersji 4.4 i zastąpionego
> przez `CHANGELOG.md` / `CHECKLIST-DEDUP.md` / `mapa_dzu`. Przez ~2 miesiące FAZA 7
> deklarowała trzy podfazy, z których jedna nie miała przedmiotu (stąd też sprzeczność
> w zdaniu wprowadzającym: „zaktualizuj **oba** pliki references" przy trzech
> podsekcjach). W to miejsce wpisano czynność, która i tak jest obowiązkowa z ZASADY 10,
> a nie miała własnego kroku w FAZIE 7 — co było drugą, cichszą luką tej samej sekcji.

Po każdej sesji, w której odkryto lub zamknięto flagę:

1. **Flaga nowa** → wiersz w TABLICY STERUJĄCEJ + wiersz w sekcji 1
   `references/WARN-OTWARTE.md` + wpis w `AUDIT-JOURNAL.md`.
2. **Flaga zamknięta** → USUŃ wiersz z obu miejsc w `WARN-OTWARTE.md`, pełny opis
   naprawy dopisz do `AUDIT-JOURNAL.md`.
3. **Naprawa częściowa** → SKRÓĆ wiersz flagi do tego, co ZOSTAŁO (nie dopisuj opisu
   tego, co zrobione — to jedyne udokumentowane źródło rozrostu tego pliku, F-86).
4. Zaktualizuj licznik flag w TABLICY STERUJĄCEJ oraz „kolejny wolny numer" w § 8.

Jeśli zmieniła się struktura katalogu skilla — zaktualizuj sekcję STRUKTURA KATALOGU
w tym pliku ORAZ `references:`/`scripts:` w YAML (wzorzec luki F-80).
