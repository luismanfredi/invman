from src.models.purchase import Purchase, PurchaseItem
from src.database.connection import create_connection

def insert_purchase(purchase: Purchase):
    conn = create_connection()
    c = conn.cursor()

    c.execute("""
        INSERT INTO purchases (supplier_name, purchase_date)
        VALUES (?, ?)
    """, (
        purchase.supplier_name,
        purchase.purchase_data))

    conn.commit()
    purchase_id = c.lastrowid
    conn.close()

    return purchase_id

def insert_purchaseitem(purchaseitem: PurchaseItem):
    conn = create_connection()
    c = conn.cursor()
    
    c.execute("""
        INSERT INTO purchase_items (purchase_id, product_id, quantity, unit_cost, expiration_date)
        VALUES (?, ?, ?, ?, ?)
    """, (
        purchaseitem.purchase_id,
        purchaseitem.product_id,
        purchaseitem.quantity,
        purchaseitem.unit_cost,
        purchaseitem.expiration_date))
    
    conn.commit()
    conn.close()

def product_exists(name: str) -> bool:
    conn = create_connection()
    c = conn.cursor()

    c.execute("""
        SELECT 1 FROM products
        WHERE name = ?
        LIMIT 1
    """, (name,))

    result = c.fetchone()
    conn.close()

    print("Result:", result)

    return result is not None