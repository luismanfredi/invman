import sqlite3
from pathlib import Path

from src.models.product import Product

PROJECT_ROOT = Path(__file__).resolve().parents[2]
db_path = PROJECT_ROOT / "inventory.db"

def create_connection():
    return sqlite3.connect(db_path)

def create_product_table():
    conn = create_connection()
    c = conn.cursor()

    c.execute(""" 
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            category TEXT,
            brand TEXT,
            quantity REAL,
            min_stock REAL,
            expiration_date TEXT
        )""") # ADICIONAR QUANTITY_TYPE

    conn.commit()
    conn.close()

def insert_product(product: Product):
    conn = create_connection()
    c = conn.cursor()

    c.execute("""
        INSERT INTO products (name, category, brand, quantity, min_stock,expiration_date)
        VALUES (?, ?, ?, ?, ?, ?)
        """, (product.name, product.category, product.brand, product.quantity, product.min_stock, product.expiration_date))
    
    # TIRAR DISTRIBUIDOR, INSERIR MINIMO DE ESTOQUE NÉ

    conn.commit()
    conn.close()

def show_products():
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

# TABLE: PURCHASES (ID, NAME, COST, DISTRIBUTOR, QUANTITY, PURCHASE DATA)
# TABLE: SALES (ID, NAME, PRICE, QUANTITY, PROFIT)

def initialize_database():
    create_connection()
    create_product_table()