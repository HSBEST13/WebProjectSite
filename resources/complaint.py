from data import db_session
from flask import jsonify
from data.complaint import Complaint
from flask_restful import Resource
from werkzeug.security import generate_password_hash


class GetComplaints(Resource):
    api_key = "AUBWEWE_EWNETWEWE_UBEMUBEM_OSAS_228"

    def get(self, user_id: str, hashed_api_key: str):
        if generate_password_hash(self.api_key) != hashed_api_key:
            return jsonify({"error": "wrong-api-key"})
        db_sess = db_session.create_session()
        complaints = db_sess.query(Complaint).filter(Complaint.user_id == user_id)
        to_return = {"complaints": []}
        for complaint in complaints:
            to_return["complaints"].append({"name": complaint.name, "address": complaint.address})
        return jsonify(to_return)
