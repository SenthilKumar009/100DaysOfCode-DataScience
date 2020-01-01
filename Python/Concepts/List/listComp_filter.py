num = [1,2,3,4,5,6,7,8,9,10]

my_list = filter(lambda n: n%2 == 0, num)
print(list(my_list))

my_list = [n for n in num if n%2 == 0]
print(list(my_list))