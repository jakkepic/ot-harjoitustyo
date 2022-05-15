# Arkkitehtuurikuvaus

## Rakenne
Ohjelman rakenteella on kolme tasoa:  
![arkkitehtuuritasot](kuvat/arkkitehtuuritasot.png)  
Pakkaus ui vastaa käyttöliittymästä, services vastaa sovelluslogiikasta ja repositories vastaa tietokannasta. Pakkaus entities sisältää luokkia jotta käytetään sovelluksen datan tallentamiseen ja esittämiseen services- ja repositories-tasoilla.

## Käyttöliittymä

Käyttöliittymä sisältää viisi eri näkymää:  
 - Päänäkymä/ valikko
 - Tositteen lisääminen
 - Kaikkien tositteiden listaesitys
 - Tuloslaskelma
 - Tilikartta / tilien lisääminen

 Käyttöliittymä on toteutettu niin, että joka näkymä on oma luokkansa, ja luokka UI näyttää eri näkymät. Käyttöliittymä kutsuu vain HTService-luokan metodeja.

## Tietojen pysyväistallennus

Pakkauksen repositories luokka VoucherRepository huolehtii tietojen tallettamisesta. Tiedot tallennetaal SQLite-tietoantaan data-kansiossa.

## Päätoiminnallisuudet

Tässä nähdään sekvenssikaavio tositteen tallentamisesta:  

```mermaid
sequenceDiagram
  Main->UI: Click "add voucher" button
  UI->Main: Show add voucher view
  Main->UI: Click "Save" button, input values (1, "10099", "d", 1000, "licence sales")
  UI->HTService: .save_voucher (1, "10099", "d", 1000, "licence sales")
  HTService->VoucherRepository: .save_voucher (1, "10099", "d", 1000, "licence sales")
  VoucherRepository->HTService:True
  HTService->UI:True
  UI->Main:Show message "Saved Voucher"
```  

Sekvenssikaavio tuloslaskelman muodostamisesta:

```mermaid
sequenceDiagram
Main->UI: Click "Income statement" button
UI->HTService: .get_income_statement_lines()
HTService->VoucherRepository: .fetch_accounts()
VoucherRepository->HTService: accounts
HTService->VoucherRepository: .fetch_vouchers()
VoucherRepository->HTService: vouchers
HTService->UI: data
UI->Main:Show income statement view
```  