from flask import Flask, redirect, url_for # import from Flask

app = Flask(__name__)

@app.route("/") # "/" means default page. In this case, the homepage.
def home():
    import webbrowser
    webbrowser.open('index-page.html') 
    
    #return "<div style=\"color: red; font-size: 16pt;\">HOMEPAGE</div><br/>Homepage bruv" # using HTML to stylize text

if __name__ == "__main__":
    app.run() #runs program