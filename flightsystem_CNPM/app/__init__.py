from flask import Flask, render_template, request, redirect, url_for, jsonify

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
flightapp = Flask(__name__)

flightapp.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/Admin/Desktop/FlightManagement/flightsystem_CNPM/app/database/flightManagement.db'
flightapp.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db.init_app(flightapp)

from .models import Customer, Employee, FlightDetail, Promotion, Price, Ticket, Booking, Payment, Review, Schedule, Reservation, ReservationHistory, Invoice, Route, Aircraft, ReportRevenue

# Function to create the flight table

# Create the tables
def create_tables():
    db.create_all()

# Drop all tables
def drop_tables():
    db.drop_all()


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
# Create the tables
