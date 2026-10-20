# Faza 1-D, 1-Z, 1-F (dopasowanie, kontrola zgodności, fallback) — orzeczenia-sadowe-v2

> Plik przeniesiony ze SKILL.md bez zmian treści (progressive disclosure). Wczytaj w całości przed wykonaniem odpowiedniego kroku.

## Faza 1-D — Dopasowanie tezy i test kierunku przeciwnego

Cel: znaleźć orzeczenia maksymalnie zbieżne z oczekiwanym rozstrzygnięciem
(Faza 0-C, Zasada 9) I jednocześnie rzetelnie sprawdzić, czy istnieje liczna
linia przeciwna (Zasada 10) — bez tego dwuetapowego podejścia wynik jest
stronniczy (confirmation bias) i niewiarygodny procesowo.

```
KROK 1 — Wyszukiwanie zgodne z oczekiwanym kierunkiem:
  Użyj fraz z Faza 0-B + słów kluczowych zgodnych z OCZEKIWANYM KIERUNKIEM
  (np. dla „oddalenie powództwa": „bezzasadność roszczenia", „brak przesłanek").

KROK 2 — Wyszukiwanie kierunku przeciwnego (OBOWIĄZKOWE, nie pomijaj):
  Te same frazy bazowe + słowa kluczowe zgodne z KIERUNKIEM PRZECIWNYM
  (np. „uwzględnienie powództwa", „zasadność roszczenia").
  Wykonaj minimum 2 zapytania w tym kroku, nawet jeśli Krok 1 dał dużo trafień.
  Cel ilościowy (Zasada 11, PLAN MINIMUM [B]): 5 orzeczeń linii przeciwnej,
  o ile istnieją — jeśli po 2 zapytaniach jest ich mniej niż 5, a Krok 1 (linia
  zgodna) dał dużo trafień, kontynuuj wyszukiwanie kierunku przeciwnego
  (kolejne portale/frazy) zanim uznasz temat za wyczerpany.

KROK 3 — Ocena dopasowania (per orzeczenie, wg Zasady 9):
  Klasyfikuj każde trafienie jako: ZGODNE (kierunek = oczekiwany) /
  PRZECIWNE (kierunek = przeciwny) / NEUTRALNE (dotyczy instytucji,
  ale rozstrzygnięcie nie przesądza kierunku, np. z innych przyczyn procesowych).

KROK 4 — Policz i przekaż do Fazy 2/4:
  N_zgodne, N_przeciwne, N_neutralne → wylicz BILANS (patrz Faza 2, Faza 4).
```

Jeśli profil oczekiwanego rozstrzygnięcia nie został ustalony w Fazie 0-C
(pytanie neutralne) → pomiń tę fazę, prowadź wyszukiwanie bez podziału na
kierunki, kategoryzuj wyłącznie wg Fazy 2 (Kat. 3A/3B linia większościowa/mniejszościowa).

---

## Faza 1-Z — Kontrola zgodności trafienia z pytaniem (przed prezentacją)

⛔ Klasa błędu (2026-10-13, aplikacja 0.1.27): prawdziwa sygnatura WSA
(II SAB/Po 175/26, bezczynność w udostępnieniu informacji publicznej) podana
jako orzeczenie o halucynacjach AI pełnomocnika — treść dopisana z pytania,
nie z pobranego dokumentu.

Przed przedstawieniem każdego orzeczenia jako trafienia:

1. **Tożsamość z pobranego tekstu** — sąd, sygnatura, data, forma i
   przedmiot sprawy odczytane z dokumentu w tej sesji. Sama zgodność sygnatury
   z rekordem nie potwierdza tematu.
2. **Treść tylko z dokumentu** — opis orzeczenia (czego dotyczy, co sąd uznał)
   wyłącznie z odczytanej metryki, sentencji lub uzasadnienia. Pojęcie z
   pytania, którego nie ma w tekście, nie trafia do opisu.
3. **Każde kryterium pytania osobno** — np. „AI”, „pełnomocnik zawodowy”,
   „sąd inny niż SN”. Orzeczenie spełniające część kryteriów opisz jako
   częściowe z nazwaniem brakującego; niespełniające — nie jest trafieniem.
4. **Brak trafień** = wprost: „nie znalazłem orzeczenia spełniającego te
   kryteria” + co sprawdzono (`OUT_OF_SCOPE`, nie dowód braku orzeczenia).
   Ponowna prośba użytkownika o „inny wyrok” nie uzasadnia dopasowania
   zastępczego.
5. **Bez zapowiedzi zamiast wyniku** — „szukam teraz…”, „przeszukuję…” bez
   wyniku w tej samej odpowiedzi jest zakazane: wykonaj wyszukiwanie narzędziami
   i podaj wynik albo brak trafień.
6. **Pytanie „co zawiodło”** — odpowiadaj z faktów: rejestr aplikacji przy
   poprzedniej odpowiedzi (`[Rejestr aplikacji dla tej odpowiedzi: …]`) i
   faktycznie wykonane wywołania. Bez domysłów („prawdopodobnie”); czego nie
   widać w rejestrze, nazwij jako nieustalone.

