from app.allImports import *
from app.logic.switch import switch
from flask import send_file
from flask_security import current_user, login_required, roles_accepted
from hurry.filesize import size
import os
import datetime
################################################################################

@app.route("/upload", methods = ["GET","POST"])
@login_required
@roles_accepted("Admin","Labor Student")
def uploadform():
  return render_template("upload.html", cfg = cfg, UserRole=UserRole)

@app.route("/uploading", methods = ["POST"])
@login_required
@roles_accepted("Admin","Labor Student")
def uploading():
  try:
    app.logger.info("Attempting to upload file.")
    ERROR = 0
    file = request.files['file']
    title = request.form['title']
    author = request.form['author']
    edition = request.form['edition']
    #try:
    get_time = datetime.datetime.now()
    time_stamp = get_time.strftime("%Y-%m-%d")
    lastmodified = get_time.strftime("%Y-%m-%d %I:%M")
    filename = (str(time_stamp) + "." + str(file.filename))
    directory_paths = "app/static/files/uploads/"
    if not os.path.exists(directory_paths):
      try:
        os.makedirs(directory_paths)
      except OSError as e:
        print e.errno
        pass
            
    complete_path = (directory_paths + str(filename)).replace(" ", "")
    filesize = os.path.getsize(path)
    convertedsize = size(filesize)
    file.save(complete_path)
    app.logger.info("Upload file.")
    Exists = os.path.exists(complete_path)
    app.logger.info(("Exists: " + str(Exists)))
      
    Fdata = File(  title     = title,
                  author    = author,
                  edition   = edition,
                  size      = convertedsize,
                  filename  = filename,
                  file_type = str(file.filename.split(".").pop()),
                  created_at = str(time_stamp),
                  last_modified = str(time_stamp),
                  asigned = current_user.id,
                  file_path = complete_path,
                  hidden    = 0)
    Fdata.save()
    app.logger.info("Updated the File table in database.")
    Ndata = Notification(title = "Uploaded a file",
                        date  = str(time_stamp),
                        user = current_user.id)
    Ndata.save()
    app.logger.info("Updated the Notification table in database.")
  except:
    ERROR = 2  
          
  if ERROR == 0:
    return redirect('/index',code=302)
  else:  
    if ERROR == 1: 
      message = "An error occured during the authentication process"
    else: 
      message = "An error occured during the upload process."
    return message
    
@app.route("/admin/uploading", methods = ["POST"])
@login_required
@roles_accepted("Admin","Labor Student")
def AdminUploading():
  try:
    app.logger.info("Attempting to upload file.")
    ERROR = 0
    file = request.files['file']
    title = request.form['title']
    author = request.form['author']
    edition = request.form['edition']
  #  asign = request.form['asign']
  #  asigned = User.select(User.id).where(User.username == asign)
    #try:
    get_time = datetime.datetime.now()
    time_stamp = get_time.strftime("%Y-%m-%d")
    lastmodified = get_time.strftime("%Y-%m-%d %I:%M")
    filename = (str(time_stamp) + "." + str(file.filename))
    directory_paths = "app/static/files/uploads/"
    if not os.path.exists(directory_paths):
      try:
        os.makedirs(directory_paths)
      except OSError as e:
        print e.errno
        pass
            
    complete_path = (directory_paths + str(filename)).replace(" ", "")
    filesize = os.path.getsize(path)
    convertedsize = size(filesize)
    file.save(complete_path)
    app.logger.info("Upload file.")
    Exists = os.path.exists(complete_path)
    app.logger.info(("Exists: " + str(Exists)))
      
    Fdata = File(  title     = title,
                  author    = author,
                  edition   = edition,
                  size      = convertedsize,
                  filename  = filename,
                  file_type = str(file.filename.split(".").pop()),
                  created_at = str(time_stamp),
                  last_modified = str(time_stamp),
                  asigned = current_user.id,
                  file_path = complete_path,
                  hidden    = 0)
    app.logger.info("Updated the File table in database.")
  except:
    ERROR = 2  
          
  if ERROR == 0:
    return redirect('/admin/file',code=302)
  else:  
    if ERROR == 1: 
      message = "An error occured during the authentication process"
    else: 
      message = "An error occured during the upload process."
    return message
    








