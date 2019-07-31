# While using any library function like shelve, never save the file name with library name itself.
# It will create Attribute error issue

import shelve
print(shelve.__file__)
with shelve.open('mydata') as shelfFile:
    cats = ['Zophie', 'Pooka', 'Simon']
    shelfFile['cats'] = cats
    shelfFile.close()

with shelve.open('mydata') as openDB:
    getData = openDB['cats']

print(getData)