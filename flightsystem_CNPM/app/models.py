from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from datetime import datetime
import json

db = SQLAlchemy()

class Role(db.Model):
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    def __str__(self):
        return f"Role ID: {self.id}, Name: {self.name}"

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), nullable=False)
    role = db.relationship('Role', backref='user_role', lazy=True)
    is_admin = db.Column(db.Boolean, default=False)
    is_employee = db.Column(db.Boolean, default=False)

    def __str__(self):
        return f"User ID: {self.id}, Username: {self.username}, Email: {self.email}"

class Admin(db.Model):
    __tablename__ = 'admin'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), nullable=False)
    role = db.relationship('Role', backref='admin_role', lazy=True)

    def __str__(self):
        return f"Admin ID: {self.id}, Role: {self.role.name}"
class Customer(db.Model):
    __tablename__ = 'customer'
    customerID = db.Column(db.String(50), primary_key=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255))
    phone = db.Column(db.String(20))
    address = db.Column(db.String(255))

    def __str__(self):
        return f"Customer ID: {self.customerID}, Name: {self.name}"


class Login(db.Model):
    __tablename__ = 'login'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref='login_user', lazy=True)

    def __str__(self):
        return f"Login ID: {self.id}, Username: {self.username}"

class ConfirmationToken(db.Model):
        __tablename__ = 'confirmationtoken'
        id = db.Column(db.Integer, primary_key=True, autoincrement=True)
        user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
        token = db.Column(db.String(120), nullable=False)
        user = db.relationship('User', backref='confirmation_token_user', lazy=True)

        def __str__(self):
            return f"Token ID: {self.id}, User: {self.user.username}"
class Employee(db.Model):
    __tablename__ = 'employee'
    employeeID = db.Column(db.String(50), primary_key=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255))
    phone = db.Column(db.String(20))
    position = db.Column(db.String(100))
    login_id = db.Column(db.Integer, db.ForeignKey('login.id'), nullable=False)
    login = db.relationship('Login', backref='employee_login', lazy=True)

    def __str__(self):
        return f"Employee ID: {self.employeeID}, Name: {self.name}"

class Airport(db.Model):
    __tablename__ = 'airport'
    airportCode = db.Column(db.String(3), primary_key=True)
    airportName = db.Column(db.String(255))

    def __str__(self):
        return f"Airport Code: {self.airportCode}, Name: {self.airportName}"



class Route(db.Model):
    __tablename__ = 'route'
    routeID = db.Column(db.String(50), primary_key=True)
    departureAirportCode = db.Column(db.String(3), db.ForeignKey('airport.airportCode'))
    arrivalAirportCode = db.Column(db.String(3), db.ForeignKey('airport.airportCode'))
    distance = db.Column(db.Float)
    estimatedDuration = db.Column(db.Float)

    departure_airport = db.relationship('Airport', foreign_keys=[departureAirportCode], backref='routes_departure')
    arrival_airport = db.relationship('Airport', foreign_keys=[arrivalAirportCode], backref='routes_arrival')

    def __str__(self):
        return f"Route ID: {self.routeID}, Departure: {self.departure_airport.airportCode}, Arrival: {self.arrival_airport.airportCode}"
class ReportRevenue(db.Model):
    __tablename__ = 'reportRevenue'
    reportID = db.Column(db.String(50), primary_key=True)
    totalRevenue = db.Column(db.Float)
    reportDateTime = db.Column(db.DateTime)
    flightID = db.Column(db.String(50), db.ForeignKey('flight_detail.flightID'))

    flight = db.relationship('FlightDetail', backref='revenue_reports')
    __table_args__ = {'extend_existing': True}
    def __str__(self):
        return f"Report ID: {self.reportID}, Flight: {self.flight.flightID}"
class CustomerFlight(db.Model):
    __tablename__ = 'customer_flight'
    customerID = db.Column(db.String(50), db.ForeignKey('customer.customerID'), primary_key=True)
    flightID = db.Column(db.String(50), db.ForeignKey('flight_detail.flightID'), primary_key=True)

    customer = db.relationship('Customer', backref='customer_flights')
    flight = db.relationship('FlightDetail', backref='customer_flights')

    def __str__(self):
        return f"CustomerFlight - Customer: {self.customer.name}, Flight: {self.flight.flightID}"

class Aircraft(db.Model):
    __tablename__ = 'aircraft'
    aircraftID = db.Column(db.String(50), primary_key=True)
    model = db.Column(db.String(255))
    capacity = db.Column(db.Integer)
    manufacturer = db.Column(db.String(255))

    def __str__(self):
        return f"Aircraft ID: {self.aircraftID}, Model: {self.model}"

