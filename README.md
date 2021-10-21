# Keskustelusovellus  
Sovelluksessa näkyy keskustelualueita, joista jokaisella on tietty aihe. Alueilla on keskusteluketjuja, joita muodostuvat viesteistä. Jokainen käyttäjä on peruskäyttäjä. Admin on Alueen kohtainen. Peruskäyttäjä voi luoda "private" tai "public" alueen. Peruskäyttääjä voi lisätä toinen peruskäyttäjä alueeseen, johon hän on liittynyt. Admin käyttäjä tulee vahvistaa pyyntöä etusivun kautta.
* Hierarkkiat:
 * Alue(Forum)
 * Ketju(Topic)
 * Viesti(Message)


## Sovelluksen ominaisuuksia:
* Käyttäjä
  * Etusivulla
    * Luoda uuden tunnuksen :heavy_check_mark:
    * Kirjaudu tunnuksella sisään. Kirjaudu ulos ✔️
    * Näkee  listalla "public" ja hänen osallistuman "private" alueen otsikot, ketjujen ja viestien määrä ja viimeksi lähetetyn viestin ajankohdan. :heavy_check_mark:
    * Alueen otsikon kautta pääsee kyseiselle aluelle ✔️
    * Pääsee 
     * 1. "Create forum"  Voi luoda uuden private/public alueen antamalla aluen nimi. ✔️
     * 2. "Search messages" 
      * Voi etsiä kaikki viestit, joiden osana on annettu sana. ✔️
      * Näytetään kaikki "Public" alueen liittyvät viestit + kaikki käyttäjä osallistuman "Private" alueen viestit ✔️
      * Navigointi suoraan alueseen ✖️
     * 3. "Show requests" 
      * Tämä painike näkyy, jos hän on joku alueen Admin :heavy_check_mark:
      * Alueen kohtainen Admin käyttäjä voi vahvistaa tai hylkää pyyntöä ✖️
      * Pyyntö on muodossa: "User1" want add "User2" to private "Forum". ✖️
  * Alueella
    * Näkee  listalla "Topic id ", "Title" ja viestien määrä ✔️
    * Ketjun otsikon kautta pääsee kyseiselle ketjulle ✔️
    * Pääsee etusivulle takaisin. heavy_check_mark: 
    * Painikkeet
     * 1. "Create topic"
      * Voi luoda uuden ketjun antamalla ketjun otsikko ja aloitusviestin sisällön. Alueen luoja on admin ✔️
     * 2. "Remove forum"
      * Vain admin pääsee poistamaan alueen ✖️
     * 3. "Show users"
      * Näyttää kaikki Alueen osallistujat ✔️
     * 4. "Invite user"
      * Muodosta "Request" viestin alueen Adminille.✖️
      * 5. "Users not in forum"
       * Näyttää käyttäjät, jotka ei ole alueessa vielä ✖️
  * Ketjulla
    * Näkee  listalla "Message id","User id", "Content, "Sent at ✔️
    * Pääsee alueelle takaisin ✔️mark: 
    * Viestin kirjoittaja pääsee muokkamaan viestiä ✖️️
    * Admin, ketjun luoja ja viestin kirjoittaja pääsee poistamaan viestin ✖️️
    * Painikkeet
     * 1. "Create Message"
      * Voi kirjoittaa uuden viestin ketjulle ✔️
     * 2. "Remove topic"
      * Vain ketjun luojalle ja Adminille näytetään tätä painiketta ✖️
      * Vain ketjun luoja ja Admin pääsee poistamaan alueen ✖️
    




#### Nykyinen tilanne（26.09.2021）:
* Tietokannan "CREATE" taulut näkyy "schema.sql" tiedostossa.<a href="https://github.com/junyuan-fang/WebChatting/blob/master/SQL.png" target="_blank">SQL.png</a>
* html-sivustot on jaettu karkeasti
* Käyttäjäliittymä on piirretty karkeasti. <a href="https://github.com/junyuan-fang/WebChatting/blob/master/Kayttoliittyma.pdf" target="_blank">Kayttoliittyma.pdf</a>
* Sivusto voidaan avata herokussa, mutta sivut ovat täysin tyhjiä.
* Click [here](https://web-chatting-app.herokuapp.com/) to the website.


#### Nykyinen tilanne（10.10.2021）:
* On mahdollista, että sovelluksessa löytyy muita haavoittuvuuksia kuin SQL-injektio.
* "request" osuus ja "haut" nämä ominaisuudet ovat toteuttamatt.
* 1-kysely on kesken
* Sovellus toimii paikallisessa ympäristössä. Herokussa ei ole testattu huolellisesti.
* Click [here](https://web-chatting-app.herokuapp.com/) to the website.

