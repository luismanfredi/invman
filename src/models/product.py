class Product:
    def __init__(self, name, category, brand, unit_type, selling_price=None, stock_quantity=0.0, min_stock=0.0, id=None):
        self.id = id
        self.name = name
        self.category = category
        self.brand = brand
        self.unit_type = unit_type
        self.selling_price = selling_price
        self.stock_quantity = stock_quantity
        self.min_stock = min_stock