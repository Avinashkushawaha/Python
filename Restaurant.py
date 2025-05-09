class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display(self):
        return f"{self.name}: ${self.price: .2f}" 

class VegMenuItem(MenuItem):
    def __init__(self, name, price, category="veg"):
        super().__init__(name, price)
        self.category = category       

    def display(self):
        return f"{self.category} - {self.name}: ${self.price:.2f}"    
    
class NonvegMenuItem(MenuItem):
    def __init__(self, name, price, category="Non-veg"):
        super().__init__(name, price)
        self.category = category       

    def display(self):
        return f"{self.category} - {self.name}: ${self.price:.2f}"    
    
class DessertMenuItem(MenuItem):
    def __init__(self, name, price, category="dessert"):
        super().__init__(name, price)
        self.category = category       

    def display(self):
        return f"{self.category} - {self.name}: ${self.price:.2f}"  

class SoftDrinkMenuItem(MenuItem):
    def __init__(self, name, price, category="Drink"):
        super().__init__(name, price)
        self.category = category       

    def display(self):
        return f"{self.category} - {self.name}: ${self.price:.2f}"        

