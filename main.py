from flask import Flask, redirect, url_for # import from Flask

app = Flask(__name__)

@app.route("/") # "/" means default page. In this case, the homepage.
def home():
    return "<h1>HOMEPAGE</h1>Homepage bruv"

if __name__ == "__main__":
    app.run() #runs program