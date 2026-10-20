---
name: analizator-przepisow-v2
version: "2.12"
type: executive-analiza
status: production
compatibility: "live_web_lookup, file_read, optional_interactive_ui"
description: "Analiza przepisów prawa polskiego: brzmienie aktualne i historyczne, przesłanki, wykładnia, orzecznictwo, zbieg norm, nowelizacje i vacatio legis."
dependencies:
  requires:
    - shared
  # 2026-09-27e: jawna zależność (każdy skill systemu korzysta z `shared`); pole czytane przy imporcie z marketplace
---

> **Universal runtime:** przed wykonaniem zastosuj kanoniczny `shared/UNIVERSAL-RUNTIME-ADAPTER.md` z osobnego skilla `shared`. Lokalna sekcja adaptera poniżej jedynie go doprecyzowuje.


## ADAPTER RUNTIME — PORTABILITY (ChatGPT / Claude / inne hosty)

Ta sekcja zmienia wyłącznie sposób wykonania operacji technicznych. Nie zmienia hard gate’ów, hierarchii źródeł, analizy przesłanek, logiki orzeczniczej, historii zmian ani modelu vacatio legis.

1. `view`, `web_search`, `web_fetch`, `show_widget`, `sendPrompt` i podobne nazwy traktuj jako nazwy operacji semantycznych, jeżeli bieżący host nie udostępnia literalnie narzędzia o tej nazwie. Użyj równoważnej funkcji hosta.
2. `view analizator-przepisow-v2/...` oznacza świeży odczyt odpowiedniego pliku lokalnego tego skilla, przede wszystkim `references/...`. Nie wymagaj literalnego katalogu `/mnt/skills`.
3. `view shared/<plik>` oznacza świeży odczyt z osobnego, kanonicznego skilla `shared`. NIE kopiuj `shared` do tej paczki. Jeżeli obowiązkowy zasób shared jest niedostępny, zastosuj fail-closed zamiast zastępować go pamięcią modelu.
4. `web_search` / `web_fetch` oznaczają świeże wyszukanie i odczyt zewnętrznego źródła. Dla przepisów i sygnatur zachowaj istniejący wymóg źródeł oficjalnych/urzędowych i zakaz cytowania z pamięci.
5. `show_widget` oznacza interaktywny widok, jeśli host go obsługuje. Jeżeli nie, zachowaj ten sam model danych, zakładki, drzewo przesłanek i funkcje jako ustrukturyzowany raport, HTML lub natywny artefakt hosta. Brak renderera nie może blokować analizy merytorycznej.
6. `sendPrompt(...)` w opisie widgetu oznacza przekazanie wybranych przez użytkownika parametrów z UI z powrotem do bieżącej rozmowy/zadania. Jeśli host nie ma takiego callbacku, pokaż gotowe polecenie lub użyj natywnego mechanizmu interakcji hosta.
7. Odwołania do innych skilli są integracjami między-skillowymi. Nie kopiuj ich do tej paczki; jeśli integracja nie jest dostępna, wykonaj lokalną część możliwą do wykonania i jawnie oznacz pominięty krok bez wymyślania wyniku.

**Zasada nadrzędna adaptera:** jeżeli istniejąca instrukcja jest zrozumiała i wykonalna przez bieżący host, wykonaj ją bez konwersji. Adapter działa tylko na rzeczywistej granicy runtime.
# Analizator Przepisów Prawnych v2

> ⛔ HARD GATE — ZAKAZ CYTOWANIA PRAWA I ORZECZEŃ Z PAMIĘCI
> Przed podaniem jakiegokolwiek przepisu, artykułu, numeru Dz.U. lub sygnatury orzeczenia:
> `view shared/PRAWO-HARDGATE.md`

