# DAS-Alternate-Format-Text-Database
DAS Alt. Format Text Database is PeeWee Flask Web Application that combines Flask-Security and Flask-Admin  
by John Hellrung
August 8, 2016

Thanks you to Flask, PeeWee, Flask-Security, and Flask-Admin to providing a convenient way to made a Flask web app.
Flask provides a quick and easy web application
PeeWee provides a quick and easy databae API
Flask-Admin provides CRUD operations on database tables. 
Flask-Security handles the authentication and authorization of the Flask web app.
Flask-Security and Flask-Admin both allow authoriztion of users and maintainace of the database. 
Flask-Admin provides a convenient way to add a  around the current Flask web app.  

Here are some helpful links:
- Flask: http://flask.pocoo.org/
- PeeWee: http://docs.peewee-orm.com/en/latest/
- Flask-PeeWee: http://docs.peewee-orm.com/projects/flask-peewee/en/latest/
- Flask-Admin: https://flask-admin.readthedocs.org/en/latest/
- Flask-Security: https://pythonhosted.org/Flask-Security/
- SQLite database: https://sqlite.org/
- The Jinja Documentation: http://jinja.pocoo.org/docs/dev/
- The Configure Documentation: http://configure.readthedocs.io/en/latest/#

To run this app, you'll need to run:
- setup.sh  
- create_db.py
- app.py

You will need to install:
-  Python 2.7

The Setup.sh file will install:
- Flask
- Peewee
- pyyaml
- Flask-PeeWee
- Flask-Admin
- Flask-Security

The create_db.py file will:
- Create the database file in the folder data
- Name the file DAS.db
- Create the tables in the database

If there is an Flask import errors try running the command . venv/bin/activate and then run the app.py again.  

I personally ran this code on Cloud 9 with a PeeWee database, but you should be able to use any operating system and database system of your choice as along as it compatable with Flask.

Once you have the app running, you can view it in your browser (e.g. http://localhost:8080).
If you are in Cloud 9 and having trouble checkout this article: http://damyanon.net/getting-started-with-flask-on-cloud9/ 

Notes (Please Read):
- When you first visit the app's home page, you'll be prompted to log in, thanks to
Flask-Security.
- If you log in with username=DASStudent@berea.edu and password=password, you'll have the
"Student" role.
- If you log in with username=DASLaborStudent@berea.edu and password=password, you'll have the
"Lobor Student" role.
- If you log in with username=DASadmin@berea.edu and password=password, you'll have the "admin"
role.
- Either LaborStudent or Student role are permitted to access any of the admin views.
- Either Student is permitted to access other than index page. 
- Only the admin role is permitted to access to the whole database. Otherwise, you'll get a "forbidden" respone.
- Note that, when editing a user, role, or userroles the names of roles and users are automatically populated thanks to
Flask-Admin.
- You can add and edit users, roles and assign user a role. The resulting users will be able to log in (unless you
set active=false) and, if they have the "admin" role, will be able to perform administration.
- For future update about about DAS-Alt. Format Text Database checkout my blog: https://hellrungj.wordpress.com/

