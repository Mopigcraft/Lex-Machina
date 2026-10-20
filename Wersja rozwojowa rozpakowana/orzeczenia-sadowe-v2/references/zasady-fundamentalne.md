# Zasady fundamentalne 2A–11 — orzeczenia-sadowe-v2

> Plik przeniesiony ze SKILL.md bez zmian treści (progressive disclosure). Wczytaj w całości przed wykonaniem odpowiedniego kroku.

**Zasada 2A — Cztery elementy potwierdzają ISTNIENIE, nie TREŚĆ (dodano 2026-07-05b,
po NSA I FZ 104/26).** Kompletne 4 elementy (Zasada 2) wystarczają, gdy orzeczenie
jest tylko wzmiankowane. Gdy orzeczenie ma POPRZEĆ tezę użytkownika/pisma (włącznie
z "gołym" powołaniem bez cudzysłowu, np. "por. też…") — wymagany dodatkowo poziom
TREŚĆ z `shared/WERYFIKACJA-SLAD.md` (GRAD-1..4): sprawdź, czy orzeczenie FAKTYCZNIE
dotyczy powoływanej instytucji/kwestii, nie tylko tej samej gałęzi prawa. Cztery
elementy + niedopasowany przedmiot = wynik nadal niecytowalny na poparcie tezy.
Ten sam mechanizm łapie również cytaty z KROK 1-T.1/1-T.2 (SAOS/CBOSA
pełnotekstowe) — one dają KANDYDATÓW, gradient TREŚĆ jest krokiem PO nich,
nie zamiast (patrz 1-T.3).

**Zasada 2B — symbol CBOSA i powołania przeciwnika (dodano 2026-09-22, F-194,
po NSA I OSK 590/26 — 🟨 snapshot bez awansu).** (a) Przy orzeczeniu NSA/WSA
powoływanym na poparcie tezy wykonaj `GRAD-3b-SYM` z `shared/WERYFIKACJA-SLAD.md`:
odczytaj pole „Symbol z opisem" z `/doc/{ID}` i porównaj z symbolem sprawy;
różny symbol = obowiązkowy odczyt przedmiotu (GRAD-3b) przed użyciem, nie
automatyczne odrzucenie. (b) Gdy weryfikujesz orzecznictwo powołane przez
PRZECIWNIKA — stosuj `KALIBRACJA-PRZECIWNIK` (tamże): wadliwe powołanie to
argument o wiarygodności pisma, nigdy zamiennik odpowiedzi na istotę zarzutu.

**Zasada 2B — KOTWICA/PINPOINT do konkretnego miejsca w źródle (dodano
2026-07-15, na wyraźne polecenie użytkownika — analogia do wskazywania
strony/punktu/akapitu w pismach procesowych, patrz `shared/FAKTY_v2.md`
KROK F2A). Cztery elementy Zasady 2 mówią GDZIE JEST dokument — Zasada 2B
mówi GDZIE W DOKUMENCIE jest cytowany fragment. Obowiązuje dla KAŻDEGO
cytatu i KAŻDEJ sentencji/tezy przywoływanej z orzeczenia LUB z interpretacji
znalezionej na stronie internetowej (komentarz, artykuł, interpretacja
urzędowa, glosa).**

⚠️ AKTUALIZACJA 2026-07-15: ten sam mechanizm wdrożono także CENTRALNIE do
`shared/PRAWO-HARDGATE.md` (KROK 5A/5B, wersja 2.1) — jako HARD GATE
aktywny w całym systemie, nie tylko w tym module. Treść poniżej pozostaje
jako szczegółowa specyfikacja robocza dla tego skilla; w razie rozbieżności
rozstrzyga PRAWO-HARDGATE jako źródło nadrzędne.

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

