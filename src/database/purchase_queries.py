from src.database.connection import create_connection
from src.models.purchase import Purchase, PurchaseItem

def insert_purchase(purchase: Purchase, conn):
    c = conn.cursor()

    c.execute("""
        INSERT INTO purchases (supplier_name, purchase_date)
        VALUES (?, ?)
    """, (
        purchase.supplier_name,
        purchase.purchase_date))
    
    purchase_id = c.lastrowid

    return purchase_id

def insert_purchaseitem(purchaseitem: PurchaseItem, conn):
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