####### IMPORTS #######
from flask import Flask, redirect, url_for, render_template, request # import from Flask

app = Flask(__name__)





####### ACTIVE PAGES #######
@app.route("/") # "/" means default page. In this case, the homepage.
@app.route("/home") # 
def home():
    return render_template("home.html") #using render_template so that it renders the content ot the HTML and does no not affect URL

@app.route("/grade-calculator")
def page1():
    return render_template("grade-calculator.html")

@app.route("/calendar")
def page2():
    return render_template("calendar.html")

@app.route("/aboutus")
def about_us():
    return render_template("about_us.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["name"]
        return redirect(url_for("user", usr=user))
    else:
        return render_template("login.html")

@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"

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
    app.run(debug = True) # runs program. every time you save any file, the new version runs automatically in console.