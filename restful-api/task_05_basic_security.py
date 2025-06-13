#!/usr/bin/python3
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager, create_access_token,
    jwt_required, get_jwt_identity
)
from werkzeug.security import generate_password_hash, check_password_hash

# Initialize the Flask application and extensions
app = Flask(__name__)
auth = HTTPBasicAuth()


# JWT configuration
app.config["JWT_SECRET_KEY"] = "super-secret"
jwt = JWTManager(app)


# Custom error handlers for JWT
@jwt.unauthorized_loader
def handle_unauthorized_error(error_string):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(error_string):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Fresh token required"}), 401

header = {
   "alg": "HS256",
   "typ": "JWT"
}

payload = {
   "sub": "1234567890",
   "name": "John Doe",
   "isAdmin": False
}

# In-memory user data store with hashed passwords and roles
users = {
    "John": {
        "password": generate_password_hash("password", method="pbkdf2:sha256"),
        "role": "user",
    },
    "Suzan": {
        "password": generate_password_hash("password", method="pbkdf2:sha256"),
        "role": "admin",
    },
    "Peter": {
        "password": generate_password_hash("password", method="pbkdf2:sha256"),
        "role": "admin",
    },
    "Lydia": {
        "password": generate_password_hash("password", method="pbkdf2:sha256"),
        "role": "user",
    },
}

# Verify username and password for HTTP Basic Auth


@auth.verify_password
def verify_password(username, password):
    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        return username
    return None

# Basic Auth protected route


@app.route("/basic-protected", methods=["GET"])
@auth.login_required
def basic_protected():
    return jsonify({"message": "Basic Auth: Access Granted"})


# Login endpoint to issue JWT token

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    if not data or "username" not in data or "password" not in data:
        return jsonify({"error": "Missing username or password"}), 400

    username = data.get("username")
    password = data.get("password")
    user = users.get(username)

    if not user or not check_password_hash(user["password"], password):
        return jsonify({"error": "Bad username or password"}), 401

    # Create JWT token with user info
    access_token = create_access_token(
        identity={
            "username": username,
            "role": user["role"],
        }
    )

    return jsonify(access_token=access_token), 200


# JWT-protected route
@app.route("/jwt-protected")
@jwt_required()
def protected():
    identity = get_jwt_identity()
    return jsonify({
        "message": "JWT Auth: Access Granted",
        "user": identity
    })


# Admin-only route protected by role
@app.route("/admin-only", methods=["GET"])
@jwt_required()
def admin_only():
    identity = get_jwt_identity()
    if identity["role"] != "admin":
        return jsonify({"error": "Access forbidden: Admins only"}), 403
    return jsonify({"message": "Admin Access: Granted"}), 200

# Run the Flask app

if __name__ == '__main__':
    app.run()
