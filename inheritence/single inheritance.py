class Calculator:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def add(self, a, b, c):
        return self.a + self.b + self.c

    def sub(self, a, b, c):
        return self.a - self.b

    def mul(self, a, b, c):
        return self.a * self.b * self.c

cal = Calculator(1,2,3)
result = cal.add(1,3,4)
print(result)