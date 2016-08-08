'''
main.py is the starting point of the application; to run the app, in the console, you run "python app.py"

This file should not change often, except maybe to rename the application from "app" to something more meaningful
such as "helloWorldForm"

To rename the app, you need to make three changes:
1) Change  "from app import app" to "from helloWorldForm import app"
2) Rename the "app" folder to "helloWorldForm"
3) Rename this file to "helloWorldForm.py"

'''
import os

from app import app

# Builds the server configuration
if os.getenv('IP'):
  IP    = os.getenv('IP')
else:
  IP    = '0.0.0.0'

if os.getenv('PORT'):
  PORT  = int(os.getenv('PORT'))
else:
  PORT  = 8080

# Print statements go to your log file in production; to your console while developing
print ("Running server at http://{0}:{1}/".format(IP, PORT))
app.run(host = IP, port = PORT, debug = True, threaded = True)