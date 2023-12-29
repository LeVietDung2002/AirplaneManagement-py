from flask import Flask, render_template, request, redirect, url_for, jsonify
import sqlite3
from sqlalchemy import ForeignKey

from models import db, FlightDetail  # Import your models

flightapp = Flask(__name__)

flightapp.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/Admin/Desktop/FlightManagement/flightsystem_CNPM/app/database/flightManagement.db'
flightapp.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db.init_app(flightapp)

# Duong dan den trang chu
@flightapp.route("/")
def home():
    return render_template("home.html")

# Duong dan den trang dang nhap
@flightapp.route("/login")
def login():
    return render_template("login.html")

# Duong dan den trang dat ve
@flightapp.route("/booktickets")
def booktickets():
    return render_template("booktickets.html")

# Duong dan den trang ban ve
@flightapp.route("/sellticket", methods=["GET", "POST"])
def sellticket():
    if request.method == "POST":
        # Process the form data here
        # For example, you can access form values using request.form['fieldname']
        # Implement your logic for selling tickets

        # Redirect to a success page or home page after form submission
        return redirect(url_for('home'))

    # Render the sellticket.html template
    return render_template("sellticket.html")
@flightapp.route("/ScheduleManagement")
def ScheduleManagement():

    return render_template("ScheduleManagement.html")

@flightapp.route("/flightManagement")
def flightManagement():
    # Fetch data from the database
    flights = FlightDetail.query.all()

    # Pass the data to the template
    return render_template("flightManagement.html", flights=flights)

@flightapp.route("/reportRevenue")
def reportRevenue():
    return render_template("reportRevenue.html")




if __name__ == '__main__':
    flightapp.run(debug=True)
