class Product:
    def __init__(self, id, name, cost_price, sale_price, category, distributor, brand, quantity_type, quantity, min_stock, registration_date, expiration_date=None, discount=None):
        self.id = id
        self.name = name
        self.cost_price = cost_price
        self.sale_price = sale_price
        self.category = category
        self.distributor = distributor
        self.brand = brand
        self.quantity_type = quantity_type
        self.quantity = quantity
        self.min_stock = min_stock
        self.registration_date = registration_date
        self.expiration_date = expiration_date
        self.discount = discount

    def __str__(self):
        return (
            f"Id: {self.id}\n"
            f"Name: {self.name}\n"
            f"Cost Price: {self.cost_price}\n"
            f"Sale Price: {self.sale_price}\n"
            f"Category: {self.category}\n"
            f"Distributor: {self.distributor}\n"
            f"Brand: {self.brand}\n"
            f"Quantity: {self.quantity}{self.quantity_type}\n"
            f"Min Stock: {self.min_stock}\n"
            f"Registration Date: {self.registration_date}\n"
            f"Expiration Date: {self.expiration_date}\n"
            f"Discount: {self.discount}"
        )