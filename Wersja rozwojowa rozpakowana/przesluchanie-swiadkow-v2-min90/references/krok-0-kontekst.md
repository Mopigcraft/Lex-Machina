# KROK 0: wczytanie kontekstu sprawy

> Plik obowiązkowy dla KROK 0. Treść przeniesiona dosłownie z SKILL.md (refaktor 2026-10-20); SKILL.md zawiera nagłówki i streszczenia.

## KROK 0 — WCZYTAJ KONTEKST SPRAWY (przed W1)

> Cel: zasilić W1 intake danymi z analizatora (KROK 3B) lub z pliku kontekstu
> sesji (MOD-KONTEKST-SESJI TRYB IMPORT), żeby nie zaczynać od zera.
> Jeśli żadne źródło niedostępne → przejdź bezpośrednio do ETAP W1 (KROK 0
> jest OPCJONALNY, nie blokujący).

```
ŹRÓDŁO 1 — BIEŻĄCA SESJA (priorytet):
  Jeśli w tej samej sesji wykonano analizator-dowodow-v3 KROK 3B → pobierz:
    kontekst_sprawy = {
      aspekty_glowne, aspekty_poboczne,   ← MOD-PRIORYTETY-ASPEKTOW
      mapa_przepisow,                       ← MOD-MAPA-PRZEPISOW §4
      selekcja_dowodow,                     ← MOD-SELEKCJA-DOWODOW §5
      ostrzezenia_krzyzowe,                 ← MOD-SELEKCJA-DOWODOW §6
      wyniki_metod,                         ← BLOK E2a-j (streszczenia)
      chronologia_wstepna                   ← chronologia-sprawy-v1 (jeśli)
    }

ŹRÓDŁO 2 — PLIK KONTEKSTU (jeśli IMPORT_AKTYWNY z MOD-KONTEKST-SESJI):
  Jeśli użytkownik wkleił/wgrał plik kontekstu → pobierz z sekcji §2-§6
  tego pliku (już sparsowane w KROK I2 MOD-KONTEKST-SESJI).

ŹRÓDŁO 3 — BRAK KONTEKSTU:
  Jeśli żadne źródło niedostępne → pomiń KROK 0, przejdź do ETAP W1.
  Poinformuj jednym zdaniem: "Nie mam kontekstu z analizatora — zadam
  pytania o sprawę w W1."
```

### CROSS-DOCUMENT-CONSISTENCY-CHECK (dodane w audycie 3.7)

> 🔴 Aktywacja: za każdym razem, gdy w toku **tej samej sprawy** (niekoniecznie
> tej samej wiadomości) zostaje wgrany nowy dokument dowodowy — nie tylko
> przy pierwszym KROK 0.

```
Przy każdym nowym dokumencie dowodowym dotyczącym sprawy już omawianej
w tej rozmowie:

1. Zidentyfikuj fakty w nowym dokumencie, które DUBLUJĄ lub ROZSZERZAJĄ
   fakty już ustalone wcześniej w tej rozmowie (daty, kwoty, nazwiska,
   cytaty przypisywane konkretnym osobom).
2. Zestaw je wprost z wcześniejszymi ustaleniami. Jeśli występuje
   rozbieżność (np. ta sama osoba figuruje z inną datą lub kwotą w dwóch
   różnych dokumentach) — zgłoś to WPROST, zanim jakiekolwiek pytanie
   oparte na tym fakcie zostanie sformułowane lub zaakceptowane.
3. Nie wybieraj milcząco "poprawnej" wersji przy rozbieżności — przedstaw
   obie, ze wskazaniem źródła każdej, i poproś użytkownika o rozstrzygnięcie
   przed użyciem tego faktu w pytaniu do świadka.

Ryzyko zaniechania: rozbieżność wykryta dopiero na sali (przez świadka lub
pełnomocnika przeciwnej strony) niszczy wiarygodność całego pytania, nawet
jeśli istota zarzutu jest słuszna.
```

### ENTITY-DISAMBIGUATION-TABLE (dodane w audycie 3.8)

> 🔴 Aktywacja: w sprawie występuje więcej niż jeden powiązany podmiot
> prawny (różne NIP, różne nazwy firm o podobnym brzmieniu, różne adresy
> e-mail przypisane do tej samej grupy kapitałowej).

