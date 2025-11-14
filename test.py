class phone :
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def display_info(self):
        return f"Brand: {self.brand}, Model: {self.model}, Price: ${self.price}"
    

phone1 = phone("Apple", "iPhone 13", 999)
print(phone1.display_info())