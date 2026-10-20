# KROK PRE-W1: profil świadka i bramki analizy dokumentów

> Plik obowiązkowy dla KROK PRE-W1 i TRANSCRIPT-MINING-GATE. Treść przeniesiona dosłownie z SKILL.md (refaktor 2026-10-20); SKILL.md zawiera nagłówki i streszczenia.

## KROK PRE-W1 — WITNESS INTELLIGENCE (faza przygotowawcza)

> Cel: zanim rozpoczniesz intake W1, zbuduj pełny profil świadka i mapę źródeł.
> Moduł aktywowany automatycznie gdy dostarczone są dokumenty dotyczące świadka.
> Pełna procedura: `view przesluchanie-swiadkow-v2-min90/references/WITNESS-INTELLIGENCE.md`

```
AKTYWACJA AUTOMATYCZNA:
  Gdy użytkownik dostarcza akta / protokoły / dokumenty przed W1 intake →
  wykonaj KROK I–V z WITNESS-INTELLIGENCE przed przejściem do KROK 0.

AKTYWACJA NA ŻĄDANIE:
  Frazy: "profil świadka", "mapa źródeł", "preparation chart",
  "co świadek mógł wiedzieć", "co wiemy o świadku z akt"

WYNIK:
  → Podsumowanie KROK V → bezpośrednio zasila pola W1 INTAKE
  → Preparation chart KROK IV → FPW-1 każdego pytania W3 ma dok_id+strona
  → Mapa wiedzy KROK II → BLOK E (tematy zakazane = WIEDZA WYKLUCZONA)
  → Cytaty KROK III-D → BLOK D (sprzeczności z sekwencją 3-pytań)
```

> 🔴 **DOCUMENT-SCAN-PROMPT (dodane w audycie 3.6):**
> Przy KAŻDYM nowo wgranym dokumencie zawierającym elementy odręczne,
> skany, zdjęcia lub podpisy — zanim przejdziesz do ekstrakcji treści
> drukowanej, zadaj jednozdaniowe pytanie (lub, jeśli jakość obrazu na to
> pozwala, od razu spróbuj i zgłoś wynik): czy są tam odręczne dopiski,
> skreślenia, poprawki, parafki lub nieczytelne fragmenty, które warto
> zbadać. Nie czekaj, aż użytkownik sam zauważy i zapyta — to on dostarczył
> dokument, ale to system ma systematycznie sprawdzić, czy dokument kryje
> coś więcej niż tekst główny. Jeśli jakość obrazu nie pozwala na pewny
> odczyt — zgłoś to wprost i nie zgaduj treści z fałszywą pewnością (patrz
> KROK III-D: brak VER = nie twierdź, że fakt jest ustalony).

> 🔴 **FOUNDATION-VERIFICATION-GATE (dodane w audycie 3.8):**
> Przed zaproponowaniem teorii kryminalistycznej, stylistycznej lub
> technicznej dotyczącej dokumentu (np. artefakt tłumacza maszynowego,
> język interfejsu programu pocztowego, analiza autorstwa) — sprawdź
> DWA warunki, zanim przedstawisz teorię jako obiecującą:
> 1. Czy ten sam wzorzec/artefakt występuje też w INNYCH dostępnych
>    dokumentach z tej sprawy? Jeśli tak — zmienia to wagę dowodową teorii
>    (może ją osłabić: wzorzec powszechny ≠ wzorzec unikalny dla jednej
>    osoby/zdarzenia) i musi być to sprawdzone PRZED zaprezentowaniem,
>    nie po tym, jak nowy dokument przypadkowo to ujawni.
> 2. Czy dokument, do którego ma być zastosowana metoda, SPEŁNIA
>    STRUKTURALNY WARUNEK KONIECZNY tej metody? (np. technika odczytu
>    języka interfejsu z linii cytowania wymaga, żeby dokument BYŁ
>    odpowiedzią na wcześniejszą wiadomość — jeśli to samodzielna,
>    pierwsza wiadomość w wątku, metoda nie ma zastosowania i nie należy
>    jej proponować jako możliwej do wykonania).
> Jeśli nie sprawdzono obu warunków — teorię przedstawia się z jawnym
> zastrzeżeniem "niezweryfikowane" zamiast jako gotowy, mocny wniosek.

