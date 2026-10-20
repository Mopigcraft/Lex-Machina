---
name: orzeczenia-sadowe-v2
version: "2.32"
type: executive-analiza
status: production
compatibility: "live_web_lookup, file_read, cross_skill_file_read, optional_code_execution, optional_document_and_interactive_ui"
description: "Research orzecznictwa: wyszukiwanie, weryfikacja sygnatur i tez, hierarchia źródeł, porównanie orzeczeń oraz dobór judykatury do argumentacji prawnej."
dependencies:
  requires:
    - shared
  # 2026-09-27e: jawna zależność (każdy skill systemu korzysta z `shared`); pole czytane przy imporcie z marketplace
---

> **Universal runtime:** przed wykonaniem zastosuj kanoniczny `shared/UNIVERSAL-RUNTIME-ADAPTER.md` z osobnego skilla `shared`. Lokalna sekcja adaptera poniżej jedynie go doprecyzowuje.


## ADAPTER RUNTIME — PORTABILITY (ChatGPT / Claude / inne hosty)

Ta sekcja zmienia wyłącznie sposób wykonania operacji technicznych. Metodologia merytoryczna, routing, hard gate’y, checklisty, schematy danych i kryteria finalizacji tego skilla pozostają bez zmian.

1. `view orzeczenia-sadowe-v2/<plik>` oraz względne `view modules/...`, `view references/...`, `view assets/...` oznaczają świeży odczyt lokalnego zasobu tego skilla. Literalny katalog `/mnt/skills/user` nie jest wymagany.
2. `view shared/<plik>` oznacza odczyt z osobnego, kanonicznego skilla `shared`. NIE kopiuj `shared` do tej paczki. Brak obowiązkowego zasobu = fail-closed.
3. `view <inny-skill>/<plik>` oznacza aktywację/odczyt osobnego skilla. Nie vendoryzuj innych skilli.
4. `web_search` / `web_fetch` oznaczają świeże wyszukanie i odczyt źródła przez równoważną funkcję hosta; zachowaj istniejące wymogi źródeł oficjalnych i statusów weryfikacji.
5. `present_files`, `create_file` i odwołania do `HOST_CAPABILITY[document_generation]` / generatorów PDF oznaczają użycie natywnej funkcji dokumentowej bieżącego hosta. Brak literalnej nazwy narzędzia nie zwalnia z HYBRID-VALIDATION, POST-VALIDATION, STEP-TRACKER ani innych bramek.
6. `show_widget`, `visualize:read_me`, `.jsx` i HTML są legacy/natywnymi wariantami UI. Jeśli host ma własny renderer interaktywny, użyj równoważnego widoku zachowującego ten sam model danych i funkcje; jeśli nie, zastosuj pełny fallback tekstowy/plikowy.
7. `/mnt/user-data/...` oznacza rzeczywiste pliki użytkownika dostępne w hoście; wymagany ponowny odczyt musi być faktycznym odczytem pliku.
8. Shell/Python/Cowork i podobne operacje traktuj jako techniki pomocnicze. Jeżeli host ich nie udostępnia, użyj natywnej funkcji równoważnej, bez fikcyjnego raportowania wykonania.

**Zasada nadrzędna:** jeśli instrukcja jest już zrozumiała i wykonalna w bieżącym hoście, wykonaj ją bez konwersji. Adapter działa tylko na granicy runtime.


# Wyszukiwanie Orzeczeń Sądowych v2

*(Nagłówek nosi sam MAJOR — decyzja generalna F-102(C); niósł v2.7 przy innym `version:`.)*

Narzędzie procesowe dla pełnomocników, sędziów i stron działających pro se.
Łączy interaktywny widget HTML (tryb laik / prawnik) z weryfikowanym
wyszukiwaniem orzeczeń, wskaźnikiem pokrycia przesłanek i systemem alertów.

## Sekwencja działania (zawsze w tej kolejności)

1. **Wyświetl widget interaktywny** — patrz: sekcja Widget poniżej
2. **Emituj profil ryzyka** — alerty wstępne przed wyszukiwaniem (Faza 0-A)
3. **Ustal przesłanki i zakres** — przepis, znamiona, ciężar dowodu (Faza 0-B)
4. **Ustal oczekiwany kierunek rozstrzygnięcia** — dla dopasowania tezy (Faza 0-C)
5. **Wyszukaj orzeczenia** — portale priorytetowe i sieć lokalna, 5 kroków (Faza 1, 1-L);
   gdy cel to dopasowanie DOSŁOWNEJ tezy/uzasadnienia — najpierw pełnotekstowo (Faza 1-T)
