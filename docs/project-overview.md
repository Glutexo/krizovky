# Přehled projektu

## Účel projektu

Projekt slouží jako jednoduchá webová správa tajenek do křížovek.

## Aktuální stav

- Aplikace běží na Django.
- Databáze je SQLite.
- Existuje aplikace `tajenky` pro základní CRUD operace.
- Autentizace ani uživatelské účty se zatím nepoužívají.
- Administrační rozhraní není vystavené.
- Vzhled používá jednoduché styly přes Pico CSS z CDN.

## Datový model

Model `Tajenka` obsahuje:

- text tajenky
- volitelnou zdrojovou URL
- datum vytvoření
- datum poslední úpravy

## Uživatelské rozhraní

- seznam tajenek
- detail tajenky
- formulář pro vytvoření a úpravu
- potvrzení smazání

## Provozní poznámky

- Spouštěcí příkaz je `poetry run python manage.py runserver`.
- Migrace se spouští přes `poetry run python manage.py migrate`.
- Testy se spouští přes `poetry run python manage.py test`.
