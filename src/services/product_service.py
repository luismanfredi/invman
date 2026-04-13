import sqlite3

from src.models.product import Product
from src.utils.formatting import separator
from src.database.connection import create_connection
from src.utils.validate import num_validation, unit_type_validation
from src.database.product_queries import (
    insert_product,
    show_products_table,
    product_exists,
)


def register_product():
    while True:
        product = collect_product_data()

        if product is None:
            separator()
            print("The product already exists. Use Register Purchase to add stock.")
            return

        review_choice = review_product_data(product)

        if review_choice == "2":
            print("Let's try again.")
            separator()
            continue

        if review_choice == "3":
            print("Product registration canceled.")
            return

        conn = None
        try:
            conn = create_connection()

            insert_product(product, conn)
            conn.commit()

        except sqlite3.Error as e:
            if conn:
                conn.rollback()
            separator()
            print(f"Error: {e}")
        else:
            separator()
            print("Product registered successfully!")
        finally:
            if conn:
                conn.close()

        return


def collect_product_data():
    print("Please write your product specifications:")
    separator()
    name = input("Name: ").lower().strip()
    if product_already_exists(name):
        return
    category = input("Category: ").strip()
    brand = input("Brand: ").strip()
    unit_type = unit_type_validation(input("Unit type: ").strip())
    stock_quantity = num_validation(input("Stock quantity: "))
    min_stock = num_validation(input("Minimum stock: "))
    selling_price = num_validation(input("Selling price: "))

    return Product(
        name=name,
        category=category,
        brand=brand,
        unit_type=unit_type,
        selling_price=selling_price,
        stock_quantity=stock_quantity,
        min_stock=min_stock,
    )


def product_already_exists(name: str):
    conn = create_connection()
    try:
        if product_exists(name, conn):
            return True
        else:
            return False
    except sqlite3.Error as e:
        separator()
        print(f"Error: {e}")
        return True
    finally:
        conn.close()


def review_product_data(product: Product):
    separator()
    print("Review product data:")
    print(
        f"1. Name: {product.name}\n"
        f"2. Category: {product.category}\n"
        f"3. Brand: {product.brand}\n"
        f"4. Unit type: {product.unit_type}\n"
        f"5. Stock quantity: {product.stock_quantity}\n"
        f"6. Minimum Stock: {product.min_stock}\n"
        f"7. Selling price: {product.selling_price}"
    )
    separator()
    print("1. Confirm\n" "2. Re-enter product data\n" "3. Cancel")
    separator()

    while True:
        choice = input("Enter your choice: ").strip()

        if choice in ["1", "2", "3"]:
            return choice

        print(f"{choice} is not a valid option. Try again!")
        separator()


def show_products():
    conn = create_connection()
    try:
        show_products_table(conn)
    except sqlite3.Error as e:
        separator()
        print(f"Error: {e}")
    finally:
        conn.close()
