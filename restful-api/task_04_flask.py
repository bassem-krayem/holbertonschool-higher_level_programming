#!/usr/bin/python3
from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}


@app.route("/")
def home():
    """
    Home route to welcome users to the Flask API.

    Returns:
        str: Welcome message.
    """
    return "Welcome to the Flask API!"


@app.route("/data")
def get_data():
    """
    Get the list of all usernames.

    Returns:
        Response: JSON response containing the list of usernames.
    """
    return jsonify(list(users.keys()))


@app.route("/status")
def get_status():
    """
    Status route to check if the API is running.

    Returns:
        str: Status message.
    """
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    """
    Get the details of a specific user.

    Args:
        username (str): The username of the user to retrieve.

    Returns:
        Response: JSON response containing user data or an error message
        if the user is not found.
    """
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """
    Add a new user to the dictionary.

    Expects:
        JSON object with the user data, must include a "username" field.

    Returns:
        Response: JSON response with a success message and the
        added user data, or an error message if the username is missing.
    """
    user_data = request.get_json()
    username = user_data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400
    users[username] = user_data
    return jsonify({"message": "User added", "user": user_data}), 201


if __name__ == "__main__":
    app.run()
