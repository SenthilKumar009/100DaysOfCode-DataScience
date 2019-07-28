class Dog():
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(self.name + " speaks Woof!!!")

class Cat():
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(self.name + " speaks Meaowww!!!")


tony = Dog('Tony')
tony.speak()

pussy = Cat('Pussy')
pussy.speak()