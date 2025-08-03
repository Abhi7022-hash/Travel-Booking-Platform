from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

flights = [
    {"id": 1, "flight": "IndiGo 6E123", "from": "Delhi", "to": "Mumbai"},
    {"id": 2, "flight": "Air India AI456", "from": "Mumbai", "to": "Bangalore"}
]

@app.route("/")
def home():
    return render_template("index.html", flights=flights)

@app.route("/api/flights", methods=["GET"])
def get_flights():
    return jsonify(flights)

@app.route("/api/flights", methods=["POST"])
def add_flight():
    new_flight = request.get_json()
    flights.append(new_flight)
    return jsonify({"message": "Flight added", "flight": new_flight}), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
