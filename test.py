class phone :
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def display_info(self):
        return f"Brand: {self.brand}, Model: {self.model}, Price: ${self.price}"