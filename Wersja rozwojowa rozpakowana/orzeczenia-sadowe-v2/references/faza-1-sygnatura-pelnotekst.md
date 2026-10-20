# Faza 1-S (V-SYG-0) i Faza 1-T (wyszukiwanie pełnotekstowe) — orzeczenia-sadowe-v2

> Plik przeniesiony ze SKILL.md bez zmian treści (progressive disclosure). Wczytaj w całości przed wykonaniem odpowiedniego kroku.

## Faza 1-S — Kontrola istnienia sygnatury (V-SYG-0)

> Wykonuje się **PRZED Fazą 1-T i przed każdym powołaniem sygnatury**, także
> sygnatury podanej przez użytkownika.

```
view shared/SYGNATURY.md
view shared/DOSTEP-MASZYNOWY-API.md §3
```

Skrót operacyjny; kanoniczny kontrakt statusów pozostaje w `shared/SYGNATURY.md`:

1. **Normalizuj** — pojedyncze spacje, bez kropek w repertorium, spacje wokół
   `/` nieistotne. Nie uzupełniaj brakującej izby, repertorium, numeru ani
   rocznika.
2. **Routuj po repertorium.**
   - sądy powszechne → `orzeczenia.ms.gov.pl`;
   - SN → `sn.pl` / `snproxy`;
   - **NSA/WSA → wykonaj świeżą próbę bezpośredniego CBOSA**.
     Gdy `orzeczenia.nsa.gov.pl` odpowiada właściwym HTML-em:
     ```
     view shared/CBOSA-ADAPTER.md
     → POST /cbo/search
     → zachowaj cookies
     → jeśli potrzeba GET /cbo/find?p=N
     → GET /doc/{ID} dla KAŻDEGO kandydata
     → tools/cbosa_parser.py (gdy host ma wykonanie kodu)
     ```
     Gdy direct CBOSA jest niedostępna → zastosuj V-SYG-0.5 z
     `shared/SYGNATURY.md`.
3. **Okno pokrycia** — zero trafień można zamienić na `NOT_FOUND` wyłącznie
   w źródle, którego pokrycie obejmuje badany sąd/okres i gdy wynik został
   pobrany kompletnie. Poza pokryciem lub przy awarii → `OUT_OF_SCOPE`.
4. **Post-check tożsamości — filtruj cały zbiór, nie pierwszy rekord.**
   Po normalizacji zachowaj wyłącznie dokumenty o sygnaturze dokładnie tożsamej
   z pytaną, a pozostałe zapisz jako `rejected_case_numbers` /
   `odrzucone_post_checkiem`:
   - 0 exact-match → `NOT_FOUND`;
   - 1 exact-match → `FOUND`;
   - ≥2 exact-match → `AMBIGUOUS`.
   Przykład klasy błędu: „blisko pasująca” inna izba/repertorium/rok nie może
   zostać automatycznie podstawiona.
5. **CBOSA jest fail-closed.** Jeżeli licznik wyników wskazuje więcej rekordów niż
   pobrano z bieżącej strony, pobierz pozostałą paginację w tej samej sesji.
   Niepełna paginacja, zmiana HTML lub błąd choć jednego `/doc/{ID}` =
   `OUT_OF_SCOPE`, nie `NOT_FOUND`.
6. **Zakres potwierdzenia.**
   - direct CBOSA + odczyt `/doc/{ID}` → `FOUND`,
     **ISTNIENIE+TREŚĆ** tylko w zakresie faktycznie odczytanym. Metryka i
     sentencja są obowiązkowe; uzasadnienie ma osobny flag
     `reasoning_available`. Gdy `false` → zakaz przypisywania tezy z
     uzasadnienia, mimo że samo orzeczenie pozostaje FOUND;
   - V-SYG-0.5 RETRIEVAL/SNAPSHOT → `FOUND` po POST-CHECK HOSTA i exact-match;
     zachowaj faktyczny `content_scope` (metryka+sentencja / uzasadnienie częściowe
     / pełne) do researchu. Provenance = `CRAWLED_OR_INDEXED`; bez niezależnego
     direct potwierdzenia nie oznaczaj ✅ [VER];
   - `FRAGMENT` dopiero po wskazaniu konkretnego miejsca zgodnie z
     `shared/WERYFIKACJA-SLAD.md` i Zasadą 2B.

⛔ Tylko `FOUND` otwiera możliwość powołania. `NOT_FOUND` i `OUT_OF_SCOPE`
nigdy nie są raportowane jako „potwierdzone”. `AMBIGUOUS` wymaga przedstawienia
kandydatów lub dalszego zawężenia, bez arbitralnego wyboru.

---

## Faza 1-T — Wyszukiwanie pełnotekstowe po treści tezy (SAOS API + CBOSA)

