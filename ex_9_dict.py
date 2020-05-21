'''Write a program that reads the words in words.txt and stores them as
keys in a dictionary. It doesn’t matter what the values are. Then you can
use the in operator as a fast way to check whether a string is in the
dictionary.'''

dict1 = {}
item = 0
for line in open('words.txt'):
    line = line.rstrip()
    line = line.split()
    for word in line:
        if word in dict1: continue
        dict1[word] = item
        item += 1
print(dict1)
#!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Same but counts words
dict1 = {}
for line in open('words.txt'):
    line = line.rstrip()
    line = line.split()
    for word in line:
        if word not in dict1: 
            dict1[word] = 1
        else:
            dict1[word] = dict1[word] + 1
print(dict1)
#!!!!!!!!!!!!!!!!!!!
dict2 ={}
for line in open('words.txt'):
    line = line.rstrip()
    line = line.split()
    for word in line:
        dict2[word] = dict2.get(word, 0) + 1
print(dict2)
#Advanced text parsing!!!!!!!!!!!!!!!!!!
import string


fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened: ', fname)
    exit()
ans = {}

for line in fhand:
    line = line.rstrip()
    line = line.translate(line.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        if word not in ans:
            ans[word] = 1
        else:
            ans[word] += 1
print(ans)

