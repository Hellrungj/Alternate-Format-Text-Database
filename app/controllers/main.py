from app.allImports import *
from app.logic.switch import switch
from flask import session, flash, abort, send_file, redirect
from flask_security import login_required, current_user
#Imports

cfg = load_config('config/config.yaml')
db = SqliteDatabase(cfg['databases']['dev'])

@app.route('/')
@login_required
def Home():
  if UserRole.select().where(UserRole.role == current_user.id, UserRole.user == 1):
    return redirect('/admin',code=302)
  else:
    return redirect('/index',code=302)
    
@app.route('/index')
@login_required
def Index():
  if UserRole.select().where(UserRole.role == current_user.id, UserRole.user == 1) or UserRole.select().where(UserRole.role == current_user.id, UserRole.user == 2):
    items = File.select()
  else:
    items = File.select().where(File.asigned == current_user.id)
  amount = File.select().count()
  Search = "All Titles"
  Notifications = Notification.select().where(Notification.user == current_user.id)
  TotalN = Notification.select().count()
  return render_template('index.html', cfg = cfg, items = items, current_user=current_user,
                          UserRole=UserRole, Notifications=Notifications, TotalN=TotalN)
  
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

@app.route("/testing", methods = ["GET"])
def testing():
   return render_template('notifications.html')
	
	















