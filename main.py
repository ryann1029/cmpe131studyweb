####### IMPORTS #######
import os
from flask import Flask, redirect, url_for, send_from_directory, render_template, request, session, flash, Markup
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
# app.add_url_rule('/favicon.ico', redirect_to=url_for('static', filename='favicon.ico'))
app.secret_key = "Test" # Make key complicated at one point
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Users.sqlite3'
app.config["SQLALCHEMY_TRACK_NOTIFICATIONS"] = False
app.permanent_session_lifetime = timedelta(days=1) # permanent session will be kept for this long

db = SQLAlchemy(app)

# class Person(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50))
#     addresses = db.relationship('Address', backref='person', lazy='dynamic')

# class Address(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(50))
#     person_id = db.Column(db.Integer, db.ForeignKey('person.id'))

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True) # unique identity
    user = db.Column(db.String(100)) # name containing max 100 characters
    email = db.Column(db.String(100)) # email containing max 100 characters
    password = db.Column(db.String(100)) # email containing max 100 characters
    notes = db.Column(db.String(100000))
    
    def __init__(self, user, email, password, notes):
        self.user = user
        self.email = email
        self.password = password
        self.notes = notes

class Flashcards(db.Model):
    id = db.Column(db.Integer, primary_key=True) # unique identity
    key = db.Column(db.String(100000))
    value = db.Column(db.String(100000))
    user_id = db.Column(db.Integer)

    def __init__(self, key, value, user_id):
        self.key = key
        self.value = value
        self.user_id = user_id




####### ACTIVE PAGES #######
# HOME PAGE
@app.route("/") # "/" means default page. In this case, the homepage.
@app.route("/home")
def home():
    current_user = None
    if "email" in session:
        email = session["email"]
        current_email = Users.query.filter(Users.email == email).one()
        current_user = current_email.user
    return render_template("home.html", user=current_user) #using render_template so that it renders the content ot the HTML and does no not affect URL

# GRADE CALCULATOR PAGE
@app.route("/grade-calculator")
def calculator():
    current_user = None
    if "email" in session:
        email = session["email"]
        current_email = Users.query.filter(Users.email == email).one()
        current_user = current_email.user
    return render_template("grade-calculator.html", user=current_user)

# CALENDAR PAGE
@app.route("/calendar")
def calender():
    current_user = None
    if "email" in session:
        email = session["email"]
        current_email = Users.query.filter(Users.email == email).one()
        current_user = current_email.user
    return render_template("calendar.html", user=current_user)

# ABOUT US PAGE
@app.route("/aboutus")
def about_us():
    current_user = None
    if "email" in session:
        email = session["email"]
        current_email = Users.query.filter(Users.email == email).one()
        current_user = current_email.user
    return render_template("about_us.html", user=current_user)






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

            flash(Markup("<img style=\"vertical-align: middle;\" src=\"static\pictures\Exclamation Point Icon.png\" height=\"18px\" width=\"18px\"/> <span style=\"color: red;\">Please fill all entries.</span>"))
            return render_template("signup.html", special_user=user1, special_email=email1)

        if password != repassword:
            flash(Markup("<img style=\"vertical-align: middle;\" src=\"static\pictures\Exclamation Point Icon.png\" height=\"18px\" width=\"18px\"/> <span style=\"color: red;\">Password does not match. Please retry sign up again.</span>"))
            return render_template("signup.html", special_user=user, special_email=email)

        else:
            found_email = Users.query.filter_by(email=email).first()

            if found_email:
                # session["email"] = email # storing value of user in the dictionary.
                flash(Markup("<img style=\"vertical-align: middle;\" src=\"static\pictures\Exclamation Point Icon.png\" height=\"18px\" width=\"18px\"/> <span style=\"color: red;\">Email already exists. Log in instead.</span>"))
            else:
                # print("Email does not exists.")
                db.session.add(Users(user, email, password, None))
                db.session.commit()

                flash(Markup("<img style=\"vertical-align: middle;\" src=\"static\pictures\Checkmark Icon.png\" height=\"18px\" width=\"18px\"/> <span style=\"color: lime;\">Signed up successful.</span>"))
            return redirect(url_for("login"))
    else:
        return render_template("signup.html")


