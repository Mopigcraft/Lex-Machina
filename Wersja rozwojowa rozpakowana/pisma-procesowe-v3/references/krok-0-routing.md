# KROK 0 — ROUTING: Test A, Test B, Test C (pełna treść)

### Test A — Czy to redakcja istniejącego pisma (nie tworzenie nowego)?

```
TAK, gdy WSZYSTKIE są prawdą:
  ✓ Użytkownik dostarczył treść GOTOWEGO pisma (wklejona / plik)
  ✓ Żądanie dotyczy formy/stylu/długości/tonu, nie nowej argumentacji
  ✓ Nie proszono o dodanie nowych przepisów/orzeczeń/zarzutów

Sygnały: "popraw to pismo", "zredaguj", "skróć", "wzmocnij ton", "przeredaguj
na bardziej stanowczy/neutralny/negocjacyjny", "wygładź styl", "sprawdź i
popraw" (po raporcie z KROK F przewodnika).

→ TAK: przejdź do `modules/MOD-REDAKCJA.md` — NIE wykonuj W1-W2-W3, NIE
  sprawdzaj Testu B/C.
→ NIE: przejdź do Testu B.

Test A ma priorytet — jeśli użytkownik dostarczył gotowe pismo i prosi
o poprawki formy, nie kwalifikuj tego jako "pismo proste" (Test B) ani
nie uruchamiaj W1 (Test C) — to są ścieżki dla pism PISANYCH OD ZERA.
```

### Test B — Czy to pismo proste?

Pismo proste = spełnia WSZYSTKIE trzy warunki:
1. Jedno żądanie procesowe
2. Jedna podstawa prawna (nie wymaga analizy wielowątkowej)
3. Należy do katalogu: sprzeciw od nakazu (art. 505 § 1 KPC — ⛔ art. 503 uchylony),
   zarzuty od nakazu (art. 493 § 1 KPC; termin obu — art. 480² § 2 KPC), wniosek o klauzulę (art. 781 KPC), wniosek o wszczęcie
   egzekucji (art. 797 KPC), zabezpieczenie (art. 730 KPC), zwolnienie od kosztów
   (art. 102 KSCU), uzasadnienie wyroku (art. 328 § 1 KPC), przywrócenie terminu
   (art. 168 KPC), wezwanie przedsądowe (art. 455 KC), wgląd do akt (art. 9 KPC),
   doręczenie przez komornika (art. 139¹ KPC), sprzeciw od orzeczenia referendarza
   (art. 398²² KPC).

→ TAK na wszystkie 3: nie pisz pisma; zaproponuj `pisma-proste-v2` tym komunikatem i zapytaj użytkownika:

```
REDUKCJA DO pisma-proste-v2
Przyczyna: [rodzaj pisma z katalogu; jedno żądanie; jedna podstawa prawna]
Czy przełączyć na pisma-proste-v2?
```

W aplikacji Lex Machina wątek z wybranym skillem przełącza aplikacja po zgodzie użytkownika.
→ NIE na którykolwiek: przejdź do Testu C i kontynuuj model trzech wiadomości.

### Test C — Intake (dane minimalne)

Przed W1 ustal minimum — brakujące dane = jedno pytanie zbiorcze:

```
□ TYP PISMA:    [pozew / apelacja / sprzeciw / wniosek / riposta / zawiadomienie]
□ DZIEDZINA:    [cywilna / pracownicza / karna / administracyjna / gospodarcza]
□ STRONY:       [powód/wnioskodawca + pozwany/uczestnik]
□ ETAP:         [nowa sprawa / sprawa w toku — sygnatura: ___]
□ CEL:          [co osiągnąć tym pismem]
□ MATERIAŁY:    [czy użytkownik dostarczył dokumenty/akta — TAK/NIE]
```

Po uzyskaniu danych stron — oznacz każdy podmiot prowadzący działalność jako ⚠️POD.
Weryfikacja ⚠️POD następuje w W3.0 (PODMIOT-GATE). W W1 i W2 stosuj dane
dostarczone przez użytkownika z adnotacją ⚠️POD — nigdy nie wpisuj danych
rejestrowych z pamięci (NIP, KRS, REGON, adres, skład zarządu).

Gdy brak danych: view shared/INTAKE-GAP.md
