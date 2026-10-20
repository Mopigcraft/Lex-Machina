# REGUŁA PRECYZJI DETALU — §P1, §P2, §P3 (szczegóły)

### §P1 — Sprzeczności wewnątrz jednej strony (INTRA-CONTRA)

Przy analizie wielodokumentowej każda strona może zmienić narrację między pismami.
Obowiązek: porównywać twierdzenia tej samej strony **pismo po piśmie**, nie tylko
twierdzenia stron między sobą. Sprzeczność wewnętrzna = zmiana wersji przez tę
samą stronę w różnych dokumentach/terminach.

Przykład kanoniczny (sprawa [SYGN-SPRAWY]):
- Odp. na pozew (kwiecień 2025): konto = `[E-MAIL-POWODA]`
  → Pozwana kwalifikuje jako konto pracownicze na domenie [DOMENA-POZWANEJ].
- Pismo procesowe (czerwiec 2025): „Powód stworzył PRYWATNEGO maila z dopiskiem
  @[DOMENA-POZWANEJ]" → Pozwana zmienia kwalifikację na prywatne konto Powoda.
- WYNIK: dwie wykluczające się charakterystyki tego samego konta w dwóch pismach
  tej samej strony → INTRA-CONTRA klasy KRYTYCZNEJ.

### §P2 — Checklist precyzji detalu

Przed wygenerowaniem każdej zakładki „Sprzeczności" wykonaj:

```
[ ] Czy ta sama strona zmienia opis faktyczny między pismami?
[ ] Czy daty w dokumentach są spójne (np. data podpisania vs data odbioru)?
[ ] Czy kwoty są identyczne we wszystkich dokumentach (np. 1 000 zł vs 1 060 zł)?
[ ] Czy nazwy własne (adresy e-mail, nazwy firm, imiona) są identyczne wszędzie?
[ ] Czy kwalifikacja prawna faktu jest spójna (np. zaliczka vs nienależne środki)?
[ ] Czy domena/serwer konta mailowego jest spójna z jego kwalifikacją jako służbowe?
[ ] Czy chronologia zdarzeń jest możliwa (daty → terminy → działania)?
[ ] Czy twierdzenia o świadkach są spójne (rola, zależność, adres doręczeń)?
```

### §P3 — Format INTRA-CONTRA w dashboardzie

Sprzeczności wewnętrzne oznaczać typem `intra` (dedykowany typ — nie `inter`):
- `[INTRA]` — `type:'intra'` — zmiana narracji tej samej strony
- `[CROSS]` — `type:'inter'` — sprzeczność między twierdzeniami różnych stron
- `[LEG]`   — `type:'legal'` — sprzeczność z przepisem prawa
- `[DOUBT]` — `type:'doubt'` — wątpliwość nierozstrzygnięta

Każda INTRA-CONTRA musi zawierać:
1. Cytat z dokumentu pierwszego (z lokalizacją: str./data pisma)
2. Cytat z dokumentu drugiego (z lokalizacją: str./data pisma)
3. Konkretną rozbieżność (co dokładnie się zmienia: słowo, liczba, kwalifikacja)
4. Rekomendację procesową: jak atakować tę sprzeczność na rozprawie
