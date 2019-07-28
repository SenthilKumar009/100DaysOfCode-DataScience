class Dog():
    species = 'Mammal'
    myDogBreed = ['Lab', 'German', 'Country']

    def __init__(self, breed, name):
        self.breed = breed
        self.name = name

    def bark(self):
        for breed in Dog.myDogBreed :
            if self.breed == breed:
                print('Woof!!!')
                break
            else:
                print('LOL!!!')
                break

my_dog = Dog(breed = 'Lab', name = 'Tony')
my_dog.bark()