```
[5] LOKALIZACJA W ŹRÓDLE — obowiązkowa, w pierwszej pasującej formie:
    (a) NUMER STRONY dokumentu źródłowego, jeśli źródło jest plikiem
        stronicowanym (PDF orzeczenia z portalu, skan, uzasadnienie
        w wersji do druku) — format: "s. 4" lub "k. 12" (dla akt sądowych)
    (b) NUMER TEZY/PUNKTU/AKAPITU, jeśli orzeczenie lub strona ma
        numerację wewnętrzną (np. "teza 3", "pkt II.4", "akapit 27" —
        częste w wyrokach TSUE i ETPC, które numerują akapity od 1)
    (c) NAZWA SEKCJI/NAGŁÓWKA, jeśli źródło (artykuł, komentarz,
        interpretacja) ma strukturę nagłówków bez numeracji — cytuj
        dosłowne brzmienie najbliższego nagłówka nadrzędnego
    (d) Jeśli ŻADNA z (a)-(c) nie istnieje w źródle (np. czysty HTML bez
        struktury) → jawna adnotacja: "brak wewnętrznej numeracji w
        źródle — lokalizacja opisowa: [1-2 zdaniowy opis miejsca, np.
        »akapit zaczynający się od: Sąd Najwyższy uznał, że...«]"

[6] KOTWICA TECHNICZNA (URL fragment) — dodaj, GDY platforma źródłowa
    wspiera adresowanie fragmentu, w kolejności preferencji:
    (a) #page=N — dla PDF-ów otwieranych w przeglądarce (działa w
        większości plików z portali sądowych i SAOS/CBOSA, gdy URL
        kończy się na .pdf) → pełny format: [URL].pdf#page=4
    (b) Kotwica nagłówka strony (#nazwa-sekcji), jeśli źródło HTML ma
        widoczne id sekcji w kodzie strony (sprawdź przez web_fetch —
        NIE zgaduj nazwy kotwicy, jeśli jej nie widziałeś w treści)
    (c) Numer akapitu w adresie, jeśli portal go udostępnia (niektóre
        bazy orzecznictwa TSUE/ETPC mają odrębny URL per punkt/paragraf)
    (d) Brak wsparcia technicznego (typowe: strony bez zakotwiczeń,
        proste PDF-y skanowane bez warstwy tekstowej) → NIE zmyślaj
        kotwicy — podaj tylko URL z Zasady 2[4] + lokalizację opisową
        z [5]. Wymyślona kotwica, która nie prowadzi do właściwego
        miejsca, jest GORSZA niż jej brak (myląca dla czytelnika).

⛔ ZAKAZ: podawanie numeru strony/tezy z pamięci lub przez odgadnięcie na
podstawie długości dokumentu — numer MUSI pochodzić z faktycznie
przeczytanej treści (web_fetch) tej konkretnej strony/akapitu.
⛔ ZAKAZ: kotwica techniczna nigdy nie zastępuje lokalizacji opisowej z
[5] — obie razem, gdy to możliwe (kotwica ułatwia KLIKNIĘCIE, opis
pozwala ZNALEŹĆ nawet gdy kotwica nie zadziała, np. link się zmienił).

PRZYKŁAD PEŁNEGO CYTOWANIA (wszystkie 6 elementów):
  Sąd Najwyższy w wyroku z 15 marca 2023 r. (II PK 123/22) wskazał, że
  "[cytat do 30 słów]" (SN, II PK 123/22, 15.03.2023, s. 7 uzasadnienia,
  https://przyklad-portalu.pl/orzeczenie/xyz.pdf#page=7)

PRZYKŁAD DLA INTERPRETACJI ZE STRONY INTERNETOWEJ (nie orzeczenie, ale
ten sam standard — komentarz prawniczy, interpretacja urzędowa, glosa):
  Zgodnie z komentarzem [autor/instytucja], "[cytat do 15 słów — limit
  ogólny PRAWO-HARDGATE, NIE 30-słowny limit orzeczeń z Zasady 3]" —
  sekcja "[dokładny nagłówek]", https://przyklad.pl/artykul#sekcja
  (jeśli brak kotwicy: "..., sekcja »Kary za naruszenie«, akapit 3 od góry")

**Zasada 2C — Weryfikacja ROLI cytowanego fragmentu (dodano 2026-08-14,
na żądanie użytkownika — CENTRALNIE w `shared/PRAWO-HARDGATE.md`, sekcja
"KROK DODATKOWY — WERYFIKACJA ROLI CYTOWANEGO FRAGMENTU").** Zasady 2/2A/
2B wyżej potwierdzają, że cytat ISTNIEJE i jest DOKŁADNY — ale NIE mówią,
czyją wypowiedź w uzasadnieniu cytujesz. Uzasadnienie typowo zawiera trzy
warstwy o różnej wartości: [1] ustalenie/rozstrzygnięcie SĄDU, [2]
wykładnia prawa dokonana PRZEZ sąd, [3] zreferowane twierdzenie STRONY
(np. "Powód podniósł, że...", zwykle PRZED zwrotem "Sąd zważył, co
następuje"). TYLKO [1] i [2] nadają się do powołania jako stanowisko
sądu. PRZED cytowaniem na poparcie tezy pisma — ustal warstwę wprost z
treści źródłowej (web_fetch), nie z samego wyrwanego zdania. Pełna
specyfikacja i sygnały tekstowe do rozpoznania warstwy [3]:
`shared/PRAWO-HARDGATE.md`, sekcja jw. — w razie rozbieżności rozstrzyga
PRAWO-HARDGATE jako źródło nadrzędne (ten sam wzorzec co Zasada 2B).

**Zasada 3 — Limit cytatu: maksymalnie 30 słów.**
Dziedzinowy override globalnego limitu 15 słów z PRAWO-HARDGATE — uzasadniony koniecznością
dokładnego oddania tezy prawnej. Dotyczy WYŁĄCZNIE cytatów z treści orzeczeń sądowych.
Dla przepisów ustawowych obowiązuje globalny limit 15 słów z PRAWO-HARDGATE.

**Zasada 4 — Link wyłącznie do oryginału.**
Zakaz linkowania do LexLege, Prawo.pl, SIP itp. jako głównego źródła.

**Zasada 5 — Jedno wiarygodne oficjalne źródło wystarczy.**
Orzeczenie jest uznane za zweryfikowane gdy potwierdzone w co najmniej JEDNYM
z portali: sn.pl, orzeczenia.ms.gov.pl (wraz z całą siecią lokalną SA/SO/SR —
patrz Zasada 5A), orzeczenia.nsa.gov.pl (CBOSA — obejmuje NSA oraz wszystkie
16 WSA), trybunal.gov.pl wraz z otkzu.trybunal.gov.pl (Zbiór Urzędowy, ten sam
organ — patrz Zasada 5B), curia.europa.eu (TSUE), hudoc.echr.coe.int (ETPC),
orzeczenia.uzp.gov.pl (KIO i skargi SO/SA/SN — zamówienia publiczne, Faza 1-K).
saos.org.pl pełni rolę wsparcia — nie jest samodzielnym źródłem weryfikacji.
Nie wymagaj potwierdzenia w wielu portalach jednocześnie.

**Zasada 5A — Sieć lokalna portali sądów powszechnych (SA/SO/SR).**
`orzeczenia.ms.gov.pl` jest punktem centralnym sieci złożonej z osobnych
portali każdego sądu apelacyjnego, okręgowego i rejonowego (np.
`orzeczenia.warszawa.so.gov.pl`, `orzeczenia.krakow-sr.sr.gov.pl`). Wszystkie
mają status Tier 1 — potwierdzenie w portalu lokalnym danego sądu jest
równoważne potwierdzeniu w portalu centralnym. Szczegółowy wzorzec URL,
lista portali głównych sądów apelacyjnych/okręgowych i procedura użycia:
patrz `references/PORTALE-LOKALNE.md` oraz Faza 1-L.
⛔ **Kanał kodu dla sieci lokalnej jest zamknięty (zmierzone T25, 2026-09-13c).**
`orzeczenia.warszawa.so.gov.pl` i pozostałe hosty `orzeczenia.*.so/sa/sr.gov.pl`
są POZA listą dozwolonych domen (`host_not_allowed`) — do portali lokalnych
sięgaj przez `web_search`/`web_fetch`, nie przez `curl`. Portal centralny
`orzeczenia.ms.gov.pl` działa w obu kanałach (Faza 1-S).

⚠️ Publikacja w sieci SA/SO/SR NIE jest wyczerpująca — sądy publikują tylko
orzeczenia z uzasadnieniem wybrane przez zespół sędziów; brak orzeczenia
w portalu ≠ jego nieistnienie. Nie formułuj wniosku o braku linii orzeczniczej
wyłącznie na tej podstawie — patrz FALLBACK F-4 i Faza 3.

**Zasada 5B — OTK ZU jako archiwum pełnych tekstów TK (dodane 2026-07-17).**
`trybunal.gov.pl/orzeczenia` to WYSZUKIWARKA (formularz po sygnaturze/haśle/
dacie), ale pełny, urzędowy tekst wyroku — łącznie z uzasadnieniem — bywa
wygodniej dostępny bezpośrednio w **Zbiorze Urzędowym (OTK ZU)**, hostowanym
pod `otkzu.trybunal.gov.pl`. To NIE jest osobna instytucja ani osobne źródło
w sensie Zasady 5 — to ten sam organ (TK), ten sam status Tier 1, tylko inny
punkt dostępu do tej samej treści urzędowej. Traktuj jako RÓWNOWAŻNY
`trybunal.gov.pl` — potwierdzenie w OTK ZU spełnia wymóg Zasady 5 tak samo
jak potwierdzenie w wyszukiwarce głównej.

Kiedy sięgać po OTK ZU zamiast/obok głównej wyszukiwarki:
- Gdy znasz orientacyjną treść tezy, ale nie masz jeszcze sygnatury —
  `web_search` (wyszukiwarka hosta; w Lex Machina DuckDuckGo/Brave) z frazą `site:otkzu.trybunal.gov.pl` + fraza tezy
  bywa skuteczniejsza niż formularz TK (który wymaga zwykle sygnatury/hasła).
- Gdy potrzebujesz PEŁNEGO tekstu uzasadnienia (nie tylko sentencji) do
  cytowania w piśmie — OTK ZU publikuje kompletne orzeczenie w PDF.
- Format oznaczenia publikacji: `OTK ZU nr X/Rok, poz. Y` (seria A — wyroki/
  postanowienia merytoryczne w trybie art. 91 u.o.t.p.TK; seria B —
  postanowienia o (nie)nadaniu dalszego biegu skardze/wnioskowi w trybie
  art. 61 u.o.t.p.TK) lub nowszy format `OTK-A RRRR/N/poz.` — podawaj ten
  identyfikator OBOK sygnatury przy cytowaniu, jeśli jest dostępny (zwiększa
  weryfikowalność cytatu niezależnie od tego, czy link jest jeszcze aktywny).
- Wzorzec URL bezpośredniego dokumentu: `otkzu.trybunal.gov.pl/downloadOTK?mpo=NUMER`
  — numer `mpo` nie jest przewidywalny z sygnatury, wymaga wyszukania.

⚠️ OTK ZU, tak jak główna wyszukiwarka TK, obejmuje pełnym pokryciem
orzeczenia od momentu elektronizacji publikacji — dla bardzo starych wyroków
(lata 90.) sprawdź czy dokument w ogóle istnieje w tej postaci, zanim uznasz
brak wyniku za błąd wyszukiwania.

**Zasada 6 — Status „Źródło niepotwierdzone w portalu sądowym".**
Gdy orzeczenie pojawia się w wynikach wyszukiwania, ale nie można uzyskać
bezpośredniego URL z oficjalnego portalu sądowego:
  → Oznacz statusem: „Źródło niepotwierdzone w portalu sądowym"
  → NIE używaj określenia „niezweryfikowane"
  → NIE powołuj w piśmie procesowym bez potwierdzenia URL
  → Poinformuj użytkownika że weryfikacja bezpośrednia nie była możliwa

**Zasada 7 — Hierarchia portali (TSUE i ETPC jako pełnoprawne źródła):**
```
Tier 1 (krajowe PL): sn.pl (link = karta …/wyszukiwarka-orzeczen?orzeczenie=ID) · orzeczenia.ms.gov.pl + sieć lokalna SA/SO/SR (Zasada 5A)
                      · orzeczenia.nsa.gov.pl = CBOSA (NSA + wszystkie 16 WSA)
                      · trybunal.gov.pl + otkzu.trybunal.gov.pl (Zasada 5B —
                        równoważne, ten sam organ, archiwum pełnych tekstów)
                      · orzeczenia.uzp.gov.pl = KIO + SO/SA/SN ws. PZP (Faza 1-K) —
                        referencyjne, nie źródło prawa (art. 87 Konstytucji), ale
                        Tier 1 dla praktyki DR-07
