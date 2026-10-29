from flask import Flask

app= Flask(__name__)

@app.route("/")
def home():
    return 'hello, flask app running in docker'

@app.route("/about")
def about():
    return 'this is a simple flask appliication'

@app.route("/contact")
def contact():
    return "Connect us at: abc"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
    