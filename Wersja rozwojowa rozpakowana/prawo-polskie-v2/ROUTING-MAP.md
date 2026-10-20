> **INDEKS (podział 2026-10-20):** ten plik to indeks. Tabele aktów (`## DR-NN`), ORKA-BAS, SKILLE WYKONAWCZE i MONITORING leżą w `prawo-polskie-v2/routing/`. Czytaj indeks, wybierz DR, a potem `view prawo-polskie-v2/routing/DR-01.md` (… `DR-16.md`) — obowiązkowo przed wskazaniem aktu, Dz.U. lub modułu.

## INDEKS SEKCJI — plik do wczytania

| Sekcja | Plik | Zakres |
|---|---|---|
| DR-01 | `routing/DR-01.md` | Ustrój Konstytucyjny i Źródła Prawa |
| DR-02 | `routing/DR-02.md` | Prawo Cywilne, Rodzinne i Gospodarcze (w tym upadłościowe i restrukturyzacyjne) |
| DR-03 | `routing/DR-03.md` | Prawo Karne, Wykroczenia, Egzekucja |
| DR-04 | `routing/DR-04.md` | Prawo Pracy, ZUS, Świadczenia Społeczne |
| DR-05 | `routing/DR-05.md` | Prawo Administracyjne i Sądownictwo Administracyjne |
| DR-06 | `routing/DR-06.md` | Podatki, Finanse Publiczne, AML |
| DR-07 | `routing/DR-07.md` | Zamówienia Publiczne, Fundusze UE, Pomoc Publiczna |
| DR-08 | `routing/DR-08.md` | Samorząd Terytorialny i Prawo Lokalne |
| DR-09 | `routing/DR-09.md` | Budownictwo, Środowisko, Energia, Transport |
| DR-10 | `routing/DR-10.md` | Zdrowie, Farmacja, Żywność, Rolnictwo |
| DR-11 | `routing/DR-11.md` | Cyfrowe, Cyberbezpieczeństwo, AI, Dane, IP |
| DR-12 | `routing/DR-12.md` | Sądownictwo, Prokuratura, Zawody Prawnicze |
| DR-13 | `routing/DR-13.md` | Służby, Bezpieczeństwo, Informacje Niejawne |
| DR-14 | `routing/DR-14.md` | Prawo UE, Międzynarodowe, Prawa Człowieka |
| DR-15 | `routing/DR-15.md` | Compliance, ISO, Governance, Audyt |
| DR-16 | `routing/DR-16.md` | Pisma, Strategia, Dowody, Orzecznictwo |
| ORKA-BAS | `routing/ORKA-BAS.md` | Leksykon definicji ministerialnych (GLOBAL) — wczytaj przy analizie definicji legalnej |
| SKILLE WYKONAWCZE I SHARED | `routing/SKILLE-WYKONAWCZE.md` | Akty powołane poza DR (skille wykonawcze, `shared`) — monitoring t.j. |
| MONITORING | `routing/MONITORING.md` | Akty opublikowane, niebędące jeszcze w pełni w życiu + legenda statusów |

---

## ⚙️ KOLEJNOŚĆ AKTUALIZACJI REJESTRÓW (przyjęta 2026-09-10e)

Rejestry aktów żyją w trzech warstwach: **moduł DR → lokalna `MAPA-AKTOW` →
`ROUTING-MAP` (ta mapa) → `audyt-systemu-v4/references/mapa_dzu_*.md`**.
Kierunek *autorytetu* biegnie w dół — moduł jest miejscem, gdzie akt naprawdę
pracuje. Kierunek *pracy aktualizacyjnej* biegnie odwrotnie:

```
1. Rozstrzygnij w ŹRÓDLE URZĘDOWYM (RZĄD 1, ELI po adresie)
2. Zamknij pozycje oznaczone jako wymagające weryfikacji w tej mapie
3. Zapisz stan w ROUTING-MAP i mapie centralnej — JEDEN zweryfikowany numer
4. Dopiero potem wyrównaj moduły DR do tego stanu (ZASADA 8)
```

⛔ **Dlaczego nie odwrotnie.** Szesnaście map dziedzinowych aktualizowanych
niezależnie rozjeżdża się szybciej, niż testy to wychwytują, a T11 widzi
wyłącznie *rozbieżność między rejestrami*, nie *błąd wpisany zgodnie wszędzie*
(F-82). Jeden zweryfikowany punkt odniesienia, do którego wyrównuje się moduły,
zamyka tę klasę rozjazdów u źródła.

