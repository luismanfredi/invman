import sqlite3

from src.models.product import Product
from src.utils.formatting import separator
from src.database.connection import create_connection
from src.utils.validate import num_validation, unit_type_validation
from src.database.product_queries import insert_product, show_products_table, product_exists

def register_product():
    conn = create_connection()
    try:
        print("Please write your product specifications:")
        separator()
        name = input("Name: ").lower().strip()
        if product_exists(name, conn):
            separator()
            print("The product already exists. Use Register Purchase to add stock.")
        else:
            category = input("Category: ").strip()
            brand = input("Brand: ").strip()
            unit_type = unit_type_validation(input("Unit type: ").strip())
            stock_quantity = num_validation(input("Stock quantity: "))
            min_stock = num_validation(input("Minimum stock: "))
            selling_price = num_validation(input("Selling price: "))
            product = Product(
                name=name,
                category=category,
                brand=brand,
                unit_type=unit_type,
                selling_price=selling_price,
                stock_quantity=stock_quantity,
                min_stock=min_stock,
                )
            
            insert_product(product, conn)
        conn.commit()
    except sqlite3.Error as e:
        separator()
        print(f"Error: {e}")
        conn.rollback()
    else:
        separator()
        print("Product registered successfully!")
    finally:
        conn.close()

def show_products():
    conn = create_connection()
    try:
        show_products_table(conn)
    except sqlite3.Error as e:
        separator()
        print(f"Error: {e}")
    finally:
        conn.close()
    