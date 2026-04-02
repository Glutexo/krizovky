# Přehled projektu

## Účel projektu

Projekt slouží jako jednoduchá webová správa tajenek do křížovek.

## Aktuální stav

- Aplikace běží na Django.
- Databáze je SQLite.
- Existuje aplikace `krizovky` pro základní CRUD operace.
- Autentizace ani uživatelské účty se zatím nepoužívají.
- Administrační rozhraní není vystavené.
- Vzhled používá jednoduché styly přes Pico CSS z CDN.
- Projekt je připravený na budoucí integraci s OpenAI API.

## Datový model

Model `SourceURL` obsahuje:

- URL zdroje
- datum vytvoření
- datum poslední úpravy
- datum skrytí

Model `CrosswordAnswer` obsahuje:

- text tajenky
- volitelný odkaz na `SourceURL`
- datum vytvoření
- datum poslední úpravy
- datum skrytí

## Uživatelské rozhraní

- seznam tajenek
- detail tajenky
- formulář pro vytvoření a úpravu s výběrem existující zdrojové URL
- formulář na hlavní stránce pro zadání zdrojové URL a hromadný AI import tajenek z obsahu stránky
- potvrzení skrytí
- samostatný seznam zdrojových URL
- formulář pro vytvoření a úpravu zdrojové URL
- skrývání tajenek i zdrojových URL místo fyzického mazání
- možnost zobrazit i skryté záznamy a znovu je obnovit
- do budoucna je skrývání systémové pravidlo pro všechny agendy

## Provozní poznámky

- Spouštěcí příkaz je `poetry run python manage.py runserver`.
- Migrace se spouští přes `poetry run python manage.py migrate`.
- Testy se spouští přes `poetry run python manage.py test`.
- OpenAI API klíč se načítá z proměnné prostředí `OPENAI_API_KEY`.
- Výchozí model je nastaven přes `OPENAI_MODEL`, implicitně `gpt-4.1-mini`.
- Aplikace při Django checku upozorní na chybějící nebo podezřele zadaný OpenAI klíč.
- Při AI importu aplikace stáhne HTML stránky, vytáhne z něj čitelný text a ten pošle OpenAI k návrhu tajenek.
- Import automaticky znovu použije existující zdrojovou URL, obnoví dříve skryté záznamy a nepřidá viditelné duplicity stejné tajenky pro stejný zdroj.

## Dokumentace

- Přehled projektu je v `docs/project-overview.md`.
- Uživatelské příběhy jsou v `docs/user-stories.md`.
