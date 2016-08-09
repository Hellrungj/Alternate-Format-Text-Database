'''
app.py is the starting point of the application; to run the app, in the console, you run "python app.py"

Just make sure that you run setup.sh and then create_db.py before running python app.py.
This will insure that your system has all the up to date with it's classes and that you have a datebase file.
Thank you for using the DAS Alt. Format Text Database.
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