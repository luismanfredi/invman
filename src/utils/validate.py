import re
from datetime import datetime

from src.utils.formatting import fmt

def num_validation(variable_name: str) -> float | int:
    while True:
        try:
            num = float(input(f"{variable_name}: "))
            if num >= 0:
                return fmt(num)
            print(f"Your {variable_name.lower()} needs to be greater than or equal zero.")
        except ValueError:
            print("Enter a valid number")

def date_validation(date: str) -> str:
    while True:
        if not re.fullmatch(r'\d{2}/\d{2}/\d{2}', date):
            print("Invalid format! Use: DD/MM/YY")
        else:
            try:
                data = datetime.strptime(date, "%d/%m/%y")
                return data.strftime('%d/%m/%y')
            except ValueError:
                print("Invalid date! This date does not exist.")
        date = input("Insert the date again: ")

def unit_type_validation(quantity_type: str) -> str:
   while True:
        type_ = quantity_type.lower()
        if type_ == "kg":
            return "Kg"
        elif type_ == "un":
            return "Un"
        print("This is not a valid quantity type! Use Kg or Un")
        quantity_type = input("Insert the quantity type again: ")

def payment_method_validation(payment_method: str):
    methods_available = ["debit card", "credit card", "cash"]

    if payment_method.lower() not in methods_available:
        print("Payment not available. Use a Debit Card, Credit Card or Cash")
        return None
    else:
        return payment_method