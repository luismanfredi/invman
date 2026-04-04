from datetime import datetime

from src.models.product import Product
from src.utils.formatting import fmt, separator
from src.models.purchase import Purchase, PurchaseItem
from src.utils.validate import num_validation, unit_type_validation, date_validation
from src.database.purchase_queries import insert_purchase, product_exists, insert_purchaseitem
from src.database.product_queries import get_product_id_by_name, update_product_stock, insert_product

def make_purchase():
    print("Write your purchase especification: ")
    separator()
    supplier_name = input("Supplier name: ").strip()
    purchase_date = datetime.now().strftime("%H:%M:%S - %d/%m/%Y")

    purchase = Purchase(
            supplier_name=supplier_name,
            purchase_data=purchase_date
            )
    
    purchase_id = insert_purchase(purchase)

    while True:
        separator()
        print("Now enter each product especification.")
        separator()
        name = input("Name: ").strip()

        if product_exists(name):
            print("The product already exists")
            product_id = get_product_id_by_name(name)
            separator()
            quantity = num_validation(("Quantity"))
            update_product_stock(product_id, quantity)
        else:
            category = input("Category: ").strip()
            brand = input("Brand: ").strip()
            unit_type = unit_type_validation(input("Unit type: ").strip())
            min_stock = num_validation(("Minimum stock").strip())
            selling_price = num_validation(("Selling price").strip())
            quantity = num_validation(("Quantity"))
            product = Product(
            name=name,
            category=category,
            brand=brand,
            unit_type=unit_type,
            selling_price=selling_price,
            stock_quantity=0,
            min_stock=min_stock,
            )

            product_id = insert_product(product)

            update_product_stock(product_id, quantity)
        
        
        unit_cost = num_validation("Unit cost")
        expiration_date = date_validation(input("Expiration_date: "))

        
        purchase_item = PurchaseItem(
            quantity=quantity,
            unit_cost=unit_cost,
            expiration_date=expiration_date,
            product_id=product_id,
            purchase_id=purchase_id
        )

        insert_purchaseitem(purchase_item)

        separator()
        more_products = input("Do you have more products in your purchase?(y/n): ").lower()

        if more_products == "yes" or more_products == "y":
            continue
        elif more_products == "no" or more_products == "n":
            break
        else:
            print("Invalid option. Ending purchase.")
            break

    separator()
    print("Your purchase have been made")