Aplikacja Lex Machina sprawdza punkt 2 mechanicznie
(`CASE_CONTENT_GROUNDING`: pojęcia z pytania przypisane orzeczeniu i cytaty
podane jako słowa sądu muszą występować w tekście pobranym w tej turze;
rozjazd = runda korekty, potem ostrzeżenie przy odpowiedzi) oraz znaczeniowo
(`CASE_SEMANTIC_CHECK`: podpięty model w osobnym kontekście ocenia, czy
orzeczenie, interpretacja, inne orzeczenie z sygnaturą (TK, KIO, TSUE, UODO,
ETPC) lub zweryfikowany przepis dotyczy pytania i czy opis w odpowiedzi wynika
z tekstu; ocena musi cytować dokument dosłownie, aplikacja sprawdza cytat).
7. **Stanowisko organu, nie strony** — teza przypisana orzeczeniu lub
   interpretacji musi pochodzić z rozstrzygnięcia, tezy albo oceny właściwego
   organu (sąd, Dyrektor KIS, KIO, TK, UODO). Zarzut skargi lub apelacji,
   wniosek, stanowisko wnioskodawcy w interpretacji, argument rządu,
   prokuratora czy uczestnika i zdanie odrębne nie są stanowiskiem organu.
   W interpretacji indywidualnej najpierw wynik oceny („stanowisko
   wnioskodawcy jest prawidłowe/nieprawidłowe”), potem uzasadnienie organu.
8. **Określenie sprawy przed tekstem** — przedmiot sprawy z metryki („w
   przedmiocie…”, hasła tematyczne, temat interpretacji) porównaj z pytaniem
   przed lekturą uzasadnienia; wyraźnie inny przedmiot = nie jest trafieniem.
   Przy liście kandydatów najpierw odsiej po przedmiocie, pełny tekst czytaj
   tylko dla pozostałych.

Aplikacja dodatkowo: oznacza role fragmentów (ROZSTRZYGNIĘCIE, TEZA, OCENA
ORGANU ORZEKAJĄCEGO, STANOWISKO STRONY, ZDANIE ODRĘBNE) i przypina
[OKREŚLENIE SPRAWY] na początku tekstu dla kontrolera; poprawia odpowiedź tylko
przy temacie NO_MATCH lub twierdzeniu nie w pełni wspartym; sprawdza sąd
przypisany sygnaturze (`CASE_COURT_ATTRIBUTION`: np. sygnatura NSA podana
jako wyrok SN).
To kontrola następcza — punkty 1–4, 7 i 8 wykonujesz sam przed oddaniem odpowiedzi.

---

## Faza 1-F — Fallback (niedostępność narzędzi)

Wykonaj gdy web_search lub web_fetch zwrócą błąd, timeout lub są niedostępne:

```
FALLBACK F-1: web_search niedostępny
→ Poinformuj użytkownika: „Wyszukiwanie w internecie chwilowo niedostępne —
  brak tropów z sieci." Rejestry urzędowe (verify_case_reference, search_case_law,
  CBOSA, portal sądu) działają dalej: sygnatury podane przez użytkownika lub
  z akt weryfikuj normalnie. Nie podam sygnatur bez weryfikacji."
→ Zaoferuj: opis instytucji prawnej i przesłanek bez powołania konkretnych sygnatur
→ Zalecenie: sprawdź orzeczenia samodzielnie na sn.pl, orzeczenia.ms.gov.pl,
  orzeczenia.nsa.gov.pl; saos.org.pl tylko w zasięgu (SP; SN do 2016, TK do 2015, KIO do 2018)

FALLBACK F-2: web_fetch na portalu sądowym zwraca błąd (portal niedostępny)
→ Przejdź do następnego portalu w hierarchii
→ Po wyczerpaniu wszystkich portali Tier 1–3: status „Brak potwierdzenia URL"
→ NIE powołuj bez potwierdzonego URL

FALLBACK F-3: wyniki wyszukiwania prowadzą do płatnej bazy (LEX, Legalis) lub serwisu wtórnego
→ Zapisz: „Dostęp płatny — nie cytuję." (serwis wtórny: „źródło wtórne — nie cytuję")
→ Nie lekceważ wyniku: weź z tytułu i fragmentu tropy — sygnaturę i datę orzeczenia,
  oznaczenie nowelizacji (Dz.U. rok, poz.), datę wejścia w życie — i sprawdź każdy
  według gradacji źródeł: sygnatura → baza urzędowa (Faza 1-0 A; SAOS tylko w zasięgu),
  nowelizacja i data → ELI / Dz.U. (verify_legal_reference z datą zdarzenia).
→ Trop niepotwierdzony urzędowo zostaje ⚠️ [NIEWERYFIKOWANE]; teza i cytat wyłącznie
  ze zweryfikowanego tekstu urzędowego.

FALLBACK F-4: luka pokrycia przesłanek < 40% po wyczerpaniu wyszukiwania
→ Alert luki: „Brak orzeczeń potwierdzających [przesłanka X]"
→ Rozszerz frazę lub zmień kategorię wyszukiwania
→ Jeśli nadal brak: poinformuj o luce w Raporcie
```
