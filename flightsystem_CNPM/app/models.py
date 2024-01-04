from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from datetime import datetime

db = SQLAlchemy()

class Role(db.Model):
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    def __str__(self):
        return self.name
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    # Thêm cột role_id và tạo mối quan hệ khóa ngoại với Role
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), nullable=False)
    role = db.relationship('Role', backref='user_role', lazy=True)

    is_admin = db.Column(db.Boolean, default=False)
    is_employee = db.Column(db.Boolean, default=False)

    def __str__(self):
        return self.username

    def __str__(self):
        return self.username

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
        return self.name


class Login(db.Model):
    __tablename__ = 'login'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    # Thêm cột user_id và tạo mối quan hệ khóa ngoại
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref='login_user', lazy=True)

    def __str__(self):
        return f"Login ID: {self.id}, User: {self.user.username}"
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

    # Thêm cột login_id và tạo mối quan hệ khóa ngoại
    login_id = db.Column(db.Integer, db.ForeignKey('login.id'), nullable=False)
    login = db.relationship('Login', backref='employee_login', lazy=True)

    def __str__(self):
        return self.name

class Airport(db.Model):
    __tablename__ = 'airport'
    airportCode = db.Column(db.String(3), primary_key=True)
    airportName = db.Column(db.String(255))

    def __str__(self):
        return f"{self.airportCode} - {self.airportName}"

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
    schedules = db.relationship('Schedule', backref='flight', lazy=True)

    def __str__(self):
        return f"Flight ID: {self.flightID}, Departure: {self.departure_airport.airportCode}, Arrival: {self.arrival_airport.airportCode}"

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
        return f"Review ID: {self.reviewID}, Reservation: {self.reservation.reservationID}"

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

class ReportRevenue(db.Model):
    __tablename__ = 'reportRevenue'
    reportID = db.Column(db.String(50), primary_key=True)
    totalRevenue = db.Column(db.Float)
    reportDateTime = db.Column(db.DateTime)
    flightID = db.Column(db.String(50), db.ForeignKey('flight_detail.flightID'))

    flight = db.relationship('FlightDetail', backref='revenue_reports')

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

# Tạo một vai trò Admin và gán cho người dùng Admin
def create_admin_role():
    admin_role = Role(name='admin')
    db.session.add(admin_role)
    db.session.commit()
# Thêm dữ liệu mẫu
def add_sample_data():
    # Thêm người dùng
    user1 = User(username='admin', email='admin@example.com', password='admin_pass', is_admin=True)
    user2 = User(username='user1', email='user1@example.com', password='user1_pass')
    user3 = User(username='user2', email='user2@example.com', password='user2_pass')

    db.session.add_all([user1, user2, user3])
    db.session.commit()

    # Thêm sân bay
    airport1 = Airport(airportCode='AAA', airportName='Airport A')
    airport2 = Airport(airportCode='BBB', airportName='Airport B')

    db.session.add_all([airport1, airport2])
    db.session.commit()

    # Thêm tuyến bay
    route1 = Route(routeID='R1', departureAirportCode='AAA', arrivalAirportCode='BBB', distance=1000, estimatedDuration=2)
    route2 = Route(routeID='R2', departureAirportCode='BBB', arrivalAirportCode='AAA', distance=1000, estimatedDuration=2)

    db.session.add_all([route1, route2])
    db.session.commit()

    # Thêm máy bay
    aircraft1 = Aircraft(aircraftID='A1', model='Boeing 747', capacity=300, manufacturer='Boeing')
    aircraft2 = Aircraft(aircraftID='A2', model='Airbus A320', capacity=150, manufacturer='Airbus')

    db.session.add_all([aircraft1, aircraft2])
    db.session.commit()

    # Thêm chi tiết chuyến bay
    flight1 = FlightDetail(flightID='F1', departureAirportCode='AAA', arrivalAirportCode='BBB',
                           departureTime=datetime(2024, 1, 3, 12, 0, 0), arrivalTime=datetime(2024, 1, 3, 14, 0, 0),
                           availableSeats=250, price=200, routeID='R1', aircraftID='A1')
    flight2 = FlightDetail(flightID='F2', departureAirportCode='BBB', arrivalAirportCode='AAA',
                           departureTime=datetime(2024, 1, 4, 12, 0, 0), arrivalTime=datetime(2024, 1, 4, 14, 0, 0),
                           availableSeats=120, price=150, routeID='R2', aircraftID='A2')

    db.session.add_all([flight1, flight2])
    db.session.commit()

    # Thêm khuyến mãi
    promotion1 = Promotion(promotionID='P1', description='Discount 20%', discount=0.2,
                           validityStartDate=datetime(2024, 1, 1), validityEndDate=datetime(2024, 1, 31),
                           flightID='F1')
    promotion2 = Promotion(promotionID='P2', description='Discount 15%', discount=0.15,
                           validityStartDate=datetime(2024, 1, 1), validityEndDate=datetime(2024, 1, 31),
                           flightID='F2')

    db.session.add_all([promotion1, promotion2])
    db.session.commit()

    # Thêm giá
    price1 = Price(priceID='Price1', basePrice=200, taxes=20, discount=0.2, promotionID='P1')
    price2 = Price(priceID='Price2', basePrice=150, taxes=15, discount=0.15, promotionID='P2')

    db.session.add_all([price1, price2])
    db.session.commit()

    # Thêm đặt chỗ
    booking1 = Booking(bookingID='B1', customerID='user1', flightClass='Economy', paymentMethod='Credit Card',
                       status='Confirmed', bookingDateTime=datetime(2024, 1, 1, 10, 0, 0), paymentID='Payment1',
                       flightID='F1')
    booking2 = Booking(bookingID='B2', customerID='user2', flightClass='Business', paymentMethod='PayPal',
                       status='Pending', bookingDateTime=datetime(2024, 1, 2, 11, 0, 0), paymentID='Payment2',
                       flightID='F2')

    db.session.add_all([booking1, booking2])
    db.session.commit()

    # Thêm thanh toán
    payment1 = Payment(paymentID='Payment1', amountPaid=180, paymentMethod='Credit Card',
                       paymentStatus='Successful', paymentDateTime=datetime(2024, 1, 1, 12, 0, 0), bookingID='B1')
    payment2 = Payment(paymentID='Payment2', amountPaid=120, paymentMethod='PayPal',
                       paymentStatus='Pending', paymentDateTime=datetime(2024, 1, 2, 14, 0, 0), bookingID='B2')

    db.session.add_all([payment1, payment2])
    db.session.commit()

    # Thêm đánh giá
    review1 = Review(reviewID='Review1', reservationID='Reservation1', rating=4, feedback='Great service!',
                     submittedBy='user1', submissionDateTime=datetime(2024, 1, 1, 15, 0, 0))
    review2 = Review(reviewID='Review2', reservationID='Reservation2', rating=5, feedback='Excellent flight!',
                     submittedBy='user2', submissionDateTime=datetime(2024, 1, 2, 16, 0, 0))

    db.session.add_all([review1, review2])
    db.session.commit()

# Thêm dữ liệu mẫu
#add_sample_data()
# Thêm các mô hình khác tương tự...

# Example of how to create the tables
def create_tables():
    db.create_all()

# Example of how to drop all tables
def drop_tables():
    db.drop_all()