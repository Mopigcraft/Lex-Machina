# Faza 1-L (sieć lokalna portali SA/SO/SR i CBOSA) — orzeczenia-sadowe-v2

> Plik przeniesiony ze SKILL.md bez zmian treści (progressive disclosure). Wczytaj w całości przed wykonaniem odpowiedniego kroku.

## Faza 1-L — Sieć lokalna portali SA/SO/SR i CBOSA (rozszerzenie bazy)

Uzupełnienie Fazy 1 — stosuj gdy:
- wyszukiwanie centralne (orzeczenia.ms.gov.pl) nie zwróciło wyników lub zwróciło
  ich mało (< 3) mimo że sprawa dotyczy powszechnej instytucji prawnej,
- użytkownik lub przeciwnik procesowy powołał konkretną sygnaturę konkretnego SR/SO/SA
  i trzeba ją zweryfikować bezpośrednio u źródła,
- sprawa jest lokalnie osadzona (właściwość miejscowa znanego sądu) i celowe jest
  sprawdzenie linii orzeczniczej WŁAŚNIE tego sądu/okręgu (praktyka lokalna bywa
  odmienna od linii krajowej — istotne dla prognozy rozstrzygnięcia w danej sprawie).

Procedura:
```
1. Ustal właściwy sąd (nazwa + siedziba) z akt sprawy lub pytania użytkownika.
2. view orzeczenia-sadowe-v2/references/PORTALE-LOKALNE.md
   → odczytaj wzorzec URL i sprawdź, czy sąd jest na liście głównych portali.
3. Jeśli sąd nieznany z listy → web_search "orzeczenia [pełna nazwa sądu]"
   → zweryfikuj adres portalu przez web_fetch (musi być subdomena *.gov.pl).
4. web_fetch na wyszukiwarkę portalu lokalnego z frazami z Fazy 0-B.
5. Każde trafienie traktuj jak Tier 1 (Zasada 5A) — te same wymogi 4 elementów
   (Zasada 2) i ten sam limit cytatu (Zasada 3).
```

Dla spraw administracyjnych: orzeczenia.nsa.gov.pl (CBOSA) już obejmuje wszystkie
16 WSA jedną bazą — NIE szukaj osobno portali poszczególnych WSA (nie istnieją
jako odrębne bazy, wyłącznie jako oddziały w ramach CBOSA po symbolu sądu).

⚠️ Publikacja w sieci lokalnej nie jest wyczerpująca (patrz Zasada 5A) — brak
wyniku w portalu lokalnym nie jest dowodem braku orzecznictwa danego sądu;
odnotuj to zastrzeżenie w Raporcie, jeśli wyszukiwanie lokalne było kluczowe
dla wniosku.
