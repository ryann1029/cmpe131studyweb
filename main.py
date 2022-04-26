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
    notes = db.Column(db.String(100000))


    def __init__(self, user, email, password, notes):
        self.user = user
        self.email = email
        self.password = password
        self.notes = notes





####### ACTIVE PAGES #######
# HOME PAGE
@app.route("/") # "/" means default page. In this case, the homepage.
@app.route("/home")
def home():
    current_user = None
    if "email" in session:
        email = session["email"]
        current_email = users.query.filter(users.email == email).one()
        current_user = current_email.user
    return render_template("home.html", user=current_user) #using render_template so that it renders the content ot the HTML and does no not affect URL

# GRADE CALCULATOR PAGE
@app.route("/grade-calculator")
def calculator():
    current_user = None
    if "email" in session:
        email = session["email"]
        current_email = users.query.filter(users.email == email).one()
        current_user = current_email.user
    return render_template("grade-calculator.html", user=current_user)

# CALENDAR PAGE
@app.route("/calendar")
def calender():
    current_user = None
    if "email" in session:
        email = session["email"]
        current_email = users.query.filter(users.email == email).one()
        current_user = current_email.user
    return render_template("calendar.html", user=current_user)

# ABOUT US PAGE
@app.route("/aboutus")
def about_us():
    current_user = None
    if "email" in session:
        email = session["email"]
        current_email = users.query.filter(users.email == email).one()
        current_user = current_email.user
    return render_template("about_us.html", current_user=user)






####### ACTIVE PAGES (USER DATABASE) #######
# SIGN UP PAGE
@app.route("/signup", methods=["POST", "GET"])
def signup():
    if "email" in session:
        return redirect(url_for("user"))

    if request.method == "POST":
        session.permanent = True         
        user = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]
        repassword = request.form["repassword"]

        if (user == "") or (email == "") or (password == "") or (repassword == ""):
            user1 = None
            email1 = None

            if user != "":
                user1 = user
            if email != "":
                email1 = email

            flash("Please fill all entries.")
            return render_template("signup.html", special_user=user1, special_email=email1)

        if password != repassword:
            flash("Password does not match. Please retry sign up again.")
            return render_template("signup.html", special_user=user1, special_email=email1)

        else:
            found_email = users.query.filter_by(email=email).first()

            if found_email:
                # session["email"] = email # storing value of user in the dictionary.
                flash("Email already exists. Log in instead.")
            else:
                # print("Email does not exists.")
                db.session.add(users(user, email, password, None))
                db.session.commit()

                flash("Signed up successful.")
            return redirect(url_for("login"))
    else:
        return render_template("signup.html")


# LOG IN PAGE
@app.route("/login", methods=["POST", "GET"])
def login():
    message = Markup("Username or email does not exist. Please check your entries or <a href=\"signup\">sign up</a>.")
    if "email" in session:
        flash(Markup("You are current logged in. <a href=\"logout\">Sign out</a> to log in on another account."))
        return redirect(url_for("user"))

    if request.method == "POST":
        session.permanent = True # enable/disable permanent session
        email = request.form["email"]
        password = request.form["password"]

        if (email == "") or (password == ""):
            email1 = None
            password1 = None

            if email != "":
                email1 = email
            if password != "":
                password1 = password
            flash("Please fill all entries.")
            return render_template("login.html", email=email1, password=password1)
        
        else:
            email_exist = users.query.filter_by(email=email).first()
            if email_exist:
                email_password_match = users.query.filter_by(email=email, password=password).first()
                if email_password_match:
                    session["email"] = email # storing value of email in the dictionary.
                    
                    flash("Logged in sucessfully!")
                    return redirect(url_for("user"))
                else:
                    flash("Password does not match.")
                    return render_template("login.html", email=email, password=password)
            else:
                flash(message)
                return render_template("login.html", email=email, password=password)
            # else:
            #     flash(message)
            #     return render_template("login.html", user=user, email=email, password=password)
    else:
        return render_template("login.html")


# CHANGE PASSWORD PAGE
@app.route("/change-password", methods=["POST", "GET"])
def changePassword():
    current_user = None
    if "email" in session:
        email = session["email"]
        current_email = users.query.filter(users.email == email).one()
        current_user = current_email.user

    if request.method == "POST":
        current_email = users.query.filter(users.email == email).one()
        current_password = current_email.password

        oldpass = request.form["oldpass"]
        newpassword = request.form["newpass"]
        renewpassword = request.form["renewpass"]

        if (oldpass == "") or (newpassword == "") or (renewpassword == ""):
            flash("Please fill all entries.")
            return render_template("change-password.html")
        
        elif current_password != oldpass:
            flash("Old Password does not match with account's current password. Enter correct current password.")
            return render_template("change-password.html")
        else:
            newpassword = request.form["newpass"]
            renewpassword = request.form["renewpass"]
            if newpassword != renewpassword:
                flash("New password and retyped new password do not match.")
                return render_template("change-password.html", user=current_user)
            else:
                current_email = users.query.filter(users.email == email).one()
                current_email.password = newpassword
                db.session.commit()
                flash("Password successfuly changed.")
                return redirect(url_for("logout"))
    else:
        return render_template("change-password.html", user=current_user)
        

# LOG OUT PAGE
@app.route("/logout")
def logout():
    if "email" in session:
        email = session["email"]

        current_email = users.query.filter(users.email == email).one()
        current_user = current_email.user

        flash(f"Successfully logged out. See you later, {current_user}!")
    else:
        return redirect(url_for("login"))
    session.pop("user", None) # pop session
    session.pop("email", None)
    return redirect(url_for("login"))


# VIEW PAGE - views the database (including password)
@app.route("/view", methods=["POST", "GET"])
def view():
    current_user = None
    if "email" in session:
        email = session["email"] # admin@sus.com
        current_email = users.query.filter(users.email == email).one()
        current_user = current_email.user

    if "email" in session:
        email = session["email"]
        if email == "admin@sus.com":
            return render_template("view.html", user=current_user, values=users.query.all())
        else:
            return redirect(url_for("login"))
    else:
        return redirect(url_for("login"))



    
# USER PAGE
@app.route("/user")
def user():
    if "email" in session: # checking if "email" in dictionary has a value
        email = session["email"]

        current_email = users.query.filter(users.email == email).one()
        current_user = current_email.user
        current_id = current_email._id
        current_notes = current_email.notes
    
        return render_template("user.html", user=current_user, email=email, id=current_id, notes=current_notes)
    else:
        return redirect(url_for("login"))

# EDITING NOTES PAGE
@app.route("/notes", methods=["POST", "GET"])
def editingNotes():
    current_user = None
    if "email" in session:
        email = session["email"]
        current_email = users.query.filter(users.email == email).one()
        current_user = current_email.user
        current_notes = current_email.notes

        if request.method == "POST":
            notes = request.form["notes"]
            current_email.notes = notes
            db.session.commit()
            current_notes = current_email.notes # grab updated notes after commit
            return render_template("notes.html", user=current_user, notes=current_notes)
        else:
            return render_template("notes.html", user=current_user, notes=current_notes)
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
        db.session.add(users("Ryan", "admin@sus.com", "adminpassiscuh!", None))
        db.session.commit()
    app.run(debug = True) # runs program. Every time you save any file, the new version will run.