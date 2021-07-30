# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
from flask import url_for
from flask import session
from flask import redirect
from flask_pymongo import PyMongo
from datetime import datetime
# from flask.ext.bcrypt import Bcrypt
# import bcrypt
# from flask import bcrypt
# from flask.ext.bcrypt import Bcrypt
# from flask.ext.pymongo import PyMongo
# from flask_pymongo import PyMongo
# -- Initialization section --
app = Flask(__name__)
# bcrypt = bcrypt(app)
# events = [
#         {"event":"First Day of Classes", "date":"2019-08-21"},
#         {"event":"Winter Break", "date":"2019-12-20"},
#         {"event":"Finals Begin", "date":"2019-12-01"}
#     ]
# name of database
app.config['MONGO_DBNAME'] = 'login'
# URI of database
app.config['MONGO_URI'] = 'mongodb+srv://admin_1:TJ3mIWlbo1eAXnAc@cluster0.6yt5n.mongodb.net/login?retryWrites=true&w=majority'
mongo = PyMongo(app)
# -- Routes section --
# INDEX
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", time = datetime.now())
# CONNECT TO DB, ADD DATA
@app.route('/add')
def add():
    # connect to the database
    # insert new data
    # return a message to the user
    return ""
@app.route('/myAccount', methods = ['GET', 'POST'])
def myAccount():
    return """<h1>Set up information for account details</h1>"""
@app.route('/Sell', methods = ['GET', 'POST'])
def Sell():
    return """<h1>Set up information selling items</h1>"""
@app.route('/Balance', methods = ['GET', 'POST'])
def Balance():
    return """<h1>Set up information for users Balance</h1>"""
#What works
@app.route('/Login')
def Login():
    if 'username' in session:
        return 'You are logged in as ' + session['username']
#Sign up information page
@app.route('/Login', methods = ['GET', 'POST'])
@app.route('/Login')
def Login():
    if 'username' in session:
        return 'You are logged in as' + session['username']
    return render_template('Login.html')
    return """<h1>Set up information for login/sign up page</h1>"""
@app.route('/login', methods=['POST'])
@app.route('/Login')
def index():
    if 'username' in session:
        return 'You are logged in as ' + session['username']
    return render_template('Login.html')
@app.route('/login', methods=['POST' , 'GET'])
def login():
    if request.method == 'POST':
        users = mongo.db.users
        users.insert({'username': 'test', 'password': 'test'})
        login_user = users.find_one({'username' : request.form['username']})
        if login_user != None:
            print('found user')
            if request.form["password"] == login_user['password']:
                # session['username'] = request.form['username']
                return redirect(url_for('index'))
        return 'Invalid username/password combination'
    else:
        return render_template('Login.html')
@app.route('/register', methods=['POST', 'GET'])
def register():
    collection = mongo.db.users
    if request.method == "POST":
        if collection.find_one({"username": request.form['username']}) == None:
            collection.insert({"username": request.form['username'], "password": request.form['password']})
            print("added user")
            return redirect(url_for('index'))
        else:
            return "An account with that username already exists"
    return render_template('register.html')   
#end of sign up information page
@app.route('/Info', methods = ['GET', 'POST'])
def Info():
    return """<img src = "https://cdn.vox-cdn.com/thumbor/s7qMSKpeavBerH1LCyFPIkNrW4k=/0x0:900x500/1400x1050/filters:focal(378x178:522x322):format(jpeg)/cdn.vox-cdn.com/uploads/chorus_image/image/49493993/this-is-fine.0.jpg">"""
@app.route('/Deals', methods = ['GET', 'POST'])
def Deals():
    return """<h1>Set up information for item deals</h1>"""
@app.route('/Cart', methods = ['GET', 'POST'])
def Cart():
    return """<h1>Set up information for shopping cart.</h1>"""