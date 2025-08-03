from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Dummy user data
users = [
    {"id": 1, "name": "Abhi", "email": "abhi@example.com"},
    {"id": 2, "name": "Meera", "email": "meera@example.com"}
]

@app.route("/")
def home():
    return render_template("index.html", users=users)

@app.route("/api/users", methods=["GET"])
def get_users():
    return jsonify(users)

@app.route("/api/users", methods=["POST"])
def add_user():
    new_user = request.get_json()
    users.append(new_user)
    return jsonify({"message": "User added", "user": new_user}), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
