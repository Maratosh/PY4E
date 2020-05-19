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
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
'''Write a program to open the file romeo.txt and read it line by line.
For each line, split the line into a list of words using the split function.
For each word, check to see if the word is already in a list. If the word is
not in the list, add it to the list. When the program completes, sort and
print the resulting words in alphabetical order.'''
fhand = open('romeo.txt')
ans = []
for line in fhand:
    line = line.split()
    #print(line)
    for word in line:
        #print(word)
        if word in ans: continue
        ans.append(word)
ans.sort()
print(ans)
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
'''Write a program to read through the mail box data and when you find
line that startswith “From”, you will split the line into words using the
split function. Weare interested in who sent the message, which is the
second word on the From line.'''

for line in open('mbox-short.txt'):
    if not line.startswith('From'): continue
    line = line.split()
    print(line.pop(1))
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
'''Rewrite the program that prompts the user for a list of numbers
and prints out the maximum and minimum of the numbers at the end when
the user enters “done”. Write the program to store the numbers the user
enters in a list and use the max() and min() functions to compute the
maximum and minimum numbers after the loop completes.'''
lst = []
while True:
    num = input('Enter a number, "done" to quit: ')
    if num == 'done': break
    try:
        num = float(num)
    except:
        print('Enter a numeric symbol')
        continue
    lst.append(num)
print(lst)
print(max(lst), min(lst))

        
    
