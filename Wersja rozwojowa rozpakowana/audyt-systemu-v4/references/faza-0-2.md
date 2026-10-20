# FAZA 0 (notatka), 0C, 0D, 0E oraz FAZA 2 (2A-2D) (przeniesione ze SKILL.md, treść bez zmian)

# FAZA 0 (notatka), FAZA 0C, 0D, 0E (przeniesione ze SKILL.md, treść bez zmian)

> ⚠️ **NAPRAWA 2026-08-15 (F-80, wykryta na skutek pytania użytkownika o
> scheduled task):** 15 plików istniało fizycznie na dysku (references/
> i scripts/), ale nie było wpisanych do YAML frontmatter powyżej —
> dokładnie ten sam wzorzec luki, jaki `scripts/check_rejestracja_modulow.py`
> wykrywa dla modułów DR (F-33/F-77), tylko dotyczący plików SAMEGO
> audyt-systemu-v4. Naprawione: wszystkie 15 plików dopisane do
> `references:`/`scripts:` w YAML. Zawierało: `SYNC-DZU-AUTOMATYCZNY.md` +
> `HARMONOGRAM-CRON.md` + `FORMAT-RAPORTU-ROZNIC.md` (mechanizm
> automatyzacji wykrywania nowych pozycji Dz.U. — odpowiedź na pytanie o
> "scheduled task": TAK, istnieje jako gotowy DO ADAPTACJI kod cron/GitHub
> Actions, ale wymaga wdrożenia przez developera w środowisku z dostępem do
> api.sejm.gov.pl — Claude w tej sesji czatu nie ma własnego mechanizmu
> cyklicznego uruchamiania), 3 archiwalne mapy Dz.U., folder
> `raporty-pokrycia-2026-08-13/`, oraz 7 skryptów pomocniczych (w tym
> `check_rejestracja_modulow.py` — ironicznie, sam był plikiem-sierotą).
> Szczegóły: `AUDIT-JOURNAL.md`, wpis AUDYT-2026-08-15h.

## FAZA 0C — ZADANIE CYKLICZNE W COWORK (POZYCJA 11, TYLKO NA ŻĄDANIE)

*(dodane 2026-08-15o; od 2026-10-10 wyłącznie na wyraźne żądanie użytkownika.)*

⛔ **Nigdy nie proponuj zadania cyklicznego automatycznie** — ani na końcu
audytu, ani po wykryciu Cowork. FAZĘ 0C uruchamia wyłącznie: wybór pozycji 11
menu (`widgets/WIDGET-MENU.md`, id `harmonogram`) albo jednoznaczna prośba
użytkownika o utworzenie zadania.

Po takim żądaniu sprawdź łącznie:

1. sesja toczy się w **Cowork** (poza Cowork: poinformuj jednym zdaniem, nie twórz);
2. użytkownik **nie ma jeszcze** zadania cyklicznego „Cotygodniowa weryfikacja
   ISAP" w harmonogramie Cowork.

⛔ **Warunku 2 NIE zgaduj** — Claude nie widzi listy zadań harmonogramu. Bez
jednoznacznego potwierdzenia w kontekście: zapytaj jednym zdaniem.

Jeśli oba spełnione → utwórz zadanie **dosłownie** wg
`references/SCHEDULED-TASK-COWORK.md` (§ 2A Description, § 2B prompt — treść
kanoniczna, bez parafrazy). Blok map pokrycia (§ 3 tamże) dołączaj do promptu
wyłącznie po **zamknięciu flagi F-83**; dopóki otwarta — pomiń i odnotuj.
Wynik (utworzono / odmowa / już istniało) zapisz w AUDIT-JOURNAL.md jednym zdaniem.

Wariant natywny (harmonogram wbudowany w Cowork, bez infrastruktury developera): `references/COWORK-HARMONOGRAM-NATYWNY.md` (do 6.146 plik bez odwołania z treści).

Pozycja 11 może być wybrana samodzielnie albo razem z pozycjami audytowymi
(wtedy zadanie tworzy się po audycie).

---

## FAZA 0D — KONTRAKT ROUTERA W PREFERENCJACH (POZYCJA 13, od 6.125)

Po wyborze pozycji 13 albo poleceniu „zsynchronizuj pamięć routera”:

