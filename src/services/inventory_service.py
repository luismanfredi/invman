from datetime import datetime

from src.models.product import Product
from src.models.category import Category
from src.utils.formatting import separator
from src.database.connection import insert_product
from src.utils.validate import num_validation, date_validation, quantity_type_validation

def create_product():
    print("Please write your product specifications")
    separator()
    name = input("Name: ")
    cost_price = num_validation("Cost price")
    sale_price = num_validation("Sale price")
    category = str(Category(input("Category: ")))
    distributor = input("Distributor: ")
    brand = input("Brand: ")
    quantity_type = quantity_type_validation(input("Quantity type (Un/Kg): "))
    quantity = num_validation("Quantity")
    min_stock = num_validation("Minimum stock")
    expiration_date = date_validation(input("Expiration Date ('Enter' if product doesn't have expiration date): "))
    product_ = Product( # product1 just demonstration of one item...
                1, # id still needs change...
                name, 
                cost_price, 
                sale_price,
                category,
                distributor, 
                brand,
                quantity_type, 
                quantity,
                min_stock,
                datetime.now().strftime("%d/%m/%y - %H:%M"), # Product register time
                expiration_date
                )
    
    insert_product(product_)