```
Prowadź i proaktywnie aktualizuj (bez czekania na prośbę użytkownika)
tabelę przypisania dokumentów i faktów do konkretnych podmiotów, np.:

| Podmiot | NIP | Dokumenty/maile z tego podmiotu | Osoby podpisujące |
|---|---|---|---|
| [SPÓŁKA-A] sp. z o.o. | [nr] | [lista] | [imiona] |
| [SPÓŁKA-B] sp. z o.o. | [nr] | [lista] | [imiona] |

Aktualizuj tę tabelę przy każdym nowym dokumencie odnoszącym się do
któregokolwiek z podmiotów. Udostępnij ją użytkownikowi, gdy:
- pojawi się pytanie dotyczące tego, który podmiot jest odpowiedzialny
  za dane działanie lub zobowiązanie,
- liczba podmiotów w sprawie przekroczy jeden i nie było jeszcze takiego
  zestawienia,
- użytkownik o to poprosi wprost.

Cel: uniknięcie sytuacji, w której przez wiele wiadomości analizuje się
dokumenty pod kątem treści, nigdy nie zestawiając ich systematycznie
względem tego, który z powiązanych podmiotów faktycznie je wystawił —
co może mieć znaczenie dla ustalenia właściwego pozwanego lub adresata
poszczególnych roszczeń.
```

### EVIDENCE-THREAD-LINKING (dodane w audycie 3.11)

> 🔴 Różnica względem CROSS-DOCUMENT-CONSISTENCY-CHECK: tamten mechanizm
> wykrywa sprzeczności między IDENTYCZNYMI faktami (ta sama osoba, inna
> data). Ten mechanizm wykrywa POWIĄZANIA TEMATYCZNE między pozornie
> różnymi faktami, które opisują to samo zjawisko z innej strony — nawet
> gdy nie dzielą żadnego identycznego słowa kluczowego.

```
Przy każdym nowym ustaleniu dowodowym (nowy dokument, nowa odpowiedź na
przeszukanie, nowy fragment zeznania) — zanim przejdziesz dalej, zapytaj
się aktywnie:

1. Czy to ustalenie opisuje TEN SAM przedmiot/zdarzenie/mechanizm co coś,
   co zostało już ustalone WCZEŚNIEJ w tej samej rozmowie, tylko z innej
   perspektywy lub w innym słownictwie? (Nie szukaj identycznych słów —
   szukaj tego samego zjawiska opisanego inaczej: np. "dokument z kwotą
   do zwrotu" wspomniany w wiadomości WhatsApp i "dokumenty wewnętrzne —
   transakcje" wspomniane w zeznaniu świadka mogą odnosić się do TEGO
   SAMEGO dokumentu, opisanego przez dwie różne osoby z przeciwstawnych
   perspektyw.)
2. Jeśli tak — przedstaw to POŁĄCZENIE wprost, jako spójną narrację,
   zamiast zostawiać oba fakty jako osobne, niepowiązane ustalenia,
   czekając aż użytkownik sam zauważy związek.
3. Zaznacz wyraźnie, czy połączenie jest PEWNE (te same konkretne dane:
   nazwisko + kwota + data) czy PRAWDOPODOBNE/DO POTWIERDZENIA (tematyczne
   podobieństwo bez twardego dowodu tożsamości) — nie przedstawiaj
   hipotezy jako ustalonego faktu.
4. Zaproponuj, jeśli to możliwe, jedno pytanie do świadka, które wprost
   testuje, czy połączenie jest prawdziwe (np. "czy dokument X, o którym
   Pani zeznała, to ten sam dokument, do którego odwoływałem się w
   wiadomości Y").

Ryzyko zaniechania: użytkownik traci mocniejszą, zunifikowaną narrację
dowodową na rzecz kilku osobnych, słabszych faktów, które w istocie
wzajemnie się potwierdzają i wzmacniają, gdyby je połączyć.
```

### PLAIN-TESTIMONY-DEFAULT (dodane w audycie 3.12) — przeciwwaga do FOUNDATION-VERIFICATION-GATE i EVIDENCE-THREAD-LINKING

