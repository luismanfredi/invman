from src.database.connection import create_connection

def create_product_table():
    conn = create_connection()
    c = conn.cursor()

    c.execute(""" 
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            brand TEXT NOT NULL,
            unit_type TEXT NOT NULL,
            stock_quantity REAL NOT NULL DEFAULT 0,
            min_stock REAL NOT NULL DEFAULT 0,
            selling_price REAL NOT NULL
        )""") 

    conn.commit()
    conn.close()

def create_purchase_table():
    conn = create_connection()
    c = conn.cursor()

    c.execute(""" 
        CREATE TABLE IF NOT EXISTS purchases (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            supplier_name TEXT NOT NULL,
            purchase_date TEXT NOT NULL
        )""")

    conn.commit()
    conn.close()

def create_purchaseitem_table():
    conn = create_connection()
    c = conn.cursor()

    c.execute(""" 
        CREATE TABLE IF NOT EXISTS purchase_item (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            purchase_id INTEGER NOT NULL,
            product_id INTEGER NOT NULL,
            quantity REAL NOT NULL,
            unit_cost REAL NOT NULL,
            expiration_date TEXT,
            FOREIGN KEY (purchase_id) REFERENCES purchases(id),
            FOREIGN KEY (product_id) REFERENCES products(id)
        )""")

    conn.commit()
    conn.close()

def create_sale_table():
    conn = create_connection()
    c = conn.cursor()

    c.execute(""" 
        CREATE TABLE IF NOT EXISTS sales (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sale_date TEXT NOT NULL,
            payment_method TEXT NOT NULL
        )""") 

    conn.commit()
    conn.close()

def create_saleitem_table():
    conn = create_connection()
    c = conn.cursor()

    c.execute(""" 
        CREATE TABLE IF NOT EXISTS sale_item (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sale_id INTEGER NOT NULL,
            product_id INTEGER NOT NULL,
            unit_price REAL NOT NULL,
            quantity REAL NOT NULL,
            FOREIGN KEY (sale_id) REFERENCES sales(id),
            FOREIGN KEY (product_id) REFERENCES products(id)
        )""")

    conn.commit()
    conn.close()

def initialize_database():
    create_connection()
    create_product_table()
    create_purchase_table()
    create_purchaseitem_table()
    create_sale_table()
    create_saleitem_table()