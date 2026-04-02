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
- datum měkkého smazání

Model `CrosswordAnswer` obsahuje:

- text tajenky
- volitelný odkaz na `SourceURL`
- datum vytvoření
- datum poslední úpravy
- datum měkkého smazání

## Uživatelské rozhraní

- seznam tajenek
- detail tajenky
- formulář pro vytvoření a úpravu s výběrem existující zdrojové URL
- potvrzení smazání
- samostatný seznam zdrojových URL
- formulář pro vytvoření a úpravu zdrojové URL
- měkké mazání tajenek i zdrojových URL
- do budoucna je měkké mazání systémové pravidlo pro všechny agendy

## Provozní poznámky

- Spouštěcí příkaz je `poetry run python manage.py runserver`.
- Migrace se spouští přes `poetry run python manage.py migrate`.
- Testy se spouští přes `poetry run python manage.py test`.
- OpenAI API klíč se načítá z proměnné prostředí `OPENAI_API_KEY`.
- Výchozí model je nastaven přes `OPENAI_MODEL`, implicitně `gpt-4.1-mini`.
- Aplikace při Django checku upozorní na chybějící nebo podezřele zadaný OpenAI klíč.

## Dokumentace

- Přehled projektu je v `docs/project-overview.md`.
- Uživatelské příběhy jsou v `docs/user-stories.md`.
