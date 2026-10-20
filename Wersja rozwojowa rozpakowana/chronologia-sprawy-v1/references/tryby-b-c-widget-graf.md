# TRYB C (graf przyczynowy) i TRYB B (widget interaktywny)

> Plik obowiązkowy dla TRYBU B i TRYBU C. Treść przeniesiona dosłownie z SKILL.md (refaktor 2026-10-20); SKILL.md zawiera nagłówki i streszczenia.

### TRYB C — Graf przyczynowy (zależności zdarzeń, wpływ wzajemny, „co jeśli”) — od v1.13

Gdy użytkownik pyta „co z czego wynika”, „jak zdarzenia na siebie wpływają”, „co jeśli X się nie
utrzyma”, „pokaż zależności / graf”, albo gdy oś czasu ma ≥ 2 wątki ze wspólnymi węzłami:

```
KROK C1 — Oś czasu z TRYBU A (zdarzenia z polem id Z-nnn; bez osi czasu TRYB C nie rusza)
KROK C2 — view shared/MOD-GRAF-PRZYCZYNOWY.md → krawędzie: dowód połączenia (MET-PT), csqn,
          przypisanie prawne; bramy I/LUB; wersja przeciwnika jako OSLABIA/PRZERYWA
KROK C3 — Raport: python3 shared/tools/graf_przyczynowy.py graf.json (MD; --mermaid dla diagramu)
          albo — gdy brak wykonania kodu — ten sam model ręcznie wg §4 modułu, z jawnym rachunkiem
KROK C4 — Widget: visualize:read_me(["interactive"]) → show_widget z
          assets/widget-graf-przyczynowy.html (podmień stałą GRAF; pasek MOD-WIDGET-IO JSON/MD;
          kliknięcie węzła = scenariusz obalony/udowodniony z przeliczeniem na żywo)
KROK C5 — Ogniwa krytyczne i flagi (post hoc, csqn, art. 361 § 1/362/441 KC, art. 2 KK) do raportu
          końcowego; liczby zawsze z zastrzeżeniem założeń (§4 modułu)
```

### TRYB B — Widget interaktywny

Gdy użytkownik wpisuje "widget" / "pokaż oś czasu" / "timeline" / "aplikację":

> ⚠️ REGUŁA RENDEROWANIA — pliki `.jsx` przez `present_files` NIE renderują się w claude.ai.
> Jedyna poprawna metoda: `show_widget` z HTML (vanilla JS).

```
KROK B1 — Wyciągnij z rozmowy zdarzenia jako strukturę chronologiczną (schemat poniżej)
KROK B2 — Wywołaj visualize:read_me z modules=["interactive","mockup"]
KROK B2a — ⛔ MOD-WIDGET-IO (OBOWIĄZKOWE przed show_widget):
            view shared/MOD-WIDGET-IO.md
            → wbuduj pasek IO w nagłówek widgetu (powyżej osi czasu)
            → IO_SKILL_ID='chronologia-sprawy-v1', IO_CASE_ID=sygnatura
            → matryca: Export JSON ✅ MD ✅ | Import JSON ✅
            → ioGetState(): { watki, zdarzenia, sprzecznosci }
            → ioSetState(s): odtwórz oś czasu z wczytanego JSON
KROK B3 — Wywołaj show_widget z HTML vanilla JS:
           • zdarzenia i wątki jako literały JS wbudowane bezpośrednio w HTML
           • osobna oś czasu per wątek (zakładki lub sekcje)
           • widok zbiorczy CROSS-WĄTEK jako opcja
           • filtrowanie po klasie pewności, wątku, znaczeniu
           • węzły wspólne wyróżnione wizualnie z linkami między wątkami
           • CSS variables (var(--color-*)) — BEZ React, BEZ importów
           • NIE używaj cp, str_replace ani present_files

SCHEMAT DANYCH (wbuduj jako literały JS w HTML):
  watki: [{ id, nazwa }]
  zdarzenia: [{
    data, pewnosc,          // BEZSPORNE / PEWNE / WYDEDUKOWANE / SPORNE
    dedukacja,              // null lub { podstawa, wniosek, pewnosc_0_10 }
    opis, strona,
    proweniencja: { typ_zrodla, dok_id, strona_dok, autor_twierdzenia },
    watki,                  // tablica id wątków
    wezel_wspolny,
    znaczenie,
    kolizja_id              // null lub "SPRZECZNOŚĆ-01"
  }]
  finanse: [{                // [NOWE v1.2] — sekcja 3B, wypełniane RÓWNOLEGLE ze zdarzeniami
    id,                      // "FIN-01"
    kwota, waluta,
    tytul,
    platnik, odbiorca,       // string lub "[OSOBA-NIEZIDENTYFIKOWANA-N]"
    termin,                  // string lub null — NIE zgaduj, jeśli brak w dokumencie
    status,                  // ZAPŁACONE / DO_ZAPŁATY / ZALEGŁE / SPORNE_CZY_ZWRÓCONE / NIEZNANY
    proweniencja: { typ_zrodla, dok_id, strona_dok, autor_twierdzenia },
    powiazane_dok_id,        // tablica DOK-XX potwierdzających/wzmiankujących tę samą kwotę
    kolizja_id               // null lub "SPRZECZNOŚĆ-01" (typ KWOTA)
  }]
  sprzecznosci: [{
    id,          // "SPRZECZNOŚĆ-01"
    typ,         // DATA / OPIS / DATA_I_OPIS / IDENT / KWOTA [NOWE v1.2]
    zdarzenie,
    watek,
    wersja_a: { tresc, dok_id, strona_dok, autor },
    wersja_b: { tresc, dok_id, strona_dok, autor },
    common_ground,       // null lub string — co OBIE strony faktycznie przyznają
                          // w tej kwestii, niezależnie od spornego elementu
                          // (np. "obie strony zgadzają się, że dokument porozumienia
                          // został podpisany 9.10.2024 — sporna jest tylko ocena
                          // okoliczności podpisania")
    roznica_dni,         // null dla TYP=OPIS/IDENT
    kategoria,           // A-KRYTYCZNA / B-ISTOTNA / C-MARGINALNA
    wplyw, rekomendacja
  }]
  Pola null → null. Nie wymyślaj dat.
```
