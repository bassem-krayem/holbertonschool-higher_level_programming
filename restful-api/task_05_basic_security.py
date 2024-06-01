#!/usr/bin/python3

from flask import Flask, jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt_identity,
)

app = Flask(__name__)
app.config["SECRET_KEY"] = "your_secret_key_here"
auth = HTTPBasicAuth()
jwt = JWTManager(app)

# Dictionary to store user data
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
    """
    Verify user password.

    Args:
        username (str): The username of the user.
        password (str): The password of the user.

    Returns:
        dict: User data if the username and password are correct, None otherwise.
    """
    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        return user
    return None

@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    """
    Route protected by Basic Authentication.

    Returns:
        str: Access granted message.
    """
    return "Basic Auth: Access Granted"

@app.route("/login", methods=["POST"])
def login():
    """
    Login route to authenticate users and provide a JWT token.

    Expects:
        JSON object with "username" and "password" fields.

    Returns:
        Response: JSON response with JWT token if credentials are valid, error message otherwise.
    """
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        access_token = create_access_token(
            identity={"username": username, "role": user["role"]}
        )
        return jsonify(access_token=access_token)
    return jsonify({"error": "Invalid credentials"}), 401

@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    """
    Route protected by JWT Authentication.

    Returns:
        str: Access granted message.
    """
    return "JWT Auth: Access Granted"

@app.route("/admin-only")
@jwt_required()
def admin_only():
    """
    Route protected by JWT Authentication and restricted to admin users.

    Returns:
        Response: Admin access granted message if the user is an admin, error message otherwise.
    """
    current_user = get_jwt_identity()
    if current_user["role"] != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"

@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """
    Handle unauthorized error for JWT.

    Args:
        err (str): Error message.

    Returns:
        Response: JSON response with error message.
    """
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """
    Handle invalid token error for JWT.

    Args:
        err (str): Error message.

    Returns:
        Response: JSON response with error message.
    """
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(err):
    """
    Handle expired token error for JWT.

    Args:
        err (str): Error message.

    Returns:
        Response: JSON response with error message.
    """
    return jsonify({"error": "Token has expired"}), 401

@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    """
    Handle revoked token error for JWT.

    Args:
        err (str): Error message.

    Returns:
        Response: JSON response with error message.
    """
    return jsonify({"error": "Token has been revoked"}), 401

@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    """
    Handle needs fresh token error for JWT.

    Args:
        err (str): Error message.

    Returns:
        Response: JSON response with error message.
    """
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == "__main__":
    app.run()
