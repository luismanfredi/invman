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
            distributor TEXT,
            brand TEXT,
            quantity REAL,
            expiration_date TEXT
        )""") # ADICIONAR QUANTITY_TYPE

    conn.commit()
    conn.close()

def insert_product(product: Product):
    conn = create_connection()
    c = conn.cursor()

    c.execute("""
        INSERT INTO products (name, category, distributor, brand, quantity, expiration_date)
        VALUES (?, ?, ?, ?, ?, ?)
        """, (product.name, product.category, product.distributor, product.brand, product.quantity, product.expiration_date))
    
    conn.commit()
    conn.close()

def show_products():
    conn = create_connection()
    c = conn.cursor()

    c.execute("SELECT * FROM products")
    rows = c.fetchall()

    for row in rows:
        print(row)

    conn.close()