> ⛔ **SELF-CHECK ANTY-FASADA — obowiązkowy przed wysłaniem odpowiedzi/pisma**
> (podłączone 2026-08-23i, flaga F-115 — ten skill cytuje prawo, a bramki nie miał):
>
> ```
> view shared/SELF-CHECK-ANTY-FASADA.md
> ```
>
> Sprawdza dwie rzeczy: (1) czy w tekście stoi „zweryfikowano", data weryfikacji
> albo URL przy przepisie, dla którego NIE wywołano narzędzia W TEJ ODPOWIEDZI;
> (2) czy znacznik statusu nie został nadany treści WYGENEROWANEJ w tej odpowiedzi
> (AF-6). Treść listy jest w module, nie tutaj — celowo, żeby nie powstało kolejne
> miejsce dryfu (7 wcześniejszych kopii rozjechało się ze źródłem przy pierwszej
> zmianie brzmienia).

Profesjonalne narzędzie do analizy przepisów prawnych z widgetem wizualnym, automatycznym orzecznictwem (MOD-ORZECZ-PRZEPIS), mapą powiązań norm, historią zmian z obsługą vacatio legis, interaktywnym drzewem przesłanek i kontekstem praktycznym dla laika. (v2)

---

## ZASADA NACZELNA

> ⛔ HARDGATE — Nigdy nie cytuj przepisów z pamięci. Każdy przepis MUSI być pobrany według kanonu E-1…E-5 (`shared/HIERARCHIA-ZRODEL.md`): najpierw ELI (RZĄD 1), ISAP wyłącznie jako adres dla człowieka, LEX/Legalis → ArsLege, gdy aktu nie da się pobrać z RZĘDU 1 — procedura w `shared/PRAWO-HARDGATE.md`. Jeśli wszystkie źródła niedostępne — oznacz `⚠️ [NIEWERYFIKOWANE]` i kontynuuj bez treści przepisu.

---

## MODUŁ 0 — INTAKE I ROUTING

### Krok 0.1 — Zbierz dane wejściowe

| Element                | Przykład                             | Wymagany? |
|------------------------|--------------------------------------|-----------|
| Identyfikator przepisu | art. 415 KC / § 3 ust. 2 pkt 1 uVAT | TAK       |
| Data analizy           | dziś / 1.01.2020 / przed nowelizacją | TAK       |
| Typ sprawy             | cywilna / karna / admin / pracownicza| TAK       |
| Stan faktyczny         | opis sytuacji, dokumenty, fakty      | TAK       |
| Strona analizująca     | powód / pozwany / oskarżony / organ  | zalecane  |
| Cel analizy            | obrona / atak / zgodność / wykładnia | zalecane  |

### Krok 0.2 — Wybierz ścieżkę analizy

```
A) Jeden przepis + stan faktyczny   → Moduł 1 → 2 → 3 → 7A → 7C → 4 → WIDGET
B) Wiele przepisów / zbieg norm     → Moduł 1 → 2 → 3 → 7A → 7B → 7C → 4 → 5 → WIDGET
C) Stan prawny na datę historyczną  → Moduł 1H → 2 → 7C → 4 → WIDGET
D) Linia orzecznicza przepisu       → Moduł 1 → 7 → 7A
E) Tylko wyjaśnienie przepisu       → Moduł 1 → 2 → 7D → Raport uproszczony
F) Brak danych od użytkownika       → WIDGET WYBORU PRZEPISU → potem A–E
G) Użytkownik-laik (wykryty)        → +7D (kontekst praktyczny) do każdej ścieżki
H) Przepis z odesłaniem do innych   → +7B (mapa powiązań) do każdej ścieżki
```

### Krok 0.3 — WIDGET WYBORU PRZEPISU

Uruchom gdy: użytkownik nie podał przepisu, pyta o "widget wyboru", "wyszukaj przepis" lub wpisał tylko kodeks bez artykułu.

#### Szablon gotowy (host z `show_widget` czytającym plik korpusu)

`show_widget(path="analizator-przepisow-v2/assets/widget-wybor-przepisu.html")` — formularz bez danych sprawy, spełnia specyfikację niżej; przycisk wysyła polecenie analizy przez `sendPrompt`.

<!-- lex:wykonuje-aplikacja: WIDGET-DANE -->
#### Specyfikacja do samodzielnego wygenerowania (host bez szablonu)

