from flask import Flask, redirect, url_for, render_template, request, session, flash

app = Flask(__name__)
app.secret_key = "dev"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        session["username"] = username
        print(username)
        flash("Login successful!")
        return redirect(url_for("address"))
    else:
        if "username" in session:
            flash("You are already logged in.")
            return redirect(url_for("address"))
        return render_template("auth/login.html")
    
@app.route("/logout")
def logout():
    print("Clearing session:", session)
    session.clear()
    flash("You are logged out.", "info")
    return redirect(url_for("home"))

@app.route("/address-book", methods=["GET", "POST"])
def address():
    if request.method == "POST":
        session["name"] = request.form["name"]
        session["email"] = request.form["email"]
        session["phone"] = request.form["phone"]
        session["homeaddr"] = request.form["homeaddr"]
        print("Saved session data:", session)
        flash("Contact information saved!")
        return render_template("address-book.html")
    else:
        if "username" in session:
            name = session["username"]
            print("Current session:", session)
            return render_template("address-book.html")
        else:
            return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug = True)
