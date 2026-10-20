# Bramki PRE-W1a: RZ-SHOW i SD-VER

> Plik obowiązkowy dla KROK PRE-W1a.4 i KROK PRE-W1a. Treść przeniesiona dosłownie z SKILL.md (refaktor 2026-10-20); SKILL.md zawiera nagłówki i streszczenia.

## KROK PRE-W1a.4 — RZ-SHOW-ZAWSZE (HARD GATE, dodane w audycie 3.17, runda 3)

> ⛔ Zaraz PO wykonaniu SD-INW/SD-REJ (poniżej), a PRZED przejściem do profilu
> świadka (KROK-PRE-W1-INTELLIGENCE), model MUSI wykonać
> `shared/MOD-REJESTR-ZALACZNIKOW-CHECKPOINT.md` FAZA 2 (RZ-SHOW)
> i wyświetlić użytkownikowi pełną listę plików ze statusem
> ✅ SPRAWDZONY / 🔶 CZĘŚCIOWO / ⬜ NIESPRAWDZONY / ➖ NIE DOTYCZY.
>
> Zasada obowiązuje w KAŻDEJ turze, w której w rozmowie obecne są dowody
> (nowo wgrane lub już wcześniej wgrane w tej sprawie) — nie tylko gdy
> użytkownik o to wprost zapyta. Reaktywne wywołanie (na pytanie
> "czy sprawdziłeś wszystko?") pozostaje w mocy jako uzupełnienie,
> nie jako jedyny tryb działania.
>
> Jeśli istnieje choć jedna pozycja ⬜/🔶 → obowiązkowe pytanie do
> użytkownika: "Czy mam teraz sprawdzić pozostałe [y] plik(i)?"
> (FAZA 3 RZ-DECYZJA z tego modułu). Nie generować tez W2 ani pytań W3
> w oparciu o materiał, dopóki użytkownik nie zdecyduje.

---

## KROK PRE-W1a — SD-VER: WERYFIKACJA KOMPLETNOŚCI SKANOWANIA DOWODÓW (HARD GATE)

> Dodano w audycie 3.13. Przyczyna: w sesji roboczej model zbudował trzy tezy
> i pytania dla świadka wyłącznie na podstawie plików tekstowych i JEDNEGO już
> zrasteryzowanego dokumentu, całkowicie pomijając 130 stron trzech dużych
> zeskanowanych plików akt osobowych — dokładnie ten typ pominięcia, przeciwko
> któremu istnieje `MOD-SKAN-DOWODOW-KOMPLETNY`. Ten skill miał go w
> `dependencies` tylko POŚREDNIO (przez `analizator-dowodow`), więc gdy ten
> drugi skill nie został wczytany, bramka nie zadziałała i nikt tego nie
> zaraportował — dopiero korekta użytkownika to ujawniła.
>
> ⛔ HARD GATE — BEZWZGLĘDNY: nie wolno wejść do KROK-PRE-W1-INTELLIGENCE
> (profil świadka), a tym bardziej do W1/W2/W3, dopóki SD-VER dla WSZYSTKICH
> dokumentów dot. świadka i sprawy nie ma statusu KOMPLET.

