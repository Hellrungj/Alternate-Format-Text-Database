from allImports import *
from app.switch import switch
from flask import send_file
from flask_security import current_user, login_required, roles_accepted
import os
import datetime
################################################################################

@app.route("/upload", methods = ["GET","POST"])
@login_required
@roles_accepted("Admin","Labor Student")
def upload():
  get_time = datetime.datetime.now()
  Day = get_time.strftime("%Y-%m-%d")
  result = File.select().where(File.last_modified_by == current_user.id)
  return render_template("upload.html", cfg = cfg, items = result)

@app.route("/uploading", methods = ["POST"])
@login_required
@roles_accepted("Admin","Labor Student")
def uploading():
  app.logger.info("Attempting to upload file.")
  ERROR = 0
  file = request.files['file']
  try:
    get_time = datetime.datetime.now()
    time_stamp = get_time.strftime("%Y-%m-%d")
    lastmodified = get_time.strftime("%Y-%m-%d %I:%M")
    filename = ('UploadedFile' + str(time_stamp) + "." + str(file.filename))
    directory_paths = "app/static/files/uploads/"
    if not os.path.exists(directory_paths):
            try:
              os.makedirs(directory_paths)
            except OSError as e:
              print e.errno
              pass
            
    complete_path = (directory_paths + str(filename)).replace(" ", "")
    file.save(complete_path)
    app.logger.info("Upload file.")
    Exists = os.path.exists(complete_path)
    app.logger.info(("Exists: " + str(Exists)))
      
    data = File(  title     = file.filename,
                  author    = " ",
                  edition   = " ",
                  size      = " ",
                  filename  = filename,
                  file_type = str(file.filename.split(".").pop()),
                  created_at = time_stamp,
                  last_modified = lastmodified,
                  last_modified_by = current_user.id,
                  file_path = complete_path,
                  hidden    = 0)
    data.save()
    app.logger.info("Updated the database.")
  except:
    ERROR = 2  
          
  if ERROR == 0:
    return redirect('/upload',code=302)
  else:  
    if ERROR == 1: 
      message = "An error occured during the authentication process"
    else: 
      message = "An error occured during the upload process."
    return message

  
  
  
  
  
  
  
  
  