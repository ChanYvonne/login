from flask import Flask, render_template

app=Flask(__name__)


@app.route("/")
def login():
    return render_template("form.html", title = "form")

if __name__== '__main__':
    app.debug = True
    app.run()
