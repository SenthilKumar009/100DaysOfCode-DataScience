def hello(func):
    func()

def great():
    print("Helloooo!!!")

a = hello(great)
print(a)