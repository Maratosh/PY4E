'''Because tuples are immutable, they don’t provide methods like sort and reverse, which modify
existing lists. However Python provides the built-in functions sorted and reversed, which take any
sequence as a parameter and return a new sequence with the same elements in a different order.'''
''' DSU
#!Decorate
a sequence by building a list of tuples with one or more sort keys preceding the elements from the sequence,
#!Sort
the list of tuples using the Python built-in sort, and
#!Undecorate
by extracting the sorted elements of the sequence'''

txt = 'but soft  what light in yonder window breaks'
lst = [(len(word), word) for word in txt.split()]
lst.sort(reverse=True)
for l, w in lst:
    print(w, l)
#!Dictionaries and tuples


d = {'a':10, 'b':1, 'c':22}
lst = [(v, k) for k, v in list(d.items())]
lst.sort()
print(lst)                          #[(1, 'b'), (10, 'a'), (22, 'c')]

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
d = {'a':10, 'b':1, 'c':22}
lst = [(v, k) for k, v in list(d.items())]
print(d)
d1 = {}             #{'a': 10, 'b': 1, 'c': 22}
for v, k in lst:
    d1[v] = k
print(d1)           #{10: 'a', 1: 'b', 22: 'c'}

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#!/usr/bin/python3
import string
fhand = open('romeo-full.txt')
counts = dict()

for line in fhand:
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) +1

lst = [(v, k) for k, v in counts.items()]
lst.sort(reverse=True)

print('The most common words!')
print('Word      Count')
print('________  _____')
for k, v in lst[:10]:
    print('{}        {}'.format(k, v))
    
    
#Using tuples as keys in dictionaries
directory[last,first] = number
#The expression in brackets is a tuple. We could use tuple assignment in a for loop to traverse this dictionary.
for last, first in directory:
    print(first, last, directory[last,first])
    
    
#!/usr/bin/python3
'''Exercise 1: Revise a previous program as follows:
Read and parse the “From” lines and pull out the addresses from
the line. Count the number of messages from each person using a
dictionary.
After all the data has been read, print the person with the most
commits by creating a list of (count, email) tuples from the
dictionary. Then sort the list in reverse order and print out the
person who has the most commits.'''

import string

fhand = open('mbox.txt')
counts = dict()
lst = list()

for line in fhand:
    line = line.rstrip()
    if not line.startswith('From'): continue
    words = line.split()
    if len(words) < 3: continue
    counts[words[1]] = counts.get(words[1], 0) +1
#print(counts) #!!Dictionary is done!!
    lst = [(v, k) for k, v in counts.items()]
#print(lst) #list of the tuples(value, key) is done
    lst.sort(reverse=True)
print(lst)
print('The most commits!')
print('Count      email')
print('________  _____')
for k, v in lst[:10]:
    print('{}        {}'.format(k, v))

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
'''Exercise 2: This program counts the distribution of the
hour of the day for each of the messages. You can pull the
hour from the “From” line by finding the time string and then
splitting that string into parts using the colon character.
Once you have accumulated the counts for each hour, print out
the counts, one per line, sorted by hour as shown below.'''

fhand = open('mbox-short.txt')
counts = dict()
lst = list()

for line in fhand:
    line = line.rstrip()
    if not line.startswith('From'): continue
    words = line.split()
    if len(words) < 3: continue
    time = words[5].split(':')
    #print(time, words[5])       # ['09', '14', '16'] 09:14:16
    counts[time[0]] = counts.get(time[0], 0) + 1
#print(counts)
lst = [(k, v) for k, v in counts.items()]
lst.sort()
print('Hour Count')
print('____ _____')
for k, v in lst:
    print('{}   {}'.format(k, v))

##############################
#!/usr/bin/python3
'''Exercise 3: Write a program that reads a file and prints
the letters in decreasing order of frequency. Your program
should convert all the input to lower case and only count
the letters a-z. Your program should not count spaces, digits,
punctuation, or anything other than the letters a-z.
Find text samples from several different languages and see
how letter frequency varies between languages. Compare your
results with the tables at
https://wikipedia.org/wiki/Letter_frequencies.'''
import string
