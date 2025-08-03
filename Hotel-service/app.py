from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

hotels = [
    {"id": 1, "hotel": "AUSK Hotel", "city": "Bengaluru"},
    {"id": 2, "hotel": "The Fern", "city": "MYsore"}
]

@app.route("/")
def home():
    return render_template("index.html", hotels=hotels)

@app.route("/api/hotels", methods=["GET"])
def get_hotels():
    return jsonify(hotels)

@app.route("/api/hotels", methods=["POST"])
def add_hotel():
    new_hotel = request.get_json()
    hotels.append(new_hotel)
    return jsonify({"message": "Hotel added", "hotel": new_hotel}), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
