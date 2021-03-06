from app.allImports import *
from app.logic.switch import switch
from flask import send_file, session
from flask_security import current_user, login_required, roles_accepted
import os
import datetime
################################################################################

@app.route('/file/<num>', methods=['GET'])
@login_required
@roles_accepted("Admin","Labor Student")
def file(num):
  item = File.select().where(File.id == num).get()
  return render_template("edit.html", item = item, cfg = cfg, UserRole=UserRole)
  
@app.route('/edit/<num>', methods=['POST'])
@login_required
@roles_accepted("Admin","Labor Student")
def edit(num):
  if request.method == 'POST':
    t  = request.form['title']
    a = request.form['author']
    e = request.form['edition']
    item = File.select().where(File.id == num).get()
      
    get_time = datetime.datetime.now()
    time_stamp = get_time.strftime("%Y-%m-%d %H:%M")
    
    item.title = t
    item.author = a
    item.edition = e
    item.last_modified = time_stamp
    item.save()
    
  item = File.select().where(File.id == num).get()
  app.logger.info("Updated the File table in database.")
  Ndata = Notification(title = "Edited a file",
                      date  = str(time_stamp),
                      user = current_user.id)
  Ndata.save()
  app.logger.info("Updated the Notification table in database.")
  return redirect('/index',code=302)

@app.route("/delete/<num>", methods = ["POST"])
@login_required
@roles_accepted("Admin","Labor Student")
def delete(num):
  try:
    file = File.select().where(File.id == num).get()
    #filepath = ('app/static/files/uploads/'+ str(file.filename)).replace(" ", "")
    #os.remove(filepath)
    #file.hidden = 1
    #file.save()
    #RECORD THE CHANGE
    get_time = datetime.datetime.now()
    time_stamp = get_time.strftime("%Y-%m-%d %I:%M")
    update_last_modified = File.update(last_modified=time_stamp, hidden = 1).where(File.id==num)
    update_last_modified.execute()
    app.logger.info("Delete a column in File the table.")
    Ndata = Notification(title = "Deleted a file",
                      date  = str(time_stamp),
                      user = current_user.id)
    Ndata.save()
    app.logger.info("Updated the Notification table in database.")
    return redirect('/index',code=302)
  except Exception,e:
    app.logger.info("{0} attempting to delete a file.".format(str(e)))
    message = "An error occured during the delete process of the file."
    return message
    
