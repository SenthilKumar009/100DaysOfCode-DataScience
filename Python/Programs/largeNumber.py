largest_so_for = -1

print('Before', largest_so_for)

for num in [9, 18, 63, 45, 99, 81] :
    if num > largest_so_for :
        largest_so_for = num
    print(largest_so_for, num)

print('After', largest_so_for)