# LOG IN PAGE
@app.route("/login", methods=["POST", "GET"])
def login():
    message = Markup("<img style=\"vertical-align: middle;\" src=\"static\pictures\Exclamation Point Icon.png\" height=\"18px\" width=\"18px\"/> <span style=\"color: red;\">Username or email does not exist. Please check your entries or <a href=\"signup\">sign up</a>.</span>")
    if "email" in session:
        flash(Markup("<img style=\"vertical-align: middle;\" src=\"static\pictures\Exclamation Point Icon.png\" height=\"18px\" width=\"18px\"/> <span style=\"color: red;\">You are current logged in. <a href=\"logout\">Sign out</a> to log in on another account.</span>"))
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
            flash(Markup("<img style=\"vertical-align: middle;\" src=\"static\pictures\Exclamation Point Icon.png\" height=\"18px\" width=\"18px\"/> <span style=\"color: red;\">Please fill all entries.</span>"))
            return render_template("login.html", email=email1, password=password1)
        
        else:
            email_exist = Users.query.filter_by(email=email).first()
            if email_exist:
                email_password_match = Users.query.filter_by(email=email, password=password).first()
                if email_password_match:
                    session["email"] = email # storing value of email in the dictionary.
                    
                    flash(Markup("<img style=\"vertical-align: middle;\" src=\"static\pictures\Checkmark Icon.png\" height=\"18px\" width=\"18px\"/> <span style=\"color: lime;\">Logged in sucessfully!</span>"))
                    return redirect(url_for("user"))
                else:
                    flash(Markup("<img style=\"vertical-align: middle;\" src=\"static\pictures\Exclamation Point Icon.png\" height=\"18px\" width=\"18px\"/> <span style=\"color: red;\">Password does not match.</span>"))
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
        current_email = Users.query.filter(Users.email == email).one()
        current_user = current_email.user

    if request.method == "POST":
        current_email = Users.query.filter(Users.email == email).one()
        current_password = current_email.password

        oldpass = request.form["oldpass"]
        newpassword = request.form["newpass"]
        renewpassword = request.form["renewpass"]

        if (oldpass == "") or (newpassword == "") or (renewpassword == ""):
            flash("<img style=\"vertical-align: middle;\" src=\"static\pictures\Exclamation Point Icon.png\" height=\"18px\" width=\"18px\"/> <span style=\"color: red;\">Please fill all entries.</span>")
            return render_template("change-password.html")
        
        elif current_password != oldpass:
            flash(Markup("<img style=\"vertical-align: middle;\" src=\"static\pictures\Exclamation Point Icon.png\" height=\"18px\" width=\"18px\"/> <span style=\"color: red;\">Old Password does not match with account's current password. Enter correct current password.</span>"))
            return render_template("change-password.html")
        else:
            newpassword = request.form["newpass"]
            renewpassword = request.form["renewpass"]
            if newpassword != renewpassword:
                flash(Markup("<img style=\"vertical-align: middle;\" src=\"static\pictures\Exclamation Point Icon.png\" height=\"18px\" width=\"18px\"/> <span style=\"color: red;\">New password and retyped new password do not match.</span>"))
                return render_template("change-password.html", user=current_user)
            else:
                current_email = Users.query.filter(Users.email == email).one()
                current_email.password = newpassword
                db.session.commit()
                flash(Markup("<img style=\"vertical-align: middle;\" src=\"static\pictures\Checkmark Icon.png\" height=\"18px\" width=\"18px\"/> <span style=\"color: lime;\">Password successfully changed.</span>"))
                return redirect(url_for("logout"))
    else:
        return render_template("change-password.html", user=current_user)
        

# LOG OUT PAGE
@app.route("/logout")
def logout():
    if "email" in session:
        email = session["email"]

        current_email = Users.query.filter(Users.email == email).one()
        current_user = current_email.user

        flash(Markup("<img style=\"vertical-align: middle;\" src=\"static\pictures\Checkmark Icon.png\" height=\"18px\" width=\"18px\"/> <span style=\"color: lime;\">Successfully logged out. See you later, ") + f"{current_user}!" + Markup("</span>"))
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
        email = session["email"] # sysop@sus.com
        current_email = Users.query.filter(Users.email == email).one()
        current_user = current_email.user

    if "email" in session:
        email = session["email"]
        if email == "sysop@sus.com":
            return render_template("view.html", user=current_user, values=Users.query.all())
        else:
            return redirect(url_for("login"))
    else:
        return redirect(url_for("login"))



    
# USER PAGE
@app.route("/user")
def user():
    if "email" in session: # checking if "email" in dictionary has a value
        email = session["email"]

        current_email = Users.query.filter(Users.email == email).one()
        current_user = current_email.user
        current_id = current_email.id
        current_notes = current_email.notes

        if current_notes == "":
            current_notes = "No Notes."
    
        return render_template("user.html", user=current_user, email=email, id=current_id, notes=current_notes)
    else:
        return redirect(url_for("login"))

# EDITING NOTES PAGE
@app.route("/notes", methods=["POST", "GET"])
def editingNotes():
    current_user = None
    if "email" in session:
        email = session["email"]
        current_email = Users.query.filter(Users.email == email).one()
        current_user = current_email.user
        current_notes = current_email.notes

        if request.method == "POST":
            notes = request.form["notes"]
            current_email.notes = notes
            db.session.commit()
            current_notes = current_email.notes # grab updated notes after commit
            flash(Markup("<img style=\"vertical-align: middle;\" src=\"static\pictures\Checkmark Icon.png\" height=\"18px\" width=\"18px\"/> <span style=\"color: lime;\">Notes saved.</span>"))
            return redirect(url_for("user"))
        else:
            return render_template("notes.html", user=current_user, notes=current_notes)
    else:
        return redirect(url_for("login"))
        
