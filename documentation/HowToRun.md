

* Virtuaaliympäristö
  * ```python3 -m venv venv```
  * ```source venv/bin/activate```
  * ```deactivate```
* SQL
  * ```start-pg.sh```
  * ```psql < schema.sql```
  * ```Ctrl-C```
* Heroku
  *  Adding enviroments
    *  ```pip freeze > requirements.txt```
    *  ```git add requirements.txt```
    *  ```git commit -m "Add requirements"```
    *  ```git push```
  *  Installation of enviroment
    *  ```pip install -r requirements.txt```
  *  Update
    *  ```heroku login```
    *  ```git push heroku master:main```
  *  SQL
    *  ```heroku psql```
    *  ```heroku psql < schema.sql```
*  Easier to run
     *  ```export FLASK_APP=app.py```
     *  ```export FLASK_ENV=development```
     *  ```flask run```
*  fly
   *  Update  
     *  ```fly auth login```   
     *  ```fly launch```  
   *  Update  
     *  ```fly auth login```   
     *  ```fly launch``` 
     
