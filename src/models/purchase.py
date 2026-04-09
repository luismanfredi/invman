class Purchase:
    def __init__(self, supplier_name, purchase_date, id=None):
        self.id = id
        self.supplier_name = supplier_name
        self.purchase_date = purchase_date

class PurchaseItem:
    def __init__(self, quantity, unit_cost, expiration_date=None, purchase_id=None, product_id=None,id=None):
        self.id = id
        self.purchase_id = purchase_id
        self.product_id = product_id
        self.quantity = quantity
        self.unit_cost = unit_cost
        self.expiration_date = expiration_date