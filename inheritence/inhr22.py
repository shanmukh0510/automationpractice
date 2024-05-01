class C():
    def __init__(self):
        self.c = 21
        self.__d = 42

class D(C):
    def __init__(self):
        self.e = 84
        super().__init__()  # Call the parent class constructor

object1 = D()

# Access the public variable 'c'
print("Value of 'c':", object1.c)

# Access the private variable '__d' (name mangling)
print("Value of '__d':", object1._C__d)