1. `view references/PAMIEC-TRWALA-ROUTER.md`;
2. porównaj preferencje użytkownika widoczne w kontekście z regułami UP-1…UP-6
   routera (treść, nie numer wersji);
3. pokaż rozbieżności i proponowany tekst preferencji (≤ 4 linie, bez numeru
   wersji) do wklejenia przez użytkownika w Ustawienia → Profil;
4. odnotuj wynik w `AUDIT-JOURNAL.md`, jeżeli host pozwala na zapis.

⛔ Zakaz zapisu bloków dyrektyw do pamięci trwałej hosta. Pomiar z sesji
produkcyjnej: klasyfikator pamięci odrzuca treść sterującą zachowaniem modelu —
zapis jest niewykonalny z założenia, a ponowienie lub przeformułowanie
stanowiłoby obchodzenie zabezpieczenia. Wynik stały: `ZAPIS: NIEOBSŁUGIWANE W HOŚCIE`.

## FAZA 0E — INSTALACJA SERWERÓW MCP (POZYCJA 14; wybór serwerów i klucz CEIDG od 6.152)

Po wyborze pozycji 14 menu („Instalacja serwerów MCP”, plakietka 🖥️ *działa w Claude Desktop*)
albo poleceniu „zainstaluj serwery MCP”. Narzędzie: `mcp-servers/instaluj_serwery_mcp.py` (ten skill).
Przebieg ma **trzy tury**: (1) lista wyboru → (2) instalacja wybranych + prośba o klucz CEIDG, jeśli
wybrano CEIDG → (3) sam klucz w kolejnej wiadomości → uzupełnienie. Tura 3 jest opcjonalna.

⛔ **Działa w Claude Desktop.** claude.ai w przeglądarce nie uruchamia serwerów lokalnych — tam
wynikiem jest plik rozszerzenia do zainstalowania w Desktopie. Nie obiecuj działania w przeglądarce.

**0. LISTA WYBORU (tura 1) — zanim cokolwiek zbudujesz.** Jedynym źródłem listy jest
`python mcp-servers/instaluj_serwery_mcp.py --lista` (stan 6.202: 16 serwerów w 3 grupach, numeracja
stała); nie przepisuj jej z pamięci. Zapytaj jednym zdaniem, które serwery zainstalować:
   - host z przyciskami wyboru (np. `ask_user_input_v0`, limit 3 pytania × 4 opcje): **jedno pytanie
     multi_select na poziomie GRUP** z `--lista` — „Akty prawne i orzecznictwo”, „Rejestry podmiotów
     (CEIDG wymaga klucza)”, „Podatki, finanse, dane osobowe”, „Wybiorę numerami”. Pojedynczych serwerów
     nie rozpisuj na przyciski: grupa orzecznicza ma 9 pozycji, więcej niż mieści pytanie (korekta 6.202 —
     dawny opis „trzy pytania = trzy grupy, ≤4 opcje” był niewykonalny od dodania sn/sp/tk/kio/etpcz).
     „Wybiorę numerami” → pokaż wynik `--lista` i poproś o numery;
   - host bez przycisków: pokaż wynik `--lista` i poproś o odpowiedź numerami, nazwami albo „wszystkie”;
   - użytkownik od razu napisał „wszystkie” / wymienił serwery → pomiń pytanie.
   **Przy CEIDG zawsze** (także w pytaniu z przyciskami — w zdaniu wprowadzającym) podaj link do
   klucza: **https://dane.biznes.gov.pl/pl/portal/034872** (Hurtownia danych CEIDG: „wypełnij wniosek
   o dostęp i zarejestruj się”, logowanie Profilem Zaufanym; token JWT = klucz API).
   Po wysłaniu pytania zakończ turę.

