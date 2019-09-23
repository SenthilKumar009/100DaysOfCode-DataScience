class Parrot:

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def sing(self, song):
        return "{} sings {}".format(self.name, song)
    
Blu = Parrot('KooKoo', 4)

print(Blu.sing('Rakkamma'))