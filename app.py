from flask import Flask, render_template, request, url_for, session, redirect
from utils import makeacc
import random, os


app=Flask(__name__)
app.secret_key='\xcf/\xc9\xdc\x1a\xc3\xe4\xc23\\v(\xad\x1d\xa7i4\x10J\x9b)\xbe\x82\\b\x12|\xf3\xfa\xfc\xdc'

@app.route("/")
def home():
    if 'user' not in session:
        return redirect(url_for('login'))
    else:
        return render_template("result.html",title = "Home", message = "Welcome back " + session['user'] + "!")

@app.route("/logout/")
def logout():
    session.pop('user')
    return redirect(url_for('login'))

@app.route("/login/")                              
def login():
    return render_template("form.html", result = "")


@app.route("/authenticate/", methods = ['POST'])
def auth():
    #print request.form
    #print request.form['user']
    #print request.form['pass']
    if 'login' in request.form:
        if request.form['user'] in makeacc.users():
        
        #print makeacc.encrypt(request.form['pass'])
        #print makeacc.encrypt(request.form['pass']) == makeacc.updatedict(request.form['user'])
        #print makeacc.updatedict(request.form['user'])
            if makeacc.encrypt(request.form['pass']).strip() == makeacc.updatedict(request.form['user']).strip():
                session['user'] = request.form['user']
                return render_template("result.html", title = "Home", message = "Welcome " + request.form['user'] + "!", link = "Logout")
            else:
                return render_template("form.html", result = "FAILURE! Bad password")
        else:
            return render_template("form.html", result = "FAILURE! Bad username")
    else:
        if request.form['user'] in makeacc.users():
            return render_template("form.html", result = "FAILURE! Username already exists")
        else:
            makeacc.writetofile(request.form['user'],request.form['pass'])
            return render_template("form.html", result = "SUCCESS! Your account was created! Log in now.")


if __name__== '__main__':
    app.debug = True
    app.run()