Tier 2 (UE/EU):      curia.europa.eu · hudoc.echr.coe.int
Tier 3 (backup):     saos.org.pl — agregator akademicki, RZĄD 3; tylko gdy baza
                      urzędowa nie działa albo nie daje trwałego linku
Tier 4 (zagraniczne): patrz sekcja „Jurysdykcje zagraniczne"
```

⛔ **Nota o dwóch skalach (dodane 2026-09-13, F-185).** „Tier" w tym skillu mierzy
**dopuszczalność jako źródła potwierdzenia sygnatury w piśmie procesowym**;
„RZĄD" w `shared/HIERARCHIA-ZRODEL.md` mierzy **moc źródła co do treści**.
Od 2026-10-06 SAOS = Tier 3 i RZĄD 3 (agregator akademicki) — jedna ranga; najpierw
baza urzędowa sądu właściwego dla repertorium, SAOS zastępczo przy jej awarii.

⛔⛔ **STAN KANAŁÓW TIER 1 — dostępność jest właściwością bieżącego runtime, nie stałą.**
Pomiar z 2026-09-13 wykazał niedostępność CBOSA w tamtym środowisku, ale nie wolno
przenosić tego statusu na kolejną sesję bez świeżej próby. Dla każdego kanału
stosuj aktualny pomiar z `shared/DOSTEP-MASZYNOWY-API.md` oraz poniższe reguły:
- `orzeczenia.ms.gov.pl` — GET po sygnaturze, patrz Faza 1-S;
- `sn.pl` — `snproxy` JSON, neutralny UA; przy 403 WAF/captcha nie obchodź ochrony —
  Faza 1-0 D (sesja użytkownika, SAOS sprzed 2017, plik);
- `orzeczenia.nsa.gov.pl` (CBOSA) — **najpierw fresh probe**. Jeżeli portal zwraca
  właściwy HTML, wczytaj `references/CBOSA-ADAPTER.md` i użyj deterministycznego
  kontraktu `POST /cbo/search → /cbo/find?p=N → /doc/{ID}`; przy hoście z
  wykonaniem kodu użyj `tools/cbosa_parser.py`. Adapter filtruje CAŁY zbiór po
  exact-match i zwraca `FOUND / NOT_FOUND / AMBIGUOUS / OUT_OF_SCOPE`.
  Jeżeli bezpośredni kanał CBOSA nie działa — wróć do kanonicznego
  `shared/SYGNATURY.md`, V-SYG-0.5 RETRIEVAL/SNAPSHOT. Wymuś POST-CHECK HOSTA
  i exact-match. Jeśli host retrieval przekazuje oficjalny `/doc/{ID}`, zachowaj
  jego faktyczny `content_scope` (metryka+sentencja; czasem uzasadnienie) do
  researchu i analizy. Provenance pozostaje `CRAWLED_OR_INDEXED`; brak
  exact-hit = OUT_OF_SCOPE, nigdy NOT_FOUND;
- `trybunal.gov.pl` / `ipo` oraz `orzeczenia.uzp.gov.pl` — stosuj ich aktualny
  kontrakt z `shared/DOSTEP-MASZYNOWY-API.md`; brak deterministycznego filtra
  po sygnaturze nie uprawnia do zgadywania.

Orzeczenia TSUE i ETPC mają status równoważny z Tier 1 dla materii objętej prawem UE
lub Konwencją. Kategoria 5 (UE/TSUE) obejmuje teraz również orzeczenia ETPC.
CBOSA jest bazą jednolitą — nie ma odrębnych portali per WSA; jedno wyszukiwanie
obejmuje NSA i wszystkie 16 WSA.

**Zasada 8 — Uchwały SN z mocą zasady prawnej (Kat. 6A — priorytet):**
Uchwały pełnego składu SN, połączonych izb lub całej izby oraz uchwały
składu 7 sędziów SN, którym nadano moc zasady prawnej (art. 87 § 1 ustawy
z 8 grudnia 2017 r. o Sądzie Najwyższym, Dz.U. 2023 poz. 1093), tworzą kategorię
6A — wyższą rangą niż zwykłe orzeczenia SN.
Wiążą wszystkie składy orzekające SN (odstąpienie wymaga uchwały całej Izby).
Sędziowie sądów powszechnych nie są nimi formalnie związani, lecz mają
fundamentalne znaczenie praktyczne dla całego systemu.
Gdy takie uchwały są dostępne → ZAWSZE powołuj jako pierwsze w piśmie.
Weryfikacja: https://www.sn.pl/pl/wyszukiwarka-orzeczen (snproxy; link = karta `?orzeczenie=ID`)

**Zasada 9 — Dopasowanie tezy do oczekiwanego rozstrzygnięcia.**
Wyszukiwanie ma na celu znalezienie orzeczeń, których teza i sentencja są
maksymalnie zbieżne z oczekiwanym rozstrzygnięciem sprawy (patrz Faza 0-C
i Faza 1-D). Bliskość dopasowania oceniaj wg trzech kryteriów łącznie:
(1) zgodność stanu faktycznego z instytucją/przesłankami sprawy,
(2) zgodność kierunku rozstrzygnięcia (nie tylko tematu, ale wyniku sprawy),
(3) aktualność linii (Faza 3). Orzeczenie zgodne tematycznie, ale o odwrotnym
kierunku rozstrzygnięcia, NIE jest „dopasowane" — trafia do Kat. 3B lub 4
wg reguł Fazy 2, nigdy nie jest prezentowane jako wspierające tezę.

**Zasada 10 — ⛔ Zakaz ukrywania liczebnej przewagi linii przeciwnej.**
Gdy w wynikach wyszukiwania (Faza 1 + Faza 1-D) liczba orzeczeń o kierunku
przeciwnym do oczekiwanego jest równa lub większa niż liczba orzeczeń zgodnych,
LUB orzeczenia przeciwne stanowią ≥ 50% wszystkich trafień w Kat. 1–2 —
wygeneruj alert krytyczny 🔴 BILANS NIEKORZYSTNY (patrz Faza 2 i Faza 4) i
umieść go jako PIERWSZY alert w zakładce Profil ryzyka, niezależnie od trybu
LAIK/PRAWNIK. Zakaz przedstawiania sprawy jako „mocnej" bez tego ujawnienia.

**Zasada 11 — ⛔ PLAN MINIMUM: 5 orzeczeń wspierających + 5 linii przeciwnej,
zawsze z przesłankami rozstrzygnięcia.**
Dotyczy każdego wyszukiwania linii orzeczniczej na poparcie tezy (nie dotyczy
pojedynczego powołania sygnatury na marginesie innej analizy).
```
PLAN MINIMUM:
[A] 5 orzeczeń NAJDOKŁADNIEJ dopasowanych do oczekiwanego rozstrzygnięcia
    (wg kryteriów Zasady 9) — to jest DOLNY próg, nie sufit: jeśli
    wyszukiwanie (Faza 1, 1-T, 1-L wg właściwości) daje więcej dobrych
    dopasowań, prezentuj wszystkie, nie ucinaj sztucznie do 5.