> 🔴 **EXHAUSTIVE-EXTRACTION-GATE (dodane w audycie 3.8):**
> Przy przeszukiwaniu archiwum lub zbioru dokumentów pod kątem "wszystkich
> przypadków X" (osób, kwot, dat, zdarzeń określonej kategorii):
> 1. Zbierz i policz WSZYSTKIE trafienia wyszukiwania (grep/keyword search),
>    nie tylko te najbardziej oczywiste lub pierwsze w kolejności.
> 2. Dla każdego akapitu/fragmentu zawierającego trafienie — sprawdź, czy
>    w TYM SAMYM fragmencie występują dodatkowe, powiązane wzmianki
>    (np. lista kilku nazwisk w jednym zdaniu), które łatwo pominąć,
>    skupiając się tylko na pierwszym/najlepiej udokumentowanym przykładzie.
> 3. Przedstaw wynik jako pełną listę z jawnie podaną liczbą znalezionych
>    przypadków, zanim uznasz zadanie za wykonane — nie przedstawiaj
>    częściowego wyniku jako kompletnego.
> Ryzyko zaniechania: użytkownik odkrywa brakujące przypadki dopiero
> własnymi, kolejnymi pytaniami, mimo że dane były dostępne od pierwszego
> przeszukania.

> 🔴 **IMMEDIATE-LOGICAL-SCAN (dodane w audycie 3.8):**
> Przy PIERWSZYM czytaniu każdego dostarczonego dokumentu — niezależnie od
> tego, czy użytkownik o to prosi — proaktywnie skanuj pod kątem
> wewnętrznych sprzeczności logicznych lub czasowych w samej treści
> dokumentu (np. zachowanie opisane słowem sugerującym powtarzalność
> "systematyczne", "notoryczne", "wielokrotne" przypisane do jednej,
> pojedynczej daty; role sprawcy i zgłaszającego zamienione miejscami
> względem opisanych faktów). Takie sprzeczności zgłoś w PIERWSZEJ analizie
> dokumentu, nie dopiero gdy użytkownik zapyta wprost "czy to nie jest
> ogólnikowe" lub podobne pytanie naprowadzające — to nie wymaga żadnego
> dodatkowego materiału, tylko uważnego czytania tego, co już dostępne.

