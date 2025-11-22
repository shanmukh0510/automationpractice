class People:
    def __init__(self,name):
        self.name = name
    def print_name(self):
        return self.name

class Mlas(People):
    def __init__(self,mlasname,name):
        self.mlasname = mlasname

        super.__init__()

