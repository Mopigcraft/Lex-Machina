# Faza 2, 3, 4 (kategoryzacja i alerty, aktualność, raport) — orzeczenia-sadowe-v2

> Plik przeniesiony ze SKILL.md bez zmian treści (progressive disclosure). Wczytaj w całości przed wykonaniem odpowiedniego kroku.

## Faza 2 — Kategoryzacja i alerty

Czytaj `references/widget.md` — tabele mapowania alertów i kategorii na klasy CSS.

### Alerty per orzeczenie

| Alert | Wyzwalacz | Priorytet |
|---|---|---|
| ⚠️ STARE | Orzeczenie starsze niż próg dziedzinowy (patrz: tabela progów) | Informacyjny |
| 🔴 SPRZECZNE | Linia niejednolita — orzeczenie trafia do Kat. 3B | Wysoki |
| 🔴 ZMIANA PRAWA | Nowelizacja przepisu po dacie wyroku | Wysoki |
| ℹ️ WYMIAR UE | Materia objęta dyrektywą UE lub orzecznictwem TSUE/ETPC | Informacyjny |
| ⛔ ŹRÓDŁO NIEPOTWIERDZONE | Sygnatura nieznaleziona w portalach Tier 1–2; zakaz powołania | Krytyczny |
| 🏛️ ZASADA PRAWNA | Uchwała SN z mocą zasady prawnej (art. 87 § 1 uSN) — Kat. 6A | Priorytetowy |
| 🔴 BILANS NIEKORZYSTNY | N_przeciwne ≥ N_zgodne LUB przeciwne ≥ 50% trafień Kat. 1–2 (Faza 1-D, Zasada 10) | Krytyczny |

### BILANS LINII ORZECZNICZEJ — obliczenie

Wykonuj zawsze gdy Faza 1-D była przeprowadzona (profil oczekiwanego rozstrzygnięcia ustalony):

```
N_zgodne     = liczba orzeczeń Kat. 1–2 o kierunku zgodnym z oczekiwanym
N_przeciwne  = liczba orzeczeń Kat. 1–2 o kierunku przeciwnym
N_neutralne  = liczba orzeczeń niekierunkowych (dotyczą instytucji, nie przesądzają)

PROPORCJA = N_przeciwne : N_zgodne
PROGI:
  N_przeciwne ≥ N_zgodne              → 🔴 BILANS NIEKORZYSTNY (krytyczny)
  N_przeciwne < N_zgodne, ale ≥ 30%   → 🟡 BILANS MIESZANY (informacyjny, odnotuj)
  N_przeciwne < 30% wszystkich        → ✅ BILANS KORZYSTNY (bez alertu)
```

Gdy 🔴 BILANS NIEKORZYSTNY → alert musi pojawić się w Profilu ryzyka (Faza 0-A,
jako pierwszy) ORAZ w Raporcie końcowym (Faza 4) z wymienieniem sygnatur linii
przeciwnej — zakaz pomijania nawet gdy linia zgodna zawiera Kat. 6A (uchwała
wiąże kierunek prawny, ale nie usuwa obowiązku ujawnienia rozbieżności w praktyce
sądów niższych instancji, jeśli taka istnieje).

### Dziedzinowe progi alertu STARE

Sztywny próg 5 lat nie jest miarodajny dla wszystkich dziedzin. Stosuj progi dziedzinowe:

| Dziedzina | Próg alertu STARE | Uzasadnienie |
|---|---|---|
| Prawo pracy (KP) | 3 lata | Dynamiczne orzecznictwo, częste nowelizacje KP |
| Prawo podatkowe, AML | 2 lata | Bardzo szybkie zmiany przepisów |
| Prawo cywilne (KC, KPC) ogólne | 7 lat | Stabilna linia, wolniejsze zmiany |
| Prawo rodzinne | 7 lat | Stabilna linia |
| Prawo karne (KK, KPK) | 5 lat | Umiarkowane tempo zmian |
| Prawo administracyjne (KPA, PPSA) | 4 lata | Aktywne orzecznictwo NSA |
| Prawo konstytucyjne | 10 lat | Zasady fundamentalne rzadko się zmieniają |
| Prawo gospodarcze, spółki | 4 lata | Zmiany KSH, upadłościowe |
| Prawo UE, TSUE | 5 lat | Zależy od materii dyrektywy |
| Prawo budowlane, środowiskowe | 4 lata | Aktywne zmiany przepisów |

