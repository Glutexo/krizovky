# Uživatelské příběhy

## Aktuální funkcionalita

### Obecné chování všech agend

- Jako správce chci, aby se záznamy ve všech agendách fyzicky nemažly, ale pouze skryly, abych o data nepřišel.
- Jako správce chci mít v každém přehledu možnost zobrazit i skryté záznamy, abych je mohl dohledat.
- Jako správce chci mít možnost skryté záznamy na požádání znovu odkrýt, abych je mohl vrátit do běžného provozu.

### Evidence tajenek

- Jako správce tajenek chci vidět seznam všech tajenek, abych se rychle zorientoval v databázi.
- Jako správce tajenek chci na hlavní stránce zadat URL článku nebo jiné stránky, aby se z jejího obsahu automaticky navrhly tajenky.
- Jako správce tajenek chci otevřít detail tajenky, abych viděl její přesné znění a případný zdroj.
- Jako správce tajenek chci založit novou tajenku, abych ji mohl uložit do databáze.
- Jako správce tajenek chci upravit existující tajenku, abych mohl opravit její text nebo zdrojovou URL.
- Jako správce tajenek chci skrýt tajenku, abych ji vyřadil z běžného přehledu bez ztráty dat.
- Jako správce tajenek chci mít možnost zobrazit i skryté tajenky a případně je obnovit.
- Jako správce tajenek chci, aby se při AI importu už existující tajenky pro stejný zdroj znovu nevytvářely, abych si databázi nezanášel duplicitami.

### Zdroj tajenky

- Jako správce tajenek chci přiřadit tajence jednu zdrojovou URL, abych věděl, odkud pochází.
- Jako správce tajenek chci používat jednu zdrojovou URL pro více tajenek, abych nemusel stejný zdroj zadávat opakovaně.
- Jako správce tajenek chci mít možnost uložit tajenku i bez zdrojové URL, pokud zdroj neznám.
- Jako správce tajenek chci spravovat seznam zdrojových URL samostatně, abych je mohl připravit předem a znovu používat.
- Jako správce tajenek chci při editaci tajenky vybírat zdrojovou URL ze seznamu, abych se vyhnul překlepům.
- Jako správce tajenek chci i zdrojové URL skrývat místo mazání, aby šly později obnovit a nezpůsobily ztrátu vazeb.
- Jako správce tajenek chci, aby se při AI importu již známá zdrojová URL znovu použila a případně obnovila, abych pro stejnou stránku neměl více záznamů.

### Technické pojmenování

- Jako vývojář chci mít modely, třídy, proměnné a databázové identifikátory anglicky, aby byl kód konzistentní.
- Jako vývojář chci mít jako výjimku název samotné aplikace `krizovky`, aby odpovídal doméně projektu.

## Připravená infrastruktura

### OpenAI integrace

- Jako vývojář chci mít aplikaci připravenou na připojení k OpenAI API, abych mohl později doplnit AI funkce bez přestavby konfigurace.
- Jako vývojář chci držet OpenAI API klíč mimo verzované soubory, aby se citlivé údaje nedostaly do repozitáře.
- Jako vývojář chci být při startu aplikace upozorněný na chybějící nebo zjevně chybný OpenAI klíč, abych rychle odhalil špatnou konfiguraci.
- Jako vývojář chci posílat do OpenAI už vytažený čitelný text zdrojové stránky místo syrového HTML, aby byl import stabilnější a levnější.
