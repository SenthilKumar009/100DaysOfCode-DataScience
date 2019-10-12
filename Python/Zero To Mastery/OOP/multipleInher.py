class User():
    def sing_in(self):
        print('Logged in')

class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power of {self.power}')

class Archer(User):
    def __init__(self, name, arrow):
        self.name = name
        self.arrow = arrow
    
    def check_arrows(self):
        print(f'attacking with arrows. Arrows left {self.arrow - 1}')
    
    def run(self):
        print(f'{self.name} runs really fast')
        
class HybridBorg(Wizard, Archer):
    def __init__(self, name, arrow, power):
        Archer.__init__(self, name, arrow)
        Wizard.__init__(self, name, power)


borg1 = HybridBorg('SKK', 50, 100)
borg1.run()
borg1.attack()
borg1.check_arrows()