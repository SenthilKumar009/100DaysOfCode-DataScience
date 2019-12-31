num = [1,2,3,4,5,6,7,8,9,10]
my_list = []

for n in num:
    my_list.append(n)

print(my_list)

my_list = [n*n for n in num]
print(my_list)

#using map method
my_list = []
my_list = map(lambda n: n*n, num)
print(list(my_list))