⛔ **Czego ta kolejność NIE znosi.** ROUTING-MAP **nigdy nie staje się źródłem
weryfikacji**. Każdy numer rozstrzyga się osobno w ELI, także wtedy, gdy stoi
już w tej mapie — zapis F-141 („NIE domykać propagacją z map lokalnych")
obowiązuje w obie strony. Propagacja przenosi *rozstrzygnięcie*, nie zastępuje
go: wpisanie do modułu numeru przepisanego z tej mapy bez odczytu u źródła jest
tym samym błędem, co przepisanie w przeciwnym kierunku.

⚠️ Wyjątek: gdy błąd wykryto **w module** (jak przy F-148a — dwie podmiany
aktu), rozstrzygnięcie zaczyna się tam, gdzie go znaleziono, a wyrównanie idzie
w obie strony w tej samej sesji.

---

# ROUTING-MAP — Centralna Mapa Aktów Prawnych → DR-skills
# prawo-polskie-v2 v8.8 (aktualizacja 2026-07-21p — DR-03: NOWY
# mod-czynny-zal-KK-KKS-samooskarzenie (KK art. 15, KKS art. 16-16a —
# KLUCZOWE: czynny żal to NIE tylko samo-donos; korekta terminologiczna
# "samooskarżenie" nie jest odrębną instytucją) + NOWY mod-dobrowolne-
# poddanie-sie-karze-KPK (art. 335 i 387, dwa odrębne tryby). 54 moduły
# łącznie w DR-03 (było 52).)
#
# Format: Akt prawny | Dz.U. | DR-skill | Moduł | Status
# Status: ✅ OK = moduł ZAREJESTROWANY / trasa istnieje; NIE oznacza kompletności całego aktu.\n#         Pokrycie treściowe ustala wyłącznie odpowiedni DR/MAPA-POKRYCIA.md.\n#         🔗 odesłanie = w innym DR | ☐ BRAK = brak jednostki do zbudowania
#
# BRAMKA SEMANTYCZNA STATUSU (2026-08-27):\n#   MAPA-AKTOW / ROUTING odpowiadają „gdzie jest akt?”, a MAPA-POKRYCIA „ile aktu naprawdę opracowano?”.\n#   Zakaz wnioskowania: ✅ OK w tej mapie -> pełne pokrycie.\n#\n# Zasada: jeden akt prawny = jeden wpis w tej tabeli = jeden moduł
# Wyjątek: rozdziały tego samego aktu mogą mieć osobne moduły (oznaczone w kolumnie Moduł)
#
# ═══════════════════════════════════════════════════════════════════════════════
# PROTOKÓŁ INTEGRACJI — jak dane przepływają w systemie
# ═══════════════════════════════════════════════════════════════════════════════
#
# PULL (DR → prawo-polskie → audyt):
#   Krok 1. Każdy DR-skill utrzymuje lokalną MAPA-AKTOW.md z Dz.U. i statusami.
#   Krok 2. Ta tabela jest WTÓRNA wobec DR-MAPA-AKTOW — aktualizuj ją przez
#            pull z DR-MAPA-AKTOW po każdej zmianie w DR-skill.
#   Krok 3. audyt-systemu-v4 w FAZA 3 porównuje tę tabelę z mapa_dzu_*.md
#            i flaguje rozbieżności jako WARN lub CRIT.
#
# MONITORING (nowe akty oczekujące):
#   Każdy akt z flagą ⏳ lub ⚡ w kolumnie Status pojawia się też w sekcji
#   MONITORING na końcu tego pliku ORAZ w mapa_dzu_*.md (tabela MONITORING).
#   [od 2026-10-20: sekcja MONITORING = routing/MONITORING.md]
#   Przy audycie DZU — sprawdź czy akt wszedł w życie i przenieś do tabeli głównej.
#
# ═══════════════════════════════════════════════════════════════════════════════

## TABELA STATUSU — SKRÓCONA WEDŁUG DR

> Historyczny snapshot liczników; nie stanowi pomiaru bieżącego pokrycia.
> Nowych modułów nie dopisuj arytmetycznie do nieprzeliczonej sumy.
> F-108/46 zarejestrowano poniżej 2026-08-27; zakres: MAPA-POKRYCIA DR-02.

| DR | Dziedzina | ✅ OK | 🔗 odesłanie | ☐ BRAK | ⏳/⚡ MON | Łącznie |
|---|---|:---:|:---:|:---:|:---:|:---:|
| DR-01 | Ustrój Konstytucyjny | 14 | 1 | 0 | 0 | 15 |
| DR-02 | Prawo Cywilne/Rodzinne/Gosp. | 19 | 1 | 0 | 0 | 20 |
| DR-03 | Prawo Karne/Wykroczenia | 16 | 0 | 0 | 2 | 18 |
| DR-04 | Prawo Pracy/ZUS/Świadczenia | 18 | 0 | 0 | 0 | 18 |
| DR-05 | Prawo Administracyjne | 13 | 2 | 0 | 0 | 15 |
| DR-06 | Podatki/Finanse/AML | 40 | 0 | 0 | 4 | 44 — ⚠️ LICZNIK NAPRAWIONY 2026-08-11v: deklarowano 21 przy rzeczywistych 32 wierszach JESZCZE PRZED tą sesją — dryf licznika istniał wcześniej i nie został wykryty przez T2 (test sprawdza liczniki modułów w SKILL.md, NIE liczniki wierszy w TABELI STATUSU ROUTING-MAP). Po dopisaniu 12 aktów rachunkowo-księgowych: 44 wierszy |
| DR-07 | Zamówienia Publiczne/Fundusze | 12 | 2 | 0 | 0 | 14 |
| DR-08 | Samorząd Terytorialny | 23 | 0 | 0 | 0 | 23 |
| DR-09 | Budownictwo/Środowisko/Energia | 29 | 0 | 0 | 2 | 31 |
| DR-10 | Zdrowie/Farmacja/Żywność | 27 | 0 | 0 | 0 | 27 |
| DR-11 | Cyfrowe/AI/Dane/IP | 20 | 0 | 0 | 0 | 20 |
| DR-12 | Sądownictwo/Zawody | 11 | 1 | 0 | 0 | 12 |
| DR-13 | Służby/Bezpieczeństwo | 16 | 1 | 0 | 0 | 17 |
| DR-14 | Prawo UE/Międzynarodowe | 18 | 0 | 0 | 0 | 18 |
| DR-15 | Compliance/ISO | 9 | 0 | 0 | 0 | 9 |
| DR-16 | Pisma/Narzędzia | 11 | 0 | 0 | 0 | 11 |
| **SUMA** | | **271** | **9** | **0** | **4** | **284** |

---

---

*Wersja: 5.5 | Data: 2026-07-13 (TRYB DZU cotygodniowy)*
*Łączna liczba wpisów w tabelach DR: 275 (262 ✅ + 9 🔗 + 4 ⏳/⚡; w tym 1 pozycja ❌ NUMER BŁĘDNY do wyjaśnienia — patrz DR-03 KPK 2025.1390)*
*Korekta 2026-09-22 (F-195): z MONITORING usunięto 2 wiersze, które weszły w życie — KPK 2026/638 (28.05.2026) i PrBud 2025/1847 art. 1 pkt 1 i 3 (20.09.2026); poprawiono daty 2026/516; OP oznaczona ⬛ (uzupełniona w 6.29 — sześć nowelizacji po t.j.). Licznik powyżej NIE był przeliczany. Wiersz DR-03 „KPK 2026.638" uzupełniony o stan RZĄD 1.*
*Źródła lokalne: dr-01..dr-16/MAPA-AKTOW.md | Źródło centralne: audyt-systemu-v4/references/mapa_dzu_2026-10-04.md (KOREKTA 2026-10-04: nowa generacja po Dz.U. 2026 poz. 1161; ⚠️ KOREKTA 2026-09-27p: wskazywało mapa_dzu_2026-07-15.md — generacja nieaktualna od 2026-08; bieżąca wg frontmattera audytu: 09-22, F-193) (⚠️ KOREKTA 2026-07-15: poprzedni wpis wskazywał "mapa_dzu_2026-07-13.md" — plik o tej nazwie NIGDY nie istniał w audyt-systemu-v4/references/; aktualne pliki to 06-14 → 07-02 → 07-04 → 07-15)*
*TRYB DZU 2026-06-14: WARN-8 ZAMKNIĘTY — 16/16 pozycji zweryfikowane na ISAP
i naprawione w dwóch sesjach. Sesja 1 (5 poz.): A1 notariat→2026/614, A2
PrAut→2025/24, A3 komornicy→2024/1458 potwierdzony (ROUTING był już poprawny; KOREKTA: wcześniejszy wynik '2026/26' był błędem wyszukiwania - to inny akt, Ustawa SUS), B1 mandat posła/senatora→2024/907,
B2 referendum→2025/300. Sesja 2 (11 poz.): A4 regulatorzy (rozwinięto na
4 akty per regulator, zgodnie z tabelą wewnętrzną modułu), A5 KSCU→2025/1228,
A6 informacje niejawne→2025/1209, B3 otwarte dane→2023/1524 t.j., B4
KKS+AML→2025/644, B5 PKWiU rejestracja w ROUTING + Op pointer, C2
narkomania→2023/1939 (dodany), C3 odpowiedzialność podmiotów
zbiorowych→2024/1822 (był 2024/1247, też nieaktualny!), C4 prawa
pacjenta→2024/581 (dodany), C5 działalność lecznicza→2026/156 (był 2024/799,
podwójnie nieaktualny). Pełny dziennik:
audyt-systemu-v4/references/AUDIT-JOURNAL.md, AUDYT-2026-06-14f.*
