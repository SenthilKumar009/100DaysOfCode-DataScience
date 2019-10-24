import re

pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9]+\.[a-zA-Z0-9-.]+$)")
string = 'Senthil Kumar Kanagaraj'

pattern2 = re.compile(r'[A-Za-z0-9@#$%^&+=]{8,}[0-9]')
password = "Kabil1187$1"

a = pattern.search(string)
b = pattern2.fullmatch(password)

print(a)
print(b)