Wygeneruj interaktywny widget HTML (CSS i JS inline) z następującymi elementami:

NAGŁÓWEK: ikona ⚖️, tytuł "Analizator Przepisów Prawnych v2"

SEKCJA 1 — IDENTYFIKACJA PRZEPISU:
- SELECT "Kodeks / Akt prawny" z grupami optgroup:
  - Prawo cywilne: KC, KPC, KRO, KSH
  - Prawo karne: KK, KPK, KKW, KW, KPW
  - Prawo administracyjne: KPA, PPSA, OP
  - Prawo pracy: KP
  - Inne ustawy: uVAT, uPIT, uCIT, PrBud, RODO, UODO, inne (pole tekstowe)
- INPUT TEXT "Numer artykułu" z podglądem na żywo obok pola (np. "art. 415 KC")
  - Obsługuje: zwykły numer (415), indeks (23¹), paragraf (§ 3 ust. 2 pkt 1)
  - Placeholder: "np. 415 lub 23 ust. 1 pkt 2"
- Szybkie przyciski-badge z popularnymi artykułami per kodeks:
  - KC: 415, 471, 448, 23, 446
  - KPC: 840, 843, 189, 193, 730
  - KK: 278, 286, 190, 193, 177
  - KP: 52, 55, 183a, 94
  - KRO: 56, 58, 61¹

SEKCJA 2 — PARAMETRY (dwie kolumny):
- SELECT "Cel analizy": czy stosuje się / wykładnia przesłanek / linia orzecznicza / stan historyczny / zbieg norm / tryb karny / tryb administracyjny / pełna analiza
- SELECT "Typ sprawy": cywilna / karna / administracyjna / pracownicza / podatkowa / gospodarcza

SEKCJA 3 — DATA STANU PRAWNEGO:
- Checkbox "Data historyczna" → odkrywa date picker
- Tekst: "Stan prawny: aktualny (dziś)" lub "Stan prawny: historyczny [data]"

SEKCJA 4 — STAN FAKTYCZNY:
- TEXTAREA opcjonalne, placeholder "Opisz swoją sytuację..."

PRZYCISK "🔍 Analizuj przepis":
- Disabled gdy brak kodeksu lub artykułu
- onClick → sendPrompt("Analizuj [kodeks] art. [artykuł]. Cel: [cel]. Typ sprawy: [typ]. Stan prawny na: [data]. Stan faktyczny: [treść lub brak]")
- Fallback gdy brak sendPrompt → alert z gotowym promptem

Paleta: --primary #1B3A6B, --accent #C8960C, --bg #F8F7F4, --success #16a34a, --danger #dc2626, --warn #d97706. Czcionka: Segoe UI lub system-ui. Responsywny, min-width 320px.

---

## MODUŁ 1 — WERYFIKACJA I POBRANIE PRZEPISU
- **Hierarchia źródeł (RZĄD 1 / RZĄD 2 / RZĄD 3)** — kanon w `shared/HIERARCHIA-ZRODEL.md`; wczytaj PRZED podaniem jakiegokolwiek linku/URL.
- **Procedura weryfikacji (OBOWIĄZKOWA)** — kanon E-1…E-5 (ELI i dalsze źródła), ZAWSZE, BEZ WYJĄTKU.
- **Karta Przepisu** — format wyniku weryfikacji.

## MODUŁ 1H — STAN PRAWNY NA WYBRANĄ DATĘ
Gdy użytkownik bada przepis w stanie na konkretną datę przeszłą; wynik: Raport historyczny (analiza zmian przepisu w czasie).

**WCZYTAJ (obowiązkowo, fail-closed):** view analizator-przepisow-v2/references/modul-1-1h-weryfikacja-historia.md
Plik MUSI być przeczytany przed wykonaniem Modułu 1 (krok 2 sekwencji) i Modułu 1H.
---

