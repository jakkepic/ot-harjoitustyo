# Käyttöohje
## Asennus:
1. Asenna riippuvuudet komennolla:

```bash poetry install```

2. Alustustoimenpiteet komennolla:

```bash poetry run invoke build```

3. Käynnistä sovellus suorittamalla komento:

```bash poetry run invoke start```

Huom: Ohjelman asettamista varten tietokoneellasi täytyy olla pythonille poetry-työkalu asetettuna. 
Ohjeita asettamiseen löydät täältä: [https://python-poetry.org/docs/](https://python-poetry.org/docs/)

## Suoritus:
Ohjelman voi suorittaa komennolla:  

```bash poetry run invoke start```  

## Ohjelman käyttö
### Tositteen lisääminen
Tositteen voi lisätä 'Add Voucher'-näkymästä.  
Huom! Jotta voit tositteita, sinun täytyy lisätä tilikartaan tili.  

Sääntöjä syötteille:
 - Samaa tositenumeroa voi käyttää vain kerran
 - Tili täytyy olla lisättynä ennen tositteen tallentamista.
 - 'Debit/Credit'-kenttään ainoat hyväksytyt syötteet ovat 'd' tai 'c'

### Tosittiden tarkastus
Tositteiden tarkastus tapahtuu 'View Vouchers'-näkymästä.  
Tästä näkymästä on myös mahdollista poistaa tositteita.

### Tuloslaskelman katsominen
'Income Statement'-näkymästä voit katsoa tuloslaskelmaa.  

### Tilikartta ja tilien lisääminen
Tilikartaan voi lisätä tilit 'Account Scheme'-näkymästä.  
Täytä kenttiin numero ja nimi tileille. Lisätessäsi tositteita täytät tilin numero-kenttään syöttämäsi numeron.  
Numero tulee olla kirjoitettuna samassa muodossa kun tilikartassa.