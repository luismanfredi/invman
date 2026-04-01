class Sale:
    def __init__(self, sale_date, payment_method, id=None):
        self.id = id
        self.sale_date = sale_date
        self.payment_method = payment_method

class SaleItem:
    def __init__(self, product_id, quantity, unit_price, sale_id=None, id=None):
        self.id = id
        self.sale_id = sale_id
        self.unit_price = unit_price
        self.quantity = quantity
        self.product_id = product_id