class FlightDetail(db.Model):
    __tablename__ = 'flight_detail'
    flightID = db.Column(db.String(50), primary_key=True)
    departureAirportCode = db.Column(db.String(3), db.ForeignKey('airport.airportCode'))
    arrivalAirportCode = db.Column(db.String(3), db.ForeignKey('airport.airportCode'))
    departureTime = db.Column(db.DateTime)
    arrivalTime = db.Column(db.DateTime)
    availableSeats = db.Column(db.Integer)
    price = db.Column(db.Float)
    routeID = db.Column(db.String(50), db.ForeignKey('route.routeID'))
    aircraftID = db.Column(db.String(50), db.ForeignKey('aircraft.aircraftID'))

    route = db.relationship('Route', backref='flights')
    aircraft = db.relationship('Aircraft', backref='flights')
    schedules = db.relationship('Schedule', backref='flight_details', lazy=True)

    def __str__(self):
        return f"Flight ID: {self.flightID}, Departure: {self.departureAirport.airportCode}, Arrival: {self.arrivalAirport.airportCode}"
class Promotion(db.Model):
    __tablename__ = 'promotion'
    promotionID = db.Column(db.String(50), primary_key=True)
    description = db.Column(db.String(255))
    discount = db.Column(db.Float)
    validityStartDate = db.Column(db.DateTime)
    validityEndDate = db.Column(db.DateTime)
    flightID = db.Column(db.String(50), db.ForeignKey('flight_detail.flightID'))

    flight = db.relationship('FlightDetail', backref='promotions')

    def __str__(self):
        return f"Promotion ID: {self.promotionID}, Description: {self.description}"

class Price(db.Model):
    __tablename__ = 'price'
    priceID = db.Column(db.String(50), primary_key=True)
    basePrice = db.Column(db.Float)
    taxes = db.Column(db.Float)
    discount = db.Column(db.Float)
    promotionID = db.Column(db.String(50), db.ForeignKey('promotion.promotionID'))

    promotion = db.relationship('Promotion', backref='prices')

    def __str__(self):
        return f"Price ID: {self.priceID}, Base Price: {self.basePrice}"

class Ticket(db.Model):
    __tablename__ = 'ticket'
    ticketID = db.Column(db.String(50), primary_key=True)
    flightID = db.Column(db.String(50), db.ForeignKey('flight_detail.flightID'))
    priceID = db.Column(db.String(50), db.ForeignKey('price.priceID'))
    bookingID = db.Column(db.String(50), db.ForeignKey('booking.bookingID'))

    flight = db.relationship('FlightDetail', backref='tickets')
    price = db.relationship('Price', backref='tickets')
    booking = db.relationship('Booking', backref='tickets')

    def __str__(self):
        return f"Ticket ID: {self.ticketID}, Flight: {self.flight.flightID}"

class Booking(db.Model):
    __tablename__ = 'booking'
    bookingID = db.Column(db.String(50), primary_key=True)
    customerID = db.Column(db.String(50), db.ForeignKey('customer.customerID'))
    flightClass = db.Column(db.String(50))
    paymentMethod = db.Column(db.String(50))
    status = db.Column(db.String(50))
    bookingDateTime = db.Column(db.DateTime)
    paymentID = db.Column(db.String(50), db.ForeignKey('payment.paymentID'))

    customer = db.relationship('Customer', backref='bookings')
    payments = db.relationship('Payment', backref='booking_payments', lazy=True, foreign_keys=[paymentID])

    def __str__(self):
        return f"Booking ID: {self.bookingID}, Customer: {self.customer.name}"

class Payment(db.Model):
    __tablename__ = 'payment'
    paymentID = db.Column(db.String(50), primary_key=True)
    amountPaid = db.Column(db.Float)
    paymentMethod = db.Column(db.String(50))
    paymentStatus = db.Column(db.String(50))
    paymentDateTime = db.Column(db.DateTime)
    bookingID = db.Column(db.String(50), db.ForeignKey('booking.bookingID'))

    booking = db.relationship('Booking', backref='payment_bookings', lazy=True, foreign_keys=[bookingID])

    def __str__(self):
        return f"Payment ID: {self.paymentID}, Amount Paid: {self.amountPaid}"

class Review(db.Model):
    __tablename__ = 'review'
    reviewID = db.Column(db.String(50), primary_key=True)
    reservationID = db.Column(db.String(50), db.ForeignKey('reservation.reservationID'))
    rating = db.Column(db.Integer)
    feedback = db.Column(db.String(255))
    submittedBy = db.Column(db.String(50))
    submissionDateTime = db.Column(db.DateTime)

    reservation = db.relationship('Reservation', backref='reviews', lazy=True)

    def __str__(self):
        return f"Review ID: {self.reviewID}, Reservation: {self.reservationID}"
