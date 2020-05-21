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

'''Exercise 2: Write a program that categorizes each mail message by
which day of the week the commit was done. To do this look for lines
that start with “From”, then look for the third word and keep a running
count of each of the days of the week. At the end of the program print
out the contents of your dictionary (order does not matter)'''

import string
string.punctuation

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
    if not line.startswith('from'): continue
    #print(line)
    words = line.split()
    if len(words) < 3 : continue
    #print(words)
    if words[2] not in ans:
        ans[words[2]] = 1
    else:
        ans[words[2]] +=1
print(ans)        
'''Exercise 4: Add code to the above program to figure out who has
the most messages in the file. After all the data has been read
and the dictionary has been created, look through the dictionary
using a maximum loop (see Chapter 5: Maximum and minimum loops)
to find who has the most messages and print how many messages
the person has.'''

import string
string.punctuation

fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened: ', fname)
    exit()
ans = {}
lst = []
for line in fhand:
    line = line.rstrip()
    #line = line.translate(line.maketrans('', '', string.punctuation))
    line = line.lower()
    if not line.startswith('from'): continue
    words = line.split()
    if len(words) < 3: continue
    if words[1] not in ans:
        ans[words[1]] = 1
    else:
        ans[words[1]] += 1
print(ans)
count = 0

for i in ans:
    if ans[i] > count:
        count = ans[i]
        winer = i
print(winer, count)
'''Exercise 5: This program records the domain name (instead of the address)
where the message was sent from instead of who the mail came from
(i.e., the whole email address). At the end of the program,
print out the contents of your dictionary.'''

import string
string.punctuation

fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened: ', fname)
    exit()
ans = {}
lst = []
for line in fhand:
    line = line.rstrip()
    #line = line.translate(line.maketrans('', '', string.punctuation))
    line = line.lower()
    if not line.startswith('from'): continue
    words = line.split()
    if len(words) < 3: continue
    domain = words[1]
    domain = domain.split('@')
    if domain[1] not in ans:
        ans[domain[1]] = 1
    else:
        ans[domain[1]] += 1
    
print(ans)
count = 0

for i in ans:
    if ans[i] > count:
        count = ans[i]
        winer = i
print(winer, count)
