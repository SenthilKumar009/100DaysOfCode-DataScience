def greet(lang):
    if(lang == 'es'):
        return('Holo')
    elif(lang == 'fr'):
        return('Bonjur')
    else:
        return('Hello')

print(greet('en'), 'Maxwell')
print(greet('es'), 'Steffy')
print(greet('fr'), 'Senthil')