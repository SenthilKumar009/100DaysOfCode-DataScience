'''
def I(n):
    s = '+'
    for i in range(n):
        s += s
        yield s
for x in I(2):
    print(x, end='')
'''

#for line in open('text.txt', 'rt'):

#print(len("\\\\"))
'''
class A:
    pass

class B(A):
    pass

class C(B):
    pass

print(issubclass(A,C))

class A:
    A = 1
    def __init__(self):
        self.a = 0

a = A()

print(hasattr(a, 'A'))


class A:
    def __init__(self, v = 2):
        self.v = v
    
    def set(self, v = 1):
        self.v += v
        return self.v


a = A()
b = a
b.set()
print(a.v)

class A:
    def __init__(self, v):
        self.__a = v + 1

a = A(0)
print(a.__a)
'''

try:
    raise Exception
except BaseException:
    print('a')
except Exception:
    print('B')
except:
    print('C')

print(float())