@app.route("/flashcards", methods=["POST", "GET"])
def flashcards():
    current_user = None
    if "email" in session:
        email = session["email"]
        current_email = Users.query.filter(Users.email == email).one()
        current_user = current_email.user
        current_id = current_email.id
        # print(Users.query.filter(Users.id == current_id).all())

        if request.method == "POST":
            flash_id_request = request.form["delete-flashcard"]
            find_id = Flashcards.query.filter(Flashcards.id == flash_id_request).first()

            if find_id:
                find_id = Flashcards.query.filter(Flashcards.id == flash_id_request).one()
                flashcard_user_id = find_id.user_id

                if flashcard_user_id == current_id:
                    db.session.delete(find_id)
                    db.session.commit()
                    flash(Markup("<img style=\"vertical-align: middle;\" src=\"static\pictures\Checkmark Icon.png\" height=\"18px\" width=\"18px\"/> <span style=\"color: lime;\">Flashcard #") + f"{find_id.id}" + Markup(" deleted successfully.</span>"))
                    return redirect(url_for("flashcards"))
                else:
                    flash(Markup("<img style=\"vertical-align: middle;\" src=\"static\pictures\Exclamation Point Icon.png\" height=\"18px\" width=\"18px\"/> <span style=\"color: red;\">Flashcard #") + f"{flash_id_request}" + Markup(" does not exist.</span>"))
                    return redirect(url_for("flashcards"))
                # return render_template("delete-flashcard.html", user=current_user, id=flash_id)
            else:
                flash(Markup("<img style=\"vertical-align: middle;\" src=\"static\pictures\Exclamation Point Icon.png\" height=\"18px\" width=\"18px\"/> <span style=\"color: red;\">Flashcard #") + f"{flash_id_request}" + Markup(" does not exist.</span>"))
                return redirect(url_for("flashcards"))
        else:
            return render_template("flashcards.html", user=current_user, id=current_id, values=Flashcards.query.all())
    
    flash(Markup("<img style=\"vertical-align: middle;\" src=\"static\pictures\Exclamation Point Icon.png\" height=\"18px\" width=\"18px\"/> <span style=\"color: red;\">You need to be logged in to use the Flashcard feature.</span>"))
    return redirect(url_for("login"))

@app.route("/add-flashcard", methods=["POST", "GET"])
def addFlashcard():
    current_user = None
    if "email" in session:
        email = session["email"]
        current_email = Users.query.filter(Users.email == email).one()
        current_user = current_email.user
        current_id = current_email.id

        if request.method == "POST":
            key = request.form["addkey"]
            value = request.form["addvalue"]

            if key == "" and value == "":
                key1 = None
                value1 = None

                if key == "":
                    key1 = key
                if value == "":
                    value1 = value

                flash(Markup("<img style=\"vertical-align: middle;\" src=\"static\pictures\Exclamation Point Icon.png\" height=\"18px\" width=\"18px\"/> <span style=\"color: red;\">Please fill all entries.</span>"))
                return render_template("add-flashcard.html", user=current_user, key=key1, value=value1)
            else:
                db.session.add(Flashcards(key, value, current_id))
                db.session.commit()
                flash(Markup("<img style=\"vertical-align: middle;\" src=\"static\pictures\Checkmark Icon.png\" height=\"18px\" width=\"18px\"/> <span style=\"color: lime;\">Flashcard added successfully.</span>"))
                return redirect(url_for("flashcards"))
        else:
            return render_template("add-flashcard.html")
    else:
        return redirect(url_for("login"))


# Any pages that don't exist goes to "error404.html"
# @app.route("/<name>")
# def user(name):
#     return render_template("error404.html")

@app.route("/ryan")
def ryan():
    current_user = None
    if "email" in session:
        email = session["email"]
        current_email = Users.query.filter(Users.email == email).one()
        current_id = current_email._id
        current_user = current_email.user
        # flashcard_all = Flashcards.query.filter(Flashcards.user_id == current_id).all()
        # print(Flashcards.user_id)

    return render_template("ryan_test.html", user=current_user)





####### INACTIVE PAGES - redirects to "home.html" #######
@app.route("/page3")
@app.route("/purpose")
def page():
    return redirect(url_for("home"))





# Run Program
if __name__ == "__main__":
    db.create_all() # creates database - must be before app.run()
    found_email = Users.query.filter_by(email="sysop@sus.com").first()
    if found_email:
        pass
    else:
        identification = Users("Sysop", "sysop@sus.com", "sysopalv", None)
        db.session.add(identification)
        db.session.commit()
    

    app.run(debug = True) # runs program. Every time you save any file, the new version will run.