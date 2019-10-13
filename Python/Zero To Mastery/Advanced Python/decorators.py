def my_decoratorStart(func):
    def wrap_func(x):
        print('**********')
        func(x)
        print('**********')
    return wrap_func

def my_decoratorEnd(func):
    def wrap_func():
        print('**********')
        func()
        print('**********')
    return wrap_func


@my_decoratorStart
def hello(greetings):
    print(greetings)


@my_decoratorEnd
def bye():
    print("Byeeee!!!")

hello('Welcome to Java')
bye()
