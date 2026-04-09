import sqlite3
from datetime import datetime

from src.utils.formatting import separator
from src.models.sale import Sale, SaleItem
from src.database.connection import create_connection
from src.database.sale_queries import insert_sale, insert_saleitem
from src.utils.validate import num_validation, payment_method_validation
from src.database.product_queries import get_product_name_by_id, get_selling_price, product_id_exists, decrease_product_stock, get_product_stock

def make_sale():
    conn = create_connection()
    try:
        print("Write your sale specification: ")
        separator()
        payment_method = payment_method_validation(input("Payment_method: ").strip())
        while payment_method is None:
            payment_method = payment_method_validation(input("Payment_method: ").strip())
        sale_date = datetime.now().strftime("%H:%M:%S - %d/%m/%Y")

        sale = Sale(
            sale_date=sale_date,
            payment_method=payment_method
            )
        
        sale_id = insert_sale(sale, conn)

        separator()
        print("Now enter each product specification.")

        while True:
            separator()
            product_id = num_validation(input("Product Id: "))

            product = product_id_exists(product_id, conn)

            if product:
                product_name = get_product_name_by_id(product_id, conn)
                separator()
                print(f"Your product is {product_name}")
                is_correct = input("Type ENTER if your product is correct, else type anything: ")
                separator()
                if is_correct != "":
                    print("Try again.")
                    continue
            else:
                print("The product id doesn't exist. Try again!")
                continue

            unit_price = get_selling_price(product_id, conn)
            quantity = num_validation(input("Quantity: "))

            stock_quantity = get_product_stock(product_id, conn)
            
            if quantity > stock_quantity:
                print("Not enough stock. Try again.")
                continue

            sale_item = SaleItem(
                product_id=product_id,
                quantity=quantity,
                unit_price=unit_price,
                sale_id=sale_id
            )

            insert_saleitem(sale_item, conn)

            decrease_product_stock(
                product_id=product_id,
                quantity_to_remove=quantity,
                conn=conn)

            separator()

            more_products = input("Do you have more products in your sale?(y/n): ").lower()

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
        separator()
        print("Your sale has been made!")
    finally:
        conn.close()