class Category:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.subcategories = []
        self.discount = 0.0

    def add_subcategory(self, name):
        sub = Category(name, parent=self)
        self.subcategories.append(sub)
        return sub
    
    def __str__(self):
        return f"{self.name}"