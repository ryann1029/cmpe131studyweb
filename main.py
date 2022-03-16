from flask import Flask # import from Flask

app = Flask(__name__)

@app.route("/") # "/" means default page. In this case, the homepage.
def home():
    return "Homepage bruv"

if __name__ == "__main__":
    app.run() #runs program