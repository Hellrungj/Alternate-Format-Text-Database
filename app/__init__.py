'''
This file is called by "from app import app" inside the app.py file. 

It includes all the imports to be used in the app (from allImports import *).
It also includes all the application files that are used as "pages" in the app
(e.g., "from app import start" imports all the code in start.py that is behind the start.html webpage)
'''

from app.allImports import *
from app import allImports

# Include an import for every python file that is serving a webpage
#import your new python files here. It is not a part of the module until it is imported
print("Starting application")
from app.controllers.admin import *
from app.controllers.auth import *
from app.controllers.edit import *
from app.controllers.main import *
from app.controllers.upload import *
from app.controllers.forms import *