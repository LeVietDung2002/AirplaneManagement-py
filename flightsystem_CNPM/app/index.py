from flask import Flask, render_template, request, redirect, url_for, jsonify
import sqlite3
from models import db, FlightDetail  # Import your models

flightapp = Flask(__name__)

flightapp.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/Admin/Desktop/CNPM/flightsystem_CNPM/app/database/flight_reservation.db'
flightapp.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db.init_app(flightapp)

# Duong dan den trang chu
@flightapp.route("/")
def home():
    return render_template("home.html")

# Duong dan den trang dang nhap
@flightapp.route("/login")
def login():
    return render_template("login.html")

# Duong dan den trang dat ve
@flightapp.route("/booktickets")
def booktickets():
    return render_template("booktickets.html")

# Duong dan den trang ban ve
@flightapp.route("/sellticket", methods=["GET", "POST"])
def sellticket():
    if request.method == "POST":
        # Process the form data here
        # For example, you can access form values using request.form['fieldname']
        # Implement your logic for selling tickets

        # Redirect to a success page or home page after form submission
        return redirect(url_for('home'))

    # Render the sellticket.html template
    return render_template("sellticket.html")

@flightapp.route("/flightManagement")
def flightManagement():
    # Fetch data from the database
    flights = FlightDetail.query.all()

    # Pass the data to the template
    return render_template("flightManagement.html", flights=flights)

# Function to create the flight table
def create_flight_table():
    # This function is not needed if you are using Flask-SQLAlchemy
    pass

# Function to add a flight to the database
def add_flight(flight_code, departure, destination, departure_date):
    new_flight = FlightDetail(
        flight_code=flight_code,
        departure=departure,
        destination=destination,
        departure_date=departure_date
    )
    db.session.add(new_flight)
    db.session.commit()

# Function to delete a flight from the database
def delete_flight(flight_code):
    flight = FlightDetail.query.filter_by(flight_code=flight_code).first()
    if flight:
        db.session.delete(flight)
        db.session.commit()

# Create the flight table when the application starts
# This is not needed with Flask-SQLAlchemy

@flightapp.route('/add_flight', methods=['POST'])
def add_flight_route():
    data = request.form
    flight_code = data['flight_code']
    departure = data['departure']
    destination = data['destination']
    departure_date = data['departure_date']

    add_flight(flight_code, departure, destination, departure_date)

    return jsonify({'message': 'Flight added successfully'})

@flightapp.route('/delete_flight', methods=['POST'])
def delete_flight_route():
    data = request.form
    flight_code = data['flight_code']

    delete_flight(flight_code)

    return jsonify({'message': 'Flight deleted successfully'})

@flightapp.route('/get_flights', methods=['GET'])
def get_flights():
    flights = FlightDetail.query.all()
    flight_data = [{'flightID': flight.flightID, 'departureAirport': flight.departureAirport,
                    'arrivalAirport': flight.arrivalAirport, 'departureTime': flight.departureTime,
                    'arrivalTime': flight.arrivalTime, 'availableSeats': flight.availableSeats,
                    'price': flight.price} for flight in flights]
    return jsonify({'flights': flight_data})

if __name__ == '__main__':
    flightapp.run(debug=True)
