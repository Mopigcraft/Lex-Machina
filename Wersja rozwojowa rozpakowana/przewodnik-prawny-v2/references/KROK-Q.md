# KROK Q — Q.1…Q.5 (tryb Q&A)

Szczegóły kroku przeniesione ze SKILL.md (treść bez zmian). Odczyt OBOWIĄZKOWY przed pierwszą odpowiedzią w trybie Q&A.

### Q.1 — Wejście w tryb Q&A

```
LAIK:
"Jasne — pytaj o wszystko. Odpowiem na każde pytanie prostym językiem
i sprawdzę każdą odpowiedź w aktualnych przepisach zanim ją dam.
Kiedy skończymy, pomogę Ci zdecydować co zrobić."

PRAWNIK:
"Tryb Q&A — pytaj. Każda odpowiedź weryfikowana online (ELI/orzecznictwo).
Historia pytań zachowana w sesji. Po zakończeniu mogę wygenerować
analizę lub pismo na podstawie omówionych zagadnień."
```

### Q.2 — Protokół odpowiedzi Q&A

**Tryb LAIK:**
```
FORMAT KAŻDEJ ODPOWIEDZI:

[Odpowiedź po ludzku — max 3-4 zdania]
Przykład: "[przykład z życia który ilustruje zasadę]"
Co to oznacza dla Ciebie: [konkretny efekt w Twojej sytuacji]
✅ Sprawdzone: [art. X ustawy Y — źródło] lub ⚠ Nie mogłem sprawdzić online.

→ Masz kolejne pytanie, czy chcesz żebyśmy przeszli do działania?
```

**Tryb PRAWNIK:**
```
FORMAT KAŻDEJ ODPOWIEDZI:

[Odpowiedź techniczna]
Podstawa: art. X §Y [ustawa] ✅ [VER: isap.sejm.gov.pl, data]
          lub ⚠ [NIEWERYFIKOWANE — sprawdź ELI (RZĄD 1)]
Orzecznictwo: [sygnatura] ✅ [VER: źródło] (jeśli relevantne)
Implikacja procesowa: [co to oznacza praktycznie dla sprawy]

→ Follow-up: [pytanie warte zadania dalej] — lub zadaj następne.
```

### Q.3 — Weryfikacja online przy każdej odpowiedzi Q&A

```
⛔ Jeśli PRAWO-HARDGATE nie był jeszcze wczytany w tej sesji:
view shared/PRAWO-HARDGATE.md

OBOWIĄZKOWO przed każdą odpowiedzią zawierającą przepis/termin/kwotę:

1. ELI (E-1): api.sejm.gov.pl/eli/acts/DU/{rok}/{poz}/text.pdf kanałem kodu;
   host bez kanału kodu → B-1 web_search "eli.gov.pl DU {rok} {poz}" → B-2 web_fetch.
   Link ISAP podaj czytelnikowi (E-2). Aktu nie da się pobrać z RZĘDU 1 → E-3/E-4.

2. Jeśli wynik: → podaj z ✅ [VER: źródło, data]
   Jeśli brak dostępu: → podaj z ⚠ [NIEWERYFIKOWANE]
   Jeśli przepis zmieniony: → podaj aktualną wersję + zaznacz zmianę

3. Sygnatury orzeczeń: ZAKAZ cytowania z pamięci
   → weryfikuj sn.pl / orzeczenia.ms.gov.pl lub oznacz [PRZYKŁADOWA]
```

### Q.4 — Przejście z Q&A do działania

```
PO 3+ PYTANIACH — zaproponuj:

LAIK:
"Mam już dobre pojęcie o Twojej sytuacji. Mogę teraz:
1️⃣ Napisać pismo w Twojej sprawie — powiedz 'napisz pismo'
2️⃣ Ocenić Twoje szanse jeśli sprawa trafi do sądu — powiedz 'oceń szanse'
3️⃣ Sprawdzić dowody które masz — powiedz 'sprawdź dowody'
4️⃣ Kontynuować pytania — zadaj następne

Co wolisz?"

PRAWNIK:
"Na podstawie sesji Q&A ([N] pytań) mogę wygenerować:
→ Analizę pozycji procesowej (.docx / raport techniczny)
→ Pismo procesowe z uwzględnieniem omówionych zagadnień
→ Listę orzecznictwa do tez z sesji
Kontynuować Q&A czy przejść do generowania?"
```

### Q.5 — Pamięć sesji Q&A

```
Historia Q&A zostaje w kontekście rozmowy.
Przy wywołaniu PRIMARY skilla po Q&A:
→ Przekaż zebrane fakty jako wejście (nie pytaj ponownie o znane dane)
→ "Na podstawie naszej rozmowy wiem już że [X, Y, Z].
   Potrzebuję jeszcze tylko [brakujące pole]."
```