## MODUŁ 2 — DEKOMPOZYCJA PRZESŁANEK
Klasyfikacja struktury logicznej, Drzewo Przesłanek (DRZEWO-LIMIT: model analityczny oparty na pobranym tekście), weryfikacja pojęć nieostrych, wykładnia orzecznicza pojęć nieostrych.

## MODUŁ 3 — ANALIZA SPEŁNIENIA PRZESŁANEK
Gdy jest stan faktyczny: matryca oceny, analiza szczegółowa przesłanki N lub ?, wynik logiczny.

**WCZYTAJ (obowiązkowo, fail-closed):** view analizator-przepisow-v2/references/modul-2-3-przeslanki.md
Plik MUSI być przeczytany przed wykonaniem Modułu 2 (krok 3 sekwencji) i Modułu 3 (krok 4).
---

## MODUŁ 4 — RAPORT KOŃCOWY
Format raportu analizy przepisu (krok 10 sekwencji).

## MODUŁ 5 — ZBIEG NORM
Porównanie przepisów, gdy analiza dotyczy wielu przepisów (krok 11).

## MODUŁ 6 — TRYBY SPECJALNE
Tryb A — przepis karny; Tryb B — przepis administracyjny; Tryb C — przepis proceduralny (KPC/KPK/PPSA) (krok 12).

**WCZYTAJ (obowiązkowo, fail-closed):** view analizator-przepisow-v2/references/modul-4-6-raport-zbieg-tryby.md
Plik MUSI być przeczytany przed wydaniem raportu końcowego (Moduł 4) oraz przed Modułem 5 lub 6.
---

## MODUŁY 7–8 — ORZECZNICTWO, MAPA POWIĄZAŃ, HISTORIA ZMIAN, KONTEKST DLA LAIKA, WIDGET WYNIKÓW

Wyodrębnione do osobnego pliku referencyjnego (refaktoryzacja 2026-06-14 — eliminacja monolitu 794 linii):

```
view analizator-przepisow-v2/references/MOD-ORZECZ-POWIAZANIA-HISTORIA.md
```

Zawiera:
- **Moduł 7** — Linia orzecznicza (wyszukiwanie i analiza stanowisk SN/NSA/TK/SA/WSA)
- **Moduł 7A** — MOD-ORZECZ-PRZEPIS (automatyczne pobranie 3 orzeczeń do przepisu)
- **Moduł 7B** — MOD-ZBIEZNOSC (mapa powiązań norm)
- **Moduł 7C** — MOD-HISTORIA-ZMIAN + MOD-VACATIO-LEGIS (nowelizacje, vacatio legis — odsyła dalej do `references/MOD-VACATIO-LEGIS.md`)
- **Moduł 7D** — MOD-KONTEKST-PRAKTYCZNY (wyjaśnienie dla laika)
- **Moduł 8** — Widget wyników HTML (7 zakładek)

Wczytaj ten plik na etapie 5–9 i 13 sekwencji obowiązkowej (patrz INSTRUKCJE OPERACYJNE poniżej).

---

---

## MODUŁ 9 — INTEGRACJA Z SYSTEMEM SKILLÓW

| Wynik analizy                           | Proponowany skill       |
|-----------------------------------------|-------------------------|
| Przepis stosuje się → chcę pismo        | pisma-procesowe-v3      |
| Brak dowodów na przesłanki              | analizator-dowodow-v3   |
| Pojęcia nieostre, linia niejednoznaczna | orzeczenia-sadowe-v2    |
| Złożona sprawa, wiele przepisów         | analiza-sadowa-v6       |
| Użytkownik zagubiony w wynikach         | przewodnik-prawny-v2    |
| Linia niejednolita ⚠️ — chcę więcej    | orzeczenia-sadowe-v2    |
| Zbieg norm — chcę mapę powiązań         | analiza-sadowa-v6       |

---

## INSTRUKCJE OPERACYJNE

### Sekwencja obowiązkowa

