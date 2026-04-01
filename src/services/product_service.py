from src.models.product import Product
from src.utils.formatting import separator
from src.utils.validate import num_validation, unit_type_validation
from src.database.product_queries import insert_product, show_products_table

def register_product():
    print("Please write your product specifications")
    separator()
    name = input("Name: ").strip()
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
    print("Product registeres successfully")

def show_products():
    show_products_table()