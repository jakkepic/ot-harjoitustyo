# Vaatimusmäärittely
## Sovelluksen tarkoitus
Sovellus toimii yksinkertaisena kirjanpitoohjelmana. Käyttäjä pystyy syöttämään debet- ja kredit-tapahtumia, ja ohjelma pystyy tuottamaan tuloslaskelman.
## Käyttäjät
Sovelluksessa on vain yksi käyttäjärooli. 
## Käyttöliittymäluonnos
Sovellus koostuu viidestä eri näkymästä.
Alkunäkymästä navigoidaan muihin näkymiin.
Jokaisella käyttöliittymän näkymällä on oma toiminnallisuus.
Toiminnallisuudet ovat seuraavat:
 - Talentaa tositteita
 - Tarkistaa kaikkia tositteita
 - Näyttää tuloslaskelman
 - Tilien/kustannuspaikkojen lisääminen
Kuvan avulla hahmoittaa käyttöliittymän näkymät (suurin piirtein)
![](./kuvat/kayttoliittyma-hahmotus.jpg)
## Toiminnallisuus
### "Perusnäkymässä"
- Parusnäkymästä voi siirtyä seuraaviin:
  - Lisää tosite
  - Tositteet
  - Tuloslaskelma
  - Tilikartta
  - Sulje ohjelma

### Lisää tosite
Käyttäjä valitsee tositenumeron, kustannuspaikan, debet/kredit ja lisää selityksen.
Kun kaikki kentät ovat syötetty oikein käyttäjä pystyy tallentamaan tositteen.

Syötteiden säännöt:
 - Samaa tositenumeroa voi käyttää vain kerran
 - Tili täytyy olla lisättynä ennen tositteen tallentamista.
 - 'Debit/Credit'-kenttään ainoat hyväksytyt syötteet ovat 'd' tai 'c'

### Tositteet
Käyttäjä voi katsella tositteita ja poistaa niitä halutessaan.

### Tuloslaskelma
Ohjelma luo tuloslaskelman ja esittää sen ruudulla.

- Kehittämismahdollisuus olisi jos ohjelma tallentaisi tuloslaskelman dokumenttiin.

# Tilikartta
Käyttäjä voi lisätä kustannuspaikkoja.
