# Bramki towarzyszące hard gate (ANTY-FASADA, DOMAIN-LOCK, RATE-COMPLETENESS, STATUSY) — analiza-sadowa-v6

> Plik przeniesiony ze SKILL.md bez zmian treści (progressive disclosure). Wczytaj w całości przed wykonaniem odpowiedniego kroku.

### ⛔ BRAMKI TOWARZYSZĄCE (dodane 2026-08-23, F-109)

Hard gate wyżej kontroluje, CZY przepis został zweryfikowany. Poniższe dwie
kontrolują, CZY ten przepis w ogóle powinien się w analizie znaleźć oraz czy
liczba jest kompletna. Wykonuj je w PRZEJŚCIU IV (4A, pytania P6–P7):

```
□ [ANTY-FASADA + AF-6] Wykonaj self-check antyfasadowy z modułu kanonicznego:
    view shared/SELF-CHECK-ANTY-FASADA.md
  ⛔ Treść listy NIE jest tu kopiowana (F-115, 2026-08-23i). Poprzednia kopia
    miała 1 z 2 pozycji: gdy F-117 dodała AF-6 do źródła, kopie nie zostały
    zaktualizowane. Jedno miejsce prawdy = jedno miejsce aktualizacji.
□ [DOMAIN-LOCK] Odpowiedź/pismo zawiera przepis SPOZA dziedziny wiodącej
  (KK/KKS/KW/KPK/KPW przy torze cywilnym, pracowniczym lub administracyjnym —
  albo odwrotnie)? NIE → OK. TAK → (a) konkretny FAKT wypełniający znamię,
  nie skojarzenie tematyczne? (b) właściwy DR wczytany w TEJ odpowiedzi?
  (c) przepis przeszedł PRAWO-HARDGATE w TEJ odpowiedzi? Którekolwiek NIE →
  ⛔ USUŃ powołanie.  → `view shared/DOMAIN-LOCK.md`
□ [RATE-COMPLETENESS] Występują odsetki / waloryzacja / wskaźnik zmienny
  w czasie? NIE → OK. TAK → przedział zapisany + reżim rozstrzygnięty
  (KC vs transakcje handlowe) + szereg podokresów BEZ LUK + znacznik na
  KAŻDYM wierszu? NIE → nie podawaj kwoty łącznej, pokaż tabelę z ⬛.
  → `view shared/RATE-COMPLETENESS.md`
□ [STATUSY] Każdy przepis ma znacznik z ZAMKNIĘTEJ hierarchii czterech:
  ✅ [VER] · 🟨 [KOTWICA-URZĘDOWA] · ⚠️ [NIEWERYFIKOWANE] · ⬛ [DO UZUPEŁNIENIA]?
  Etykieta spoza tej listy = naruszenie hard gate (PRAWO-HARDGATE v2.5).
```
