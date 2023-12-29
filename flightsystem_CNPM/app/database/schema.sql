-- Customer Table
CREATE TABLE Customer (
    customerID VARCHAR(50) PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255),
    phone VARCHAR(20),
    address VARCHAR(255)
);

-- Employee Table
CREATE TABLE Employee (
    employeeID VARCHAR(50) PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255),
    phone VARCHAR(20),
    position VARCHAR(100)
);

-- FlightDetail Table
CREATE TABLE FlightDetail (
    flightID VARCHAR(50) PRIMARY KEY,
    departureAirport VARCHAR(255),
    arrivalAirport VARCHAR(255),
    departureTime DATETIME,
    arrivalTime DATETIME,
    availableSeats INT,
    price DOUBLE
);

-- Promotion Table
CREATE TABLE Promotion (
    promotionID VARCHAR(50) PRIMARY KEY,
    description VARCHAR(255),
    discount DOUBLE,
    validityStartDate DATETIME,
    validityEndDate DATETIME
);

-- Price Table
CREATE TABLE Price (
    priceID VARCHAR(50) PRIMARY KEY,
    basePrice DOUBLE,
    taxes DOUBLE,
    discount DOUBLE
);

-- Ticket Table
CREATE TABLE Ticket (
    ticketID VARCHAR(50) PRIMARY KEY,
    flightID VARCHAR(50),
    priceID VARCHAR(50),
    bookingID VARCHAR(50),
    FOREIGN KEY (flightID) REFERENCES FlightDetail(flightID),
    FOREIGN KEY (priceID) REFERENCES Price(priceID),
    FOREIGN KEY (bookingID) REFERENCES Booking(bookingID)
);

-- Booking Table
CREATE TABLE Booking (
    bookingID VARCHAR(50) PRIMARY KEY,
    customerID VARCHAR(50),
    flightClass VARCHAR(50),
    paymentMethod VARCHAR(50),
    status VARCHAR(50),
    bookingDateTime DATETIME,
    FOREIGN KEY (customerID) REFERENCES Customer(customerID)
);

-- Payment Table
CREATE TABLE Payment (
    paymentID VARCHAR(50) PRIMARY KEY,
    amountPaid DOUBLE,
    paymentMethod VARCHAR(50),
    paymentStatus VARCHAR(50),
    paymentDateTime DATETIME
);

-- Review Table
CREATE TABLE Review (
    reviewID VARCHAR(50) PRIMARY KEY,
    reservationID VARCHAR(50),
    rating INT,
    feedback VARCHAR(255),
    submittedBy VARCHAR(50),
    submissionDateTime DATETIME,
    FOREIGN KEY (reservationID) REFERENCES Reservation(reservationID)
);

-- Schedule Table
CREATE TABLE Schedule (
    flightID VARCHAR(50) PRIMARY KEY,
    departureAirport VARCHAR(255),
    arrivalAirport VARCHAR(255),
    departureDateTime DATETIME,
    arrivalDateTime DATETIME,
    availableSeats INT,
    layoverAirports VARCHAR(255)
);

-- Reservation Table
CREATE TABLE Reservation (
    reservationID VARCHAR(50) PRIMARY KEY,
    customerID VARCHAR(50),
    flightID VARCHAR(50),
    status VARCHAR(50),
    bookingDateTime DATETIME,
    paymentStatus VARCHAR(50),
    amountPaid DOUBLE,
    reservationDateTime DATETIME,
    FOREIGN KEY (customerID) REFERENCES Customer(customerID),
    FOREIGN KEY (flightID) REFERENCES FlightDetail(flightID)
);

-- ReservationHistory Table
CREATE TABLE ReservationHistory (
    historyID VARCHAR(50) PRIMARY KEY,
    reservationID VARCHAR(50),
    status VARCHAR(50),
    updateDateTime DATETIME,
    FOREIGN KEY (reservationID) REFERENCES Reservation(reservationID)
);

-- Invoice Table
CREATE TABLE Invoice (
    invoiceID VARCHAR(50) PRIMARY KEY,
    reservationID VARCHAR(50),
    amountDue DOUBLE,
    dueDate DATETIME,
    FOREIGN KEY (reservationID) REFERENCES Reservation(reservationID)
);

-- Route Table
CREATE TABLE Route (
    routeID VARCHAR(50) PRIMARY KEY,
    departureAirport VARCHAR(255),
    arrivalAirport VARCHAR(255),
    distance DOUBLE,
    estimatedDuration DOUBLE
);

-- Aircraft Table
CREATE TABLE Aircraft (
    aircraftID VARCHAR(50) PRIMARY KEY,
    model VARCHAR(255),
    capacity INT,
    manufacturer VARCHAR(255)
);
CREATE TABLE ReportRevenue (
    reportID VARCHAR(50) PRIMARY KEY,
    reservationID VARCHAR(50),
    customerID VARCHAR(50),
    flightID VARCHAR(50),
    price DOUBLE,
    taxes DOUBLE,
    discount DOUBLE,
    amountPaid DOUBLE,
    totalRevenue DOUBLE,
    reportDateTime DATETIME,
    FOREIGN KEY (reservationID) REFERENCES Reservation(reservationID),
    FOREIGN KEY (customerID) REFERENCES Customer(customerID),
    FOREIGN KEY (flightID) REFERENCES FlightDetail(flightID)
);
