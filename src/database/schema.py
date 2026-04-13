from src.database.connection import create_connection

def create_products_table():
    conn = create_connection()
    c = conn.cursor()

    c.execute(""" 
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            brand TEXT NOT NULL,
            unit_type TEXT NOT NULL,
            stock_quantity REAL NOT NULL DEFAULT 0 CHECK(stock_quantity >= 0),
            min_stock REAL NOT NULL DEFAULT 0 CHECK(min_stock >= 0),
            selling_price REAL CHECK(selling_price IS NULL OR selling_price >=0),
            UNIQUE(name, brand, unit_type)
        )""") 

    conn.commit()
    conn.close()

def create_purchases_table():
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

def create_purchaseitems_table():
    conn = create_connection()
    c = conn.cursor()

    c.execute(""" 
        CREATE TABLE IF NOT EXISTS purchase_items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            purchase_id INTEGER NOT NULL,
            product_id INTEGER NOT NULL,
            quantity REAL NOT NULL CHECK(quantity > 0),
            unit_cost REAL NOT NULL CHECK(unit_cost >= 0),
            expiration_date TEXT,
            FOREIGN KEY (purchase_id) REFERENCES purchases(id),
            FOREIGN KEY (product_id) REFERENCES products(id)
        )""")

    conn.commit()
    conn.close()

def create_sales_table():
    conn = create_connection()
    c = conn.cursor()

    c.execute(""" 
        CREATE TABLE IF NOT EXISTS sales (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sale_date TEXT NOT NULL,
            payment_method TEXT NOT NULL CHECK(payment_method IN ('cash', 'debit card', 'credit card'))
        )""") 

    conn.commit()
    conn.close()

def create_saleitems_table():
    conn = create_connection()
    c = conn.cursor()

    c.execute(""" 
        CREATE TABLE IF NOT EXISTS sale_items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sale_id INTEGER NOT NULL,
            product_id INTEGER NOT NULL,
            unit_price REAL NOT NULL CHECK(unit_price >= 0),
            quantity REAL NOT NULL CHECK(quantity > 0),
            FOREIGN KEY (sale_id) REFERENCES sales(id),
            FOREIGN KEY (product_id) REFERENCES products(id)
        )""")

    conn.commit()
    conn.close()

def initialize_database():
    create_connection()
    create_products_table()
    create_purchases_table()
    create_purchaseitems_table()
    create_sales_table()
    create_saleitems_table()