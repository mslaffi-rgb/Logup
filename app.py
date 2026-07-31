from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("signup.html")


@app.route("/signup", methods=["POST"])
def signup():
    name = request.form["name"]
    password = request.form["password"]
    confirm_password = request.form["confirm_password"]

    if password != confirm_password:
        return "Password and Re-enter Password do not match!"

    return f"Welcome {name}! Signup Successful."


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        debug=False
    )
