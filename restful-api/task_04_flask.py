from flask import Flask, jsonify, request

app = Flask(__name__)

users = {
    "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}
}

@app.route('/')
def home():
    return "Welcome to the Flask API!"

@app.route('/data')
def get_data():
    if users:
        return jsonify(list(users.keys()))
    else:
        return jsonify([])  # Return empty list if no users exist

@app.route('/status')
def status():
    return "OK"

@app.route('/users/<username>')
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.json
    if not data or 'username' not in data or 'name' not in data:
        return jsonify({"error": "Invalid request. Username and name are required."}), 400
    
    username = data['username']
    if username in users:
        return jsonify({"error": "User already exists"}), 409
    
    # Validate age if provided
    age = data.get('age')
    if age is not None and not isinstance(age, int):
        return jsonify({"error": "Invalid age. Age must be an integer."}), 400
    
    users[username] = data
    return jsonify({"message": "User added", "user": data}), 201

if __name__ == "__main__":
    app.run(debug=True)
