from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("signup.html")

@app.route("/signup", methods=["POST"])
def signup():
    if request.form["password"] != request.form["re_password"]:
        return "Password and Re-enter Password do not match!"
    return f"Welcome {request.form['name']}! Signup Successful."

if __name__ == "__main__":
    app.run(debug=True)
