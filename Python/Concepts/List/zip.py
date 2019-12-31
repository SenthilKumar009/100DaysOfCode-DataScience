names = ['Bruce', 'Art', 'Peter', 'Tony', 'Steve']
heros = ['Batman', 'Joker', 'Spiderman', 'Iron Man', 'Captain America']

print(list(zip(names, heros)))

my_dict = {}

#for name, hero in zip(names, heros):
#    my_dict[name] = hero

my_dict = {name: hero for name, hero in zip(names, heros)}
print(my_dict)

