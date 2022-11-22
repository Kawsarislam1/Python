import string

file = input ("enter file name: ")
file = open(file,'r')
f = file.read()
f = f.lower()
dict1 = {}

file.close()

for letters in string.ascii_lowercase:
    dict1[letters] = 0

for letters in f:
    if letters in dict1:
        dict1[letters] = dict1[letters] + 1

print('letter    count')

for letters in dict1.keys():
    print('{}         {}'.format(letters,dict1[letters]))