[B] 5 orzeczeń linii PRZECIWNEJ (Faza 1-D, Krok 2) — O ILE takie w ogóle
    istnieją w wynikach. Brak linii przeciwnej po wyczerpującym
    wyszukiwaniu (Faza 1-F nie została wywołana z powodu błędu narzędzi,
    tylko wyniki są puste) = stan FAKTYCZNY do odnotowania wprost w
    Raporcie ("nie odnaleziono linii przeciwnej po przeszukaniu [portale]"),
    nie sygnał by przestać szukać po 1–2 próbach.
```
Reguły realizacji planu minimum:
1. Dopasowanie (Zasada 9) ma pierwszeństwo przed liczbą — zakaz uzupełniania
   grupy [A] lub [B] orzeczeniem o odwrotnym kierunku albo niedopasowanym
   stanie faktycznym tylko po to, by osiągnąć 5. Jeśli po wyczerpującym
   wyszukiwaniu (wszystkie właściwe portale Tier 1–3 + Faza 1-T gdy zasadna)
   znaleziono mniej niż 5 w danej grupie — podaj tyle, ile faktycznie
   istnieje, i napisz to wprost („znaleziono 3 z planowanych 5 — wyszukiwanie
   wyczerpujące, brak dalszych trafień w [lista portali]").
2. Dla KAŻDEGO orzeczenia z obu grup — obok czterech elementów Zasady 2 —
   podaj **kluczowe przesłanki rozstrzygnięcia**: konkretne okoliczności
   faktyczne i argumenty prawne, które zdecydowały o takim, a nie innym
   wyniku (2–4 zdania, parafraza — limit cytatu z Zasady 3 nadal obowiązuje).
   Sama sygnatura + jednozdaniowa teza NIE spełnia tego wymogu.
3. Dla grupy [B] (linia przeciwna) przesłanki muszą dodatkowo wskazywać
   **czynnik odróżniający** — co w stanie faktycznym, wykładni albo etapie
   postępowania spowodowało, że sąd orzekł odwrotnie niż linia zgodna
   (np. inny moment powstania roszczenia, brak przesłanki formalnej,
   odmienna kwalifikacja prawna zdarzenia). Bez tego elementu orzeczenie
   przeciwne jest tylko wymienione, a nie wyjaśnione — niewystarczające.
4. Kolejność prezentacji w obu grupach: najpierw Kat. 6A (zasada prawna SN),
   potem pozostałe wg Zasady 7/8, w obrębie tej samej rangi — od najnowszego.
5. Plan minimum NIE zwalnia z Zasady 1 (zakaz cytowania z pamięci) ani z
   V-SYG — każde z 10 (do 5+5) orzeczeń przechodzi tę samą weryfikację co
   pojedyncze powołanie.
6. Gdy profil oczekiwanego rozstrzygnięcia nie został ustalony w Fazie 0-C
   (pytanie neutralne, analityczne) — plan minimum stosuje się analogicznie
   do Kat. 3A (linia dominująca, docelowo 5) i Kat. 3B (linia mniejszościowa,
   docelowo 5, o ile istnieje), bez podziału na „zgodne/przeciwne z interesem
   strony".