6. **Wyszukaj kierunek przeciwny** — test równoważny pod kątem linii przeciwnej (Faza 1-D)
   ⛔ Przed prezentacją każdego trafienia: zgodność z pytaniem i treść tylko z pobranego dokumentu (Faza 1-Z)
7. **Skategoryzuj z alertami** — taksonomia 8 kategorii + BILANS (Faza 2)
8. **Zweryfikuj aktualność linii** — jednolitość, zmiany prawa (Faza 3)
9. **Zrealizuj PLAN MINIMUM** — 5 wspierających + 5 linii przeciwnej z przesłankami rozstrzygnięcia dla każdego (Zasada 11)
10. **Wygeneruj raport końcowy** — wskaźnik pokrycia, BILANS, PLAN MINIMUM, rekomendacje (Faza 4)
11. **Wyświetl widget ponownie** — z kompletnymi danymi z Faz 1–4

---

## Widget interaktywny

Uruchom widget: szablon zasilany danymi `assets/widget-orzeczenia.html` albo kod z `references/widget.md` (warianty niżej).

Widget zawiera 5 zakładek:
- **Profil ryzyka** — alerty wstępne dla sprawy w trybie laik lub prawnik
- **Przesłanki** — pasek pokrycia per przesłanka i rozkład ciężaru dowodu
- **Orzeczenia** — pełna sygnatura, sąd z izbą, data, link do oryginału w nowym oknie, przesłanki rozstrzygnięcia (Zasada 11)
- **Alerty** — katalog aktywnych ostrzeżeń per orzeczenie z wyjaśnieniami (patrz: szablon Alerty w widget.md)
- **Raport** — wskaźnik pokrycia, ocena linii orzeczniczej, kolejność powołania

Przełącznik **LAIK / PRAWNIK** w nagłówku zmienia język alertów, tez i rekomendacji jednocześnie we wszystkich zakładkach.

Widget wywołujesz **dwukrotnie:**
- przed wyszukiwaniem — z danymi Fazy 0-A i 0-B, komunikat „Trwa wyszukiwanie…" w zakładkach Orzeczenia i Raport
- po wyszukiwaniu — z kompletnymi danymi wszystkich faz

### Szablon zasilany danymi (host z `show_widget` przyjmującym `data`)

`show_widget(path="orzeczenia-sadowe-v2/assets/widget-orzeczenia.html", data=DANE)` — bez kodu; host wstawia dane i dokłada pasek eksportu. DANE (pola opcjonalne można pominąć):
```
tytul, tryb: laik|prawnik, etap: wyszukiwanie|wynik
ryzyko: [{poziom: high|mid|low, laik, prawnik}]                         — Faza 0-A
przeslanki: {przepis, instytucja, jurysdykcja, lista: [{tresc, ciezar, pokrycie 0–100, stan: ok|warn|gap}]}
orzeczenia: [{sygnatura, kategoria: 6A|1|2|3A|3B|4|5|6|7, sad, teza_laik, teza_prawnik,
              przeslanki (Zasada 11), url, alerty: [{typ: old|conflict|law|eu|nurl|zp, laik, prawnik}]}]
bilans: {ocena: bad|mid|good, zgodne, przeciwne, neutralne, laik, prawnik, przeciwne_sygnatury: [{sygnatura, teza}]}
ocena: {laik, prawnik}; kolejnosc: [{sygnatura, dlaczego}]; jurysdykcja_zagraniczna
```
Zasady treści (status źródeł, linia przeciwna, Zasada 11) — bez zmian; dane to wyłącznie wyniki Faz 0–4.

<!-- lex:wykonuje-aplikacja: WIDGET-DANE -->
### Kod widgetu i pasek IO (host bez pola `data`)

Kod widgetu: patrz `references/widget.md` — wklej jako argument `widget_code` narzędzia
`show_widget`, podstawiając dane konkretnej sprawy w miejsca oznaczone `<!-- DANE: ... -->`.

