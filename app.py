from aiohttp import request
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/user/<username>")
def show_user(username):
    return f"User: {username}"


@app.route("/user/<int:user_id>/edit", methods=["GET", "POST"])
def edit_user(user_id):
    if request.method == "POST":
        # update user in database...
        pass
    return render_template("edit_user.html")


if __name__ == "__main__":
    app.run(debug=True)
