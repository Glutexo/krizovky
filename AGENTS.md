# Pravidla Codexu Pro Tento Repozitář

## Cíl
- Udržovat změny malé, jednoznačné a snadno kontrolovatelné.
- Upřednostnit dokončený funkční celek před rozpracovaným scaffoldem.

## Postup Práce
- Před úpravou číst související soubory.
- Stručně uvést předpoklady, pokud ovlivňují implementaci.
- Důležité změny ověřovat nejmenším smysluplným příkazem nebo testem.
- Neměnit nesouvisející soubory jen kvůli úklidu pracovního stromu.
- Vést dokument nebo složku s dokumenty popisujícími aktuální stav projektu podle dosud vytvořeného řešení.
- Po každé změně, přidání nebo odebrání funkcionality tuto dokumentaci aktualizovat.
- Projektová dokumentace je vedená ve složce `docs/`, výchozí přehled je v `docs/project-overview.md`.
- Součástí projektové dokumentace je i seznam uživatelských příběhů v `docs/user-stories.md`.
- Po každé změně funkcionality aktualizovat i odpovídající uživatelské příběhy.

## Úpravy
- Upřednostňovat jednoduchá řešení před předčasnou abstrakcí.
- Zachovat stávající strukturu projektu a pojmenování, pokud není jasný důvod to měnit.
- Komentáře psát stručně a jen tam, kde skutečně přidávají hodnotu.
- Ve výchozím stavu používat ASCII, pokud soubor už sám nevyžaduje Unicode.
- Všechny české řetězce v aplikaci, dokumentaci i šablonách psát s diakritikou.
- Názvy modelů, tříd, proměnných, tabulek, sloupců a podobných technických identifikátorů psát anglicky.
- Výjimka: samotná Django aplikace se jmenuje `krizovky`, ne `crossword_answers`.
- Před spuštěním každé migrace udělat zálohu dat; až pokud migrace i následné ověření projdou, zálohu smazat.

## Bezpečnost Gitu
- Bez výslovného požadavku nikdy nepřepisovat ani nemažat uživatelské změny.
- Vyhýbat se destruktivním git příkazům, pokud je uživatel výslovně nepožaduje.
- Pokud je worktree znečištěný, omezit úpravy na soubory související s úkolem.
- Commitovat co nejmenší logické změny.
- Pokud se v projektu udělalo více změn, rozdělit je do samostatných commitů podle tématu.
- Spouštět vždy jen jeden gitový proces naráz.
- Po každé dokončené provedené změně udělat commit a push.
- Pro práci s GitHubem je k dispozici příkaz `gh`.
- Remote `origin` patří veřejnému repozitáři `Glutexo/krizovky`.
- URL repozitáře je `https://github.com/Glutexo/krizovky`.

## Komunikace
- Být stručný a věcný.
- Blokery hlásit okamžitě.
- Shrnovat, co se změnilo a jak bylo ověření provedeno.
