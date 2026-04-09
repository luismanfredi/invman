import sqlite3
from datetime import datetime

from src.models.product import Product
from src.utils.formatting import separator
from src.database.connection import create_connection
from src.models.purchase import Purchase, PurchaseItem
from src.database.purchase_queries import insert_purchase, insert_purchaseitem
from src.utils.validate import num_validation, unit_type_validation, date_validation
from src.database.product_queries import get_product_id_by_name, increase_product_stock, insert_product, product_exists

def make_purchase():
    conn = create_connection()
    try:
        print("Write your purchase specification: ")
        separator()
        supplier_name = input("Supplier name: ").strip()
        purchase_date = datetime.now().strftime("%H:%M:%S - %d/%m/%Y")

        purchase = Purchase(
                supplier_name=supplier_name,
                purchase_date=purchase_date
                )
        
        purchase_id = insert_purchase(purchase, conn)

        while True:
            separator()
            print("Now enter each product specification:")
            separator()
            name = input("Name: ").strip()

            if product_exists(name, conn):
                print("The product already exists")
                product_id = get_product_id_by_name(name, conn)
                separator()
                quantity = num_validation(input("Quantity: "))
                increase_product_stock(product_id, quantity, conn)
            else:
                category = input("Category: ").strip()
                brand = input("Brand: ").strip()
                unit_type = unit_type_validation(input("Unit type: ").strip())
                min_stock = num_validation(input("Minimum stock: "))
                selling_price = num_validation(input("Selling price: "))
                quantity = num_validation(input("Quantity: "))
                product = Product(
                name=name,
                category=category,
                brand=brand,
                unit_type=unit_type,
                selling_price=selling_price,
                stock_quantity=0,
                min_stock=min_stock,
                )

                product_id = insert_product(product, conn)

                increase_product_stock(product_id, quantity, conn)
            
            
            unit_cost = num_validation(input("Unit cost: "))
            expiration_date = date_validation(input("Expiration date: "))

            
            purchase_item = PurchaseItem(
                quantity=quantity,
                unit_cost=unit_cost,
                expiration_date=expiration_date,
                product_id=product_id,
                purchase_id=purchase_id
            )

            insert_purchaseitem(purchase_item, conn)

            separator()
            more_products = input("Do you have more products in your purchase?(y/n): ").lower()

            if more_products == "yes" or more_products == "y":
                continue
            elif more_products == "no" or more_products == "n":
                break
            else:
                print("Invalid option. Ending purchase.")
                break

        conn.commit()
    except sqlite3.Error as e:
        print(f"Error: {e}")
        conn.rollback()
    else:
        separator()
        print("Purchase completed successfully!")
    finally:
        conn.close()