print('imported from my_module!!!')

test = 'Test String!!!'

def find_index(to_search, target):
    for i, val in enumerate(to_search):
        if val == target:
            return i
    
    return -1