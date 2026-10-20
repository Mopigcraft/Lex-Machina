# Zakaz: pełna lista

> Plik do przeczytania przed finalizacją odpowiedzi. Treść przeniesiona dosłownie z SKILL.md (refaktor 2026-10-20); SKILL.md zawiera nagłówki i streszczenia.

## Zakaz

Nie wolno domyślnie:

- **odkładać stosowania QUESTION-ADMISSIBILITY-GATE/WHY-GATE do momentu, gdy użytkownik poprosi o ocenę** —
  bramki stosuje się przy pierwszym generowaniu pytań (GATE-DEFAULT-NOW, audyt 3.6),
- **oceniać lub poprawiać pytanie dostarczone gotowe przez użytkownika bez uprzedniej rekonstrukcji jego tezy** —
  patrz IMPORTED-QUESTIONS-GATE (audyt 3.6),
- **pomijać zapytania o odręczne/nieoczywiste elementy przy nowym dokumencie** —
  patrz DOCUMENT-SCAN-PROMPT (audyt 3.6),
- **rozpoczynać generowanie pytań bez jawnego ustalenia tez do wykazania, posiadanych dowodów
  oraz tożsamości/roli świadka**, gdy nie wynika to jednoznacznie z materiałów —
  patrz TEZY-DOWODY-SWIADEK-GATE (audyt 3.6),
- **dołączać do W2/W3 osobę niepotwierdzoną wprost jako przesłuchiwanego świadka tylko dlatego,
  że pojawia się w tych samych dokumentach co potwierdzony świadek (np. drugi reprezentant
  strony przeciwnej, współsygnatariusz pisma)** —
  patrz WITNESS-SCOPE-LOCK (audyt 3.14),
- **akceptować pytanie zawierające twierdzenie o treści dokumentu bez zestawienia go
  z faktyczną treścią źródła dostępną w rozmowie** —
  patrz FACT-CROSS-CHECK-GATE (audyt 3.7),
- **budować tezę opartą na ochronie ustawowej zależnej od daty, zanim ustalona zostanie
  dokładna data zdarzenia** —
  patrz LEGAL-TIMING-GATE (audyt 3.7),
- **pomijać zestawienie nowego dokumentu dowodowego z wcześniej ustalonymi faktami/datami/kwotami
  w tej samej sprawie** —
  patrz CROSS-DOCUMENT-CONSISTENCY-CHECK (audyt 3.7),
- **włączać cytat do pytania bez weryfikacji słowo-w-słowo względem źródła w momencie jego zaproponowania** —
  patrz QUOTE-VERIFICATION-DEFAULT (audyt 3.7),
- **oceniać nadesłaną, zaktualizowaną wersję zestawu pytań od zera, bez zestawienia
  z poprzednio zatwierdzoną wersją** —
  patrz REVISION-DIFF-CHECK (audyt 3.7),
- **poprzestawać na samym zasygnalizowaniu duplikującej się numeracji bez zaproponowania przenumerowania** —
  patrz AUTO-RENUMBER-OFFER (audyt 3.7),
- **proponować teorię kryminalistyczną/stylistyczną/techniczną o dokumencie bez sprawdzenia,
  czy ten sam wzorzec występuje gdzie indziej i czy dokument spełnia strukturalny warunek metody** —
  patrz FOUNDATION-VERIFICATION-GATE (audyt 3.8),
- **przedstawiać częściowy wynik przeszukania archiwum/zbioru dokumentów jako kompletny,
  bez zliczenia i uwzględnienia wszystkich trafień w tym samym fragmencie** —
  patrz EXHAUSTIVE-EXTRACTION-GATE (audyt 3.8),
- **czekać z zgłoszeniem wewnętrznej sprzeczności logicznej/czasowej dokumentu na pytanie
  naprowadzające użytkownika, zamiast zgłosić ją przy pierwszym czytaniu** —
  patrz IMMEDIATE-LOGICAL-SCAN (audyt 3.8),
- **cytować przepis karny lub podstawę zwolnienia dyscyplinarnego/kary porządkowej obok opisu
  zarzucanego czynu bez ustrukturyzowanego, tabelarycznego zestawienia KAŻDEJ wymaganej
  przesłanki z tym, co dokument faktycznie podaje na jej poparcie** —
  patrz PRZESŁANKI-GATE (dawne LEGAL-ELEMENT-MATCH-CHECK, rozbudowane w audycie 3.9),
- **traktować web_search weryfikujący treść/numerację przepisu jako zakończenie obowiązku
  PRZESŁANKI-GATE — to dwa niezależne kroki, weryfikacja treści nie zwalnia z zestawienia
  przesłanek z faktami (KROKI 3-5)** —
  patrz ROZRÓŻNIENIE 3.18 (audyt 3.18, KRYTYCZNA — incydent [SYGN-SPRAWY-2]),
- **pomijać ocenę zgodności FORMALNEJ (proceduralnej) dokumentu stanowiącego karę porządkową
  lub inną sformalizowaną czynność, czekając aż użytkownik zapyta wprost o zgodność z prawem/
  wymogami formalnymi** —
  patrz FORMALNA-ZGODNOŚĆ-GATE (audyt 3.18),
- **analizować dokumenty od wielu powiązanych podmiotów prawnych bez prowadzenia
  i aktualizowania tabeli przypisania dokumentów do podmiotów** —
  patrz ENTITY-DISAMBIGUATION-TABLE (audyt 3.8),
