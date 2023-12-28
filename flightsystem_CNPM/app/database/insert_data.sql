-- Insert data into the Customer table
INSERT INTO Customer VALUES
    ('C001', 'John Doe', 'john.doe@example.com', '1234567890', '123 Main St'),
    ('C002', 'Jane Smith', 'jane.smith@example.com', '9876543210', '456 Oak St');

-- Insert data into the Employee table
INSERT INTO Employee VALUES
    ('E001', 'Alice Johnson', 'alice.johnson@example.com', '1112223333', 'Manager'),
    ('E002', 'Bob Williams', 'bob.williams@example.com', '4445556666', 'Staff');

-- Insert data into the FlightDetail table
INSERT INTO FlightDetail VALUES
    ('F001', 'Airport1', 'Airport2', '2023-01-01 08:00:00', '2023-01-01 10:00:00', 100, 150.00),
    ('F002', 'Airport3', 'Airport4', '2023-02-01 12:00:00', '2023-02-01 14:00:00', 120, 200.00);

-- Insert data into the Promotion table
INSERT INTO Promotion VALUES
    ('P001', 'Summer Discount', 0.1, '2023-06-01 00:00:00', '2023-08-31 23:59:59'),
    ('P002', 'Winter Sale', 0.2, '2023-12-01 00:00:00', '2023-12-31 23:59:59');

-- Insert data into the Price table
INSERT INTO Price VALUES
    ('PR001', 100.00, 10.00, 0.05),
    ('PR002', 120.00, 15.00, 0.1);

-- Insert data into the Ticket table
INSERT INTO Ticket VALUES
    ('T001', 'F001', 'PR001', 'B001'),
    ('T002', 'F002', 'PR002', 'B002');

-- Insert data into the Booking table
INSERT INTO Booking VALUES
    ('B001', 'C001', 'Economy', 'Credit Card', 'Confirmed', '2023-01-01 09:00:00'),
    ('B002', 'C002', 'Business', 'PayPal', 'Pending', '2023-02-01 13:00:00');

-- Insert data into the Payment table
INSERT INTO Payment VALUES
    ('PM001', 120.00, 'Credit Card', 'Success', '2023-01-01 10:00:00'),
    ('PM002', 180.00, 'PayPal', 'Pending', '2023-02-01 14:00:00');

-- Insert data into the Review table
INSERT INTO Review VALUES
    ('R001', 'Res001', 4, 'Great service!', 'C001', '2023-01-02 11:00:00'),
    ('R002', 'Res002', 5, 'Excellent flight!', 'C002', '2023-02-02 15:00:00');

-- Insert data into the Schedule table
INSERT INTO Schedule VALUES
    ('F001', 'Airport1', 'Airport2', '2023-01-01 08:00:00', '2023-01-01 10:00:00', 100, 'Airport3'),
    ('F002', 'Airport3', 'Airport4', '2023-02-01 12:00:00', '2023-02-01 14:00:00', 120, 'Airport5');

-- Insert data into the Reservation table
INSERT INTO Reservation VALUES
    ('Res001', 'C001', 'F001', 'Confirmed', '2023-01-01 09:00:00', 'Success', 120.00, '2023-01-01 09:00:00'),
    ('Res002', 'C002', 'F002', 'Pending', '2023-02-01 13:00:00', 'Pending', 180.00, '2023-02-01 13:00:00');

-- Insert data into the ReservationHistory table
INSERT INTO ReservationHistory VALUES
    ('RH001', 'Res001', 'Confirmed', '2023-01-01 09:00:00'),
    ('RH002', 'Res002', 'Pending', '2023-02-01 13:00:00');

-- Insert data into the Invoice table
INSERT INTO Invoice VALUES
    ('I001', 'Res001', 120.00, '2023-01-10 00:00:00'),
    ('I002', 'Res002', 180.00, '2023-02-10 00:00:00');

-- Insert data into the Route table
INSERT INTO Route VALUES
    ('Route001', 'Airport1', 'Airport2', 500.00, 2.5),
    ('Route002', 'Airport3', 'Airport4', 600.00, 3.0);

-- Insert data into the Aircraft table
INSERT INTO Aircraft VALUES
    ('A001', 'Boeing 737', 150, 'Boeing'),
    ('A002', 'Airbus A320', 180, 'Airbus');
