from allImports import *
from peewee import *
from flask_peewee.db import Database
from flask_security import UserMixin, RoleMixin

import os
#from allImports import *   #Don't believe this import is needed for this file
# Create a database
from app.loadConfig import *

cfg = load_config('app/config.yaml')
db = SqliteDatabase(cfg['databases']['dev'])

# Create database connection object
class BaseModel(Model):
  class Meta:
    database = db

class Role(BaseModel, RoleMixin):
    name = CharField(unique=True)
    description = TextField(null=True)
    
    def __unicode__(self):
        return self.name

class User(BaseModel, UserMixin):
    username = CharField(max_length=80)
    email = CharField(max_length=120)
    password = TextField()
    active = BooleanField(default=True)
    confirmed_at = DateTimeField(null=True)
    notes = TextField(null=True)
    
    def __unicode__(self):
        return self.username

class UserRole(BaseModel):
    # Because peewee does not come with built-in many-to-many
    # relationships, we need this intermediary class to link
    # user to roles.
    user = ForeignKeyField(User, related_name='roles')
    role = ForeignKeyField(Role, related_name='users')
    name = property(lambda self: self.role.name)
    description = property(lambda self: self.role.description)

class Post(BaseModel):
    title = CharField(max_length=120)
    text = TextField(null=False)
    date = DateTimeField()
    user = ForeignKeyField(User)

    def __unicode__(self):
        return self.title

class File(BaseModel):
    title = TextField()
    author = TextField()
    edition = TextField()
    size = TextField()
    filename = TextField()
    file_type = TextField()
    created_at = DateTimeField()
    last_modified = DateTimeField()
    last_modified_by = ForeignKeyField(User)
    file_path = TextField()
    hidden = IntegerField() 

