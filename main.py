from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def main():
    return render_template("main.html")


@app.route("/vk")
def vk():
    return render_template("vk_redirect.html")


@app.route("/complaint/<int:user_id>")
def complaint(user_id):
    return render_template("complaint.html")


if __name__ == "__main__":
    app.run()
