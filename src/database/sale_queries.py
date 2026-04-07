from src.models.sale import Sale, SaleItem
from src.database.connection import create_connection

def insert_sale(sale: Sale) -> int:
    conn = create_connection()
    c = conn.cursor()

    c.execute("""
        INSERT INTO sales (sale_date, payment_method)
        VALUES (?, ?)
    """, (
    sale.sale_date,
    sale.payment_method))

    conn.commit()
    sale_id = c.lastrowid
    conn.close()

    return sale_id

def insert_saleitem(saleitem: SaleItem):
    conn = create_connection()
    c = conn.cursor()

    c.execute("""
        INSERT INTO sale_items (sale_id, product_id, unit_price, quantity)
        VALUES (?, ?, ?, ?)
    """, (
        saleitem.sale_id,
        saleitem.product_id,
        saleitem.unit_price,
        saleitem.quantity
    ))

    conn.commit()
    conn.close()

