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
    
def show_purchases_table(conn):
    c = conn.cursor()

    c.execute("""
        SELECT id, supplier_name, purchase_date
        FROM purchases""")
    rows = c.fetchall()

    if not rows:
        print("No registered purchases!")
        return
    
    print("=" * 50)
    print(f"{'ID':<4} {'Supplier':<15} {'Date':<10}")
    print("=" * 50)

    for row in rows:
        id_, supplier_name, purchase_date = row

        print(f"{id_:<4} {supplier_name:<15} {purchase_date:<8}")

    print("=" * 50)