⛔ MOD-WIDGET-IO (OBOWIĄZKOWE — wykonaj PRZED każdym show_widget):
```
view shared/MOD-WIDGET-IO.md
→ wbuduj pasek IO w nagłówek widgetu (powyżej zakładek)
→ IO_SKILL_ID='orzeczenia-sadowe-v2', IO_CASE_ID=sygnatura_sprawy
→ matryca: Export JSON ✅ MD ✅ | Import JSON —
→ w obu wywołaniach (przed i po wyszukiwaniu): pasek IO obecny
```

---

## Zasady fundamentalne

**Zasada 1 — ⛔ PERMANENT GATE: zakaz cytowania z pamięci (przez CAŁĄ rozmowę):**
Przed każdym web_search/web_fetch poniżej: sprawdź KROK 1 z
`view shared/MCP-INTEGRACJA.md` — jeśli connector MCP dla
orzecznictwa (np. SAOS/CBOSA) jest podłączony i dostępny w tej rozmowie, użyj
go najpierw (KROK 2 tamtego pliku); w przeciwnym razie przejdź od razu do
web_search/web_fetch poniżej, bez zmian względem dotychczasowej procedury.
Każde powołanie sygnatury, daty lub sądu = osobny web_search/web_fetch w tej odpowiedzi
(lub odpowiadające zapytanie MCP, jeśli tryb MCP-FIRST aktywny).
Zakaz nie wygasa po żadnej liczbie wiadomości. Nawet gdy model "jest pewny" — weryfikacja obowiązkowa.
Jeśli nie możesz zweryfikować: „Nie odnalazłem tego źródła online. Nie powołuję."
Przed cytowaniem wykonaj procedurę V-SYG z modułu SYGNATURY:
```
view shared/SYGNATURY.md
→ Wykonaj V-SYG-1 przez V-SYG-4
→ Dopiero po wyniku OK: cytuj z linkiem źródłowym
```

**Zasada 2 — Cztery obowiązkowe elementy każdego orzeczenia:**
```
[1] SYGNATURA — pełna, np. II PK 123/22
[2] DATA      — dzień-miesiąc-rok, np. 15 marca 2023
[3] SĄD       — pełna nazwa + izba/wydział
[4] URL       — link do oryginału w oficjalnym portalu, nowe okno
```
Brak któregokolwiek = błąd krytyczny, orzeczenie nie może być powołane.

**Zasady 2A–11 (szczegóły w pliku poniżej; brak odczytu pliku = nie wykonuj kroków, których dotyczą):**
- **Zasada 2A** — 4 elementy potwierdzają ISTNIENIE, nie TREŚĆ; przy poparciu tezy wymagany poziom TREŚĆ (GRAD-1..4).
- **Zasada 2B** — symbol CBOSA i powołania przeciwnika (GRAD-3b-SYM); KOTWICA/PINPOINT do miejsca w źródle.
- **Zasada 2C** — weryfikacja ROLI cytowanego fragmentu (czyją wypowiedź cytujesz).
- **Zasada 3** — limit cytatu 30 słów. **Zasada 4** — link wyłącznie do oryginału.
- **Zasada 5 / 5A / 5B** — jedno oficjalne źródło wystarcza; sieć lokalna SA/SO/SR; OTK ZU dla TK.
- **Zasada 6** — status „Źródło niepotwierdzone w portalu sądowym". **Zasada 7** — hierarchia portali (Tier 1–4).
- **Zasada 8** — uchwały SN z mocą zasady prawnej (Kat. 6A). **Zasada 9** — dopasowanie tezy do oczekiwanego rozstrzygnięcia.
- **Zasada 10 — ⛔ Zakaz ukrywania liczebnej przewagi linii przeciwnej** (alert BILANS NIEKORZYSTNY jako pierwszy).
- **Zasada 11 — ⛔ PLAN MINIMUM:** 5 wspierających + 5 linii przeciwnej, zawsze z przesłankami rozstrzygnięcia.

**WCZYTAJ (obowiązkowo, fail-closed):** view orzeczenia-sadowe-v2/references/zasady-fundamentalne.md
Plik MUSI być przeczytany przed Fazą 1 (Zasady 2A–2C, 5–7), przed Fazą 1-D (9–10) i przed Fazą 4 (11).
---

## Faza 0-A — Profil ryzyka
Przed wyszukiwaniem emituj alerty wstępne (dwa warianty: laik / prawnik).

## Faza 0-B — Przesłanki i ciężar dowodu
Rodzaj postępowania, kluczowy przepis, przesłanki i ciężar dowodu.