> 🔴 Ostrzeżenie przed nadużyciem poprzednich mechanizmów: dążenie do
> weryfikacji założeń i łączenia wątków (FOUNDATION-VERIFICATION-GATE,
> EVIDENCE-THREAD-LINKING) NIE oznacza, że KAŻDE zeznanie świadka trzeba
> potraktować jako coś do obalenia lub reinterpretacji. Gdy proste, dosłowne
> odczytanie zeznania jest już zgodne z materiałem dowodowym i NIE jest
> niekorzystne dla użytkownika — przyjmij je wprost i zbuduj na nim, zamiast
> konstruować kontrariańską teorię ("świadek się pomylił", "świadek celowo
> przeformułował", "świadek coś ukrywa"), która nie ma oparcia w żadnej
> sprzeczności czy nieścisłości.

```
Przed zaproponowaniem alternatywnej/kontrariańskiej interpretacji zeznania:

1. Sprawdź: czy PROSTE, dosłowne znaczenie tego zeznania jest sprzeczne
   z materiałem dowodowym, czy z nim zgodne?
   - Jeśli ZGODNE i NIEKORZYSTNE dla użytkownika → to legitymny grunt do
     analizy strategicznej (jak złagodzić/skontrować), ale nie do
     zaprzeczania faktowi, który po prostu jest prawdziwy.
   - Jeśli ZGODNE i KORZYSTNE (lub neutralne) dla użytkownika → PRZYJMIJ
     WPROST jako potwierdzony fakt i buduj na nim dalszą strategię.
     Nie szukaj w nim ukrytego drugiego dna, którego nic nie sugeruje.
   - Jedynie gdy istnieje KONKRETNA, wskazywalna sprzeczność z innym
     dowodem — dopiero wtedy uzasadnione jest budowanie teorii o pomyłce,
     nieścisłości lub celowym zniekształceniu.
2. Nie myl entuzjazmu analitycznego z konfliktem interesu: nie każde
   zeznanie świadka strony przeciwnej jest z definicji wrogie lub
   wymagające obalenia — jeśli jego treść jest prawdziwa i nieszkodliwa,
   powiedz to wprost, zamiast szukać sposobu, by uczynić je spornym.
```

### Mapowanie kontekstu na pola W1

```
PO WCZYTANIU kontekstu — wypełnij wstępnie następujące pola W1 INTAKE:

WARSTWA A (dane wspólne):
  "Okoliczność dowodowa" → z aspekty_glowne: które roszczenie ma świadek
    potwierdzić lub obalić (pytaj użytkownika TYLKO o to, którego aspektu
    dotyczy ten konkretny świadek, nie ekstrahujesz tego automatycznie).
  "Typ postępowania" → z kontekstu §1 STRONY I KONTEKST (jeśli znany).

MATERIAŁ DO W2 (tezy i model przesłuchania):
  Tezy DO WYKAZANIA przez świadka → z aspekty_glowne powiązanych z
    okolicznością dowodową świadka + przepis kandydujący z mapa_przepisow.
  Tezy DO OBALENIA (kontrprzesłuchanie) → z aspekty_glowne strony przeciwnej
    (jeśli dostępne) lub z wyniki_metod MET-ACH (hipotezy najsłabsze).

MATERIAŁ DO W3 (pytania):
  Blok B (pytania potwierdzające) → zatwierdzone dowody z selekcja_dowodow
    powiązane z okolicznością dowodową świadka.
  Blok D (pytania na sprzeczności / looping) → per metoda:
    MET-ACH  → pytania eliminujące hipotezy konkurencyjne
    MET-CA   → pytania o zmianę narracji między pismami/oświadczeniami
    MET-NET  → pytania weryfikujące rolę świadka w sieci powiązań
    MET-COMP → pytania o konkretny krok proceduralny (kto/kiedy/forma)
    MET-FTL  → pytania o sekwencję dat i luki logiczne w chronologii
  Blok E (pytania których NIE ZADAWAĆ) → z ostrzezenia_krzyzowe:
    jeśli pytanie o temat X mogłoby zmusić świadka do przyznania faktu
    szkodzącego tezie T_B → BLOK E oznacza to jako "temat zakazany" z
    uzasadnieniem (HARDGATE-SD-02: konkretny fragment i konkretna teza).
  Chronologia → z chronologia_wstepna: zdarzenia do loopingu
    ("zeznał pan X, tymczasem [zdarzenie BEZSPORNE] nastąpiło Y — jak
    to możliwe?").
```

### Informacja zwrotna dla użytkownika (jeśli kontekst wczytany)

```
"Wczytałem kontekst sprawy [nazwa].

Dla tego świadka przygotowuję przesłuchanie w kontekście:
  Roszczenia: [lista aspektów_glowne — 1 linijka per roszczenie]
  Zatwierdzone dowody do potwierdzenia przez świadka: [n]
  Tematy do unikania (ostrzeżenia krzyżowe): [n] 🔴 [jeśli >0]
  Materiał do sprzeczności z metod: [lista MET-XXX których wyniki są dostępne]

Jedno pytanie: KTÓREGO roszczenia dotyczy ten świadek — lub czy ma
świadczyć o całości?"
```

Odpowiedź → przypisz świadka do konkretnego aspektu_glowne (lub "całość")
→ kontynuuj do ETAP W1 z wstępnie wypełnionymi polami.

---
