# when a sub class provides specific implimentation of a method already defined in super calss
# this allows the subclass to modify or extend the behaviour of super class


class Animal:
    def make_sound(self):
        return "some animal sound  "

class Dog(Animal):
    def make_sound(self):
        return "bark"

class Cat(Animal):
    def make_sound(self):
        return  "meow"

def make_animal_sound(animal):
    print(animal.make_sound())

dog = Dog()

cat = Cat()
make_animal_sound(dog)
make_animal_sound(cat)