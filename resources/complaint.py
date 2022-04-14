from data import db_session
from flask import jsonify
from data.complaint import Complaint
from flask_restful import Resource


class GetComplaints(Resource):
    def get(self, user_id: str) -> jsonify():
        db_sess = db_session.create_session()
        complaints = db_sess.query(Complaint).filter(Complaint.user_id == user_id)
        to_return = {"complaints": []}
        for complaint in complaints:
            to_return["complaints"].append({"name": complaint.name, "address": complaint.address})
        return jsonify(to_return)
