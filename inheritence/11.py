# Python program to demonstrate
# multilevel inheritance

# Base class


class Grandfather:

    def __init__(self, grandfathername):
       self.grandfathername = grandfathername

    def print_name(self):
       print('Grandfather name :', self.grandfathername)

# Intermediate class


class Father(Grandfather):
    def __init__(self, fathername, grandfathername):
       self.fathername = fathername

       def print_name(self):
           print("Father name :", self.fathername)

       # invoking constructor of Grandfather class
       super().__init__(grandfathername)

# Derived class


class Son(Father):
    def __init__(self, sonname, fathername, grandfathername):
       self.sonname = sonname

       # invoking constructor of Father class
       super().__init__(fathername, grandfathername)

    def print_name(self):
       print("Son name :", self.sonname)


# Driver code
s1 = Son('Prince', 'Rampal', 'Lal mani')
print(s1.grandfathername)
print(s1.fathername)
s1.print_name()