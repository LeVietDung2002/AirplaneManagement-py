from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Customer(db.Model):
    customerID = db.Column(db.String(50), primary_key=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255))
    phone = db.Column(db.String(20))
    address = db.Column(db.String(255))

class Employee(db.Model):
    employeeID = db.Column(db.String(50), primary_key=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255))
    phone = db.Column(db.String(20))
    position = db.Column(db.String(100))

class FlightDetail(db.Model):
    __tablename__ = 'FlightDetail'  # Set the table name explicitly

    flightID = db.Column(db.String(50), primary_key=True)
    departureAirport = db.Column(db.String(255))
    arrivalAirport = db.Column(db.String(255))
    departureTime = db.Column(db.DateTime)
    arrivalTime = db.Column(db.DateTime)
    availableSeats = db.Column(db.Integer)
    price = db.Column(db.Float)
    # Add other columns as needed
class Promotion(db.Model):
    promotionID = db.Column(db.String(50), primary_key=True)
    description = db.Column(db.String(255))
    discount = db.Column(db.Float)
    validityStartDate = db.Column(db.DateTime)
    validityEndDate = db.Column(db.DateTime)

class Price(db.Model):
    priceID = db.Column(db.String(50), primary_key=True)
    basePrice = db.Column(db.Float)
    taxes = db.Column(db.Float)
    discount = db.Column(db.Float)

class Ticket(db.Model):
    ticketID = db.Column(db.String(50), primary_key=True)
    flightID = db.Column(db.String(50), db.ForeignKey('flight_detail.flightID'))
    priceID = db.Column(db.String(50), db.ForeignKey('price.priceID'))
    bookingID = db.Column(db.String(50), db.ForeignKey('booking.bookingID'))

class Booking(db.Model):
    bookingID = db.Column(db.String(50), primary_key=True)
    customerID = db.Column(db.String(50), db.ForeignKey('customer.customerID'))
    flightClass = db.Column(db.String(50))
    paymentMethod = db.Column(db.String(50))
    status = db.Column(db.String(50))
    bookingDateTime = db.Column(db.DateTime)

class Payment(db.Model):
    paymentID = db.Column(db.String(50), primary_key=True)
    amountPaid = db.Column(db.Float)
    paymentMethod = db.Column(db.String(50))
    paymentStatus = db.Column(db.String(50))
    paymentDateTime = db.Column(db.DateTime)

class Review(db.Model):
    reviewID = db.Column(db.String(50), primary_key=True)
    reservationID = db.Column(db.String(50), db.ForeignKey('reservation.reservationID'))
    rating = db.Column(db.Integer)
    feedback = db.Column(db.String(255))
    submittedBy = db.Column(db.String(50))
    submissionDateTime = db.Column(db.DateTime)

class Schedule(db.Model):
    flightID = db.Column(db.String(50), primary_key=True)
    departureAirport = db.Column(db.String(255))
    arrivalAirport = db.Column(db.String(255))
    departureDateTime = db.Column(db.DateTime)
    arrivalDateTime = db.Column(db.DateTime)
    availableSeats = db.Column(db.Integer)
    layoverAirports = db.Column(db.String(255))

class Reservation(db.Model):
    reservationID = db.Column(db.String(50), primary_key=True)
    customerID = db.Column(db.String(50), db.ForeignKey('customer.customerID'))
    flightID = db.Column(db.String(50), db.ForeignKey('flight_detail.flightID'))
    status = db.Column(db.String(50))
    bookingDateTime = db.Column(db.DateTime)
    paymentStatus = db.Column(db.String(50))
    amountPaid = db.Column(db.Float)
    reservationDateTime = db.Column(db.DateTime)

class ReservationHistory(db.Model):
    historyID = db.Column(db.String(50), primary_key=True)
    reservationID = db.Column(db.String(50), db.ForeignKey('reservation.reservationID'))
    status = db.Column(db.String(50))
    updateDateTime = db.Column(db.DateTime)

class Invoice(db.Model):
    invoiceID = db.Column(db.String(50), primary_key=True)
    reservationID = db.Column(db.String(50), db.ForeignKey('reservation.reservationID'))
    amountDue = db.Column(db.Float)
    dueDate = db.Column(db.DateTime)

class Route(db.Model):
    routeID = db.Column(db.String(50), primary_key=True)
    departureAirport = db.Column(db.String(255))
    arrivalAirport = db.Column(db.String(255))
    distance = db.Column(db.Float)
    estimatedDuration = db.Column(db.Float)

class Aircraft(db.Model):
    aircraftID = db.Column(db.String(50), primary_key=True)
    model = db.Column(db.String(255))
    capacity = db.Column(db.Integer)
    manufacturer = db.Column(db.String(255))
class ReportRevenue(db.Model):
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