'''class Parrot:

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def sing(self, song):
        return "{} sings {}".format(self.name, song)
    
Blu = Parrot('KooKoo', 4)

print(Blu.sing('Rakkamma'))

# test examples here

class Classy:
    varia = 2
    def method(self):
        print(self.varia, self.var)

obj = Classy()
obj.var = 3
obj.method()
'''

class Classy:
    varia = 1
    def __init__(self):
        self.var = 2

    def method(self):
        pass

    def __hidden(self):
        pass

obj = Classy()

print(obj.__dict__)
print(Classy.__dict__)