
from flask import Flask, render_template
import otp_module

app = Flask(__name__)


# Home Route

@app.route("/")

def home():

    return render_template("home.html")


@app.route("/about")

def about():

    return render_template("about.html")


# Contact Page

@app.route("/contact")

def contact():

    return "<h2>Contact us : chanduneduri7273@gmail.com</h2>"


# Dashboard Page

@app.route("/dashboard")

def dashboard():

    return "<h2>Welcome to Dashboard</h2>"


# Generate OTP

@app.route("/generate_otp")

def generate_otp():

    otp = otp_module.generate_otp()

    return f"<h2>Your OTP is : {otp}</h2>"


# Dynamic URL

@app.route("/user/<name>")

def user(name):

    return f"<h2>Welcome {name}</h2>"


app.run(debug=True)