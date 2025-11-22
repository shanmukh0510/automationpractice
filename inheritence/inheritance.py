# from datetime import date
#
#
# class Person:
#     def _init_(self, name, country, date_of_birth):
#         self.name = name
#         self.country = country
#         self.date_of_birth = date_of_birth
#
#     def age(self):
#         today = date.today()
#         age = today.year - self.date_of_birth.year
#         if today < date(today.year, self.date_of_birth_month, self.date_of_birth_day):
#             age -= 1
#             return age
#
#
# person1 = Person("Rahul", "India", date(1945, 12, 1))
# print('name', Person.name)

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
print(f"Name: {person1.name}, Age: {person1.age()} years")
