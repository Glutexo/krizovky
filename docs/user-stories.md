# Uživatelské příběhy

## Aktuální funkcionalita

### Evidence tajenek

- Jako správce tajenek chci vidět seznam všech tajenek, abych se rychle zorientoval v databázi.
- Jako správce tajenek chci otevřít detail tajenky, abych viděl její přesné znění a případný zdroj.
- Jako správce tajenek chci založit novou tajenku, abych ji mohl uložit do databáze.
- Jako správce tajenek chci upravit existující tajenku, abych mohl opravit její text nebo zdrojovou URL.
- Jako správce tajenek chci smazat tajenku, abych odstranil záznam, který už nechci evidovat.

### Zdroj tajenky

- Jako správce tajenek chci přiřadit tajence jednu zdrojovou URL, abych věděl, odkud pochází.
- Jako správce tajenek chci používat jednu zdrojovou URL pro více tajenek, abych nemusel stejný zdroj zadávat opakovaně.
- Jako správce tajenek chci mít možnost uložit tajenku i bez zdrojové URL, pokud zdroj neznám.
- Jako správce tajenek chci spravovat seznam zdrojových URL samostatně, abych je mohl připravit předem a znovu používat.
- Jako správce tajenek chci při editaci tajenky vybírat zdrojovou URL ze seznamu, abych se vyhnul překlepům.

### Technické pojmenování

- Jako vývojář chci mít modely, třídy, proměnné a databázové identifikátory anglicky, aby byl kód konzistentní.

## Připravená infrastruktura

### OpenAI integrace

- Jako vývojář chci mít aplikaci připravenou na připojení k OpenAI API, abych mohl později doplnit AI funkce bez přestavby konfigurace.
- Jako vývojář chci držet OpenAI API klíč mimo verzované soubory, aby se citlivé údaje nedostaly do repozitáře.
- Jako vývojář chci být při startu aplikace upozorněný na chybějící nebo zjevně chybný OpenAI klíč, abych rychle odhalil špatnou konfiguraci.
