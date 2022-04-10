import os
from data import db_session
from flask_restful import Api
from data.complaint import Complaint
from werkzeug.utils import secure_filename
from resources.complaint import GetComplaints
from flask import Flask, render_template, request, redirect

app = Flask(__name__)
api = Api(app)
app.config["SECRET_KEY"] = "12344321"
app.config["UPLOAD_FOLDER"] = os.path.join(os.getcwd(), "images\\")
api.add_resource(GetComplaints, "/api/v2/get-complaints/<string:user_id>")
ALLOWED_EXTENSIONS = tuple(["jpg", "jpeg", "png", "img"])


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1] in ALLOWED_EXTENSIONS


@app.route("/")
def main_page():
    return render_template("main.html")


@app.route("/vk")
def vk_redirect():
    return render_template("vk_redirect.html")


@app.route("/complaint", methods=["GET", "POST"])
def complaint():
    if request.method == "POST":
        db_sess = db_session.create_session()
        complaint = Complaint()
        file = request.files["file"]
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
            user_id = request.form["user-id"]
            address = request.form["address"]
            name = request.form["name"]
            description = request.form["description"]
            complaint.user_id = user_id
            complaint.address = address
            complaint.name = name
            complaint.description = description
            complaint.filename = file.filename
            db_sess.add(complaint)
            db_sess.commit()
            return redirect("/")
        return render_template("complaint.html", title="Жалоба")
    return render_template("complaint.html", title="Жалоба")


def main():
    db_session.global_init("db/ecology.db")
    app.run(debug=True)


if __name__ == "__main__":
    main()
