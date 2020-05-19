#!/usr/bin/python3

fname = input('Enter the file name: ')
print(fname)
try:
    fhand = open(fname)
except:
    print('The file cannot be opened')
    exit()
for line in fhand:
    line = line.rstrip()
    #print(line)
    if not line.startswith('From '): continue
    words = line.split()
    day = words.pop(2)  #pop modifies the list and returns the element that was removed
    sentence = ' '.join(words) #join is the inverse of split. It takes a list of strings and concatenates the elements.
    #print(sentence)
    print(day, '    ', words)
    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
fhand = open('mbox-short.txt')
for line in fhand:
    words = line.split()
    #print('Debug:', words)
    if len(words) == 0: continue
    if words[0] != 'From': continue
    print(words[2])
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
fhand = open('mbox-short.txt')
for line in fhand:
    words = line.split()
    #print('Debug:', words)
    if len(words) == 0 or words[0] != 'From': continue
    print(words[2])
        
    