# Faza 1 — Wyszukiwanie (kolejność odkrywania, portale) — orzeczenia-sadowe-v2

> Plik przeniesiony ze SKILL.md bez zmian treści (progressive disclosure). Wczytaj w całości przed wykonaniem odpowiedniego kroku.

## Faza 1 — Wyszukiwanie

### Faza 1-0 — Kolejność odkrywania (discovery) — wybierz ścieżkę PRZED zapytaniem

⛔ Odkrycie ≠ weryfikacja. Każda ścieżka kończy się w bazie urzędowej (Faza 1-S,
V-SYG); reguły statusów bez zmian: NSA/WSA z CBOSA bez odczytu direct = 🟨 snapshot,
nigdy awansowany; brak trafienia w CBOSA = `OUT_OF_SCOPE`.

**Dlaczego tak — zmierzony zasięg SAOS** (`shared/KONEKTORY-REKOMENDOWANE.md`,
`shared/DOSTEP-MASZYNOWY-API.md` §3): sądy powszechne bieżąco, SN do 2016, TK do
2015, KIO do 2018, NSA/WSA — brak. SAOS nie znajdzie nowszych orzeczeń SN/TK/KIO
ani żadnych NSA/WSA.

| Sytuacja | Ścieżka |
|---|---|
| **A. Sygnatura znana** | od razu baza urzędowa po repertorium (`shared/SYGNATURY.md`, ROUTING BAZ; Faza 1-S). Bez `web_search`, bez SAOS. |
| **B. Temat, orzeczenia nowsze** (SN po 2016, TK po 2015, KIO po 2018 albo dowolne z ostatnich ~2–3 lat) | **równolegle:** (1) `web_search` ogólny — szuka sygnatur w źródłach wtórnych (komunikaty prasowe sądów, serwisy prawnicze, artykuły kancelarii); (2) wyszukiwarki pełnotekstowe urzędowe: formularz `sn.pl` (pole treści), CBOSA (`wszystkieSlowa`), `orzeczenia.uzp.gov.pl`, TK. |
| **C. Temat, orzeczenia starsze albo sądy powszechne** | SAOS (Faza 1-T.1) + `web_search`; SAOS także jako **cytator** (późniejsze orzeczenia powołujące sygnaturę: `saos_cytator` / `saos_cite_check`). |
| **D. `sn.pl` zablokowany** (403 WAF / captcha) | `web_search` po tropy + SAOS **tylko dla orzeczeń sprzed 2017**. Brak trafienia ≠ nieistnienie orzeczenia (`OUT_OF_SCOPE`). Użytkownik może przejść weryfikację `sn.pl` we własnej przeglądarce (aplikacja Lex Machina: okno weryfikacji `sn.pl`) albo dostarczyć plik. ⛔ Bez podmiany UA i obchodzenia WAF (`shared/DOSTEP-MASZYNOWY-API.md` §0–§1). |

⛔ **Zapytanie `web_search` (ścieżki B i D) = abstrakcyjna fraza prawna.** Zakaz
danych sprawy i danych osobowych (nazwisk, firm, adresów, dat i kwot ze sprawy,
sygnatury akt własnej sprawy). Przykład: ✅ `uchwała SN zachowek darowizna
doliczenie` — ⛔ `Kowalski zachowek darowizna 2019 Kraków`.

⛔ **Źródło wtórne = wyłącznie trop.** Z artykułu/komunikatu bierzesz TYLKO
sygnaturę (i ew. datę/sąd do zawężenia). Tezę i cytat bierzesz z tekstu
urzędowego po weryfikacji (Faza 1-S → 1-T.3, Zasada 2A). Nie powołuj źródła
wtórnego jako źródła orzeczenia (Zasada 4).

### Portale krajowe i UE (Tier 1–3)

