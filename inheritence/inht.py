class Grandfather:
    def __init__(self,grandfather_name):
        self.grandfather_name = grandfather_name

    def print_name(self):
        print("grandfathername :" ,self.grandfather_name)

class Father(Grandfather):
    def __init__(self):





    super().__init__(Grandfather)