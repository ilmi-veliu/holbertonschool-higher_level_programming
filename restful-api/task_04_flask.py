#!/usr/bin/python3
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the Flask API!"

@app.route("/data")
def get_data():
    sample_data = {
        "name": "John",
        "age": 30,
        "city": "New York"
    }
    return jsonify(sample_data)

@app.route("/status")
def status():
    return "OK"

users = {}

@app.route("/users/<username>")
def get_user(username):
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404

@app.route("/add_user", methods=["POST"])
def add_user():
    data = request.get_json()

    if "username" not in data:
        return jsonify({"error": "Username is required"}), 400

    username = data["username"]
    users[username] = data

    return jsonify({
        "message": "User added",
        "user": data
    }), 201

if __name__ == "__main__":
    app.run(port=5050)
