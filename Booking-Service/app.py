from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

bookings = []

@app.route('/book', methods=['POST'])
def book():
    data = request.get_json()
    booking_id = str(uuid.uuid4())
    booking = {
        'booking_id': booking_id,
        'user_id': data['user_id'],
        'flight_id': data['flight_id'],
        'hotel_id': data['hotel_id'],
        'status': 'confirmed'
    }
    bookings.append(booking)
    return jsonify({'message': 'Booking successful', 'booking_id': booking_id}), 201

@app.route('/bookings', methods=['GET'])
def get_bookings():
    return jsonify(bookings), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004)
