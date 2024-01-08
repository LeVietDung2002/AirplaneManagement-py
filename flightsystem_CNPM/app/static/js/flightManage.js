
    // Định nghĩa dữ liệu chuyến bay từ server

var flightData = [
    { code: 'CB001', departure: 'TPHCM', destination: 'Hà Nội', date: '2023-12-25', arrivalTime: '2023-12-27', availableSeats: 100, price: 1000000, routeID: 'HNVT1', aircraftID: 'Boeing1' },
    {code: 'CB002', departure: 'Đà Nẵng', destination: 'Nha Trang', date: '2023-12-26', arrivalTime: '2023-12-28', availableSeats: 120, price: 1200000, routeID: 'DNNT1', aircraftID: 'Airbus1' },
    {code: 'CB003', departure: 'Hà Nội', destination: 'Đà Lạt', date: '2023-12-27', arrivalTime: '2023-12-29', availableSeats: 150, price: 1500000, routeID: 'HNDL1', aircraftID: 'Boeing2' },
    {code: 'CB004', departure: 'Hải Phòng', destination: 'Đồng Hới', date: '2023-12-28', arrivalTime: '2023-12-30', availableSeats: 110, price: 1100000, routeID: 'HPDH1', aircraftID: 'Airbus2' },
    {code: 'CB005', departure: 'Nha Trang', destination: 'Phú Quốc', date: '2023-12-29', arrivalTime: '2023-12-31', availableSeats: 130, price: 1300000, routeID: 'NTPQ1', aircraftID: 'Boeing3' },
    {code: 'CB006', departure: 'Huế', destination: 'Buôn Ma Thuột', date: '2023-12-30', arrivalTime: '2024-01-01', availableSeats: 95, price: 950000, routeID: 'HBM1', aircraftID: 'Airbus3' },
    {code: 'CB007', departure: 'Cần Thơ', destination: 'Vũng Tàu', date: '2023-12-31', arrivalTime: '2024-01-02', availableSeats: 115, price: 1150000, routeID: 'CTVT1', aircraftID: 'Boeing4' },
    {code: 'CB008', departure: 'Quy Nhơn', destination: 'Pleiku', date: '2024-01-01', arrivalTime: '2024-01-03', availableSeats: 125, price: 1250000, routeID: 'QNP1', aircraftID: 'Airbus4' },
    {code: 'CB009', departure: 'Cà Mau', destination: 'Bắc Ninh', date: '2024-01-02', arrivalTime: '2024-01-04', availableSeats: 105, price: 1050000, routeID: 'CMNB1', aircraftID: 'Boeing5' },
    {code: 'CB010', departure: 'Lào Cai', destination: 'Yên Bái', date: '2024-01-03', arrivalTime: '2024-01-05', availableSeats: 98, price: 980000, routeID: 'LCYB1', aircraftID: 'Airbus5' },
    {code: 'CB011', departure: 'Quảng Ngãi', destination: 'Quảng Bình', date: '2024-01-04', arrivalTime: '2024-01-06', availableSeats: 102, price: 1020000, routeID: 'QNGQB1', aircraftID: 'Boeing6' },
    {code: 'CB012', departure: 'Long Xuyên', destination: 'Tiền Giang', date: '2024-01-05', arrivalTime: '2024-01-07', availableSeats: 108, price: 1080000, routeID: 'LXTG1', aircraftID: 'Airbus6' },
    {code: 'CB013', departure: 'Hòa Bình', destination: 'Nam Định', date: '2024-01-06', arrivalTime: '2024-01-08', availableSeats: 94, price: 940000, routeID: 'HBN1', aircraftID: 'Boeing7' }
];

// Lặp qua dữ liệu chuyến bay và thêm vào bảng
var tableBody = document.querySelector('.list-flight tbody');

flightData.forEach(function (flight) {
    var row = tableBody.insertRow();
    row.insertCell(0).innerHTML = '<input type="radio" name="selectedFlight" value="' + flight.code + '">';
    row.insertCell(1).innerHTML = flight.code;
    row.insertCell(2).innerHTML = flight.departure;
    row.insertCell(3).innerHTML = flight.destination;
    row.insertCell(4).innerHTML = flight.date;
    row.insertCell(5).innerHTML = flight.arrivalTime;
    row.insertCell(6).innerHTML = flight.availableSeats;
    row.insertCell(7).innerHTML = flight.price;
    row.insertCell(8).innerHTML = flight.routeID;
    row.insertCell(9).innerHTML = flight.aircraftID;
    // Thêm các ô dữ liệu khác nếu cần
});

// Function to populate the flight dropdown
function populateFlightDropdown() {
    var dropdown = document.getElementById("searchFlightID");
    dropdown.innerHTML = ''; // Clear existing options

    for (var i = 0; i < flightData.length; i++) {
        var option = document.createElement("option");
        option.value = i;
        option.text = flightData[i].code;
        dropdown.add(option);
    }
}

// Function to delete the selected flight
// Function to delete the selected flight
function deleteSelectedFlight() {
    var selectedFlightIndex = document.getElementById("searchFlightID").value;

    // Check if the selected index is valid
    if (selectedFlightIndex >= 0 && selectedFlightIndex < flightData.length) {
        // Remove the selected flight from the array
        flightData.splice(selectedFlightIndex, 1);

        // Repopulate the dropdown list after deleting the flight
        populateFlightDropdown();

        // Clear the selected flight details in the table
        populateTable();
    } else {
        alert("Please select a valid flight to delete.");
    }
}


// Function to populate the table with flight details
function populateTable() {
    var table = document.getElementById("flightTable");
    table.innerHTML = ''; // Clear existing table

    // Add table headers
    var thead = table.createTHead();
    var headerRow = thead.insertRow();
    Object.keys(flightData[0]).forEach(function (key) {
        var th = document.createElement("th");
        th.appendChild(document.createTextNode(key));
        headerRow.appendChild(th);
    });

    // Add table body
    var tbody = table.createTBody();
    flightData.forEach(function (flight) {
        var row = tbody.insertRow();
        Object.values(flight).forEach(function (value) {
            var cell = row.insertCell();
            cell.appendChild(document.createTextNode(value));
        });
    });
}

// Call the function to populate flight dropdown options
populateFlightDropdown();

// Call the function to populate the table
populateTable();