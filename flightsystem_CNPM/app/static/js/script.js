
    // Định nghĩa dữ liệu chuyến bay từ server
 var flightData = [
    { code: 'CB001', departure: 'TPHCM', destination: 'Hà Nội', date: '2023-12-25',price: 1000000, routeID: 'HNVT1', aircraftID: 'Boeing1' },
    { code: 'CB002', departure: 'Đà Nẵng', destination: 'Nha Trang', date: '2023-12-26', price: 1200000, routeID: 'DNNT1', aircraftID: 'Airbus1' },
    { code: 'CB003', departure: 'Hà Nội', destination: 'Đà Lạt', date: '2023-12-27', price: 1500000, routeID: 'HNDL1', aircraftID: 'Boeing2' },
    { code: 'CB004', departure: 'Hải Phòng', destination: 'Đồng Hới', date: '2023-12-28', price: 1100000, routeID: 'HPDH1', aircraftID: 'Airbus2' },
    { code: 'CB005', departure: 'Nha Trang', destination: 'Phú Quốc', date: '2023-12-29', price: 1300000, routeID: 'NTPQ1', aircraftID: 'Boeing3' },
    { code: 'CB006', departure: 'Huế', destination: 'Buôn Ma Thuột', date: '2023-12-30', price: 950000, routeID: 'HBM1', aircraftID: 'Airbus3' },
    { code: 'CB007', departure: 'Cần Thơ', destination: 'Vũng Tàu', date: '2023-12-31', price: 1150000, routeID: 'CTVT1', aircraftID: 'Boeing4' },
    { code: 'CB008', departure: 'Quy Nhơn', destination: 'Pleiku', date: '2024-01-01', price: 1250000, routeID: 'QNP1', aircraftID: 'Airbus4' },
    { code: 'CB009', departure: 'Cà Mau', destination: 'Bắc Ninh', date: '2024-01-02', price: 1050000, routeID: 'CMNB1', aircraftID: 'Boeing5' },
    { code: 'CB010', departure: 'Lào Cai', destination: 'Yên Bái', date: '2024-01-03', price: 980000, routeID: 'LCYB1', aircraftID: 'Airbus5' },
    { code: 'CB011', departure: 'Quảng Ngãi', destination: 'Quảng Bình', date: '2024-01-04', price: 1020000, routeID: 'QNGQB1', aircraftID: 'Boeing6' },
    { code: 'CB012', departure: 'Long Xuyên', destination: 'Tiền Giang', date: '2024-01-05', price: 1080000, routeID: 'LXTG1', aircraftID: 'Airbus6' },
    { code: 'CB013', departure: 'Hòa Bình', destination: 'Nam Định', date: '2024-01-06', price: 940000, routeID: 'HBN1', aircraftID: 'Boeing7' }
];


// Lặp qua dữ liệu chuyến bay và thêm vào bảng
var tableBody = document.querySelector('.list-flight tbody');

flightData.forEach(function(flight) {
    var row = tableBody.insertRow();
    row.insertCell(0).innerHTML = '<input type="radio" name="selectedFlight" value="' + flight.code + '">';
    row.insertCell(1).innerHTML = flight.code;
    row.insertCell(2).innerHTML = flight.departure;
    row.insertCell(3).innerHTML = flight.destination;
    row.insertCell(4).innerHTML = flight.date;
    row.insertCell(5).innerHTML = flight.price;
    row.insertCell(6).innerHTML = flight.routeID;
    row.insertCell(7).innerHTML = flight.aircraftID;
    // Thêm các ô dữ liệu khác nếu cần
});

// Function to populate select options
function populateSelectOptions(selectId, cities) {
    var select = document.getElementById(selectId);
    select.innerHTML = '';

    cities.forEach(function (city) {
        var option = document.createElement('option');
        option.value = city;
        option.text = city;
        select.appendChild(option);
    });
}

// Function to initialize the select boxes
function initializeSelectBoxes() {
    var uniqueDepartures = Array.from(new Set(flightData.map(flight => flight.departure)));
    var uniqueDestinations = Array.from(new Set(flightData.map(flight => flight.destination)));

    populateSelectOptions('from', uniqueDepartures);
    populateSelectOptions('to', uniqueDestinations);
}

// Call the initializeSelectBoxes function when the page loads
window.onload = function () {
    initializeSelectBoxes();
};

