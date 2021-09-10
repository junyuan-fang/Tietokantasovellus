# Keskustelusovellus  
Sovelluksessa näkyy keskustelualueita, joista jokaisella on tietty aihe. Alueilla on keskusteluketjuja, jotka muodostuvat viesteistä. Jokainen käyttäjä on peruskäyttäjä tai ylläpitäjä.

## Sovelluksen ominaisuuksia:
* Käyttäjä
  * Etusivulla
    * Luoda uuden tunnuksen
    * Kirjaudu tunnuksella sisään. Kirjaudu ulos
    * Näkee  1. listalla hänen osallistuman keskustelujen otsikot, lukemattomien viestien määrä, keskustelussa viimeksi lähetetyn viestin ajankohdan.
    * Näkee  2. listalla muut käyttäjät jotka haluvat liittyä omistamaasi keskustelun alueeseen
    * Pääsee käyttäjän henkilökohtaiseen sivustoon
  * Henkilökohtainen sivustolla
    * Pääsee muokkamaan yhteystiedot.
  * 2.lista: Lista on sulautettu etusivulle, mikä käsittelee lisäyksen pyyntöä
    * Näkee pyyntöä muodossa: "User1" want add "User2" to "Group"
    * Admin käyttäjä voi vahvistaa pyyntöä
  * Keskustelualueella 
    * Voi lisätä/poistaa keskustelun osallistujat
    * Voi kirjoittaa uuden viestin olemassa olevaan ketjuun.
    * Voi muokata luomansa ketjun otsikkoa sekä lähettämänsä viestin sisältöä.
    * Voi myös poistaa ketjun tai viestin.
    * Voi etsiä kaikki viestit, joiden osana on annettu sana.
    * Voi etsiä käyttäjät.(Valitsemalla käyttäjän painikkeella siirrytään Käyttäjän sivustolle)
    * Pääsee etusivulle takaisin
  * Käyttäjän sivusto
    * Näkee käyttäjän nimi, yhteystiedot
    * Voi lisätä käyttäjä keskustelualueeseen(Admin)
      * peruskäyttäjä tulee lähettämään pyyntöä Adminin etusivun 2.listalle 
    * Voi poistaa käyttäjä keskustelualueelta(Admin)
    * Pääsee keskustelualueelle takaisin 
  
* Ylläpitäjä 
  * Näkee kaikki keskustelualueita
  * Voi lisätä ja poistaa keskustelualueita.
  * Voi muokata käyttäjän tietoa, tai poistaa käyttäjä tietokannasta
