from src.models.sale import Sale, SaleItem


def insert_sale(sale: Sale, conn) -> int:
    c = conn.cursor()

    c.execute(
        """
        INSERT INTO sales (sale_date, payment_method)
        VALUES (?, ?)
    """,
        (sale.sale_date, sale.payment_method),
    )

    sale_id = c.lastrowid

    return sale_id


def insert_saleitem(saleitem: SaleItem, conn):
    c = conn.cursor()

    c.execute(
        """
        INSERT INTO sale_items (sale_id, product_id, unit_price, quantity)
        VALUES (?, ?, ?, ?)
    """,
        (saleitem.sale_id, saleitem.product_id, saleitem.unit_price, saleitem.quantity),
    )


def show_sales_table(conn):
    c = conn.cursor()

    c.execute("""
        SELECT id, sale_date, payment_method
        FROM sales""")
    rows = c.fetchall()

    if not rows:
        print("No registered sales!")
        return

    print("=" * 50)
    print(f"{'ID':<4} {'Date':<25} {'Payment Method':<10}")
    print("=" * 50)

    for row in rows:
        id_, sale_date, payment_method = row

        print(f"{id_:<4} {sale_date:<25} {payment_method.capitalize():<10}")

    print("=" * 50)
