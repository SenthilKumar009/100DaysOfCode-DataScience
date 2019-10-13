#Decorator Pattern

def my_decorator(func):
    def wrap_fun(*args, **kwargs):
        print('*********')
        func(*args, **kwargs)
        print('*********')
    return wrap_fun

@my_decorator
def hello(greetings, emoji):
    print(greetings, emoji)

hello('Welcome', '🛩 ')