Kolejność priorytetu dla spraw polskich:
1. https://www.sn.pl/pl/wyszukiwarka-orzeczen — SN, uchwały (w tym Kat. 6A); link = karta `?orzeczenie=ID`
2. orzeczenia.ms.gov.pl — SA, SO, SR
3. orzeczenia.nsa.gov.pl — Administracyjne
4. trybunal.gov.pl/orzeczenia — TK
5. curia.europa.eu — TSUE (dla materii objętej prawem UE)
6. hudoc.echr.coe.int — ETPC (dla materii objętej Konwencją)
7. saos.org.pl — Agregator (discovery dla orzeczeń starszych/sądów powszechnych i cytator — Faza 1-0 C/D; weryfikacja zastępcza tylko przy awarii bazy urzędowej)

Jedno trafienie w portalach 1–2 i 4–6 = orzeczenie zweryfikowane. NSA/WSA (3, CBOSA) =
🟨 snapshot bez awansu do ✅; brak trafienia w CBOSA = `OUT_OF_SCOPE`.
Brak trafienia w 1–6 + trafienie tylko w innych źródłach → status „Źródło niepotwierdzone w portalu sądowym".

Strategia: fraza + przepis → instytucja prawna → zagadnienie ogólne; źródło
tropów wg Faza 1-0 (SAOS tylko w zasięgu: ścieżki C/D).
Gdy celem jest odnalezienie KONKRETNEJ tezy (dosłownego sformułowania z uzasadnienia),
a nie tylko orzeczeń „w temacie" — nie zaczynaj od web_search (przeszukuje zaindeksowane
strony, nie treść uzasadnień) — zacznij od Fazy 1-T (pełnotekstowo: `sn.pl`/CBOSA dla
orzeczeń nowszych, SAOS API dla starszych i sądów powszechnych — Faza 1-0).

### Sądy szczególne i dyscyplinarne służb mundurowych

Sądy wojskowe, postępowania dyscyplinarne Policji/PSP i status OSP NIE
mieszczą się w Tier 1–3 powyżej wprost — mają odrębny status weryfikowalności
(część niepubliczna/brak portalu, część routowana przez CBOSA/sn.pl jak
zwykle). Pełna procedura: `shared/ORZECZENIA-HIERARCHIA.md` §4 — wczytaj
PRZED odpowiedzią dotyczącą orzeczenia/sygnatury z tych obszarów.

### Portale zagraniczne (Tier 4)

Stosuj gdy sprawa zawiera element obcy lub użytkownik pyta o orzecznictwo
sądu innego niż polski. Tier 4 nie zastępuje Tier 1–2 dla spraw krajowych.

| Jurysdykcja | Portal oficjalny | Uwagi |
|---|---|---|
| Niemcy (DE) | bundesgerichtshof.de (BGH, od 2000); bundesverfassungsgericht.de (BVerfG) | Treść wyłącznie w języku niemieckim |
| Francja (FR) | legifrance.gouv.fr (bazy CASS, INCA, CAPP); courdecassation.fr | Dostęp bezpłatny; treść po francusku |
| Wielka Brytania (UK) | bailii.org; uksc.gov.uk (Supreme Court) | Neutral citation system; brak ECLI |
| Inne państwa UE | e-justice.europa.eu → National justice systems | Portal odsyła do portali krajowych |
| Wyszukiwarka ECLI (UE) | e-justice.europa.eu/ecli-search | Integruje bazy państw uczestniczących (bez PL — PL nie wdrożyła ECLI) |

Dla Tier 4:
- Weryfikacja możliwa wyłącznie przez web_fetch na oficjalnym portalu danego państwa.
- Brak możliwości fetch → status „Brak weryfikacji bezpośredniej (Tier 4)" — nie powołuj w piśmie polskim.
- Orzeczenia Tier 4 nie mogą być powoływane w polskim piśmie procesowym jako samodzielna podstawa; stosować wyłącznie pomocniczo (prawo porównawcze, argumentacja).

---
