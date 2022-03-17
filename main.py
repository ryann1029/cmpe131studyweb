from flask import Flask, redirect, url_for, render_template # import from Flask
import webbrowser

app = Flask(__name__)

@app.route("/") # "/" means default page. In this case, the homepage.
@app.route("/home") # 
def home():
    #webbrowser.open('index-page.html') # This renders template but affects URL...
    return render_template("index-page.html") #using render_template so that it renders the content ot the HTML and does no not affect URL
    
    #return "<div style=\"color: red; font-size: 16pt;\">HOMEPAGE</div><br/>Homepage bruv" # using HTML to stylize text

'''@app.route("/<name>")
def user(name):
    return f"Hello {name}"'''

@app.route("/page1")
@app.route("/page2")
@app.route("/page3")
@app.route("/aboutus")
@app.route("/purpose")
def page():
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug = True) #runs program. every time you save any file, the new version runs automatically in console.