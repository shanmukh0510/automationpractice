class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        return f"{self.year} {self.make} {self.model}"

class Car(Vehicle):
    def __init__(self, make, model, year, mileage):
        super().__init__(make, model, year)
        self.mileage = mileage  # Renamed the attribute

class Motorcycle(Car):
    def __init__(self, make, model, year, mileage, discount):
        super().__init__(make, model, year, mileage)
        self.discount = discount

    def apply_discount(self, price):
        return price - (price * self.discount / 100)

car = Car("Toyota", "Camry", 2020, 30)
print(car.display_info())
print("Mileage:", car.mileage)  # Corrected attribute name

motorcycle = Motorcycle("Harley-Davidson", "Sportster", 2021, 10, 10)
print(motorcycle.display_info())
print("Discounted Price:", motorcycle.apply_discount(10000))