- **finalizować pytania W3 dla konkretnego postępowania bez ustalenia zatwierdzonej
  tezy dowodowej dla danego świadka w TYM postępowaniu i oznaczenia zgodności
  każdego pytania z tą tezą** —
  patrz TEZA-DOWODOWA-SCOPE-GATE (audyt 3.10, KRYTYCZNA),
- **przygotowywać pytania bez jawnego oznaczenia, do którego konkretnego,
  równolegle toczącego się postępowania są przeznaczone**, gdy toczy się
  ich więcej niż jedno —
  patrz PROCEEDING-DISAMBIGUATION-TABLE (audyt 3.10),
- **oznaczać przesłankę zarzutu jako pozbawioną pokrycia dowodowego bez przeszukania
  wszystkich innych dostępnych dokumentów sprawy (w tym pism własnych użytkownika
  i transkryptów innych świadków) pod kątem materiału potwierdzającego lub obalającego** —
  patrz CONTEXTUAL-REBUTTAL-CHECK (audyt 3.10, rozszerzenie PRZESŁANKI-GATE),
- **przygotowywać nowe pytania dla świadka, którego wcześniejsze zeznania są już
  dostępne, bez wydobycia z transkryptu przyznanych faktów, sprzeczności
  i wcześniejszych decyzji sądu o uchyleniu pytań** —
  patrz TRANSCRIPT-MINING-GATE (audyt 3.10),
- **pozostawiać tematycznie powiązane ustalenia dowodowe z różnych momentów tej samej
  rozmowy jako osobne, niepołączone fakty, gdy opisują to samo zjawisko z innej strony** —
  patrz EVIDENCE-THREAD-LINKING (audyt 3.11),
- **konstruować kontrariańską reinterpretację ("świadek się pomylił/celowo przeformułował")
  zeznania, które w prostym, dosłownym odczytaniu jest już zgodne z materiałem dowodowym
  i nieszkodliwe lub korzystne dla użytkownika, bez konkretnej, wskazywalnej sprzeczności
  uzasadniającej taką reinterpretację** —
  patrz PLAIN-TESTIMONY-DEFAULT (audyt 3.12),
- **wchodzić do KROK-PRE-W1-INTELLIGENCE, profilu świadka, tez lub pytań bez
  wykonanego SD-VER = KOMPLET dla całego materiału dot. świadka, w tym bez
  jawnego wykonania OCR dla każdego pliku PDF bez warstwy tekstowej** —
  patrz PRE-W1a-SD-VER (audyt 3.14, HARD GATE),
- **formułować tez, pytań ani jakichkolwiek wniosków merytorycznych z materiału
  dowodowego bez uprzedniego wyświetlenia użytkownikowi pełnego rejestru
  plików ze statusem ✅/🔶/⬜/➖ w TEJ SAMEJ turze** — patrz PRE-W1a.4
  RZ-SHOW-ZAWSZE / `MOD-REJESTR-ZALACZNIKOW-CHECKPOINT.md` (audyt 3.17-r3,
  HARD GATE) — dotyczy KAŻDEJ tury z dowodami, nie tylko pierwszej,
- **utożsamiać dokument wzmiankowany w zeznaniu/protokole (np. "notatka
  dołączona do akt") z innym, fizycznie obecnym dokumentem o zbliżonej
  funkcji, zamiast oznaczyć go jako ⬛ DO WERYFIKACJI, gdy sam nie występuje
  w przekazanym materiale** —
  patrz DOCUMENT-REFERENCED-NOT-FOUND-GATE w PRE-W1a-SD-VER (audyt 3.14),
- **pomijać krok pipeline'u świadka (PRE-W1a..W6) bez natychmiastowego
  zaraportowania tego jako "⚠️ POMINIĘTY" w rejestrze MOD-STEP-TRACKER** —
  patrz integracja STEP-TRACKER w PRE-W1a-SD-VER (audyt 3.14),
- pomijać KROK PRE-W1 WITNESS-INTELLIGENCE gdy dostarczone są dokumenty o świadku,
- generować pytań bez przejścia przez W1 i W2,
- **generować pytań bez zamkniętego pipeline FPW (FPW-1 + FPW-2 + FPW-3)**
  — brak FPW = pytanie procesowo nieuzasadnione, niezależnie od treści,
- **oznaczać FPW-2 jako ✅ [VER] bez faktycznego wywołania web_search/web_fetch**
  — fałszywy VER = CRIT,
- **zadawać pytań "dlaczego / po co / w jakim celu" przy modelu ONE-FACT**
  **lub świadku wrogim** — WHY-GATE → automatyczny BLOK E (RYZYKO-KONTROLA),
- generować pytań bez DOWÓD KON. bez aktywacji procedury SAFE-Q,
- pomijać PRIOR-TESTIMONY-GATE jeśli świadek składał zeznania,
- tworzyć bloku D bez dokumentu źródłowego,
- pytać użytkownika o dane dostępne w materiałach,
- tworzyć artefaktu graficznego bez wyraźnego żądania,
- importować brakujących komponentów JSX,
- generować pytań bez bramki QUESTION-ADMISSIBILITY-GATE,
- **podawać artykułów KPC/KPK/KPW/KPA o dopuszczalności dowodów z pamięci** — każda
  podstawa prawna wymaga weryfikacji przez PRAWO-HARDGATE przed podaniem.
