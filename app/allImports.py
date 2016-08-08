from __future__ import print_function
'''
Include all imports in this file; it will be called at the beginning of all files.
'''
# We need a bunch of Flask stuff
from flask import Flask, render_template, redirect, \
    request, g, url_for
import pprint
from app import models
from models import *                # all the database models
from app.switch import switch       # implements switch/case statements
from flask_security import Security, PeeweeUserDatastore

''' Creates an Flask object; @app will be used for all decorators.
from: http://simeonfranklin.com/blog/2012/jul/1/python-decorators-in-12-steps/
"A decorator is just a callable that takes a function as an argument and 
returns a replacement function. See start.py for an example"
'''

app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SqliteDatabase(cfg['databases']['dev'])

# Setup Flask-Security    
user_datastore = PeeweeUserDatastore(db, User, Role, UserRole)
security = Security(app, user_datastore)
#from app import app

# Builds all the database connections on app run
# Don't panic, if you need clarification ask.

@app.before_request
def before_request():
    g.dbMain =  db.connect()

@app.teardown_request
def teardown_request(exception):
    dbM = getattr(g, 'db', None)
    if (dbM is not None) and (not dbM.is_closed()):
      dbM.close()
