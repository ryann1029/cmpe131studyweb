####### IMPORTS #######
import os
from flask import Flask, redirect, url_for, send_from_directory, render_template, request, session, flash, Markup
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
# app.add_url_rule('/favicon.ico', redirect_to=url_for('static', filename='favicon.ico'))
app.secret_key = "Test" # Make key complicated at one point
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config["SQLALCHEMY_TRACK_NOTIFICATIONS"] = False
app.permanent_session_lifetime = timedelta(days=1) # permanent session will be kept for this long

db = SQLAlchemy(app)

class users(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True) # unique identity
    user = db.Column(db.String(100)) # name containing max 100 characters
    email = db.Column(db.String(100)) # email containing max 100 characters
    password = db.Column(db.String(100)) # email containing max 100 characters

    def __init__(self, user, email, password):
        self.user = user
        self.email = email
        self.password = password





####### ACTIVE PAGES #######
# HOME PAGE
@app.route("/") # "/" means default page. In this case, the homepage.
@app.route("/home")
def home():
    return render_template("home.html") #using render_template so that it renders the content ot the HTML and does no not affect URL

# GRADE CALCULATOR PAGE
@app.route("/grade-calculator")
def page1():
    return render_template("grade-calculator.html")

# CALENDAR PAGE
@app.route("/calendar")
def page2():
    return render_template("calendar.html")

# ABOUT US PAGE
@app.route("/aboutus")
def about_us():
    return render_template("about_us.html")






####### ACTIVE PAGES (USER DATABASE) #######
# SIGN UP PAGE
@app.route("/signup", methods=["POST", "GET"])
def signup():
    # found_email = None
    if request.method == "POST":
        session.permanent = True         
        user = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]
        repassword = request.form["repassword"]

        if repassword != repassword:
            flash("Password does not match. Please retry sign up again.")
        else:

            found_email = users.query.filter_by(email=email).first()

            if found_email:
                # session["email"] = email # storing value of user in the dictionary.
                flash("Email already exists. Log in instead.")
            else:
                # print("Email does not exists.")
                db.session.add(users(user, email, password))
                db.session.commit()

                flash("Signed up successful.")
            return redirect(url_for("login"))
    else:
        return render_template("signup.html")


# LOG IN PAGE
@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True # enable/disable permanent session
        user = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]

        email_exist = users.query.filter_by(email=email).first()
        if email_exist:
            email_password_match = users.query.filter_by(email=email, password=password).first()

            if email_password_match:
                session["user"] = user # storing value of user in the dictionary.
                session["email"] = email
                flash("Logged In Sucessfully.")
                return redirect(url_for("user"))
            else:
                flash("Password does not match.")
                return redirect(url_for("login"))
        else:
            message = Markup("Email does not exist. Please <a href=\"signup\">sign up</a>.")
            flash(message)
            return redirect(url_for("login"))
    else:
        return render_template("login.html")
        

# LOG OUT PAGE
@app.route("/logout")
def logout():
    if "user" in session:
        user = session["user"]
        flash(f"Successfully logged out. See you later, {user}!")
    session.pop("user", None) # pop session
    session.pop("email", None)
    return redirect(url_for("login"))


# VIEW PAGE - views the database (including password)
@app.route("/view", methods=["POST", "GET"])
def view():
    if "user" in session:
        user = session["user"]
        if user == "admin":
            return render_template("view.html", values=users.query.all())
        else:
            return redirect(url_for("login"))
    else:
        return redirect(url_for("login"))
    

@app.route("/user")
def user():
    email = None
    if "user" in session: # checking if "user" in dictionary has a value
        user = session["user"]

        if request.method == "POST":
            email = request.form["email"]
            session["email"] = email
        else:
            if "email" in session:
                email = session["email"]
        
        return render_template("user.html", user=user, email=email)
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
@app.route("/page3")
@app.route("/purpose")
def page():
    return redirect(url_for("home"))





# Run Program
if __name__ == "__main__":
    db.create_all() # creates database - must be before app.run()
    found_email = users.query.filter_by(email="ryannguyen1029@gmail.com").first()
    if found_email:
        pass
    else:
        db.session.add(users("admin", "ryannguyen1029@gmail.com", "adminpassiscuh!"))
        db.session.commit()
    app.run(debug = True) # runs program. Every time you save any file, the new version will run.