from app.allImports import *
from app.logic.switch import switch
from flask import session, flash, abort, send_file, redirect
from flask_security import login_required, current_user
import datetime

################################################################################

@app.route('/request/', methods=['GET'])
@login_required
def RequestForm():
    return render_template("request.html", cfg = cfg, UserRole=UserRole)
  
@app.route('/request/submit/', methods=['POST'])
@login_required
def SubmitRequest():
    app.logger.info("Attempting to upload a request.")
    title = request.form['title']
    author = request.form['author']
    edition = request.form['edition']
    ISBN = request.form['ISBN']
    get_time = datetime.datetime.now()
    time_stamp = get_time.strftime("%Y-%m-%d")
    
    Rdata = Request(title   = title,
                    author  = author,
                    edition = edition,
                    ISBN    = ISBN,
                    created_at = time_stamp,
                    user    = current_user.id)
    Rdata.save()
    app.logger.info("Updated the File table in database.")
    Ndata = Notification(title = "Submit a request",
                        date  = str(time_stamp),
                        user = current_user.id)
    Ndata.save()
    app.logger.info("Updated the Request table in database.")    
    return redirect('/index', code=302)
    
@app.route('/request/view/<cmd>', methods=['GET'])
@login_required
def RequestFormView(cmd):
    request = Request.select().where(Request.id == cmd).get()
    return render_template("admin/request.html", request=request, cfg = cfg, UserRole=UserRole)
    
    
    
    
    
    
    
    