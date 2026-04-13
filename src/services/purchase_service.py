import sqlite3
from datetime import datetime

from src.models.product import Product
from src.utils.formatting import separator
from src.database.connection import create_connection
from src.models.purchase import Purchase, PurchaseItem
from src.utils.validate import num_validation, unit_type_validation, date_validation
from src.database.purchase_queries import insert_purchase, insert_purchaseitem, show_purchases_table
from src.database.product_queries import get_product_id_by_name, increase_product_stock, insert_product, product_exists

def make_purchase():
    conn = create_connection()

    try:
        print("Write your purchase specification:")
        separator()
        supplier_name = input("Supplier name: ").strip()
        purchase_date = datetime.now().strftime("%H:%M:%S - %d/%m/%Y")

        purchase = Purchase(
                supplier_name=supplier_name,
                purchase_date=purchase_date
        )
        
        purchase_id = insert_purchase(purchase, conn)

        while True:
            product_id = get_or_create_product(conn)

            if product_id is None:
                print("Product step canceled.")
                separator()
                continue
            
            quantity = num_validation(input("Quantity: "))
            unit_cost = num_validation(input("Unit cost: "))
            expiration_date = date_validation(input("Expiration date: "))

            increase_product_stock(product_id, quantity, conn)

            
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

            if more_products in ["y", "yes"]:
                continue
            elif more_products in ["n", "no"]:
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

def get_or_create_product(conn):
    separator()
    name = input("Product name: ").strip().lower()

    if product_exists(name, conn):
        print("The product already exists.")
        separator()
        return get_product_id_by_name(name, conn)

    print("New product detected. Please enter product data:")
    separator()

    product = collect_new_product_data(name)

    if product is None:
        return None

    review_choice = review_product_data(product)

    if review_choice == "2":
        return get_or_create_product(conn)

    if review_choice == "3":
        return None

    return insert_product(product, conn)

def collect_new_product_data(name: str):
    category = input("Category: ").strip()
    brand = input("Brand: ").strip()
    unit_type = unit_type_validation(input("Unit type: ").strip())
    min_stock = num_validation(input("Minimum stock: "))
    selling_price = num_validation(input("Selling price: "))

    return Product(
        name=name,
        category=category,
        brand=brand,
        unit_type=unit_type,
        selling_price=selling_price,
        stock_quantity=0,
        min_stock=min_stock
    )

def review_product_data(product: Product):
    separator()
    print("Review product data:")
    print(
        f"1. Name: {product.name}\n"
        f"2. Category: {product.category}\n"
        f"3. Brand: {product.brand}\n"
        f"4. Unit type: {product.unit_type}\n"
        f"5. Minimum stock: {product.min_stock}\n"
        f"6. Selling price: {product.selling_price}"
    )
    separator()
    print(
        "1. Confirm\n"
        "2. Re-enter product data\n"
        "3. Cancel"
    )
    separator()

    while True:
        choice = input("Enter your choice: ").strip()

        if choice in ["1", "2", "3"]:
            return choice

        print(f"{choice} is not a valid option. Try again!")
        separator()


def show_purchases():
    conn = create_connection()
    try:
        show_purchases_table(conn)
    except sqlite3.Error as e:
        separator()
        print(f"Error: {e}")
    finally:
        conn.close()