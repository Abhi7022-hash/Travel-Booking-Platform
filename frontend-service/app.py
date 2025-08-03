from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

BACKEND_URL = {
    'user': 'http://user-service:5001',
    'flight': 'http://flight-service:5002',
    'hotel': 'http://hotel-service:5003',
    'booking': 'http://booking-service:5004'
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    user_data = {
        'name': request.form['name'],
        'email': request.form['email']
    }
    requests.post(f"{BACKEND_URL['user']}/register", json=user_data)
    return redirect(url_for('home'))

@app.route('/flights')
def flights():
    flights = requests.get(f"{BACKEND_URL['flight']}/flights").json()
    return render_template('flights.html', flights=flights)

@app.route('/hotels')
def hotels():
    hotels = requests.get(f"{BACKEND_URL['hotel']}/hotels").json()
    return render_template('hotels.html', hotels=hotels)

@app.route('/book', methods=['POST'])
def book():
    booking_data = {
        'user_id': request.form['user_id'],
        'flight_id': request.form['flight_id'],
        'hotel_id': request.form['hotel_id']
    }
    requests.post(f"{BACKEND_URL['booking']}/book", json=booking_data)
    return redirect(url_for('home'))

@app.route('/bookings')
def bookings():
    bookings = requests.get(f"{BACKEND_URL['booking']}/bookings").json()
    return render_template('bookings.html', bookings=bookings)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