1. **Ścieżka pomiarem, nie domysłem (tura 2).** `python mcp-servers/instaluj_serwery_mcp.py --diagnoza`.
   `WYBÓR` = numery/nazwy z tury 1 (argument `--serwery` przyjmuje jedne i drugie).
   - **kod 0 — „ŚCIEŻKA: --scal-desktop”** (komputer z Claude Desktop: Claude Code, terminal lokalny).
     Jednym zdaniem uprzedź, że skrypt dopisze wybrane serwery `lex-*` do `claude_desktop_config.json`
     i zrobi kopię `.kopia-przed-lex`; następnie `… --scal-desktop --serwery WYBÓR --bez-pytan`.
     Przekaż wynik dosłownie (✅/⛔, ścieżka kopii); poproś o restart Claude Desktop.
   - **kod 3 — „ŚCIEŻKA: --mcpb”** (piaskownica: claude.ai, czat Desktop, Cowork):
     `… --mcpb <katalog wyjściowy hosta> --serwery WYBÓR` → `lex-machina.mcpb` tylko z wybranymi
     serwerami (manifest wymienia wyłącznie ich narzędzia); udostępnij plik (`present_files`).
     Instrukcja: Claude Desktop → Ustawienia → Rozszerzenia → zainstaluj z pliku.
     ⛔ Przy kodzie 3 NIGDY nie uruchamiaj `--scal-desktop` i nie raportuj „zainstalowano”.
   - **Bez wykonania kodu:** podaj polecenie do uruchomienia u siebie
     (`python <katalog skilla>/mcp-servers/instaluj_serwery_mcp.py --scal-desktop --serwery WYBÓR`)
     — bez fikcyjnego raportu wykonania (adapter hosta, zasada 5).
   - **Wybrano CEIDG, a klucza jeszcze nie ma** → na końcu odpowiedzi DOKŁADNIE ta treść w sensie:
     „Klucz CEIDG uzyskasz tu: https://dane.biznes.gov.pl/pl/portal/034872. Gdy go dostaniesz, **wklej
     w kolejnej wiadomości sam klucz** — sprawdzę go i uzupełnię instalację o CEIDG.” (Na ścieżce
     `.mcpb` dodaj: albo wpisz go sam w polu „Klucz API CEIDG” rozszerzenia.) Bez klucza serwer
     CEIDG jest nieaktywny — pozostałe działają normalnie.

2. **KLUCZ W KOLEJNEJ WIADOMOŚCI (tura 3).** Wyzwalacz: wiadomość, której treścią jest (prawie)
   wyłącznie token JWT (`eyJ….eyJ….…`), w rozmowie, w której trwa FAZA 0E albo padła prośba z pkt 1.
   ⛔ Token to dane osobowe — ładunek (base64, nie szyfrowanie) zawiera PESEL, imię i nazwisko:
   - NIE powtarzaj tokenu ani jego fragmentów w odpowiedzi, NIE dekoduj na głos PESEL-u, NIE zapisuj
     go w pamięci rozmów ani w plikach skilla; w myśleniu nie przepisuj go ponad potrzebę polecenia;
   - zapisz go do pliku POZA katalogiem skilla z uprawnieniami 600 (piaskownica: plik roboczy hosta,
     np. `~/.ceidg_token`; komputer użytkownika: `~/.lex-machina/ceidg.token`);
   - `… --ceidg-test --ceidg-klucz-plik PLIK` (jedno żądanie; 204/200 = działa, 401 = zły lub wygasły
     → podaj link ponownie i poproś o nowy klucz; 429 → poproś o ponowienie za kilka minut, nie ponawiaj sam);
   - po teście 204/200:
     • kod 0 → `… --scal-desktop --serwery ceidg --ceidg-klucz-plik PLIK` (uzupełnia istniejącą
       instalację wyłącznie o CEIDG; konfiguracja z tokenem ląduje w `~/.lex-machina/`, nie w repo);
     • kod 3 → `… --mcpb <katalog wyjściowy> --serwery WYBÓR --ceidg-klucz-plik PLIK` →
       **`lex-machina-osobisty.mcpb`** z kluczem wpisanym na stałe (CEIDG dołączany automatycznie).
       Powiedz wprost: przed instalacją odinstaluj wcześniejsze „Lex Machina”; plik jest OSOBISTY
       (zawiera token) — nie udostępniać, nie wrzucać do repozytorium;
     • w piaskownicy usuń plik z tokenem po zbudowaniu rozszerzenia;
   - przypomnij jednym zdaniem, że token pozostaje w historii tej rozmowy (decyzja użytkownika, czy ją usunąć).
   Brak wybranego wcześniej zestawu (tura 3 bez tur 1–2) → przyjmij „wszystkie”.

