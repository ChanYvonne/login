from flask import Flask, render_template, request
import random

app=Flask(__name__)

@app.route("/")
#@app.route("/login/")
def login():
    return render_template("form.html", title = "form")

@app.route("/authenticate/", methods = ['POST'])
def auth():
    print request.form
    print request.form['user']
    print request.form['pass']
    randnum = 2*random.random()
    if randnum < 1:
        return render_template("result.html", title = "Results", result = "SUCCESS")
    else:
        return render_template("result.html", title = "Results", result = "FAILURE")

if __name__== '__main__':
    app.debug = True
    app.run()
