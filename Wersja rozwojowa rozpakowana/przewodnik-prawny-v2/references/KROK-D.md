# KROK D — PISMO (D.1…D.4)

Szczegóły kroku przeniesione ze SKILL.md (treść bez zmian). Odczyt OBOWIĄZKOWY przed D.1.

### D.1 Ocena złożoności

```
"Opowiedz mi w kilku zdaniach o co chodzi i co chcesz pismem osiągnąć."

PROSTE (jedno żądanie, jedna podstawa prawna):
  Wyjaśnij: "To pismo możemy napisać szybko. Potrzebuję kilku danych..."
  → view pisma-proste-v2/SKILL.md
  → INTAKE sekwencyjny (jedno pytanie na raz z wyjaśnieniem po co)
  → MOD-FAKTY (jeśli są materiały źródłowe)
  → HYBRID-VALIDATION → docx-skill → present_files

ZŁOŻONE (wiele wątków, orzecznictwo, obalanie strony przeciwnej):
  Wyjaśnij: "To bardziej złożone — pismo wymaga analizy prawnej
  i wyroków sądów. Przeprowadzę Cię krok po kroku..."
  → view pisma-procesowe-v3/SKILL.md
  → INTAKE + KROK D.2
```

### D.2 INTAKE sekwencyjny — zbieranie danych do pisma

```
⛔ Przed rozpoczęciem zbierania danych:
view shared/INTAKE-GAP.md

Dla każdego wymaganego pola — PRZED pytaniem wyjaśnij po co:

ZAMIAST: "Podaj wartość przedmiotu sporu."
POWIEDZ:  "Potrzebuję kwoty o którą się spierasz — od tego zależy
           ile zapłacisz za złożenie sprawy i do jakiego sądu idziesz.
           Ile wynosi ta kwota?"

ZAMIAST: "Wskaż sygnaturę akt."
POWIEDZ:  "Czy masz numer sprawy z sądu? To ciąg liter i cyfr na piśmie,
           np. 'I C 123/25'. Jeśli nie masz pisma z sądu — wpisz 'nowa'."

ZAMIAST: "Podstawa prawna roszczenia."
POWIEDZ:  "Właściwe przepisy znajdę sam — Ty nie musisz ich znać.
           Powiedz tylko co się stało i czego chcesz."

Pola opcjonalne → "(możesz pominąć — wpisz 'dalej')"
```

### D.3 Weryfikacja faktów przed generowaniem (MOD-FAKTY)

```
Gdy użytkownik dostarczył dokumenty jako materiał źródłowy:
→ view shared/FAKTY_v2.md
→ "Sprawdzam teraz czy każdy fakt który trafi do pisma
   ma potwierdzenie w Twoich dokumentach..."
→ Wynik ✅ wymagany przed generowaniem

Brak dokumentów:
→ każdy fakt bez źródła = ⬛ [UZUPEŁNIJ] w piśmie
```

### D.4 Po wygenerowaniu pisma

```
1. Dostarcz pismo przez docx-skill → zapisz w katalogu wyjściowym hosta
   (claude.ai: /mnt/user-data/outputs/; UNIVERSAL-RUNTIME-ADAPTER §4) → present_files lub odpowiednik hosta
2. LAIK — instrukcja złożenia:
   "Oto gotowe pismo. Teraz:
   📌 Wydrukuj [X] egzemplarzy
   📌 Złóż w [sąd/urząd] — adres: [adres]
   📌 Zachowaj potwierdzenie złożenia
   📌 Termin: do [data]"
3. Zaproponuj Raport Sytuacyjny jeśli sprawa złożona:
   view shared/raport-sytuacyjny-integracja.md
4. PRAWNIK — zaproponuj raport dla klienta:
   "Czy wygenerować raport statusu sprawy dla klienta?
   → Powiedz 'raport dla klienta' żebym przygotował dokument zewnętrzny."
   (wywołuje raport-klienta-v1 po potwierdzeniu)
5. → KROK I (co dalej?)
```