Uzupełnienie Fazy 1 — stosuj PRZED klasycznym wyszukiwaniem frazowym, gdy celem jest
„znajdź tezę" (dosłowne sformułowanie prawne w uzasadnieniu/sentencji), nie tylko
„znajdź orzeczenie w danym temacie". `web_search` nie przeszukuje treści uzasadnień —
trafia wyłącznie tam, gdzie fraza już została zacytowana na zaindeksowanej stronie
(np. w artykule prawniczym). SAOS i CBOSA indeksują pełny tekst orzeczeń bezpośrednio
i pozwalają przeszukać go wprost.

### 1-T.1 — SAOS REST API (zapytanie bezpośrednie do API, nie przez wyszukiwarkę web)

Punkt wejścia: `https://www.saos.org.pl/api/search/judgments`

⛔⛔ **NAJPIERW Faza 1-S (kontrola istnienia), potem 1-T (wyszukiwanie treści).**
Te dwie operacje używają RÓŻNYCH parametrów i mylenie ich jest trybem awarii:
`all=III CZP 999/11` na fabrykacie zwraca **67 576 trafień**, `caseNumber=III CZP 999/11`
zwraca **0**. Faza 1-T służy do znalezienia TREŚCI, nigdy do potwierdzenia BYTU
sygnatury.

Kluczowe parametry (dowolna kombinacja, doklejane jako query string):
```
caseNumber=SYGNATURA     → ⭐ DOKŁADNE dopasowanie sygnatury (kontrola istnienia,
                            nie wyszukiwanie). Wielkość liter bez znaczenia;
                            białe znaki — istotne. Patrz Faza 1-S.
all=FRAZA                → pełnotekstowe przeszukanie treści/tezy/uzasadnienia.
                            Obsługuje język zapytań: "fraza w cudzysłowie" (dokładna
                            kolejność słów), -słowo (wyklucza), A OR B.
judgmentDateFrom / judgmentDateTo   → filtr dat, format yyyy-MM-dd
courtType                → COMMON | SUPREME | ADMINISTRATIVE | CONSTITUTIONAL_TRIBUNAL
                            | NATIONAL_APPEAL_CHAMBER
                            ⛔ okno pokrycia jest NIERÓWNE — patrz Faza 1-S
ccCourtType               → APPEAL | REGIONAL | DISTRICT (tylko sądy powszechne)
ccCourtName                → nazwa konkretnego sądu
judgmentTypes              → SENTENCE | RESOLUTION | DECISION | REGULATION | REASONS
keywords                  → lista haseł tematycznych SAOS
sortingField / sortingDirection, pageSize / pageNumber → paginacja/sortowanie
```

Procedura:
```
1. web_fetch: https://www.saos.org.pl/api/search/judgments?all=FRAZA+TEZY&courtType=...
   &judgmentDateFrom=...&judgmentDateTo=...&pageSize=10
2. Z odpowiedzi JSON odczytaj per trafienie: caseNumber, judgmentDate,
   division.court.name (lub chambers dla SN), fragment textContent zawierający frazę, href.
3. To jest ETAP WYSZUKANIA KANDYDATÓW, nie weryfikacji — saos.org.pl nadal pełni
   wyłącznie rolę wsparcia (Zasada 5) → przejdź do 1-T.3 przed powołaniem sygnatury.
```
⚠️ SAOS to projekt akademicki (ICM UW) — pokrycie nie jest wyczerpujące. Zasięg
zmierzony: sądy powszechne bieżąco, SN do 2016, TK do 2015, KIO do 2018, NSA/WSA brak
(Faza 1-0) — dla nowszych SN/TK/KIO i dla NSA/WSA nie używaj SAOS do wyszukiwania.
Traktuj trafienie jako trop, nie jako potwierdzenie.

### 1-T.2 — CBOSA (NSA/WSA) — formularz HTML + pełny tekst

CBOSA nie wymaga publicznego REST/JSON API, aby działać jako deterministyczne
źródło Tier 1. Aktualny kontrakt integracyjny znajduje się w:

```
view shared/CBOSA-ADAPTER.md
```

Dla wyszukiwania po sygnaturze adapter ma zweryfikowany kontrakt:

```text
POST https://orzeczenia.nsa.gov.pl/cbo/search
Content-Type: application/x-www-form-urlencoded

wszystkieSlowa=
wystepowanie=gdziekolwiek
odmiana=on
sygnatura={SYGNATURA}
sad=dowolny
rodzaj=dowolny
symbole=
odDaty=
doDaty=
sedziowie=
funkcja=
submit=Szukaj
```

Pierwszy POST zwraca stronę 1 i może ustanowić sesję. Zachowaj cookies; kolejne
strony pobieraj przez `GET /cbo/find?p=N`. Z każdego wyniku wyciągaj wyłącznie
`/doc/{10-znakowy-ID}`, a następnie odczytaj każdy dokument przez
`GET /doc/{ID}`.

