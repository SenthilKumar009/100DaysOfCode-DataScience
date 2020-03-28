class ExampleClass:
    counter = 0
    def __init__(self, val = 1):
        self.__first = val
        ExampleClass.counter += 1

exampleObject1 = ExampleClass()
print(exampleObject1.__dict__, exampleObject1.counter)
exampleObject2 = ExampleClass(2)
exampleObject3 = ExampleClass(4)

print(exampleObject2.__dict__, exampleObject2.counter)
print(exampleObject3.__dict__, exampleObject3.counter)