from src.models.product import Product
from src.utils.formatting import separator
from src.utils.validate import num_validation, unit_type_validation
from src.database.product_queries import insert_product, show_products_table, product_exists

def register_product():
    print("Please write your product specifications:")
    separator()
    name = input("Name: ").lower().strip()
    if product_exists(name):
        separator()
        print("The product already exists. Use Register Purchase to add stock.")
    else:
        category = input("Category: ").strip()
        brand = input("Brand: ").strip()
        unit_type = unit_type_validation(input("Unit type: ").strip())
        stock_quantity = num_validation(("Stock quantity"))
        min_stock = num_validation(("Minimum stock").strip())
        selling_price = num_validation(("Selling price").strip())
        product = Product(
            name=name,
            category=category,
            brand=brand,
            unit_type=unit_type,
            selling_price=selling_price,
            stock_quantity=stock_quantity,
            min_stock=min_stock,
            )
        
        insert_product(product)

        separator()
        print("Product registered successfully!")

def show_products():
    show_products_table()