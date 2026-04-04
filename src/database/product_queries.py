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
    product_id = c.lastrowid
    conn.close()

    return product_id

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

def update_product_stock(product_id, quantity_to_add):
    conn = create_connection()
    c = conn.cursor()
    
    c.execute("""
        UPDATE products
        SET stock_quantity = stock_quantity + ?
        WHERE id = ?
    """, (quantity_to_add, product_id))

    conn.commit()
    conn.close()

def get_product_id_by_name(name: str):
    conn = create_connection()
    c = conn.cursor()

    c.execute("""
        SELECT id FROM products
        WHERE LOWER(name) = LOWER(?)
        LIMIT 1
    """, (name,))
    
    result = c.fetchone()
    conn.close()

    return None if result is None else result[0]