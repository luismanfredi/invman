from src.models.product import Product
from src.database.connection import create_connection

def insert_product(product: Product, conn):
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

    product_id = c.lastrowid 

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

def product_exists(name: str, conn) -> bool:
    c = conn.cursor()

    c.execute("""
        SELECT 1 FROM products
        WHERE name = ?
        LIMIT 1
    """, (name,))

    result = c.fetchone()

    return result is not None

def increase_product_stock(product_id, quantity_to_add, conn):
    c = conn.cursor()
    
    c.execute("""
        UPDATE products
        SET stock_quantity = stock_quantity + ?
        WHERE id = ?
    """, (quantity_to_add, product_id))

def decrease_product_stock(product_id, quantity_to_remove, conn):
    c = conn.cursor()

    c.execute("""
        UPDATE products
        SET stock_quantity = stock_quantity - ?
        WHERE id = ?          
    """, (quantity_to_remove, product_id))

def get_product_id_by_name(name: str, conn):
    c = conn.cursor()

    c.execute("""
        SELECT id FROM products
        WHERE LOWER(name) = LOWER(?)
        LIMIT 1
    """, (name,))
    
    result = c.fetchone()

    return None if result is None else result[0]

def get_product_name_by_id(product_id, conn):
    c = conn.cursor()

    c.execute("""
        SELECT name FROM products
        WHERE id = ?
        LIMIT 1
    """, (product_id,))

    result = c.fetchone()

    if result is None:
        return None

    return result[0]

def product_id_exists(product_id, conn):
    c = conn.cursor()

    c.execute("""
        SELECT 1 FROM products
        WHERE id = ?
        LIMIT 1
    """, (product_id,))

    result = c.fetchone()

    return result is not None

def get_selling_price(product_id, conn):
    c = conn.cursor()

    c.execute("""
        SELECT selling_price FROM products
        WHERE id = ?
        LIMIT 1
    """, (product_id,))

    result = c.fetchone()

    if result is None:
        return None

    return result[0]

def get_product_stock(product_id, conn):
    c = conn.cursor()

    c.execute("""
        SELECT stock_quantity FROM products
        WHERE id = ?
        LIMIT 1
    """, (product_id,))

    result = c.fetchone()

    if result is None:
        return None
    
    return result[0]