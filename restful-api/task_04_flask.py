#!/usr/bin/python3
from flask import Flask, jsonify, request

# Création de l'application Flask
app = Flask(__name__)

# Route racine : renvoie un message de bienvenue
@app.route("/")
def home():
    return "Welcome to the Flask API!"

# Route de test : renvoie un dictionnaire sous forme de JSON
@app.route("/data")
def get_data():
    sample_data = {
        "name": "John",
        "age": 30,
        "city": "New York"
    }
    return jsonify(sample_data)

# Route pour vérifier que l'API fonctionne
@app.route("/status")
def status():
    return "OK"

# Dictionnaire pour stocker les utilisateurs (base de données en mémoire)
users = {}

# Route dynamique pour récupérer les infos d'un utilisateur
@app.route("/users/<username>")
def get_user(username):
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404

# Route pour ajouter un utilisateur (POST uniquement)
@app.route("/add_user", methods=["POST"])
def add_user():
    data = request.get_json()

    # Vérifie qu'un nom d'utilisateur a bien été envoyé
    if "username" not in data:
        return jsonify({"error": "Username is required"}), 400

    # Ajoute l'utilisateur dans le dictionnaire
    username = data["username"]
    users[username] = data

    # Retourne une confirmation avec le code 201 (Created)
    return jsonify({
        "message": "User added",
        "user": data
    }), 201

# Démarrage du serveur sur le port 5050 avec le mode debug activé
if __name__ == "__main__":
    app.run(debug=True)
