# BLOK-KONSEKWENCJE — szczegóły

> **Trigger:** ZAWSZE po ustaleniu tez procesowych (MODE A/B/C).
> **Cel:** każda teza musi generować ≥2 automatyczne skutki prawne.
> **Zasada:** bez tej warstwy pismo broni tez, ale nie buduje strategii.
> **Źródło:** DTA W6 (warstwa konsekwencji).

Dla każdej tezy T-X z dashboardu wykonaj trzy kroki:

```
KROK KC1 — Skutek bezpośredni:
  "Co ta teza UDOWADNIA w sensie prawnym?"
  → wskaż normę prawną którą teza realizuje (z W1.4 / ELI RZĄD 1 ⚠ HARDGATE)
  → format: C-X.1: [skutek] → [norma]

KROK KC2 — Skutek pośredni:
  "Jakie INNE ROSZCZENIA lub ARGUMENTY wzmacnia udowodnienie tej tezy?"
  → myśl o tezie jako środku do celu, nie celu samym w sobie
  → format: C-X.2: [skutek wtórny] → [roszczenie / argument]

KROK KC3 — Skutek strategiczny (gdy nieoczywisty):
  "Jak udowodnienie tej tezy ZMIENIA pozycję procesową?"
  → wpływ na ciężar dowodu, zakres pism, orzecznictwo, ugodę
  → format: C-X.3: [zmiana pozycji] (opcjonalny)
```

Przykład (sprawa pracownicza — wzorzec [SYGN-SPRAWY]):

```
T-1: Ciągłość stosunku pracy / tożsamość pracodawcy rzeczywistego
  C-1.1: Pracodawca rzeczywisty = [SPÓŁKA-B] → żądanie zapłaty od [SPÓŁKA-B] (art. 22 §1 KP)
  C-1.2: Ciągłość umów = czwarta umowa terminowa → art. 25¹ KP (bezterminowa)
  C-1.3: Obciąża [SPÓŁKA-B] całością roszczeń: wynagrodzenie, PFRON, gotowość

T-2: Gotowość do pracy — niedopuszczenie po stronie pracodawcy
  C-2.1: Prawo do wynagrodzenia za przestój (art. 81 §1 KP) od daty niedopuszczenia
  C-2.2: Przelicza ciężar dowodu — pracodawca musi wykazać brak gotowości powoda
  C-2.3: Wzmacnia T-1: osobisty akt Prezesa = organ z art. 31 KP → tożsamość podmiotu
```

**Zasada:** Bez ≥2 konsekwencji per teza → BLOK-KONSEKWENCJE niekompletny.
Teza bez konsekwencji nie trafia do W1.3 pisma-procesowe-v3 jako GOTOWA.

**Integracja:**
- Konsekwencje C-X.1 → sekcja petitum pisma (co żądamy i od kogo)
- Konsekwencje C-X.2 → sekcja uzasadnienia (alternatywne podstawy)
- Konsekwencje C-X.3 → W2.1 MOD-TIMING / MOD-STRATEGIA-WYBOR

**Dashboard:** nowa tablica `consequences[]` per teza (id tezy, C-X.1, C-X.2, C-X.3, norma).