3. **Kontrola po instalacji** (nowa rozmowa w Claude Desktop): narzędzia `lex-*` widoczne; wywołanie
   `nbp_kurs_waluty` dla EUR (jeśli wybrany) zwraca FOUND; `ceidg_szukaj_firmy` dla NIP spółki
   → NOT_FOUND z odesłaniem do KRS (dowód, że klucz działa). `cbosa_sprawdz_sygnature` „III OSK 1959/22”
   → FOUND zamyka **F-213** (z sandboxa Claude CBOSA jest nieosiągalna).
4. Zapisz w AUDIT-JOURNAL.md jednym zdaniem: ścieżka, wybrane serwery, CEIDG tak/nie — **bez tokenu**.

# FAZA 2 — weryfikacja zależności: 2A, 2B, 2C, 2D (przeniesione ze SKILL.md, treść bez zmian)

### 2A — Spójność ścieżek

Dla każdego SKILL.md sprawdź, czy wszystkie `view`/`load` odwołania wskazują na istniejące pliki:

```bash
grep -r "view " "${LEX_MACHINA_SKILLS_ROOT:?}" --include="*.md" | grep -v archive
```

Każda ścieżka nieistniejąca = błąd **CRIT**.

### 2B — Wersje skilli w cross-referencjach

Sprawdź, czy żaden skill nie odwołuje się do usuniętej wersji innego skilla (np. v1 zamiast v2):

```bash
grep -r "przewodnik-prawny-v1\|analiza-sadowa-v5\|pisma-procesowe-v2" \
  "${LEX_MACHINA_SKILLS_ROOT:?}" --include="*.md" | grep -v archive
```

Dodaj tu wzorce wg historii napraw z `references/CHANGELOG.md` i `references/CHECKLIST-DEDUP.md`.
*(Do 2026-08-20y ta linia odsyłała do `SKILLS-MAP-AND-FIXES` — pliku USUNIĘTEGO
2026-06-14g i zastąpionego przez CHANGELOG/CHECKLIST-DEDUP/mapa_dzu. Odwołanie
przetrwało 2 miesiące i ~90 sesji, bo FAZA 2A sprawdza tylko ścieżki `view`, a to
była nazwa w prozie — wzorzec do uwzględnienia przy rozbudowie testu T6.)*

### 2C — Pole description: OBECNOŚĆ + profil uniwersalny ≤200 znaków

Wczytaj moduł i uruchom procedurę:

```
view audyt-systemu-v4/modules/MOD-DESCRIPTION.md
```

Kontrola automatyczna (test **T14**, zalecana zamiast ręcznego liczenia):

```bash
python3 audyt-systemu-v4/scripts/check_description.py "${LEX_MACHINA_SKILLS_ROOT:?}"
```

**Brak pola / pole puste = CRIT** (F-130). Długość >200 = **CRIT**,
181–200 = **WARN**, ≤180 = **OK**. To wspólny profil przenośności; nie
utrzymuj osobnych opisów per host.

> ⛔ **ROZSZERZENIE 2026-08-24 (F-130).** Ta faza sprawdzała dotąd WYŁĄCZNIE
> długość — i przez to była ślepa na jedyny przypadek, który naprawdę wystąpił:
> **brak pola w ogóle**. Skrypt z `MOD-DESCRIPTION.md` dla takiego pliku wypisywał
> `0` znaków i klasyfikował go jako ✅ OK. `audyt-systemu-v4` — ten plik — był
> JEDYNYM skillem w systemie bez `description:`, przez nieustaloną liczbę sesji,
> i żadna faza tego nie zgłosiła. Naprawione na wskazanie użytkownika.

---

## FAZA 2D — CZYSTOŚĆ KODU (NOWE MODUŁY)

### 2D-1 — Zbędne interlinie

Wczytaj moduł:
```
view audyt-systemu-v4/modules/MOD-INTERLINIE.md
```

Wykonaj procedurę wykrycia → napraw każdy plik z ≥2 kolejnymi pustymi liniami → zapisz wynik do raportu.

### 2D-2 — Wstawki opisowe

Wczytaj moduł:
```
view audyt-systemu-v4/modules/MOD-WSTAWKI.md
```

Wykonaj skan regex → oceń każde trafienie wg tabeli kwalifikacji → usuń tylko jednoznacznie opisowe wstawki → zapisz wynik do raportu.

**Zasada obu modułów**: zmiany tylko przez `str_replace` na skopiowanych plikach. Nigdy `sed -i` na `` (read-only mount).
