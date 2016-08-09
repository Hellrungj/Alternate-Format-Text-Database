from app.allImports import *
from app.logic.switch import switch
from flask import session, flash, abort, send_file, redirect
from flask_security import login_required, current_user
#Imports

cfg = load_config('app/config/config.yaml')
db = SqliteDatabase(cfg['databases']['dev'])

@app.route('/')
@login_required
def Home():
  if UserRole.select().where(UserRole.role == current_user.id, UserRole.user == 1):
    return redirect('/admin',code=302)
  else:
    return redirect('/index',code=302)
    #return str(current_user.UserRole)
    
    
@app.route('/index')
@login_required
def Index():
  items = File.select()
  amount = File.select().count()
  Search = "All Titles"
  return render_template('index.html', cfg = cfg, items = items)
  
@app.route("/download/<cmd>/", methods = ["POST","GET"])
@login_required
def filedownload(cmd):
  try:
    file = File.select().where(File.id == cmd).get()
    filepath = ('static/files/uploads/'+ str(file.filename)).replace(" ", "")
    return send_file(filepath, as_attachment=True, attachment_filename = file.fulltitle)
  
  except Exception,e:
    app.logger.info("{0} attempting to upload file.".format(str(e)))
    message = "An error occured during the download process."
    return message


	
	















