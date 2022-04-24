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
    user = None
    if "user" in session:
        user = session["user"]
    return render_template("home.html", user=user) #using render_template so that it renders the content ot the HTML and does no not affect URL

# GRADE CALCULATOR PAGE
@app.route("/grade-calculator")
def calculator():
    user = None
    if "user" in session:
        user = session["user"]
    return render_template("grade-calculator.html", user=user)

# CALENDAR PAGE
@app.route("/calendar")
def page2():
    user = None
    if "user" in session:
        user = session["user"]
    return render_template("calendar.html", user=user)

# ABOUT US PAGE
@app.route("/aboutus")
def about_us():
    user = None
    if "user" in session:
        user = session["user"]
    return render_template("about_us.html", user=user)






####### ACTIVE PAGES (USER DATABASE) #######
# SIGN UP PAGE
@app.route("/signup", methods=["POST", "GET"])
def signup():
    if "user" in session:
        return redirect(url_for("user"))

    if request.method == "POST":
        session.permanent = True         
        user = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]
        repassword = request.form["repassword"]

        if (user == "") or (email == "") or (password == "") or (repassword == ""):
            flash("Please fill all entries.")
            return render_template("signup.html")

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
    message = Markup("Username or email does not exist. Please check your entries or <a href=\"signup\">sign up</a>.")
    if "user" in session:
        flash(Markup("You are current logged in. <a href=\"logout\">Sign out</a> to log in on another account."))
        return redirect(url_for("user"))

    if request.method == "POST":
        session.permanent = True # enable/disable permanent session
        user = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]

        if (user == "") or (email == "") or (password == ""):
            user1 = None
            email1 = None
            password1 = None
            if user != "":
                user1 = user
            if email != "":
                email1 = email
            if password != "":
                password1 = password
            flash("Please fill all entries.")
            return render_template("login.html", user=user1, email=email1, password=password1)
        
        else:
            username_exist = users.query.filter_by(user=user).first()
            if username_exist:
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
                        return render_template("login.html", user=user, email=email, password=password)
                else:
                    flash(message)
                    return render_template("login.html", user=user, email=email, password=password)
            else:
                flash(message)
                return render_template("login.html", user=user, email=email, password=password)
    else:
        return render_template("login.html")
        

# LOG OUT PAGE
@app.route("/logout")
def logout():
    if "user" in session:
        user = session["user"]
        flash(f"Successfully logged out. See you later, {user}!")
    else:
        return redirect(url_for("login"))
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
    
# USER PAGE
@app.route("/user")
def user():
    if "email" in session: # checking if "user" in dictionary has a value
        user = session["user"]
        email = session["email"]
        
        # found_email = users.query.filter_by(email=email).first()
        # fetch_user = users.query(users).one(found_email.user)
        # session["user"] = fetch_user.user
        # user = session["user"]
    
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
    found_email = users.query.filter_by(email="admin@sus.com").first()
    if found_email:
        pass
    else:
        db.session.add(users("Ryan", "admin@sus.com", "adminpassiscuh!"))
        db.session.commit()
    app.run(debug = True) # runs program. Every time you save any file, the new version will run.