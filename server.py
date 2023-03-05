from flask import Flask, session, redirect, render_template, request

app = Flask (__name__)
app.secret_key = "passweird"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/result", methods=["POST"])
def result():
    session["name"] = request.form["name"]
    session["location"] = request.form["Location"]
    session["fav_language"] = request.form["fav_language"]
    session["comment"] = request.form["comment"]
    return redirect('/display_results')

@app.route("/display_results")
def display():
    return render_template("results.html")

if __name__=="__main__":
    app.run(port=8000,debug=True)