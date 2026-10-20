# DTA-ID-MODE — szczegóły

> **Trigger opcjonalny:** na żądanie użytkownika przy każdej sprawie.
> **Cel:** cross-referencja Dowód → Fakt → Teza w raportach i pismach.
> **Źródło:** DTA Warstwa 1–5 (identyfikacja + ekstrakcja + numeracja).

```
FORMAT IDENTYFIKATORÓW:

  D-NNN  = Dowód (dokument / plik)
    Format: D-[numer trzycyfrowy]
    Przykład: D-001 = Pracownicy13_08_2024.xlsx
              D-002 = Protokół rozprawy 27.01.2026

  F-NNN  = Fakt (wyekstrahowany z dowodu — TYLKO opis zdarzenia, NIE wniosek)
    Format: F-[numer trzycyfrowy]
    Zasada DTA W2: F-NNN zawiera WYŁĄCZNIE fakty, NIGDY wnioski prawne.
    Przykład: F-101 = "Arkusze [SPÓŁKA-A] i [SPÓŁKA-B] w jednym pliku XLS"
              F-102 = "Numeracja pracowników ciągła — brak resetu po 1.07.2023"
    ⛔ ZAKAZ: F-101 = "Spółki stanowią jeden organizm" → to wniosek, nie fakt → [LA-WNIOSEK-W-FAKCIE]

  T-NN   = Teza procesowa (wniosek prawny z faktów)
    Format: T-[numer dwucyfrowy]
    Przykład: T-01 = "[SPÓŁKA-A] i [SPÓŁKA-B] korzystały ze wspólnego systemu kadrowego"
              T-02 = "Powód manifestował gotowość do pracy"

CROSS-REFERENCE w raportach i pismach:
  "Jak wynika z D-001 (xlsx), fakt F-102 (ciągła numeracja) potwierdza T-01."
  "D-007 (RCS Park 21.03.2026) → F-301 (osobiste żądanie zaprzestania kontaktu) → T-02 + T-05"
```

```
KIEDY AKTYWOWAĆ DTA-ID-MODE:

  ⛔ OBOWIĄZKOWY (auto-trigger):
     ≥5 plików dostarczonych przez użytkownika
     LUB ≥5 tez w CLAIM-VALIDATION
     LUB TRYB ETAPOWY (>30 plików — HARD GATE z MOD-PORCJOWANIA)

  Opcjonalny (na żądanie):
     Użytkownik mówi: "numeruj", "D-NNN", "DTA", "cross-reference"

  Nieaktywny (domyślny dla małych spraw):
     <5 plików i <5 tez → używaj Lp. (prostsze, wystarczające)
```

```
PROCEDURA INICJALIZACJI DTA-ID-MODE:

KROK DTA-1: Utwórz rejestr D-NNN
  D-001: [nazwa pliku] | [typ wg MT1.2 DOK-URZ/DOK-PRY/etc.] | [klasa A-G z DOWODY-METODOLOGIA §5]
  D-002: ...

KROK DTA-2: Ekstrakcja faktów F-NNN per dowód
  Dla D-001: wylistuj fakty F-101, F-102, F-103...
  Zasada: jeden fakt = jedno zdanie opisowe zdarzenia/stanu (bez ocen prawnych)

KROK DTA-3: Budowanie tez T-NN z faktów
  T-01 wynika z: F-101, F-102, F-103 (D-001), F-205 (D-002)
  T-02 wynika z: F-301 (D-007), F-302 (D-008), F-303 (D-018)

KROK DTA-4: Zasilenie macierzy D×T (MOD-MACIERZ-DOWOD-TEZA)
  Macierz używa D-NNN zamiast D1/D2 → pełna cross-referencja
```
