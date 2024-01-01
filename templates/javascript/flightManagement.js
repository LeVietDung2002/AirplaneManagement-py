// flightManagement.js

$(document).ready(function () {
    // Load existing flight data when the page loads
    loadFlightData();
    populateDeleteDropdown(); // Load dropdown data

    // Event handlers
    $('#addFlightButton').click(addFlight);
    $('#deleteFlightButton').click(deleteFlight);

    // Function to add a flight
    function addFlight() {
        var flightCode = $('#flight_code').val();
        var departure = $('#departure').val();
        var destination = $('#destination').val();
        var departureDate = $('#departure_date').val();

        $.ajax({
            url: '/add_flight',
            method: 'POST',
            data: {
                flight_code: flightCode,
                departure: departure,
                destination: destination,
                departure_date: departureDate
            },
            success: function (response) {
                console.log(response.message);
                loadFlightData(); // Reload the flight data after adding
            },
            error: function (error) {
                console.error('Error adding flight:', error);
            }
        });
    }

    // Function to delete a flight
    function deleteFlight() {
        var selectedFlightCode = $('#delete_flight_code').val();

        $.ajax({
            url: '/delete_flight',
            method: 'POST',
            data: {
                flight_code: selectedFlightCode
            },
            success: function (response) {
                console.log(response.message);
                loadFlightData(); // Reload the flight data after deleting
            },
            error: function (error) {
                console.error('Error deleting flight:', error);
            }
        });
    }

    // Function to load flight data from the server
    function loadFlightData() {
        $.ajax({
            url: '/get_flights',
            method: 'GET',
            success: function (response) {
                // Populate the flight table with the received data
                populateFlightTable(response.flights);
            },
            error: function (error) {
                console.error('Error retrieving flight data:', error);
            }
        });
    }

    // Function to populate the flight table body with data
    function populateFlightTable(flights) {
        var tableBody = $('#flightTableBody');
        tableBody.empty(); // Clear existing data

        flights.forEach(function (flight) {
            var row = $('<tr></tr>');
            row.append($('<td></td>').text(flight.flight_code));
            row.append($('<td></td>').text(flight.departure));
            row.append($('<td></td>').text(flight.destination));
            row.append($('<td></td>').text(flight.departure_date));

            tableBody.append(row);
        });
    }

    // Function to populate the delete dropdown
    function populateDeleteDropdown() {
        var dropdown = $('#delete_flight_code');
        $.ajax({
            url: '/get_flight_codes',
            method: 'GET',
            success: function (response) {
                dropdown.empty();
                response.flight_codes.forEach(function (code) {
                    dropdown.append($('<option></option>').attr('value', code).text(code));
                });
            },
            error: function (error) {
                console.error('Error retrieving flight codes:', error);
            }
        });
    }
});
