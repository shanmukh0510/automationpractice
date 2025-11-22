# inheritence allows us to define class that inherits all the properties and methods from another class
# parent class is the class where we inherited from
#child class is the class inherits from another class, also clled as derived class

class Students:
    def __init__(self,fname, lname,ID):
        self.firstname = fname
        self.lastname = lname
        self.ID = ID
    def printname(self):
        print(self.firstname, self.lastname)
    def printid(self):
        print(self.ID)


s = Students("shan","ravi",7)
s.printname()
s.printid()
class Person(Students):
    pass
p = Person("vasu","kiran",5)
p.printname()
p.printid()


