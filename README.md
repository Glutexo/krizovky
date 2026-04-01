## Křížovky

Minimální Django aplikace pro evidenci tajenek do křížovek.

Rozhraní je zatím záměrně prosté: bez přihlašování, bez administrace, jen CRUD nad samotnými tajenkami.

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

### Testy

```bash
poetry run python manage.py test
```
