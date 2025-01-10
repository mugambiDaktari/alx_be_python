import datetime
from datetime import timedelta

current_date = datetime.datetime.now()

def display_current_datetime():
    formatted_current_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(formatted_current_date)

display_current_datetime()

daysToAdd = int(input("Enter the number of days to add to the current date: "))

def calculate_future_date():
    future_date = current_date + timedelta(days = daysToAdd)
    formatedFutureDate = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatedFutureDate}")

calculate_future_date()