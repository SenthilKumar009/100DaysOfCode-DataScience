stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print('{} {}'.format(v,k))
        item_total += v

    print("Total number of items: " + str(item_total))

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

displayInventory(stuff)

def addToInventory(inventory, addedItems):
    # your code goes here
    #item_total = 0
    for val in addedItems:
        if val in inventory:
            inventory[val] += 1
        else:
            inventory[val] = 1
    
    #for k, v in inventory.items():
    #    print('{} {}'.format(v,k))
    #    item_total += v

    #print("Total number of items: " + str(item_total))
    #print(inventory)
    return inventory

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)

displayInventory(inv)