> 🔴 **LEGAL-ELEMENT-MATCH-CHECK → rozbudowany do PRZESŁANKI-GATE (audyt 3.9):**
> Gdy dokument zarzuca Panu popełnienie czynu zabronionego (powołanie na
> przepis Kodeksu karnego) LUB stanowi podstawę zwolnienia dyscyplinarnego
> albo kary porządkowej (art. 52 KP, art. 108-109 KP) — przy PIERWSZYM
> czytaniu tego dokumentu wykonaj pełny, ustrukturyzowany przegląd, nie
> tylko wyrywkową obserwację:
>
> ```
> KROK 1 — Zidentyfikuj każdą przywołaną podstawę prawną osobno
>   (jeśli dokument cytuje kilka artykułów — każdy dostaje osobny wiersz
>   analizy, nie jedną łączną ocenę).
>
> KROK 2 — Zweryfikuj ustawowe znamiona/przesłanki KAŻDEJ podstawy
>   przez ELI (RZĄD 1) lub zweryfikowane orzecznictwo — zgodnie z PRAWO-HARDGATE,
>   zakaz cytowania znamion z pamięci bez weryfikacji. ⚠️ DODANE 2026-07-15:
>   każdy cytat z orzeczenia lub interpretacji online użyty w tej analizie
>   (np. do przygotowania pytania konfrontacyjnego opartego na tezie prawnej)
>   wymaga lokalizacji w źródle (strona/teza/punkt) + kotwicy technicznej gdy
>   możliwa — pełny standard: `orzeczenia-sadowe-v2/SKILL.md` Zasada 2B.
>   Ten sam wymóg co QUOTE-VERIFICATION-DEFAULT (patrz niżej) dla cytatów z
>   dokumentów sprawy, rozszerzony na źródła zewnętrzne.
>
> KROK 3 — Zestaw KAŻDĄ wymaganą przesłankę z tym, co dokument KONKRETNIE
>   podaje na jej poparcie (nie z tym, co dokument ogólnie twierdzi, tylko
>   z faktycznym opisem zdarzenia/dowodu, jeśli taki występuje).
>
>   🔴 **CONTEXTUAL-REBUTTAL-CHECK (dodane w audycie 3.10):** zanim oznaczysz
>   przesłankę jako 🔴 BRAK z powodu braku poparcia w SAMYM dokumencie
>   oskarżycielskim — przeszukaj WSZYSTKIE inne dokumenty już dostępne w tej
>   sprawie (własne pisma procesowe użytkownika, transkrypty zeznań innych
>   świadków, umowy, zakresy obowiązków, korespondencję), pod kątem materiału
>   POTWIERDZAJĄCEGO lub OBALAJĄCEGO tę konkretną przesłankę. Dokument
>   oskarżycielski rzadko zawiera sam w sobie pełny obraz — kontekst
>   potwierdzający lub obalający przesłankę często znajduje się w innych,
>   już przesłanych materiałach, które trzeba aktywnie przeszukać, a nie
>   czekać, aż użytkownik wskaże je wprost.
>
> KROK 4 — Zwróć wynik w formie tabeli:
>   | Podstawa prawna | Wymagana przesłanka | Co dokument podaje na poparcie | Kontekst z innych dokumentów (CONTEXTUAL-REBUTTAL-CHECK) | Ocena | Uwaga |
>   Ocena: ✅ SPEŁNIONA (opisany fakt realnie wyczerpuje przesłankę) /
>          ⚠️ NIEPEŁNA (opisano coś, ale nie wprost tę przesłankę) /
>          🔴 BRAK (dokument nie podaje nic na poparcie tej przesłanki,
>          lub opisane zachowanie jest przesłance przeciwne — np. dochodzenie
>          własnych praw podane jako "groźba bezprawna") —
>          **i żaden inny dostępny dokument tego nie potwierdza ani nie
>          obala** (dopiero po sprawdzeniu CONTEXTUAL-REBUTTAL-CHECK).
>
> KROK 5 — Sformułuj JEDNOZDANIOWY wniosek zbiorczy dla każdej podstawy
>   prawnej: czy zarzut ma pełne pokrycie w opisanych faktach, częściowe,
>   czy żadne — i czy dokument w ogóle nadaje się jako podstawa
>   ewentualnego zwolnienia dyscyplinarnego / postępowania karnego, czy
>   jest to zarzut czysto deklaratywny bez opisu skonkretyzowanego
>   zdarzenia.
> ```
>
> Ten przegląd jest wykonywany **automatycznie, jako osobna, wyraźnie
> wydzielona część pierwszej odpowiedzi** na taki dokument — nie wplatany
> pojedynczym zdaniem w szerszą analizę, i nie odkładany do momentu, gdy
> użytkownik o to poprosi. Przykład wzorca łatwego do przeoczenia bez tego
> mechanizmu: żądanie zwrotu należnych pieniędzy lub wydania własnych
> dokumentów, opisane jako "szantaż"/"groźba bezprawna" z powołaniem na
> art. 191 KK — zwykłe domaganie się przysługujących praw nie wypełnia
> typowo znamion przemocy lub groźby bezprawnej, co ujawnia się dopiero
> przy systematycznym zestawieniu przesłanki z opisem faktu, nie przy
> samym odnotowaniu, że przepis został przywołany. Drugi przykład: przesłanka
> "działanie bez upoważnienia/poza zakresem obowiązków" oznaczona jako brak
> pokrycia w jednym dokumencie (zakres obowiązków niesprecyzowany), mimo że
> własne pismo procesowe użytkownika ORAZ transkrypt zeznań świadka strony
> przeciwnej — oba już dostępne w aktach — wprost tę przesłankę potwierdzają.

