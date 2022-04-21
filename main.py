####### IMPORTS #######
from flask import Flask, redirect, url_for, render_template, request, session, flash # import from Flask
from datetime import timedelta
import sqlalchemy


app = Flask(__name__)
app.secret_key = "Test" # Make key complicated at one point
app.permanent_session_lifetime = timedelta(days=1) # permanent session will be kept for this long





####### ACTIVE PAGES #######
@app.route("/") # "/" means default page. In this case, the homepage.
@app.route("/home") # 
def home():
    return render_template("home.html") #using render_template so that it renders the content ot the HTML and does no not affect URL

@app.route("/grade-calculator")
def page1():
    return render_template("grade-calculator.html")

@app.route("/aboutus")
def about_us():
    return render_template("about_us.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True # enable/disable permanent session
        user = request.form["name"]
        session["user"] = user # storing value of user in the dictionary.
        flash("Logged In Sucessfully.")
        return redirect(url_for("user"))
    else:
        return render_template("login.html")
        

@app.route("/logout")
def logout():
    if "user" in session:
        user = session["user"]
        flash(f"Successfully logged out. Bye, {user}")
    session.pop("user", None) # pop session
    return redirect(url_for("login"))

    

@app.route("/user")
def user():
    if "user" in session: # checking if "user" in dictionary has a value
        user = session["user"]
        return render_template("user.html", user=user)
    else:
        return redirect(url_for("login"))
        

# Any pages that don't exist goes to "error404.html"
# @app.route("/<name>")
# def user(name):
#     return render_template("error404.html")

@app.route("/ryan")
def ryan():
    return render_template("ryan_test.html")





####### INACTIVE PAGES - redirects to "home.html" #######
@app.route("/page2")
@app.route("/page3")
@app.route("/purpose")
def page():
    return redirect(url_for("home"))





# Run Program
if __name__ == "__main__":
    app.run(debug = True) # runs program. every time you save any file, the new version runs automatically in console.