## Faza 0-C — Profil oczekiwanego rozstrzygnięcia
Warunek konieczny dla Zasady 9 i Fazy 1-D.

**WCZYTAJ (obowiązkowo, fail-closed):** view orzeczenia-sadowe-v2/references/etap-faza-0.md — przed wykonaniem Fazy 0-A.
---

## Faza 1 — Wyszukiwanie
- **Faza 1-0 — Kolejność odkrywania (discovery)** — wybierz ścieżkę A/B/C/D PRZED zapytaniem; odkrycie != weryfikacja; zapytanie web_search bez danych sprawy; źródło wtórne = tylko trop.
- **Portale krajowe i UE (Tier 1–3)**, **Sądy szczególne i dyscyplinarne służb mundurowych**, **Portale zagraniczne (Tier 4)**.

**WCZYTAJ (obowiązkowo, fail-closed):** view orzeczenia-sadowe-v2/references/faza-1-wyszukiwanie.md — przed pierwszym zapytaniem.
## Faza 1-S — Kontrola istnienia sygnatury (V-SYG-0)
Wykonuje się PRZED Fazą 1-T i przed każdym powołaniem sygnatury: normalizacja, routing po repertorium, okno pokrycia, post-check tożsamości, CBOSA fail-closed, zakres potwierdzenia. Tylko `FOUND` otwiera możliwość powołania; `NOT_FOUND`/`OUT_OF_SCOPE`/`AMBIGUOUS` nie są „potwierdzone".

## Faza 1-T — Wyszukiwanie pełnotekstowe po treści tezy (SAOS API + CBOSA)
Gdy celem jest dosłowna teza w uzasadnieniu/sentencji: 1-T.1 SAOS REST API; 1-T.2 CBOSA (NSA/WSA) — formularz HTML + pełny tekst; 1-T.3 krok weryfikacji (wspólny); 1-T.4 inne bazy z wyszukiwaniem pełnotekstowym.

**WCZYTAJ (obowiązkowo, fail-closed):** view orzeczenia-sadowe-v2/references/faza-1-sygnatura-pelnotekst.md — przed każdym powołaniem sygnatury (1-S) i przed wyszukiwaniem pełnotekstowym (1-T).
---

<!-- lex:wczytaj-gdy: ZAMOWIENIA-PUBLICZNE -->
## Faza 1-K — Orzecznictwo KIO / zamówienia publiczne (PZP)

Stosuj gdy sprawa dotyczy zamówień publicznych: odwołanie do KIO, skarga na
orzeczenie KIO do sądu, rażąco niska cena, wykluczenie/odrzucenie oferty,
warunki udziału, SWZ — zwłaszcza gdy współpracujesz z `dr-07-zamowienia-
publiczne-fundusze-ue`.

