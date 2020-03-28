from os import strerror
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}
for character in message.lower():
    count.setdefault(character, 0)
    count[character] = count[character] + 1

text =''

try:
    with open('readText.txt', 'wt') as f:
        for key, value in count.items():
            if key not  in (' ', ',', '.'):
                text = key + '--> ' + str(value)
                f.write(text + '\n')
    f.close()
except IOError as e:
    print('I/O error Occured!!!')

try:
	for line in open('readText.txt', 'rt'):
		for ch in line:
			print(ch, end='')
except IOError as e:
	print("I/O error occurred: ", strerr(e.errno))

#print(count)