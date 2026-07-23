#!/usr/bin/python3
"""A Flask API demonstrating Basic Auth, JWT auth, and role-based access control."""
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import ( # type: ignore
    JWTManager,
    create_access_token,
    get_jwt_identity,
    jwt_required,
)
from werkzeug.security import check_password_hash, generate_password_hash
 
app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "super-secret-key-change-this-in-production"
jwt = JWTManager(app)
auth = HTTPBasicAuth()
 
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user",
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin",
    },
}
 
 
@auth.verify_password
def verify_password(username, password):
    """Check a username/password pair against the stored, hashed passwords."""
    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        return username
    return None
 
 
@auth.error_handler
def basic_auth_error(status):
    """Force every Basic Auth failure to return 401, regardless of status."""
    return jsonify({"error": "Unauthorized"}), 401
 
 
@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    """Route protected by Basic Authentication."""
    return "Basic Auth: Access Granted"
 
 
@app.route("/login", methods=["POST"])
def login():
    """Authenticate a user and issue a JWT access token."""
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "Invalid JSON"}), 400
 
    username = data.get("username")
    password = data.get("password")
    user = users.get(username)
 
    if not user or not check_password_hash(user["password"], password):
        return jsonify({"error": "Invalid credentials"}), 401
 
    access_token = create_access_token(
        identity=username, additional_claims={"role": user["role"]}
    )
    return jsonify({"access_token": access_token})
 
 
@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    """Route protected by a valid JWT — any authenticated user."""
    return "JWT Auth: Access Granted"
 
 
@app.route("/admin-only")
@jwt_required()
def admin_only():
    """Route protected by a valid JWT, restricted to the admin role."""
    username = get_jwt_identity()
    user = users.get(username)
    if not user or user["role"] != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"
 
 
# --- JWT error handlers: force every auth failure to 401, per task spec ---
 
@jwt.unauthorized_loader
def missing_token_callback(reason):
    """Triggered when no JWT is present at all."""
    return jsonify({"error": "Unauthorized"}), 401
 
 
@jwt.invalid_token_loader
def invalid_token_callback(reason):
    """Triggered when the JWT is malformed or fails validation."""
    return jsonify({"error": "Unauthorized"}), 401
 
 
@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_payload):
    """Triggered when the JWT has expired."""
    return jsonify({"error": "Unauthorized"}), 401
 
 
if __name__ == "__main__":
    app.run()
 