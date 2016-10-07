from flask import Flask, render_template, request, url_for, session
from utils import makeacc
import random, os


app=Flask(__name__)
app.secret_key='\xcf/\xc9\xdc\x1a\xc3\xe4\xc23\\v(\xad\x1d\xa7i4\x10J\x9b)\xbe\x82\\b\x12|\xf3\xfa\xfc\xdc'

@app.route("/")
def home():
    if request.form['user'] != session['user']:
        return redirect(url_for('login'))
    else:
        return render_template("home.html", title = "Home",message = request.form['user']

@app.route("/login/")
def login():
    if request.form['user'] in session:
    return render_template("form.html", title = "Login", result = "")

@app.route("/register/")
def register():
    return render_template("register.html", title = "Register")

@app.route("/authenticate/", methods = ['POST'])
def auth():
    #print request.form['user']
    #print request.form['pass']
    if request.form['user'] in makeacc.users():
        return render_template("result.html", result = "FAILURE! Please try again.", message = "Return and try again!")
    else:
        makeacc.writetofile(request.form['user'],request.form['pass'])
        return render_template("form.html", title = "login", result = "SUCCESS! Your account was created! Log in now.")

@app.route("/loggedin/", methods = ['POST'])
def loggedin():
    if request.form['user'] in makeacc.users():
        #print makeacc.encrypt(request.form['pass'])
        #print makeacc.encrypt(request.form['pass']) == makeacc.updatedict(request.form['user'])
        #print makeacc.updatedict(request.form['user'])
        if makeacc.encrypt(request.form['pass']).strip() == makeacc.updatedict(request.form['user']).strip():
            session['user'] = request.form['user']
            return render_template("result.html", result = "SUCCESS! You have logged in!", message = "Return to make another account!")
        else:
            return render_template("result.html", result = "FAILURE! Bad password", message = "Return to try again.")
    else:
        return render_template("result.html", result = "FAILURE! Bad username", message = "Return to try again.")
        
    
if __name__== '__main__':
    app.debug = True
    app.run()
