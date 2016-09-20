# WARNING: NOT FOR USE IN PRODUCTION AFTER REAL DATA EXISTS!!!!!!!!!!!!!!!!!!!!!!
'''
This script creates the database tables in the SQLite file. 
Update this file as you update your database.
'''
import os, sys
import importlib

# Don't forget to import your own models!
from app.models import *

conf = load_config('config/config.yaml')

sqlite_dbs  = [ conf['databases']['dev']
                # add more here if multiple DBs
              ]

# Remove DBs
for fname in sqlite_dbs:
  try:
    print ("Removing {0}.".format(fname))
    os.remove(fname)
  except OSError:
    pass

# Creates DBs
for fname in sqlite_dbs:
  if os.path.isfile(fname):
    print ("Database {0} should not exist at this point!".format(fname))
  print ("Creating empty SQLite file: {0}.".format(fname))
  open(fname, 'a').close()
  

def class_from_name (module_name, class_name):
  # load the module, will raise ImportError if module cannot be loaded
  # m = __import__(module_name, globals(), locals(), class_name)
  # get the class, will raise AttributeError if class cannot be found
  c = getattr(module_name, class_name)
  return c
    
"""This file creates the database and fills it with some dummy run it after you have made changes to the models pages."""
def get_classes (db):
  classes = []
  for str in conf['models'][db]:
    print ("\tCreating model for '{0}'".format(str))
    c = class_from_name(sys.modules[__name__], str)
    classes.append(c)
  return classes

  
db.create_tables(get_classes('mainDB'))

###############
#Data Creation#
###############

# Creating the DASAdmin User and Role and Assigning the User a Role of Admin
user1  = User ( username  = "DASAdmin",
                email     = "DASAdmin@berea.edu",
                password  = "Password"
                ).save()

role1 = Role ( name = "Admin",
              description = "All Access."
              ).save()
              
userrole = UserRole ( user = 1,
                      role = 1
                      ).save()
                      
# Creating the DASLaborStudent User and Role Assigning the User a Role of LaborStudent 
user2  = User ( username  = "DASLaborStudent",
                email     = "DASLaborStudent@berea.edu",
                password  = "Password"
                ).save()

role2 = Role ( name = "LaborStudent",
              description = "Semi Access. No Admin Access."
              ).save()
              
userrole = UserRole ( user = 2,
                      role = 2
                      ).save()
                      
# Creating the DASStudent User and Role Assigning the User a Role of Student  
user3  = User ( username  = "DASStudent",
                email     = "DASStudent@berea.edu",
                password  = "Password"
                ).save()

role3 = Role ( name = "Student",
              description = "Limited Access."
              ).save()
              
userrole = UserRole ( user = 3,
                      role = 3
                      ).save()

# Creating default status
status_open = Status (title = "Open",
                      description = "Shows that the request is open."
                      ).save()
                      
status_close = Status (title = "Close",
                      description = "Shows that the request is closed."
                      ).save()
