class Vehicle:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year

    def disply_info(self):
        return f"{self.make}{self.model}{self.year}"

class Car(Vehicle):
    def __init__(self, make, model, year, milage):
        super().__init__(make, model,year)
        self.milage = milage

class motorcycle(Car):
    def __init__(self,make,model,year,milage,discount):
        super().__init__(make, model, year, milage)
        self.discount = discount
    def apply_discount(self,price):
        return price - price * self.discount / 100

c = Car("ford","BMW","2021",20)
print(c.disply_info())
print(c.milage)

M = motorcycle("ford","BMW","2021",20,10)
print(M.apply_discount(1000000))