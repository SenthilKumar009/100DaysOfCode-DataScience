class Animal:
    def __init__(self):
        print('Animal is created!!!')
    
    def who_am_i(self):
        print("I'm an Animal")
    
    def eat(self):
        print("I'm eating!!!")

class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog created!!!")
    
    def who_am_i(self):
        print("I'm a Dog...")

    def bark(self):
        print('Woof Woof!!!')

    def eat(self):
        print('I am a dog and eating')

myDog = Dog()
myDog.who_am_i()
myDog.bark()
myDog.eat()