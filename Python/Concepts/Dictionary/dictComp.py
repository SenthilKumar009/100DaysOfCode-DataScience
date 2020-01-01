names = ['Bruce', 'Clark', 'Peter', 'Tony', 'Rogers']
superHeros = ['Batman', 'Superman', 'Spiderman', 'Ironman', 'Captain America']

myDict = {}

for name, hero in zip(names, superHeros):
    myDict[name] = hero

print(myDict)

myDict = {name: hero for name, hero in zip(names, superHeros)}
print(myDict)