> 🔴 **ROZRÓŻNIENIE 3.18 (naprawa incydentu — sprawa [SYGN-SPRAWY-2], pismo 7.10.2024):**
> PRAWO-HARDGATE (weryfikacja treści/numeracji przepisu przez web_search) i
> PRZESŁANKI-GATE (dopasowanie faktów z dokumentu do przesłanek tego przepisu)
> to DWA NIEZALEŻNE obowiązki. Wykonanie web_search potwierdzającego treść
> art. X k.k./k.p. **nie zwalnia** z obowiązku przejścia przez KROKI 3-5
> powyżej. Incydent, który to ujawnił: model zweryfikował treść 5 przepisów
> karnych przywołanych w piśmie oskarżycielskim (art. 270, 286, 191§1, 287§1,
> 212 k.k.), uznał to za wystarczające, i dopiero na wprost zadane pytanie
> użytkownika ("czy analizowałeś dokumenty pod kątem zgodności z prawem")
> wykonał właściwe zestawienie przesłanek — które ujawniło, że 3 z 5 zarzutów
> nie mają żadnego pokrycia faktycznego, a 2 z nich opisują działania
> pokrzywdzonego, które są realizacją jego własnych uprawnień (dostęp do akt
> osobowych) lub czynnością zgłoszeniową (zgłoszenie podejrzenia włamania),
> nie czynem zabronionym.
>
> **SELF-CHECK-PO-WERYFIKACJI-PRAWNEJ (obowiązkowy):** bezpośrednio po
> KAŻDYM web_search weryfikującym treść przepisu karnego lub przepisu k.p.
> stanowiącego podstawę zarzutu wobec strony w dokumencie oskarżycielskim,
> model w TEJ SAMEJ odpowiedzi zadaje sobie pytanie: "Czy zestawiłem już
> KAŻDĄ przesłankę tego przepisu z konkretnym opisem faktu w dokumencie
> (KROK 3), sprawdziłem kontekst innych dokumentów (KROK 4) i sformułowałem
> ocenę (KROK 5)? Jeśli NIE — nie kończ odpowiedzi na samej weryfikacji
> treści przepisu, przejdź do tych kroków od razu."

> 🔴 **FORMALNA-ZGODNOŚĆ-GATE (dodane w audycie 3.18):**
> Analogicznie do PRZESŁANKI-GATE, ale dla zgodności FORMALNEJ (proceduralnej)
> dokumentu, nie merytorycznej treści zarzutów. Aktywacja: dokument stanowi
> lub dokumentuje zastosowanie kary porządkowej (upomnienie, nagana, kara
> pieniężna — art. 108 k.p.) lub inną sformalizowaną czynność proceduralną
> (np. zawiadomienie o rozwiązaniu umowy). Przy PIERWSZYM czytaniu takiego
> dokumentu — RÓWNOLEGLE z PRZESŁANKI-GATE, nie zamiast niego — wykonaj
> tabelaryczne zestawienie: wymóg formalny (konkretyzacja zarzutu i daty,
> uprzednie wysłuchanie pracownika art. 109 §2, pouczenie o prawie i
> 7-dniowym terminie sprzeciwu art. 112 §1, dowód doręczenia, podpis osoby
> uprawnionej) → stan faktyczny w dokumencie → ocena ✅/⚠️/🔴. Nie odkładaj
> tego do momentu, gdy użytkownik zapyta wprost o zgodność formalną.

### TRANSCRIPT-MINING-GATE (dodane w audycie 3.10)

> 🔴 Aktywacja: dostępny jest pełny protokół/transkrypt WCZEŚNIEJSZEGO
> przesłuchania TEGO SAMEGO świadka (w tym lub powiązanym postępowaniu).

```
Przed przygotowaniem NOWYCH pytań dla świadka, którego wcześniejsze zeznania
są już dostępne w materiałach — wydobądź systematycznie z transkryptu:

1. Fakty już przyznane przez świadka (nie trzeba o nie pytać ponownie —
   chyba że celem jest technika loopingu/konfrontacji).
2. Sprzeczności między zeznaniami tego świadka a innymi dokumentami/
   zeznaniami (kandydat do BLOKU D).
3. Pytania wcześniej ZADANE i UCHYLONE przez sąd, wraz z PODANYM PRZEZ SĄD
   POWODEM uchylenia (np. "poza tezą dowodową", "hipotetyczne", "dublujące").
   Nowe pytania o tej samej naturze i tym samym ryzyku uchylenia — oznacz
   z ostrzeżeniem, że sąd już raz zastosował to kryterium wobec tego
   świadka/tej sprawy i może zrobić to ponownie.
4. Fakty ustalone przez sąd wprost w protokole (np. potwierdzone przez
   pełnomocnika, niekwestionowane) — takich nie trzeba już ponownie
   dowodzić, tylko rozwijać ich konsekwencje (patrz BLOK 4 w przykładzie
   z tej sesji: fakt wysłania wiadomości "Pracownicy YSP" był już
   niekwestionowany, więc pytania powinny rozszerzać konsekwencje, nie
   ustalać fakt od nowa).
```

---