```
PRE-W1a.1 — WYWOŁANIE MODUŁU (bezpośrednie, nie przez analizator-dowodow):
  view shared/MOD-SKAN-DOWODOW-KOMPLETNY.md
  Wykonaj FAZĘ 0 (SD-GATE-0) → FAZĘ 1 (SD-INW) → FAZĘ 2 (SD-READ) → FAZĘ 3 (SD-VER).

PRE-W1a.2 — WYMÓG OCR JAWNY (bez tego kroku SD-READ jest niekompletny):
  Dla KAŻDEGO pliku PDF w materiale dot. świadka:
    a) sprawdź ekstrakcję tekstu (pdftotext / pdffonts) — czy >0 znaków na stronę?
    b) jeśli TAK dla wszystkich stron → plik tekstowy, kontynuuj normalnie
    c) jeśli NIE (0 znaków na ≥1 stronie) → plik lub strona jest SKANEM →
       OBOWIĄZKOWO: pdftoppm -jpeg -r 120 -f [n] -l [n] plik.pdf /tmp/strona
                    → tesseract -l pol /tmp/strona.jpg stdout
                    (lub view rastra, jeśli tesseract niedostępny)
    d) ⛔ ZAKAZ pominięcia strony/pliku z powodu "prawdopodobnie mało istotny"
       lub "duży plik" — rozmiar/liczba stron NIE zwalnia z odczytu.
    e) Krok ten jest BEZWARUNKOWY: wykonuje się automatycznie, bez czekania
       na to, aż użytkownik zauważy brak i poprosi o korektę.

PRE-W1a.3 — REJESTR KROKÓW (integracja z MOD-STEP-TRACKER):
  view shared/MOD-STEP-TRACKER.md (jeśli REJESTR jeszcze
  nie zainicjowany w tej sesji) → ST-INIT z pozycjami dedykowanymi świadkowi:
    "SW-PRE-W1a" (SD-VER świadka), "SW-PRE-W1" (WITNESS-INTELLIGENCE),
    "SW-KROK0" (kontekst), "SW-W1" (intake), "SW-W1-SUPP" (uzupełnienie),
    "SW-W2" (tezy/model), "SW-CP-W2" (checkpoint), "SW-W3" (pytania),
    "SW-W4" (próba generalna), "SW-W5" (binder), "SW-W6" (live/adaptacja).
  Każdy pominięty krok → status "⚠️ POMINIĘTY" + natychmiastowy raport do
  użytkownika (FAZA 2 MOD-STEP-TRACKER), nie odłożony do końca pracy.

PRE-W1a.4 — DOCUMENT-REFERENCED-NOT-FOUND-GATE:
  Gdy w zeznaniu, protokole lub piśmie strony pada odniesienie do KONKRETNEGO
  dokumentu (np. "notatka dołączona do akt", "kopia upomnienia", "załącznik nr X")
  — sprawdź, czy ten dokument FIZYCZNIE istnieje w przekazanym materiale (SD-REJ).
    ✅ ZNALEZIONY → połącz z właściwym D[id], kontynuuj normalnie.
    ⬛ DO WERYFIKACJI → dokument wzmiankowany, ale nieobecny w SD-REJ:
       - oznacz jawnie jako osobną pozycję "⬛ DO WERYFIKACJI — [opis dokumentu],
         wzmiankowany w [źródło], nieodnaleziony w przekazanym materiale",
       - ⛔ ZAKAZ milczącego pominięcia,
       - ⛔ ZAKAZ utożsamienia go "na wyczucie" z innym, fizycznie obecnym
         dokumentem o zbliżonej funkcji (np. odręczny dopisek na innym piśmie
         ≠ odrębna notatka służbowa, nawet jeśli oba dotyczą tego samego
         zdarzenia — to różne dokumenty, dopóki nie ma dowodu przeciwnego),
       - zapytaj użytkownika, gdzie (który protokół/minuta/inne postępowanie)
         można znaleźć ten dokument, zamiast budować tezę na przypuszczeniu.

PRE-W1a.5 — RAPORT SD-VER PRZED PIERWSZĄ ODPOWIEDZIĄ MERYTORYCZNĄ:
  Zanim padnie profil świadka, teza lub pytanie — wyświetl raport z FAZY 3
  MOD-SKAN-DOWODOW-KOMPLETNY (format CHECKPOINT SD-VER: N plików / M stron /
  K obrazów, status KOMPLET/BRAKI, lista D[id], pozycje ⬛ DO WERYFIKACJI z
  PRE-W1a.4) oraz stan REJESTRU KROKÓW z PRE-W1a.3.
  ⛔ KOMPLET → kontynuuj do KROK PRE-W1.
  ⚠️/⛔ BRAKI → wróć do SD-READ, nie przechodź dalej bez zamknięcia braków
  lub jawnej, świadomej decyzji użytkownika o kontynuacji mimo braków.
```

---
