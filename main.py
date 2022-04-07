from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def main():
    return "1"


@app.route("/complaint/<int:user_id>")
def complaint(user_id):
    return render_template("complaint.html")


if __name__ == "__main__":
    app.run()
