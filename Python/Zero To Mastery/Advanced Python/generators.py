def generator_function(num):
    for i in range(num):
        yield i*2

for item in generator_function(1000):
    print(item)