my_dict = {num: num*2 for num in [1,2,3]}

print(my_dict)

sample_dict = {
    'val1' : 2,
    'val2' : 3,
    'va;3' : 4
}

my_dict = {key:val*2 for key, val in sample_dict.items()}
print(my_dict)