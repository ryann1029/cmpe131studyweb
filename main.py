from flask import Flask, redirect, url_for, render_template # import from Flask
import webbrowser

app = Flask(__name__)

@app.route("/") # "/" means default page. In this case, the homepage.
@app.route("/home") # 
def home():
    return render_template("home.html") #using render_template so that it renders the content ot the HTML and does no not affect URL

@app.route("/page1")
def page1():
    return render_template("page1.html")

@app.route("/page2")
@app.route("/page3")
@app.route("/aboutus")
@app.route("/purpose")
def page():
    return redirect(url_for("home"))

@app.route("/<name>")
def user(name):
    return render_template("error404.html")

if __name__ == "__main__":
    app.run(debug = True) #runs program. every time you save any file, the new version runs automatically in console.