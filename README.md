# Keskustelusovellus  
Sovelluksessa näkyy keskustelualueita, joista jokaisella on tietty aihe. Alueilla on keskusteluketjuja, jotka muodostuvat viesteistä. Jokainen käyttäjä on peruskäyttäjä tai ylläpitäjä. Peruskäyttäjä voi luoda "private" tai "public" alueen. Peruskäyttääjä voi lisätä toinen peruskäyttäjä alueeseen, johon hän on liittynyt. Admin käyttäjä tulee vahvistaa pyyntöä etusivustolla. 


## Sovelluksen ominaisuuksia:
* Käyttäjä
  * Etusivulla
    * Luoda uuden tunnuksen
    * Kirjaudu tunnuksella sisään. Kirjaudu ulos
    * Näkee  1. listalla "public" ja hänen osallistuman "private" alueen otsikot, ketjujen ja viestien määrä ja viimeksi lähetetyn viestin ajankohdan.
    * Näkee  2. listalla muut käyttäjät jotka haluvat liittyä "private" keskustelun alueeseen.
    * Voi luoda uuden private/public alueen antamalla aleen nimi.
  * 2.lista: Lista on sulautettu etusivulle, mikä käsittelee lisäyksen pyyntöä
    * Näkee pyyntöä muodossa: "User1" want add "User2" to "Group" private group.
    * Admin käyttäjä voi vahvistaa pyyntöä.
  * Keskustelualueella 
    * Voi luoda uuden ketjun antamalla ketjunotsikko ja aloitusviestin sisällön.
    * Voi kirjoittaa uuden viestin olemassa olevaan ketjuun.
    * Voi muokata luomansa ketjun otsikkoa sekä lähettämänsä viestin sisältöä. 
    * Voi myös poistaa ketjun tai viestin(admin).
    * Voi etsiä kaikki viestit, joiden osana on annettu sana.
    * Voi etsiä alueella ja alueen ulkopuolella olevat käyttäjät.(Valitsemalla käyttäjän painikkeella siirrytään Käyttäjän sivustolle).
    * Pääsee etusivulle takaisin.
  * Käyttäjän sivusto
    * Näkee käyttäjän tunnus.
    * Voi lisätä käyttäjä keskustelualueeseen(Admin).
      * peruskäyttäjä tulee lähettämään pyyntöä Adminin etusivun 2.listalle 
    * Voi poistaa käyttäjä keskustelualueelta(Admin).
    * Pääsee keskustelualueelle takaisin .

* Ylläpitäjä 
  * Näkee kaikki keskustelualueita
  * Voi lisätä ja poistaa keskustelualueita.    
  * Voi luoda salaisen alueen ja määrittää, keillä käyttäjillä on pääsy alueelle.
