import sqlite3
from datetime import datetime

from src.utils.formatting import separator
from src.models.sale import Sale, SaleItem
from src.database.connection import create_connection
from src.database.sale_queries import insert_sale, insert_saleitem, show_sales_table
from src.utils.validate import num_validation, payment_method_validation, id_validation
from src.database.product_queries import (
    get_product_name_by_id,
    get_selling_price,
    product_id_exists,
    decrease_product_stock,
    get_product_stock,
)


def make_sale():
    conn = create_connection()
    sales = 0
    try:
        print("Write your sale specification: ")
        separator()
        payment_method = payment_method_validation(input("Payment method: ").strip())
        while payment_method is None:
            payment_method = payment_method_validation(
                input("Payment method: ").strip()
            )
        sale_date = datetime.now().strftime("%H:%M:%S - %d/%m/%Y")

        sale = Sale(sale_date=sale_date, payment_method=payment_method)

        separator()
        print("Now enter each product specification.")

        while True:
            separator()
            product_id = id_validation(input("Product Id: "))

            product = product_id_exists(product_id, conn)

            if product:
                product_name = get_product_name_by_id(product_id, conn)
                separator()
                print(f"Your product is {product_name}")
                is_correct = input("Confirm product?(y/n) ").lower()
                separator()
                if is_correct in ["y", "yes"]:
                    pass
                elif is_correct in ["n", "no"]:
                    print("Try again.")
                    continue
                else:
                    print("Invalid command.")
                    break
            else:
                print("The product id doesn't exist. Try again!")
                continue

            unit_price = get_selling_price(product_id, conn)
            quantity = num_validation(input("Quantity: "))

            stock_quantity = get_product_stock(product_id, conn)

            if quantity > stock_quantity:
                print("Not enough stock. Try again.")
                continue

            if sales == 0:
                sale_id = insert_sale(sale, conn)

            sale_item = SaleItem(
                product_id=product_id,
                quantity=quantity,
                unit_price=unit_price,
                sale_id=sale_id,
            )

            insert_saleitem(sale_item, conn)

            decrease_product_stock(
                product_id=product_id, quantity_to_remove=quantity, conn=conn
            )

            separator()

            sales += 1
            more_products = (
                input("Do you have more products in your sale?(y/n): ").strip().lower()
            )

            if more_products == "yes" or more_products == "y":
                continue
            elif more_products == "no" or more_products == "n":
                break
            else:
                print("Invalid option. Ending sale.")
                break

        conn.commit()
    except sqlite3.Error as e:
        separator()
        print(f"Error: {e}")
        conn.rollback()
    else:
        if sales > 0:
            separator()
            print("Sale completed successfully!")
    finally:
        conn.close()


def show_sales():
    conn = create_connection()
    try:
        show_sales_table(conn)
    except sqlite3.Error as e:
        separator()
        print(f"Error: {e}")
    finally:
        conn.close()