```
1. Moduł 0 → intake + routing
   Jeśli brak przepisu → Widget wyboru przepisu (Moduł 0.3)
2. Moduł 1 → pobierz przepis z ELI — kanon E-1…E-5 (ZAWSZE, BEZ WYJĄTKU)
   Lub Moduł 1H → tryb historyczny
3. Moduł 2 → dekompozycja przesłanek
4. Moduł 3 → analiza spełnienia (jeśli jest stan faktyczny)
5. Moduł 7 → linia orzecznicza (pojęcia nieostre lub żądanie)
6. Moduł 7A → MOD-ORZECZ-PRZEPIS (AUTOMATYCZNIE — 3 orzeczenia + alert rozbieżności)
7. Moduł 7B → MOD-ZBIEZNOSC (jeśli przepis odsyła lub ścieżka B)
8. Moduł 7C → MOD-HISTORIA-ZMIAN (AUTOMATYCZNIE — w tle, wynik w zakładce widgetu)
   8a. Jeśli wykryto vacatio legis lub nowelizację wieloetapową → MOD-VACATIO-LEGIS
       `view analizator-przepisow-v2/references/MOD-VACATIO-LEGIS.md`
9. Moduł 7D → MOD-KONTEKST-PRAKTYCZNY (gdy laik lub żądanie wyjaśnienia)
10. Moduł 4 → raport końcowy
11. Moduł 5 → zbieg norm (jeśli wiele przepisów)
12. Moduł 6 → tryb specjalny (karny / admin / proceduralny)
13. Moduł 8 → Widget wyników z 7 zakładkami (zawsze po analizie) — wykonanie: „Moduł 8 — wykonanie widgetu” niżej
14. Moduł 9 → propozycja kolejnych skillów
```

#### Moduł 8 — wykonanie widgetu: szablon zasilany danymi (host z `show_widget` przyjmującym `data`)

`show_widget(path="analizator-przepisow-v2/assets/widget-wyniki.html", data=DANE)` — bez kodu; host wstawia dane i dokłada pasek eksportu/importu. Zakładki i funkcje jak w `references/MOD-ORZECZ-POWIAZANIA-HISTORIA.md` § MODUŁ 8. DANE (pola opcjonalne można pominąć):
```
przepis: {oznaczenie, akt, tresc, status: obowiazuje|zmieniony|uchylony, stan_na, url, w_praktyce, os_czasu: [{data, opis}]}
przeslanki: {logika: AND|OR|MIXED, lista: [{id, nazwa, status: T|N|?, pewnosc 0–100, uzasadnienie, braki}]}
wynik: {ocena: stosuje|nie_stosuje|watpliwe, opis}
orzeczenia: {jednolita: true|false, rozbieznosc: {a, b, przyczyna, rekomendacja},
             lista: [{sygnatura, sad, rok, teza, url, trafnosc 0–100, tier: 1|2|3}]}
powiazania: [{artykul, akt, relacja: odeslanie|wyjatek|lex_specialis|uzupelnienie|definicja, opis}]
historia: [{data, akt_zmieniajacy, opis, istotnosc: wysoka|niska}]; porownanie: {poprzednia, aktualna}
raport: {konkluzja, kolor: zielony|czerwony|pomaranczowy, pewnosc 0–100, ryzyka: [], rekomendacje: [], dla_ciebie}
```
Zasady treści bez zmian: brzmienie z ELI, statusy źródeł, sygnatury wyłącznie zweryfikowane.

<!-- lex:wykonuje-aplikacja: WIDGET-DANE -->
#### Moduł 8 — wykonanie widgetu: kod HTML i pasek IO (host bez pola `data`)

Wygeneruj widget wg `references/MOD-ORZECZ-POWIAZANIA-HISTORIA.md` § MODUŁ 8. Przed `show_widget`:
```
⛔ MOD-WIDGET-IO (OBOWIĄZKOWE przed show_widget):
view shared/MOD-WIDGET-IO.md
→ wbuduj pasek IO w nagłówek widgetu
→ IO_SKILL_ID='analizator-przepisow-v2', IO_CASE_ID=sygnatura_lub_przepis
→ matryca: Export JSON ✅ MD ✅ | Import JSON ✅
```

