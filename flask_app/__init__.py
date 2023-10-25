from flask import Flask
from .blueprints.users import users
from datetime import datetime

app = Flask(__name__)

app.secret_key = "091cc8231ad5679fab233a2153538fa0d5877d6ebf1865aa621583b7999e6245"


@app.template_filter()
def format_date(date):
    """
    This is a custom template filter.
    It formats a date to "January 1, 2023", for example.
    """
    return date.strftime("%B %-d, %Y")


@app.template_filter()
def format_date_with_time(date):
    """
    This is a custom template filter.
    It formats a date to "January 1, 2023 at 12:00 am", for example.
    """
    return date.strftime("%B %-d, %Y at %-I:%M %p")


app.register_blueprint(users)