Jeżeli host ma wykonanie kodu, użyj:

```
tools/cbosa_parser.py
```

Parser:
- wyciąga i deduplikuje `/doc/{ID}`,
- odczytuje sygnaturę, sąd, datę, sentencję i — gdy opublikowane — uzasadnienie,
- zwraca `reasoning_available`, aby brak uzasadnienia nie był mylony z pełną treścią,
- normalizuje kosmetykę sygnatury,
- filtruje **cały** zbiór kandydatów,
- odrzuca „blisko pasujące” sygnatury,
- zwraca `FOUND / NOT_FOUND / AMBIGUOUS / OUT_OF_SCOPE`,
- fail-closed przy nierozpoznanym liczniku, niepełnej/zapętlonej paginacji,
  krytycznym driftcie HTML, błędzie pobrania i przerwanym transporcie.

Dla researchu po treści można użyć pola `wszystkieSlowa` jako wejścia tekstowego
formularza i dodatkowych filtrów, ale nie zgaduj nazw nieweryfikowanych kontrolek.
Jeżeli potrzebujesz konkretnej tezy, odczytaj pełne `/doc/{ID}` kandydatów i
wykonaj gradient TREŚĆ/FRAGMENT na realnym uzasadnieniu.

⚠️ **RZĄD źródła:** CBOSA jest źródłem **RZĘDU 2A** zgodnie z
`shared/HIERARCHIA-ZRODEL.md`; adapter/parser jest wyłącznie kanałem transportowym
i nie ma własnego RZĘDU.

⚠️ Dostępność jest środowiskowa. Przed użyciem wykonaj fresh probe. Jeżeli direct
CBOSA jest niedostępna, zastosuj V-SYG-0.5 z `shared/SYGNATURY.md`. Retrieval może
przekazać metrykę, sentencję, a czasem uzasadnienie; wykorzystaj faktycznie odczytaną
treść badawczo z `access_mode=CRAWLED_OR_INDEXED`, ale nie promuj jej do ✅ [VER].

Każde trafienie → 1-T.3 przed powołaniem.

### 1-T.3 — Krok weryfikacji (wspólny dla 1-T.1 i 1-T.2)

Wyszukiwanie wskazuje KANDYDATÓW — nie zwalnia z Zasady 1 ani z V-SYG.

```
Dla każdego kandydata:
→ wykonaj exact-match V-SYG / post-check na CAŁYM zbiorze;
→ direct CBOSA: tylko FOUND po odczycie /doc/{ID} daje ISTNIENIE+TREŚĆ;
  następnie sprawdź, czy sentencja/uzasadnienie naprawdę wspiera przypisywaną tezę;
→ CBOSA fallback V-SYG-0.5: po host post-check + exact-match odczytaj faktyczny
  `content_scope`; treść może wspierać research tezy, ale provenance pozostaje
  `CRAWLED_OR_INDEXED` i bez niezależnego direct potwierdzenia nie daje ✅ [VER];
→ SAOS: kandydat dla sądów powszechnych/SN musi zostać potwierdzony w źródle
  właściwym (orzeczenia.ms.gov.pl / portal lokalny / sn.pl), chyba że zweryfikowany
  rekord prowadzi do oryginalnego źródła i odczytano je bezpośrednio;
→ dopiero po potwierdzeniu cytuj z URL ORYGINAŁU i zastosuj Zasadę 2B
  dla konkretnego fragmentu.
```

### 1-T.4 — Rozszerzenie na inne bazy z wyszukiwaniem pełnotekstowym

Logikę „najpierw pełnotekstowe zapytanie po treści tezy → dopiero potem weryfikacja
sygnatury" stosuj analogicznie wszędzie tam, gdzie portal na to pozwala:
- `sn.pl` — wyszukiwarka SN ma pole treści orzeczenia/uzasadnienia,
- portale lokalne SA/SO/SR (`references/PORTALE-LOKALNE.md`) — część ma wyszukiwanie
  pełnotekstowe, część wyłącznie po sygnaturze/dacie — sprawdź formularz danego
  portalu przed założeniem, że pole istnieje,
- `trybunal.gov.pl` — wyszukiwarka TK obejmuje treść uzasadnień; dla pełnego
  tekstu urzędowego i wyszukiwania po frazie przez `web_search` (operator `site:`)
  patrz też `otkzu.trybunal.gov.pl` (Zasada 5B — równoważne źródło, ten sam organ).
Brak pola pełnotekstowego w danym portalu → wróć do strategii Fazy 1 (fraza → przepis
→ instytucja; SAOS jako uzupełnienie tylko w zasięgu — Faza 1-0).
