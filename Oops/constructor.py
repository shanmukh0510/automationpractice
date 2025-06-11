from numpy.f2py.symbolic import as_ge


class person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender =gender

p1 = person("sandana",20,"female")
print(p1.name)
print(p1.age)

del p1.name


class student():
    pass
