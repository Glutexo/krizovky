## Křížovky

Minimální Django aplikace pro evidenci tajenek do křížovek.

Rozhraní je zatím záměrně prosté: bez přihlašování, bez administrace, jen CRUD nad samotnými tajenkami.

Technické identifikátory v kódu používají anglické názvy; uživatelské texty zůstávají česky.

### Spuštění

```bash
poetry install
cp .env.example .env
poetry run python manage.py migrate
poetry run python manage.py runserver
```

Aplikace pak běží na `http://127.0.0.1:8000/`.

### OpenAI nastavení

Pro budoucí integraci s OpenAI API aplikace načítá tyto proměnné prostředí:

```bash
OPENAI_API_KEY=...
OPENAI_MODEL=gpt-4.1-mini
```

Lokálně je doporučené je držet v souboru `.env`, který není verzovaný.
Při `manage.py check` aplikace upozorní, pokud klíč chybí nebo má podezřelý formát.

### Testy

```bash
poetry run python manage.py test
```
