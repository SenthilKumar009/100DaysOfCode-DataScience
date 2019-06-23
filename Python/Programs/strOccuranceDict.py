text = input("Enter the String:")

dict = {}

for x in text:
    dict[x] = dict.get(x, 0) + 1

for key, value in dict.items():
    print("Text {} has occured {} time in the given text {}".format(key, value, text))