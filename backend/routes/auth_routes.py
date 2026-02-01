from flask import Blueprint, request, jsonify
from models.user_model import User

auth_bp = Blueprint("auth", __name__)

# Temporary in-memory storage
users = []

@auth_bp.route("/signup", methods=["POST"])
def signup():
    data = request.json
    user = User(
        name=data.get("name"),
        email=data.get("email"),
        password=data.get("password")
    )
    users.append(user)
    return jsonify(user.to_dict()), 201


@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    for user in users:
        if user.email == data.get("email") and user.password == data.get("password"):
            return jsonify({"message": "Login successful"}), 200
    return jsonify({"error": "Invalid credentials"}), 401
