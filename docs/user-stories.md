# Uživatelské příběhy

## Aktuální funkcionalita

### Evidence tajenek

- Jako správce tajenek chci vidět seznam všech tajenek, abych se rychle zorientoval v databázi.
- Jako správce tajenek chci otevřít detail tajenky, abych viděl její přesné znění a případný zdroj.
- Jako správce tajenek chci založit novou tajenku, abych ji mohl uložit do databáze.
- Jako správce tajenek chci upravit existující tajenku, abych mohl opravit její text nebo zdrojovou URL.
- Jako správce tajenek chci smazat tajenku, abych odstranil záznam, který už nechci evidovat.

### Zdroj tajenky

- Jako správce tajenek chci u tajenky uložit zdrojovou URL, abych věděl, odkud pochází.
- Jako správce tajenek chci mít možnost nechat zdrojovou URL prázdnou, aby šlo uložit i tajenku bez dohledaného zdroje.

## Připravená infrastruktura

### OpenAI integrace

- Jako vývojář chci mít aplikaci připravenou na připojení k OpenAI API, abych mohl později doplnit AI funkce bez přestavby konfigurace.
- Jako vývojář chci držet OpenAI API klíč mimo verzované soubory, aby se citlivé údaje nedostaly do repozitáře.
- Jako vývojář chci být při startu aplikace upozorněný na chybějící nebo zjevně chybný OpenAI klíč, abych rychle odhalil špatnou konfiguraci.
