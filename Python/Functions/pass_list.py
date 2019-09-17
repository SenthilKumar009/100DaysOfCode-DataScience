def modify(lst):
    lst.append(5)
    print(lst, id(lst))

lst = [1,2,3,4]
print(lst, id(lst))
modify(lst)