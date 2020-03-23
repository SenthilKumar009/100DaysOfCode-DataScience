import random

greating = ['Good Morning', 'Good Noon', 'Good Evening', 'Good Night']
colors = ['red', 'green', 'white', 'black', 'yellow']

print(random.random())
print(random.randint(1,10))
print(random.randrange(2,10))

print(random.choice(greating))
print(random.choices(colors, k=9))