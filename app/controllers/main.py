from app.allImports import *
from app.logic.switch import switch
from mtgsdk import Card
#Imports

cfg = load_config('config/config.yaml')
db = SqliteDatabase(cfg['databases']['dev'])

@app.route('/')
<<<<<<< HEAD
@login_required
def Index():
  return redirect(url_for('morethan', cnt = 0), code=302)
  
@app.route('/profile')
@login_required
<<<<<<< HEAD
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
=======
def Index():
  # Get all cards
  cards = Card.all()
  
  # Filter Cards
  # You can chain 'where' clauses together. The key of the hash
  # should be the URL parameter you are trying to filter on
  cards = Card.where(supertypes='legendary') \
              .where(types='creature') \
              .where(colors='red,white') \
              .all()
=======
def filedownload(cmd):
  try:
    file = File.select().where(File.id == cmd).get()
    filepath = ('static/files/uploads/'+ str(file.filename)).replace(" ", "")
    return send_file(filepath, as_attachment=True, attachment_filename = file.fulltitle)
>>>>>>> parent of 9e7bcc7... Mering with master
  
  # Get cards on a specific page / pageSize
  cards = Card.where(page=50).where(pageSize=50).all()
  return(str(cards))



>>>>>>> 9c35178847f7ffcfba3bec48c69e42fc82e14e93
















