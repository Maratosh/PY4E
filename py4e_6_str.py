#!/usr/bin/python3

''' Python for everybody
    chapter 6 '''
#With while loop
string = input('Enter a string:')
index = 0
while index < len(string):
    letter = string[index]
    print(index, letter)
    index += 1
#With for loop        
string = input('same with for loop:')
index = 0
for i in string:
    print(index, i)
    index += 1
#Count a letter
count = 0
for i in string:
    if i == "n":
        count +=1
print(count)
# while loop works its way backwards
print(string, len(string))
count = -1
while count >= -6:
    print(count, string[count])
    count -=1
#for loop works its way backwards
print('Same with for')
index = -1
for i in string:
    print(index, string[index])
    index -=1
#Chack's example
data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
atpos = data.find('@')
print(atpos)
21
sppos = data.find(' ',atpos)
print(sppos)
31
host = data[atpos+1:sppos]
print(host)
uct.ac.za
>>>
