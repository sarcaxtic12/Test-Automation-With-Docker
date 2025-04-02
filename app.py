import os
from flask import Flask, jsonify, request

app = Flask(__name__)

# Define the path to the users file
USERS_FILE = "users.txt"

def generate_users_file():
    """
    Generates a text file with usernames 'user1' to 'user100'
    if the file doesn't already exist.
    """
    if not os.path.exists(USERS_FILE):
        with open(USERS_FILE, "w") as f:
            for i in range(1, 101):
                f.write(f"user{i}\n")

def load_users():
    """
    Loads the list of users from the users.txt file.
    Returns a list of usernames.
    """
    with open(USERS_FILE, "r") as f:
        users = [line.strip() for line in f.readlines()]
    return users

# Dummy in-memory data store for demonstration purposes
data_store = []

@app.route("/")
def home():
    """
    Home endpoint returns a simple welcome message.
    """
    return jsonify({"message": "Hello, world! This is your microservice."})

@app.route("/health")
def health():
    """
    Health endpoint returns the current status of the service.
    """
    return jsonify({"status": "OK"})

@app.route("/info")
def info():
    """
    Info endpoint returns basic information about the service.
    """
    return jsonify({
        "app": "Microservice",
        "version": "1.0",
        "description": "This endpoint provides basic info about the service."
    })

@app.route("/user/<username>")
def get_user(username):
    """
    User endpoint returns a user profile if the username exists in the user_list.
    If the user is not found, returns a 404 error.
    """
    if username in user_list:
        return jsonify({
            "username": username,
            "role": "guest",
            "status": "active"
        })
    else:
        return jsonify({"error": "User not found"}), 404

@app.route("/data", methods=["GET", "POST"])
def data():
    """
    Data endpoint supports GET and POST methods.
    GET: Returns the current data store.
    POST: Adds a new item (provided in JSON with an 'item' key) to the data store.
    """
    if request.method == "GET":
        return jsonify({"data": data_store})
    elif request.method == "POST":
        item = request.json.get("item")
        if item:
            data_store.append(item)
            return jsonify({"message": "Item added", "data": data_store}), 201
        else:
            return jsonify({"error": "No item provided"}), 400

if __name__ == "__main__":
    # Generate the file if needed and load the users list
    generate_users_file()
    user_list = load_users()
    
    app.run(host="0.0.0.0", port=5000)