### Poziomy pewności

| Poziom | %     | Kryterium                                           |
|--------|-------|-----------------------------------------------------|
| Wysoka | 80–100| Materiały jednoznacznie i bezpośrednio potwierdzają |
| Średnia| 50–79 | Pośrednie wskazanie, możliwa inna interpretacja     |
| Niska  | <50   | Brak materiałów lub wzajemna sprzeczność            |

### Cytowanie orzeczeń

- Nigdy sygnatur z pamięci AI
- Format: [Sąd], [data], sygn. [sygnatura], [teza skrócona]
- Link do źródła oficjalnego obowiązkowy

### Postępowanie przy braku dostępu do źródeł (kanon E-1…E-5)

```
Brak dostępu do ISAP = stan normalny (kanał maszynowy martwy) — NIE przerywa
pracy i NIE uruchamia źródeł zastępczych; brzmienie bierzesz z ELI.
ELI niedostępny → sprawdź kształt żądania (DOSTEP-MASZYNOWY-API §1), drugi
kanał (web_fetch/B-1→B-2 ↔ kanał kodu), ISAP / dziennikustaw.gov.pl; zapisz
wynik prób. Aktu nie da się pobrać z RZĘDU 1 → obowiązkowo kolejno: E-3 LEX/Legalis (przy licencji) → E-4 ArsLege
(🟨 na warunkach K-1…K-4). Prawo UE → EUR-Lex; akty organu → BIP / dziennik
urzędowy.
Jeśli wszystkie niedostępne (E-5):
  ZATRZYMAJ analizę
  Poinformuj użytkownika
  Zaproponuj dostarczenie tekstu przez użytkownika
  NIE analizuj z pamięci AI
```

---

## PRZYKŁAD

Zapytanie: "Czy art. 415 KC stosuje się do mojej sprawy? Stan na 1.01.2020."

```
[M0]  Ścieżka C — historyczna
[M1H] Pobrano ELI DU/2019/1145 (text.pdf), stan na 01.01.2020
[M2]  Koniunkcja: P1 Szkoda | P2 Wina | P3 Związek przyczynowy
[M3]  P1 T 90% | P2 ? 55% (brak protokołu) | P3 T 80%
[M7]  SN: "wina" — wykładnia obiektywna (sygn. zweryfikowana)
[M7A] 3 orzeczenia pobrane z saos.org.pl + sn.pl — LINIA NIEJEDNOLITA ⚠️
      Stanowisko A (dominujące SN): subiektywna miara staranności
      Stanowisko B (mniejszościowe SA): obiektywny wzorzec "dobrego gospodarza"
      Przyczyna: różna wykładnia pojęcia "wina" przed uchwałą SN z 2018
[M7C] Przepis bez zmian w ostatnich 3 latach ✅
[M4]  KONKLUZJA: ? NIEJEDNOZNACZNY — blokuje P2, ryzyko linii niejednolitej
[M7D] Dla laika: "Przepis mówi, że kto wyrządził komuś szkodę przez własną winę,
      musi ją naprawić. Tu kwestią sporną jest, czy winę oceniamy przez Twoje
      zamierzenia czy przez to, co zrobiłby 'rozsądny człowiek' na Twoim miejscu."
[M8]  Widget wyników z 7 zakładkami.
```

---

## Integracja z kancelaryjnym jądrem shared

Jeżeli wynik tego skilla ma służyć do pisma, strategii procesowej, oceny ryzyka albo decyzji terminowej, wczytaj właściwe moduły shared:

```text
view shared/TRYBY-PROCESOWE.md
view shared/RISK-ASSESSMENT.md
view shared/TERM-CALC.md
view shared/DOWODY-METODOLOGIA.md
view shared/PREKLUZJA-DOWODOWA.md
view shared/STRATEGIA-PROCESOWA.md
view shared/QUALITY-CHECK.md
```

Nie dubluj logiki shared w lokalnych plikach. Lokalne moduły mogą tylko doprecyzować analizę dziedzinową.