function searchFlights() {
    var fromDropdown = document.getElementById('from');
    var toDropdown = document.getElementById('to');
    var dateInput = document.getElementById('date').value;

    // Extract city names from the dropdown values
    var from = fromDropdown.value;
    var to = toDropdown.value;

    // Convert date input to 'YYYY-MM-DD' format
    var date = new Date(dateInput);
    var formattedDate = date.toISOString().split('T')[0];

    // Thực hiện tìm kiếm chuyến bay dựa vào giá trị from, to, date
    var searchResults = flightData.filter(function (flight) {
        return flight.departure.toLowerCase() === from.toLowerCase() &&
            flight.destination.toLowerCase() === to.toLowerCase() &&
            flight.date === formattedDate;
    });

    // Hiển thị kết quả tìm kiếm trong bảng
    displaySearchResults(searchResults);
}

// Function to populate the table with flight details
function populateTable() {
    const tableBody = document.getElementById("flightTable").getElementsByTagName('tbody')[0];

    // Clear existing rows
    tableBody.innerHTML = '';

    // Loop through the flightDetails array and create a row for each entry
    flightDetails.forEach((flight) => {
        const row = tableBody.insertRow();
        Object.values(flight).forEach((value) => {
            const cell = row.insertCell();
            cell.textContent = value;
        });
    });
}
function populateFlightSelect() {
    var select = document.getElementById('searchFlightID');

    flightData.forEach(function (flight) {
        var option = document.createElement('option');
        option.value = flight.code;
        option.text = flight.code + ' - ' + flight.departure + ' to ' + flight.destination;
        select.appendChild(option);
    });
}

// Call the function to populate flight select options
populateFlightSelect();
// Function to delete a flight by flightID
function deleteFlight(code) {
    const indexToDelete = flightData.findIndex(flight => flight.code === code);

    if (indexToDelete !== -1) {
        flightData.splice(indexToDelete, 1);
        populateTable(); // Update the table after deletion
    }
}
function deleteSelectedFlight() {
    var selectedFlightCode = document.querySelector('input[name="selectedFlight"]:checked');

    if (selectedFlightCode) {
        var flightCode = selectedFlightCode.value;
        deleteFlight(flightCode);
    } else {
        alert('Please select a flight to delete.');
    }
}

function displaySearchResults(results) {
    var tableBody = document.querySelector('.list-flight tbody');
    tableBody.innerHTML = '';

    results.forEach(function (flight) {
        var row = tableBody.insertRow();
        row.insertCell(0).innerHTML = '<input type="radio" name="selectedFlight" value="' + flight.code + '">';
        row.insertCell(1).innerHTML = flight.code;
        row.insertCell(2).innerHTML = flight.departure;
        row.insertCell(3).innerHTML = flight.destination;
        row.insertCell(4).innerHTML = flight.date;
        row.insertCell(5).innerHTML = flight.price;
        row.insertCell(6).innerHTML = flight.routeID;
        row.insertCell(7).innerHTML = flight.aircraftID;
        // Thêm cột giá vào bảng
        // Thêm các ô dữ liệu khác nếu cần
    });
}

// Sample passenger data
var passengerData = [
    { customerID: 'CUST003', name: 'Nguyễn Văn A', email: 'nguyenvana@example.com', phone: '098-765-4321', address: '789 Tran Phu, Hanoi' },
    { customerID: 'CUST004', name: 'Trần Thị B', email: 'tranthib@example.com', phone: '012-345-6789', address: '456 Le Loi, Ho Chi Minh City' },
    { customerID: 'CUST005', name: 'Phạm Văn C', email: 'phamvanc@example.com', phone: '090-123-4567', address: '123 Nguyen Hue, Da Nang' },
    { customerID: 'CUST006', name: 'Lê Thị D', email: 'lethid@example.com', phone: '097-654-3210', address: '567 Vo Van Kiet, Can Tho' },
    // Add more passenger data as needed
];

// Function to populate passenger select options
function populatePassengerSelect() {
    var select = document.getElementById('passengerSelect');

    passengerData.forEach(function (passenger) {
        var option = document.createElement('option');
        option.value = passenger.customerID;
        option.text = passenger.name;
        select.appendChild(option);
    });
}

// Function to display selected passenger in the table
function displaySelectedPassenger() {
    var selectedCustomerId = document.getElementById('passengerSelect').value;

    // Find the selected passenger from the data
    var selectedPassenger = passengerData.find(function (passenger) {
        return passenger.customerID === selectedCustomerId;
    });

    // Display the selected passenger in the table
    var tableBody = document.getElementById('passengerTableBody');
    tableBody.innerHTML = '';

    var row = tableBody.insertRow();
    row.insertCell(0).innerHTML = selectedPassenger.customerID;
    row.insertCell(1).innerHTML = selectedPassenger.name;
    row.insertCell(2).innerHTML = selectedPassenger.email;
    row.insertCell(3).innerHTML = selectedPassenger.phone;
    row.insertCell(4).innerHTML = selectedPassenger.address;
}

// Call the function to populate passenger select options
populatePassengerSelect();
