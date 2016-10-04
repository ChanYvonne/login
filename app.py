from flask import Flask, render_template, request
from utils import makeacc
import random, cgitb, cgi
cgitb.enable()

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html", title = "Home")

@app.route("/login/")
def login():
    return render_template("form.html", title = "Login", result = "")

@app.route("/register/")
def register():
    return render_template("register.html", title = "Register")

@app.route("/authenticate/", methods = ['POST'])
def auth():
    print request.form['user']
    print request.form['pass']
    if request.form['user'] in makeacc.users():
        return render_template("result.html", result = "FAILURE! Please try again.", message = "Return and try again!")
    else:
        makeacc.writetofile()
        return render_template("form.html", title = "login", result = "SUCCESS! Your account was created! Log in now.")

@app.route("/loggedin/", methods = ['POST'])
def loggedin():
    if request.form['user'] in makeacc.users():
        return render_template("result.html", result = "SUCCESS! You have logged in!", message = "Return to make another account!")
    else:
        return render_template("result.html", result = "FAILURE! Bad username", message = "Return to try again.")
        
    
if __name__== '__main__':
    app.debug = True
    app.run()
