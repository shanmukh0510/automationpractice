"""

1.single inheritance
2.multiple inheritance
3.multilevel inheritance
4.Hierachical Inheritance
5.hybrid inheritance

"""
#single inheritence
class parent:
    def show(self):
        print("this is parent class ")

class child(parent):
    def display(self):
        print("this is child class")
obj1 = parent()
obj1.show()
obj = child()
obj.show()
obj.display()


class Animal:
    def sound(self):
        print("Animal sound")
    def walk(self):
        print("Animal walking")
class dog(Animal):
    def bark(self):
        print("Dog barking")
class cat(dog):
    def meow(self):
        print("Cat meowing")





