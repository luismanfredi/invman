from src.models.product import Product
from src.database.connection import create_connection

def insert_product(product: Product):
    conn = create_connection()
    c = conn.cursor()

    c.execute("""
        INSERT INTO products (name, category, brand, unit_type, stock_quantity, min_stock, selling_price)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            product.name, 
            product.category, 
            product.brand, 
            product.unit_type, 
            product.stock_quantity, 
            product.min_stock, 
            product.selling_price))

    conn.commit()
    conn.close()

def show_products_table():
    conn = create_connection()
    c = conn.cursor()

    c.execute("SELECT * FROM products")
    rows = c.fetchall()

    if not rows:
        print("Inventory is empty")
        return

    for row in rows:
        print(row)

    conn.close()