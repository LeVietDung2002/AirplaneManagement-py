from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from sqlalchemy.orm import relationship

db = SQLAlchemy()

class User(db.Model, UserMixin):
    __tablename__ ='user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    def __str__(self):
        return self.username
class Admin(db.Model):
    __tablename__ ='admin'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    def __str__(self):
        return self.name


class Customer(db.Model):
    __tablename__ = 'customer'
    customerID = db.Column(db.String(50), primary_key=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255))
    phone = db.Column(db.String(20))
    address = db.Column(db.String(255))
class ConfirmationToken(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    token = db.Column(db.String(120), nullable=False)
class Employee(db.Model):
    __tablename__ ='employee'

    employeeID = db.Column(db.String(50), primary_key=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255))
    phone = db.Column(db.String(20))
    position = db.Column(db.String(100))

class FlightDetail(db.Model):
    __tablename__ = 'flightDetail'  # Set the table name explicitly

    flightID = db.Column(db.String(50), primary_key=True)
    departureAirport = db.Column(db.String(255))
    arrivalAirport = db.Column(db.String(255))
    departureTime = db.Column(db.DateTime)
    arrivalTime = db.Column(db.DateTime)
    availableSeats = db.Column(db.Integer)
    price = db.Column(db.Float)

    routeID = db.Column(db.String(50), db.ForeignKey('route.routeID'))
    route = db.relationship('Route', backref='flights')
    # Mối quan hệ giữa FlightDetail và Route (một chuyến bay có thể có một tuyến đường):
    aircraftID = db.Column(db.String(50), db.ForeignKey('aircraft.aircraftID'))
    aircraft = db.relationship('Aircraft', backref='flights')
    #Mối quan hệ giữa FlightDetail và Aircraft (một chuyến bay sử dụng một máy bay):

    schedules = db.relationship('Schedule', backref='flight', lazy=True)
#Mối quan hệ giữa FlightDetail và Schedule (một chuyến bay có thể có nhiều lịch trình):

def __str__(self):
    return self.flightID

class Promotion(db.Model):
    __tablename__ ='promotion'

    promotionID = db.Column(db.String(50), primary_key=True)
    description = db.Column(db.String(255))
    discount = db.Column(db.Float)
    validityStartDate = db.Column(db.DateTime)
    validityEndDate = db.Column(db.DateTime)



class Price(db.Model):
    __tablename__ = 'price'
    priceID = db.Column(db.String(50), primary_key=True)
    basePrice = db.Column(db.Float)
    taxes = db.Column(db.Float)
    discount = db.Column(db.Float)

class Ticket(db.Model):
    __tablename__ = 'ticket'
    ticketID = db.Column(db.String(50), primary_key=True)
    flightID = db.Column(db.String(50), db.ForeignKey('flight_detail.flightID'))
    priceID = db.Column(db.String(50), db.ForeignKey('price.priceID'))
    bookingID = db.Column(db.String(50), db.ForeignKey('booking.bookingID'))

class Booking(db.Model):
    __tablename__ = 'booking'
    bookingID = db.Column(db.String(50), primary_key=True)
    customerID = db.Column(db.String(50), db.ForeignKey('customer.customerID'))
    flightClass = db.Column(db.String(50))
    paymentMethod = db.Column(db.String(50))
    status = db.Column(db.String(50))
    bookingDateTime = db.Column(db.DateTime)

    tickets = db.relationship('Ticket', backref='booking', lazy=True)
#Mối quan hệ giữa Booking và Ticket (một đặt vé có thể có nhiều vé):
    payments = db.relationship('Payment', backref='booking', lazy=True)
#Mối quan hệ giữa Booking và Payment (một đặt vé có thể có nhiều thanh toán):

class Payment(db.Model):
    __tablename__ = 'payment'
    paymentID = db.Column(db.String(50), primary_key=True)
    amountPaid = db.Column(db.Float)
    paymentMethod = db.Column(db.String(50))
    paymentStatus = db.Column(db.String(50))
    paymentDateTime = db.Column(db.DateTime)

class Review(db.Model):
    __tablename__ = 'review'
    reviewID = db.Column(db.String(50), primary_key=True)
    reservationID = db.Column(db.String(50), db.ForeignKey('reservation.reservationID'))
    rating = db.Column(db.Integer)
    feedback = db.Column(db.String(255))
    submittedBy = db.Column(db.String(50))
    submissionDateTime = db.Column(db.DateTime)

class Schedule(db.Model):
    __tablename__ = 'schedule'
    flightID = db.Column(db.String(50), primary_key=True)
    departureAirport = db.Column(db.String(255))
    arrivalAirport = db.Column(db.String(255))
    departureDateTime = db.Column(db.DateTime)
    arrivalDateTime = db.Column(db.DateTime)
    availableSeats = db.Column(db.Integer)
    layoverAirports = db.Column(db.String(255))

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

    reviews = db.relationship('Review', backref='reservation', lazy=True)
#Mối quan hệ giữa Reservation và Review (một đặt chỗ có thể có nhiều đánh giá):
    invoices = db.relationship('Invoice', backref='reservation', lazy=True)
#Mối quan hệ giữa Reservation và Invoice (một đặt chỗ có thể có nhiều hóa đơn):

class ReservationHistory(db.Model):
    historyID = db.Column(db.String(50), primary_key=True)
    reservationID = db.Column(db.String(50), db.ForeignKey('reservation.reservationID'))
    status = db.Column(db.String(50))
    updateDateTime = db.Column(db.DateTime)

class Invoice(db.Model):
    __tablename__ = 'invoice'
    invoiceID = db.Column(db.String(50), primary_key=True)
    reservationID = db.Column(db.String(50), db.ForeignKey('reservation.reservationID'))
    amountDue = db.Column(db.Float)
    dueDate = db.Column(db.DateTime)

class Route(db.Model):
    __tablename__ = 'route'
    routeID = db.Column(db.String(50), primary_key=True)
    departureAirport = db.Column(db.String(255))
    arrivalAirport = db.Column(db.String(255))
    distance = db.Column(db.Float)
    estimatedDuration = db.Column(db.Float)

class Aircraft(db.Model):
    __tablename__ = 'aircraft'
    aircraftID = db.Column(db.String(50), primary_key=True)
    model = db.Column(db.String(255))
    capacity = db.Column(db.Integer)
    manufacturer = db.Column(db.String(255))
class ReportRevenue(db.Model):
    __tablename__ = 'reportRevenue'
    reportID = db.Column(db.String(50), primary_key=True)
    totalRevenue = db.Column(db.Float)
    reportDateTime = db.Column(db.DateTime)
# Define the rest of the models...

# Example of how to create the tables
def create_tables():
    db.create_all()

# Example of how to drop all tables
def drop_tables():
    db.drop_all()