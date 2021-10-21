# Keskustelusovellus  
Sovelluksessa näkyy keskustelualueita, joista jokaisella on tietty aihe. Alueilla on keskusteluketjuja, joita muodostuvat viesteistä. Jokainen käyttäjä on peruskäyttäjä. Admin on Alueen kohtainen. Peruskäyttäjä voi luoda "private" tai "public" alueen. Peruskäyttääjä voi lisätä toinen peruskäyttäjä alueeseen, johon hän on liittynyt. Admin käyttäjä tulee vahvistaa pyyntöä etusivun kautta.
* Hierarkkiat:
 * Alue = Forum
 * Ketju = Topic
 * Viesti = Message

## Sovelluksen ominaisuuksia:

### Etusivulla
* Luoda uuden tunnuksen :heavy_check_mark:
* Kirjaudu tunnuksella sisään. Kirjaudu ulos ✔️
* Näkee  listalla "public" ja hänen osallistuman "private" alueen otsikot, ketjujen ja viestien määrä ja viimeksi lähetetyn viestin ajankohdan. :heavy_check_mark:
* Alueen otsikon kautta pääsee kyseiselle aluelle ✔️
* "Create forum"  
  * Voi luoda uuden private/public alueen antamalla aluen nimi. ✔️
* "Search messages" 
  * Voi etsiä kaikki viestit, joiden osana on annettu sana. ✔️
  * Näytetään kaikki "Public" alueen liittyvät viestit + kaikki käyttäjä osallistuman "Private" alueen viestit ✔️
  * Navigointi suoraan alueseen ✔️
* "Show requests" 
  * Tämä painike näkyy, jos hän on joku alueen Admin :heavy_check_mark:
  * Alueen kohtainen Admin käyttäjä voi vahvistaa tai hylkää pyyntöä ✖️
  * Pyyntö on muodossa: "User1" want add "User2" to private "Forum". ✖️
  * Navigointi suoraan alueseen ✔️
### Alueella
* Näkee  listalla "Topic id ", "Title" ja viestien määrä ✔️
* Ketjun otsikon kautta pääsee kyseiselle ketjulle ✔️
* Pääsee etusivulle takaisin. ✔️
* "Create topic"
  * Voi luoda uuden ketjun antamalla ketjun otsikko ja aloitusviestin sisällön. Alueen luoja on admin ✔️
* "Remove forum"
  * Vain admin pääsee poistamaan alueen ✖️
* "Show users"
  * Näyttää kaikki Alueen osallistujat ✔️
* "Invite user"
  * Muodosta "Request" viestin alueen Adminille.✖️
  * "Users not in forum"
   * Näyttää käyttäjät, jotka ei ole alueessa vielä ✖️
### Ketjulla
* Näkee  listalla "Message id","User id", "Content, "Sent at ✔️
* Pääsee alueelle takaisin ✔️mark: 
* Viestin kirjoittaja pääsee muokkamaan viestiä ✖️️
* Admin, ketjun luoja ja viestin kirjoittaja pääsee poistamaan viestin ✖️️
* "Create Message"
  * Voi kirjoittaa uuden viestin ketjulle ✔️
* "Remove topic"
  * Vain ketjun luojalle ja Adminille näytetään tätä painiketta ✖️
  * Vain ketjun luoja ja Admin pääsee poistamaan alueen ✖️
    
***



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

