from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_login import LoginManager
import os

flightapp = Flask(__name__)

# Configuration for SQLAlchemy
flightapp.config['SECRET_KEY'] = '123456'
flightapp.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/Admin/Desktop/FlightManagement/flightsystem_CNPM/app/database/FlightRes.db'
flightapp.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy with the Flask app
db = SQLAlchemy(flightapp)

# Configuration for Flask-Mail
mail_settings = {
    "MAIL_SERVER": "smtp.gmail.com",
    "MAIL_PORT": 587,
    "MAIL_USE_TLS": True,
    "MAIL_USE_SSL": False,
    "MAIL_USERNAME": os.environ.get('MAIL_USERNAME'),  # Use environment variable for email
    "MAIL_PASSWORD": os.environ.get('MAIL_PASSWORD'),  # Use environment variable for password
}
mail = Mail(flightapp)
flightapp.config.update(mail_settings)

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.init_app(flightapp)

# Import your models after initializing db
from .models import Customer, Employee, Promotion, Price, Ticket, Booking, Payment, Review, Schedule, Reservation, ReservationHistory, Invoice, Route, Aircraft, ReportRevenue, FlightDetail

# Create the tables when the application starts
@flightapp.before_first_request
def create_tables():
    db.create_all()



# Function to add a flight to the database
def add_flight(flightID, departureAirport, arrivalAirport, departureTime, arrivalTime, availableSeats, price):
    new_flight = FlightDetail(
        flightID=flightID,
        departureAirport=departureAirport,
        arrivalAirport=arrivalAirport,
        departureTime=departureTime,
        arrivalTime=arrivalTime,
        availableSeats=availableSeats,
        price=price
    )
    db.session.add(new_flight)
    db.session.commit()
# Function to delete a flight from the database
def delete_flight(flightID):
    try:
        flight = FlightDetail.query.filter_by(flightID=flightID).first()
        if flight:
            db.session.delete(flight)
            db.session.commit()
            return jsonify({'message': 'Flight deleted successfully'})
        else:
            return jsonify({'error': 'Flight not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Create the flight table when the application starts
# This is not needed with Flask-SQLAlchemy

@flightapp.route('/add_flight', methods=['POST'])
def add_flight_route():
    data = request.form
    required_fields = ['flightID', 'departureAirport', 'arrivalAirport', 'departureTime', 'arrivalTime', 'availableSeats', 'price']

    if all(field in data for field in required_fields):
        flightID = data['flightID']
        departureAirport = data['departureAirport']
        arrivalAirport = data['arrivalAirport']
        departureTime = data['departureTime']
        arrivalTime = data['arrivalTime']
        availableSeats = data['availableSeats']
        price = data['price']

        add_flight(flightID, departureAirport, arrivalAirport, departureTime, arrivalTime, availableSeats, price)

        return jsonify({'message': 'Flight added successfully'})
    else:
        return jsonify({'error': 'Missing required fields'}), 400
@flightapp.route('/delete_flight', methods=['POST'])
def delete_flight_route():
    data = request.form
    flightID  = data['flightID']

    delete_flight(flightID)

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
