class Dog:

    species = 'Mammal'
    def __init__(self, breed, name, spots):
        self.breed = breed
        self.breedName = name
        self.spots = spots
    
    def printData(self):
        print('Species:', self.species)
        print('Breed Type:', self.breed)
        print('Breed Name:', self.breedName)
        print('Spots:', self.spots)
    
    def bark(self):
        print('Woof!!!')

myDog = Dog('Lab', 'Hashkie', True)
myDog.printData()
myDog.bark()