# pythonProject10_FLASK_SITE_BLOG
Сначала откройте отдельно cmd обязательно от администратора и там введите setx /M path "%path%;c:/program files/heroku/bin" 

терминал
git init
heroku git:remote -a flask15

pip install gunicorn

pip freeze > requirements.txt

new file Procfile
внем web: gunicorn app:app

Терминал
git add .

 git commit -am "make it better"
 git push heroku master

https://flask15.herokuapp.com/
https://git.heroku.com/flask15.git
1
