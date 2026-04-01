## Křížovky

Minimální Django aplikace pro evidenci tajenek do křížovek.

Rozhraní je zatím záměrně prosté: bez přihlašování, bez administrace, jen CRUD nad tajenkami.

### Spuštění

```bash
poetry install
poetry run python manage.py migrate
poetry run python manage.py runserver
```

Aplikace pak běží na `http://127.0.0.1:8000/`.

### Testy

```bash
poetry run python manage.py test
```