⚠️ **Korekta adresu (zweryfikowane 2026-07-05c):** `kio.gov.pl` jako
"wyszukiwarka wyroków" jest NIEAKTUALNE — domena przekierowuje na strony
informacyjne `uzp.gov.pl/kio` (o KIO, skład, kontakt), NIE na wyszukiwarkę
orzeczeń. Właściwa, działająca wyszukiwarka orzecznictwa PZP jest pod
odrębną subdomeną: **`orzeczenia.uzp.gov.pl`**. Obejmuje nie tylko KIO, ale
też SO/SA/SN w zakresie skarg na orzeczenia KIO (zakładki „Wszystkie/KIO/
SO/SA/SN" w wyszukiwarce) — szerszy zakres niż sama Izba.

⚠️ **Status prawny:** orzeczenia KIO NIE są źródłem prawa (art. 87
Konstytucji RP) — są materiałem referencyjnym praktyki PZP. Traktuj jak
Tier 1 dla spraw DR-07 mimo braku mocy precedensowej formalnej — patrz
Zasada 7.

### 1-K.1 — Wyszukiwanie

Punkt wejścia: `https://orzeczenia.uzp.gov.pl/Home/Search`

Parametry zweryfikowane bezpośrednim fetchem (2026-07-05c) — używaj TYLKO tych,
inne pola widoczne w formularzu (Rodzaj dokumentu, Wynik postępowania, Izba,
Zamawiający, Miejscowość itd.) wymagają ustalenia dokładnej nazwy parametru
przez inspekcję formularza PRZED użyciem — nie zgaduj nazw po wzorze innych API:
```
Phrase=FRAZA     → hasło wyszukiwania (URL-encode spacji i polskich znaków)
Fle=0|1          → 0 = szukaj dokładnej formy, 1 = "odmiana słów" (fleksja)
SCnt=0|1         → 0 = szukaj w metadanych, 1 = "szukaj również w treści" (pełny tekst)
Pg=N             → numer strony wyników
```
Przykład zweryfikowany: `.../Home/Search?Phrase=art.%207%20ust.%201&Fle=0&SCnt=0`
(filtr po konkretnym artykule PZP — link ten sam wzorzec, który portal
generuje sam dla „Kluczowe przepisy ustawy Pzp" na stronie wyniku).

### 1-K.2 — Pobranie pojedynczego orzeczenia

Z listy wyników każdy wpis linkuje do strony szczegółów
(`/Home/Details/{internal_id}?Pg=...&Phrase=...&ind=...&total=...` lub
`/Home/Move?...` przy nawigacji strzałkami między wynikami tego zapytania).
Strona szczegółów zawiera KOMPLET metadanych bezpośrednio w HTML (nie trzeba
osobnego zapytania):
```
Organ wydający | Rodzaj dokumentu | Data wydania rozstrzygnięcia |
Przewodniczący | Zamawiający | Miejscowość | Sygnatura akt / Sposób
rozstrzygnięcia (np. "KIO 827/18 / oddalone") | Tryb postępowania |
Rodzaj zamówienia | Kluczowe przepisy ustawy Pzp (linkowane) |
Indeks tematyczny (linkowany)
```
Pełny tekst: link „Treść dokumentu" → `/Home/ContentHtml/{id}?Kind=KIO&phrase=...`
(fragment HTML) lub „Pobierz treść PDF" → `/Home/PdfContent/{id}?Kind=KIO`.

> ℹ️ Zewnętrzny konektor `kio-orzeczenia-mcp` (POC, oceniony osobno) opisuje
> nieco inny wzorzec URL (`/Home/HtmlContent/{id}`) — przy fetchu 2026-07-05c
> rzeczywisty portal zwrócił `/Home/Details/{id}` + `/Home/ContentHtml/{id}`.
> Rozbieżność potwierdza to, co ten konektor sam przyznał w CHANGELOG
> (4/4 nieudane testy live, selektory best-effort) — nie kopiuj jego
> endpointów bez własnej weryfikacji fetchem, tak jak wykonano tutaj.

### 1-K.3 — Cytowanie (Zasada 2 + rozszerzenie domenowe)

Cztery elementy Zasady 2 (sygnatura/data/sąd/URL) + dla KIO dodaj obowiązkowo
z metadanych strony szczegółów: **Sposób rozstrzygnięcia** (oddalone/
uwzględnione/odrzucone/umorzone) — pole to jest już otagowane przez portal,
więc stanowi mocniejszy, tańszy pierwszy test GUARD INSTYTUCJA (Zasada 2A/
GRAD-3b z `shared/WERYFIKACJA-SLAD.md`) niż czytanie całego uzasadnienia:
jeśli teza pisma twierdzi „KIO uwzględniło odwołanie w zakresie X", a pole
Sposób rozstrzygnięcia = „oddalone" — to sprzeczność wykrywalna od razu,
bez analizy treści.

Format:
```
Wyrok/postanowienie KIO z [data], sygn. [KIO NNN/RR] ([sposób rozstrzygnięcia])
— [URL Home/Details/{id}]
```

### 1-K.4 — Powiązanie z przepisem (RZĄD 1 — ELI)

Strona szczegółów linkuje "Kluczowe przepisy ustawy Pzp" — to potwierdza
TYLKO, że KIO powołało dany artykuł, NIE zwalnia z odrębnej weryfikacji
brzmienia przepisu w ELI — kanon E-1…E-5 (ustawa z 11.09.2019 r. — Prawo zamówień
publicznych, t.j. — sprawdź aktualny numer Dz.U. przed cytowaniem, zmienia
się często). Dwa źródła, dwa kroki — nigdy nie wyprowadzaj brzmienia
przepisu z tego, jak cytuje go orzeczenie.

### 1-K.5 — Zastrzeżenia praktyczne

- Brak oficjalnego udokumentowanego API i publikowanego limitu zapytań —
  traktuj jak każdy portal publiczny: rozsądna liczba zapytań w ramach
  jednej sprawy, bez zbędnego powtarzania tego samego zapytania.
- Filtry poza Phrase/Fle/SCnt/Pg (Rodzaj dokumentu, Wynik postępowania,
  Izba, Zamawiający, Skarżony organ, Miejscowość, Publikator, Tryb
  postępowania) są dostępne w formularzu, ale ich dokładne nazwy parametrów
  URL NIE zostały zweryfikowane w tej sesji — jeśli potrzebne, sprawdź
  fetchem strony formularza przed założeniem nazwy.
- Zakładki „SO/SA/SN" na tym portalu to skargi NA orzeczenia KIO — osobna
  droga procesowa (art. 579–589 PZP), nie duplikat KIO.

---

## Faza 1-L — Sieć lokalna portali SA/SO/SR i CBOSA (rozszerzenie bazy)
Gdy wyszukiwanie centralne (orzeczenia.ms.gov.pl) nie dało wyników lub dało ich mało (< 3): portale lokalne sądów i CBOSA.

**WCZYTAJ (obowiązkowo, fail-closed):** view orzeczenia-sadowe-v2/references/faza-1-siec-lokalna.md — przed wejściem w Fazę 1-L.
---

## Faza 1-D — Dopasowanie tezy i test kierunku przeciwnego
KROK 1 wyszukiwanie zgodne z kierunkiem; KROK 2 kierunek przeciwny (OBOWIĄZKOWE, min. 2 zapytania); KROK 3 ocena dopasowania (ZGODNE/PRZECIWNE/NEUTRALNE); KROK 4 liczby do BILANSU.

## Faza 1-Z — Kontrola zgodności trafienia z pytaniem (przed prezentacją)
⛔ GATE: przed przedstawieniem każdego orzeczenia jako trafienia — tożsamość i treść tylko z pobranego dokumentu, każde kryterium pytania osobno, brak trafień = wprost, bez zapowiedzi zamiast wyniku, teza tylko ze stanowiska organu, określenie sprawy przed tekstem.

## Faza 1-F — Fallback (niedostępność narzędzi)
Gdy web_search/web_fetch zwracają błąd lub timeout: procedury F-1..; brak narzędzia nie zwalnia z zakazu cytowania z pamięci.

**WCZYTAJ (obowiązkowo, fail-closed):** view orzeczenia-sadowe-v2/references/faza-1-dopasowanie-kontrola.md
Plik MUSI być przeczytany przed wykonaniem Fazy 1-D i PRZED prezentacją jakiegokolwiek trafienia (Faza 1-Z).
---

## Faza 2 — Kategoryzacja i alerty
Alerty per orzeczenie, BILANS LINII ORZECZNICZEJ (obliczenie), dziedzinowe progi alertu STARE, kategorie orzeczeń (taksonomia 8 kategorii); tabele klas CSS w `references/widget.md`.

## Faza 3 — Weryfikacja aktualności
Jednolitość linii, nowelizacje po datach orzeczeń, odmienne stanowisko SN.

## Faza 4 — Raport końcowy
Wskaźnik pokrycia, BILANS, PLAN MINIMUM, rekomendacje.

**WCZYTAJ (obowiązkowo, fail-closed):** view orzeczenia-sadowe-v2/references/faza-2-4-kategoryzacja-raport.md — przed Fazą 2.
---

## Dualny tryb narracji

Skill wykrywa poziom automatycznie. Użytkownik może wpisać „tryb prawnik" / „tryb laik" lub kliknąć przełącznik w widgecie.

| Element | Tryb LAIK | Tryb PRAWNIK |
|---------|-----------|--------------|
| Alerty | Prosty język, co zrobić | Precyzyjny, przepis + ryzyko |
| Teza | Jedno zdanie bez żargonu | Pełna kwalifikacja prawna |
| Rekomendacje | Kroki działania | Argumentacja procesowa, kolejność |

---

## Obsługa błędów i fallback

| Sytuacja | Działanie |
|----------|-----------|
| Portal Tier 1–3 niedostępny | Przejdź do następnego w kolejności |
| Wszystkie portale Tier 1–3 niedostępne | Wykonaj FALLBACK F-1 |
| Brak wyników | Rozszerz frazę; SAOS tylko w zasięgu (Faza 1-0 C); rozważ Fazę 1-L (sieć lokalna) |
| `sn.pl` 403 WAF / captcha | Faza 1-0 D: `web_search` po tropy, SAOS tylko sprzed 2017, sesja użytkownika albo plik; brak trafienia = `OUT_OF_SCOPE` |
| Portal lokalny (SA/SO/SR) sądu nieznany lub niedostępny | web_search nazwy sądu → zweryfikuj URL przez web_fetch; brak potwierdzenia → traktuj jak F-2 |
| Sprzeczne orzeczenia | Kat. 3A + Kat. 3B — nigdy nie ukrywaj |
| Liczna linia przeciwna do oczekiwanego rozstrzygnięcia | Wykonaj Fazę 1-D → oblicz BILANS (Faza 2) → alert 🔴/🟡 w Raporcie (Zasada 10) |
| Sygnatura nieweryfikowalna w Tier 1–2 | „Źródło niepotwierdzone w portalu sądowym" — nie powołuj |
| Orzeczenie TSUE/ETPC | Weryfikuj w curia.europa.eu / hudoc — traktuj jako Tier 2 |
| Luka pokrycia < 40% | Wykonaj FALLBACK F-4 |
| Dostęp tylko przez LEX / Legalis | Wykonaj FALLBACK F-3 |
| Jurysdykcja zagraniczna | Sprawdź portal Tier 4; wyraźnie oznacz w raporcie |
| web_search / web_fetch niedostępne | Wykonaj FALLBACK F-1 |

## REGUŁA RENDEROWANIA WIDGETÓW

> Pliki `.jsx` przez `present_files` NIE renderują się w claude.ai — użytkownik widzi tylko link.
> Mechanizm `window.__INJECTED__` działa tylko z bundlerem React — NIE w czacie.
> Jedyna poprawna metoda renderowania widgetu inline: `show_widget` z HTML (vanilla JS).
> NIE używaj: `cp`, `str_replace`, `present_files`, `.jsx`, `window.__INJECTED__`.

---

## Output schema — dane przekazywane downstream

Gdy wynik tego skilla trafia do pisma-procesowe-v3, analizator-umow-v1 lub innych konsumentów:

```
view references/ORZECZENIA-OUTPUT-SCHEMA.md
→ Format rekordu ORZ-REKORD (pola OBL + OPT)
→ Instrukcje per consumer (pisma-procesowe-v3 W3.2, analizator-umow-v1, analiza-sadowa-v6)
→ Reguły integralności (brak URL = ⛔, Kat. 6A priorytet, zakaz ukrywania Kat. 3B)
```

Każde orzeczenie przekazywane downstream MUSI mieć: sygnaturę, sąd, datę, URL, znacznik VER,
kategorię, tezę (≤30 słów), aktualność linii. Brak któregokolwiek = rekord przekazywany jako ⛔.

---

## Integracja z kancelaryjnym jądrem shared

Jeżeli wynik tego skilla ma służyć do pisma, strategii procesowej, oceny ryzyka albo decyzji terminowej, wczytaj właściwe moduły shared:

```text
view shared/SYGNATURY.md           ← ZAWSZE przed cytowaniem sygnatury
view shared/TRYBY-PROCESOWE.md
view shared/RISK-ASSESSMENT.md
view shared/TERM-CALC.md
view shared/DOWODY-METODOLOGIA.md
view shared/PREKLUZJA-DOWODOWA.md
view shared/STRATEGIA-PROCESOWA.md
view shared/QUALITY-CHECK.md
view shared/ORZECZENIA-HIERARCHIA.md
```

Nie dubluj logiki shared w lokalnych plikach. Lokalne moduły mogą tylko doprecyzować analizę dziedzinową.

---

## CHANGELOG

> Pełna historia wersji (2.1...2.6) wyniesiona do `references/CHANGELOG.md`
> (redukcja kosztu kontekstu, 2026-07-12 runda 2) — treść zachowana w 100%,
> tylko przeniesiona: `view orzeczenia-sadowe-v2/references/CHANGELOG.md`
>
> Najnowsza pozycja: **2.17 (2026-09-14)** — snapshot CBOSA z host post-check i jawnym provenance. — routing CBOSA wpięty do RZĄD 2A/shared,
> exact-match sygnatur NSA/WSA, pełny odczyt sentencji/uzasadnienia oraz
> statusy FOUND / NOT_FOUND / AMBIGUOUS / OUT_OF_SCOPE z fallbackiem V-SYG-0.5.
