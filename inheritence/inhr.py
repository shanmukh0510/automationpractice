


from datetime import date

class Person:
    def __init__(self, name, country, date_of_birth):
        self.name = name
        self.country = country
        self.date_of_birth = date_of_birth

    def age(self):
        today = date.today()
        age = today.year - self.date_of_birth.year
        if today < date(today.year, self.date_of_birth.month, self.date_of_birth.day):
            age -= 1
        return age

person1 = Person("Rahul", "India", date(1945, 12, 1))
print('name:', person1.name)
print('date of birth:', person1.date_of_birth)
print('age:', person1.age())
