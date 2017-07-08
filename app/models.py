from allImports import *
from peewee import *
from flask_peewee.db import Database
from flask_security import UserMixin, RoleMixin

import os
#from allImports import *   #Don't believe this import is needed for this file
# Create a database
from app.loadConfig import *

cfg = load_config('config/config.yaml')
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

class Food(BaseModel):
    name = CharField(max_length=80)
    calories = IntegerField(null=True)
    serving_size = IntegerField(null=True)
    total_fat = IntegerField(null=True)
    saturated_fat = IntegerField(null=True)
    trans_fat = IntegerField(null=True)
    cholesterol = IntegerField(null=True)
    sodium = IntegerField(null=True)
    total_carbohydrate = IntegerField(null=True)
    dietray_fiber = IntegerField(null=True)
    suger = IntegerField(null=True)
    protein = IntegerField(null=True)
    vitamin_a = IntegerField(null=True)
    vitamin_c = IntegerField(null=True)
    calcium = IntegerField(null=True)
    iron = IntegerField(null=True)
    amount = IntegerField(null=True)
    
    def __unicode__(self):
        return self.name
    
class Profile(BaseModel):
    user = ForeignKeyField(User, related_name='profile')
    calories = IntegerField()
    

    