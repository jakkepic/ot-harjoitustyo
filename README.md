# Ohjelmistotekniikka, harjoitustyö  
*Jakob kråkström*  
## Kirjanpitoohjelma

Ohjelma on yksinkertainen kirjanpitoohjelma. Ohjelmaan voi syöttää debit ja kredit-tapahtumia ja ohjelma tekee syötetyistä tositteista tuloslaskelman. (HUOM! Ennen kuin syötät tositteet, sinun täytyy lisätä tilikartaan ainakin yksi tili.)

## Asennus:
1. Asenna riippuvuudet komennolla:
Bash
poetry install
2. Alustustoimenpiteet komennolla:
Bash
poetry run invoke build
3. Käynnistä sovellus suorittamalla komento:
Bash
poetry run invoke start