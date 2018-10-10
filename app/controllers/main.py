from app.allImports import *
from app.logic.switch import switch
from flask_security import login_required
#Imports

cfg = load_config('config/config.yaml')
db = SqliteDatabase(cfg['databases']['dev'])

@app.route('/')
@login_required
def Index():
  return redirect(url_for('morethan', cnt = 0), code=302)
  
@app.route('/profile')
@login_required
def Profile():
  food = Food.select()
  return render_template("profile.html", cfg = cfg, User=str(current_user.username), food = food )
  
@app.route('/morethan/<int:cnt>')
def morethan (cnt):
  # We scan all of the items, finding ones that have a 
  # count greater than the value of the variable 'cnt'.
  # response = Item.scan(count__gt = cnt)
  response = Food.select().where(Food.amount > cnt)
  # Render the search results, passing the list of items
  # that we found in our scan.
  return render_template('searchresults.html', items = response)  

@app.route('/contains/<search_string>', methods = ['POST', 'GET'])
def contains (search_string):
  # If they did a post, then just redirect to the GET version
  # The FORM on the page does a POST, so we handle this here
  # in this way.
  if request.method == 'POST':
    return redirect("/contains/{0}".format(request.form['name']))
  # By redirecting to the GET, we guarantee bookmarkable search results.
  elif request.method == 'GET':
    search_result = Food.select().where(Food.name.contains(search_string))
    return render_template('searchresults.html', items = search_result)
  else:
    # FIXME: Return a proper error message here.
    return "404"

@app.route('/insert', methods = ['POST'])
def insert ():
  # This only handles POST requests.
  if request.method == 'POST':
    n  = request.form['name']
    c = request.form['calories']
    a = int(request.form['amount'])
    # Field name = variable
    stuff = Food(name = n, amount = a, calories = c)
    stuff.save()
    return redirect("/")
  else:
    # FIXME: Properly handle other request types.
    return "404"
















