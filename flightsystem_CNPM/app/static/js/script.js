
    // Định nghĩa dữ liệu chuyến bay từ server
   var flightData = [
    { code: 'CB001', departure: 'TPHCM', destination: 'Hà Nội', date: '2023-12-25', price: 1000000 },
    { code: 'CB002', departure: 'Đà Nẵng', destination: 'Nha Trang', date: '2023-12-26', price: 1200000 },
    { code: 'CB003', departure: 'Hà Nội', destination: 'Đà Lạt', date: '2023-12-27', price: 1500000 },
     { code: 'CB004', departure: 'Hải Phòng', destination: 'Đồng Hới', date: '2023-12-28', price: 1100000 },
    { code: 'CB005', departure: 'Nha Trang', destination: 'Phú Quốc', date: '2023-12-29', price: 1300000 },
    { code: 'CB006', departure: 'Huế', destination: 'Buôn Ma Thuột', date: '2023-12-30', price: 950000 },
    { code: 'CB007', departure: 'Cần Thơ', destination: 'Vũng Tàu', date: '2023-12-31', price: 1150000 },
    { code: 'CB008', departure: 'Quy Nhơn', destination: 'Pleiku', date: '2024-01-01', price: 1250000 },
    { code: 'CB009', departure: 'Cà Mau', destination: 'Bắc Ninh', date: '2024-01-02', price: 1050000 },
    { code: 'CB010', departure: 'Lào Cai', destination: 'Yên Bái', date: '2024-01-03', price: 980000 },
    { code: 'CB011', departure: 'Quảng Ngãi', destination: 'Quảng Bình', date: '2024-01-04', price: 1020000 },
    { code: 'CB012', departure: 'Long Xuyên', destination: 'Tiền Giang', date: '2024-01-05', price: 1080000 },
    { code: 'CB013', departure: 'Hòa Bình', destination: 'Nam Định', date: '2024-01-06', price: 940000 }
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
            row.insertCell(5).innerHTML = flight.price; // Thêm cột giá vào bảng
            // Thêm các ô dữ liệu khác nếu cần
        });
    }


