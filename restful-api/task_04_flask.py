from flask import Flask, jsonify, request

app = Flask(__name__)

# Route racine
@app.route("/")
def home():
    return "Welcome to the Flask API!"

# Route JSON de test
@app.route("/data")
def get_data():
    sample_data = {
        "name": "John",
        "age": 30,
        "city": "New York"
    }
    return jsonify(sample_data)

# Route de statut
@app.route("/status")
def status():
    return "OK"

# Base de données simulée : dictionnaire des utilisateurs
users = {
    "john": {
        "username": "john",
        "name": "John",
        "age": 30,
        "city": "New York"
    },
    "jane": {
        "username": "jane",
        "name": "Jane",
        "age": 28,
        "city": "Los Angeles"
    }
}

# Route dynamique pour récupérer un utilisateur
@app.route("/users/<username>")
def get_user(username):
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404

# Route POST pour ajouter un utilisateur
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