Jeśli dziedzina nie pasuje do tabeli → stosuj domyślny próg 5 lat.
Alert ⚠️ STARE nie wyklucza orzeczenia — informuje o potrzebie sprawdzenia aktualności.

### Kategorie orzeczeń

| Kat. | Etykieta | Opis |
|---|---|---|
| 1 | Najnowsze | Orzeczenia w granicach progu dziedzinowego |
| 2 | Starsze | Orzeczenia przekraczające próg, ale poniżej 2× progu |
| 3A | Linia dominująca | Jednolita linia większościowa |
| 3B | Linia mniejszościowa | ZAWSZE prezentuj — zakaz ukrywania |
| 4 | Wspierające | Potwierdzają linię główną |
| 5 | UE / TSUE / ETPC | Materia objęta dyrektywą lub wyrokiem TSUE/ETPC |
| 6 | Interpretacje | Zwykłe uchwały SN, wytyczne, interpretacje |
| **6A** | **Zasada prawna SN** | **Uchwały z mocą zasady prawnej (art. 87 § 1 uSN) — NAJWYŻSZY PRIORYTET powołania** |
| 7 | Literatura | Komentarze, glosy (pomocniczo) |

ZAKAZ ukrywania Kat. 3B — jeśli istnieje linia mniejszościowa, zawsze prezentuj.
Kat. 6A zawsze powołuj jako pierwsze w piśmie — przed Kat. 1, 3A, 5.

---

## Faza 3 — Weryfikacja aktualności

1. Czy linia jest jednolita?
2. Czy doszło do nowelizacji po datach orzeczeń?
3. Czy SN nie zajął odmiennego stanowiska w uchwale składu 7 / całej Izby / pełnego składu?
4. Czy dostępna jest uchwała Kat. 6A dotycząca tej materii? (sprawdź na sn.pl → Izba=Uchwaly)

---

## Faza 4 — Raport końcowy

```
RAPORT ORZECZEŃ: [TEMAT]
Data: [data] | Tryb: [LAIK / PRAWNIK] | Jurysdykcja: [PL / UE / mieszana]
Znaleziono: [n] | URL zweryfikowanych: [n] | Zasady prawne SN (Kat. 6A): [n]
WSKAŹNIK POKRYCIA PRZESŁANEK:
P1: ██████░░  62%  ← Kat.1: 2 orz.
P2: █████████  90%  ← Kat.6A: 1 uchwała SN
P3: ██░░░░░░  20%  ⚠️ LUKA

BILANS LINII ORZECZNICZEJ (jeśli Faza 1-D wykonana):
Zgodne z oczekiwanym rozstrzygnięciem: [N_zgodne]
Przeciwne:                             [N_przeciwne]
Neutralne:                             [N_neutralne]
Status: [🔴 BILANS NIEKORZYSTNY / 🟡 BILANS MIESZANY / ✅ BILANS KORZYSTNY]

PLAN MINIMUM (Zasada 11) — [n_A]/5 wspierających, [n_B]/5 linii przeciwnej:

[A] ORZECZENIA WSPIERAJĄCE TEZĘ (docelowo 5, w kolejności: Kat.6A → reszta wg rangi/daty)
  1. [SYGNATURA] · [SĄD + IZBA] · [DATA] · [URL] · [lokalizacja: s./teza/pkt — Zasada 2B]
     Przesłanki: [2–4 zdania — co konkretnie w stanie faktycznym/wykładni
     zdecydowało o takim rozstrzygnięciu; parafraza, limit cytatu Zasada 3]
  2. ...
  (do 5; jeśli mniej — napisz wprost: „znaleziono [n] z 5 — wyszukiwanie
   wyczerpujące w [lista portali/faz użytych], brak dalszych trafień")

[B] LINIA PRZECIWNA (docelowo 5, o ile istnieje — Faza 1-D)
  1. [SYGNATURA] · [SĄD + IZBA] · [DATA] · [URL] · [lokalizacja: s./teza/pkt — Zasada 2B]
     Przesłanki + czynnik odróżniający: [2–4 zdania — dlaczego sąd orzekł
     odwrotnie: inny stan faktyczny, brak przesłanki, odmienna wykładnia]
  2. ...
  (do 5; brak linii przeciwnej po wyczerpującym wyszukiwaniu → napisz wprost:
   „nie odnaleziono linii przeciwnej po przeszukaniu [portale]", nie pomijaj
   milczeniem)
```
