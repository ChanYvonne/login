from flask import Flask, render_template, request

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
    return "done"

if __name__== '__main__':
    app.debug = True
    app.run()
