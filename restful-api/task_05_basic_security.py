#!/usr/bin/env python3
"""
Module task_05_basic_security
"""
from flask import Flask
from flask import jsonify
from flask import request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()
users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"}
}
app.config["JWT_SECRET_KEY"] = "ton_secret_ultra_secret"
jwt = JWTManager(app)


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "Fresh token required"}), 401


@auth.verify_password
def verify_password(username, password):
    """
    Verifying password for authentication
    """

    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        return user


@app.route("/basic-protected")
@auth.login_required
def authentication():
    """
    Route for authentication
    """

    return "Basic Auth: Access Granted"


@app.route("/login", methods=["POST"])
def login():
    """
    Route for login
    """

    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    user = users.get(username)
    if not user or not check_password_hash(user["password"], password):
        return jsonify({"error": "Invalid credentials"}), 401
    access_token = create_access_token(identity=username, additional_claims={"role": user.get("role", "user")})
    return jsonify(access_token=access_token)


@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    """
    JWT protected route
    """
    return "JWT Auth: Access Granted"


@app.route("/admin-only")
@jwt_required()
def admin_check():
    """
    Check if user is admin
    """

    claims = get_jwt()
    if claims.get("role") != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"


if __name__ == "__main__":
    app.run()
