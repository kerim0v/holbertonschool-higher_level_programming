#!/usr/bin/python3
"""A simple Flask API demonstrating routing, JSON responses, and POST handling."""
from flask import Flask, jsonify, request
 
app = Flask(__name__)
 
users = {}
 
 
@app.route("/")
def home():
    """Root endpoint — simple welcome message."""
    return "Welcome to thpe Flask API!"
 
 
@app.route("/data")
def get_usernames():
    """Return a JSON list of all usernames currently stored."""
    return jsonify(list(users.keys()))
 
 
@app.route("/status")
def status():
    """Simple health check endpoint."""
    return "OK"
 
 
@app.route("/users/<username>")
def get_user(username):
    """Return the full user object for a given username, or 404 if missing."""
    user = users.get(username)
    if user is None:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)
 
 
@app.route("/add_user", methods=["POST"])
def add_user():
    """Add a new user to the in-memory users dictionary."""
    data = request.get_json(silent=True)
 
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400
 
    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400
 
    if username in users:
        return jsonify({"error": "Username already exists"}), 409
 
    users[username] = data
    return jsonify({"message": "User added", "user": data}), 201
 
 
if __name__ == "__main__":
    app.run()
 