class Schedule(db.Model):
    __tablename__ = 'schedule'
    scheduleID = db.Column(db.String(50), primary_key=True)
    flightID = db.Column(db.String(50), db.ForeignKey('flight_detail.flightID'))
    departureAirportCode = db.Column(db.String(3), db.ForeignKey('airport.airportCode'))
    arrivalAirportCode = db.Column(db.String(3), db.ForeignKey('airport.airportCode'))
    departureDateTime = db.Column(db.DateTime)
    arrivalDateTime = db.Column(db.DateTime)
    availableSeats = db.Column(db.Integer)
    layoverAirports = db.Column(db.String(255))

    flight = db.relationship('FlightDetail', backref='schedules')
    departure_airport = db.relationship('Airport', foreign_keys=[departureAirportCode], backref='schedules_departure')
    arrival_airport = db.relationship('Airport', foreign_keys=[arrivalAirportCode], backref='schedules_arrival')

    def __str__(self):
        return f"Schedule ID: {self.scheduleID}, Flight: {self.flight.flightID}"

class Reservation(db.Model):
    __tablename__ = 'reservation'
    reservationID = db.Column(db.String(50), primary_key=True)
    customerID = db.Column(db.String(50), db.ForeignKey('customer.customerID'))
    flightID = db.Column(db.String(50), db.ForeignKey('flight_detail.flightID'))
    status = db.Column(db.String(50))
    bookingDateTime = db.Column(db.DateTime)
    paymentStatus = db.Column(db.String(50))
    amountPaid = db.Column(db.Float)
    reservationDateTime = db.Column(db.DateTime)

    customer = db.relationship('Customer', backref='reservations')
    flight = db.relationship('FlightDetail', backref='reservations')

    reviews = db.relationship('Review', backref='reservation', lazy=True)
    invoices = db.relationship('Invoice', backref='reservation', lazy=True)

    def __str__(self):
        return f"Reservation ID: {self.reservationID}, Customer: {self.customer.name}"

class ReservationHistory(db.Model):
    __tablename__ = 'reservationHistory'
    historyID = db.Column(db.String(50), primary_key=True)
    reservationID = db.Column(db.String(50), db.ForeignKey('reservation.reservationID'))
    status = db.Column(db.String(50))
    updateDateTime = db.Column(db.DateTime)

    reservation = db.relationship('Reservation', backref='history', lazy=True)

    def __str__(self):
        return f"History ID: {self.historyID}, Reservation: {self.reservation.reservationID}"

class Invoice(db.Model):
    __tablename__ = 'invoice'
    invoiceID = db.Column(db.String(50), primary_key=True)
    reservationID = db.Column(db.String(50), db.ForeignKey('reservation.reservationID'))
    amountDue = db.Column(db.Float)
    dueDate = db.Column(db.DateTime)

    reservation = db.relationship('Reservation', backref='invoices', lazy=True)

    def __str__(self):
        return f"Invoice ID: {self.invoiceID}, Reservation: {self.reservation.reservationID}"





# Tạo một vai trò Admin và gán cho người dùng Admin
def create_admin_role():
    admin_role = Role(name='admin')
    db.session.add(admin_role)
    db.session.commit()
# Thêm dữ liệu mẫu
    def add_sample_data():
        # Serialize data to JSON
        data = {
            'roles': [role.__dict__ for role in Role.query.all()],
            'users': [user.__dict__ for user in User.query.all()],
            'admins': [admin.__dict__ for admin in Admin.query.all()],
            'customers': [customer.__dict__ for customer in Customer.query.all()],
            'logins': [login.__dict__ for login in Login.query.all()],
            'confirmation_tokens': [token.__dict__ for token in ConfirmationToken.query.all()],
            'employees': [employee.__dict__ for employee in Employee.query.all()],
            'airports': [airport.__dict__ for airport in Airport.query.all()],
            'routes': [route.__dict__ for route in Route.query.all()],
            'report_revenues': [report.__dict__ for report in ReportRevenue.query.all()],
            'customer_flights': [customer_flight.__dict__ for customer_flight in CustomerFlight.query.all()],
            'aircrafts': [aircraft.__dict__ for aircraft in Aircraft.query.all()],
            'flight_details': [flight.__dict__ for flight in FlightDetail.query.all()],
            'promotions': [promotion.__dict__ for promotion in Promotion.query.all()],
            'prices': [price.__dict__ for price in Price.query.all()],
            'tickets': [ticket.__dict__ for ticket in Ticket.query.all()],
            'bookings': [booking.__dict__ for booking in Booking.query.all()],
            'payments': [payment.__dict__ for payment in Payment.query.all()],
            'reviews': [review.__dict__ for review in Review.query.all()],
            'schedules': [schedule.__dict__ for schedule in Schedule.query.all()],
            'reservations': [reservation.__dict__ for reservation in Reservation.query.all()],
            'reservation_histories': [history.__dict__ for history in ReservationHistory.query.all()],
            'invoices': [invoice.__dict__ for invoice in Invoice.query.all()]
            # ... add more entities as needed
        }

        # Write data to a JSON file
        with open('data.json', 'w') as json_file:
            json_file.write(json.dumps(data, default=str, indent=4))


# Thêm dữ liệu mẫu
#add_sample_data()
# Thêm các mô hình khác tương tự...

# Example of how to create the tables
def create_tables():
    db.create_all()

# Example of how to drop all tables
#def drop_tables():
    #db.drop_all()
