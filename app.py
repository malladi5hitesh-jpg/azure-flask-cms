from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Title: "Hello World!"
Author: "Jane Doe"
Body: "My name is Jane Doe and this is my first article!""

if __name__ == "__main__":
    app.run()
