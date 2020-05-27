'''https://docs.python.org/3/library/re.html
  https://en.wikipedia.org/wiki/Regular_expression '''
#!/usr/bin/python3
'''Python Regular Expression Quick Guide

^        Matches the beginning of a line
$        Matches the end of the line
.        Matches any character
\s       Matches whitespace
\S       Matches any non-whitespace character
*        Repeats a character zero or more times
*?       Repeats a character zero or more times 
         (non-greedy)
+        Repeats a character one or more times
+?       Repeats a character one or more times 
         (non-greedy)
[aeiou]  Matches a single character in the listed set
[^XYZ]   Matches a single character not in the listed set
[a-z0-9] The set of characters can include a range
(        Indicates where string extraction is to start
)        Indicates where string extraction is to end
'''
# Search for lines that contain 'From'
import re
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if re.search('From', line):     #line.find('From') >=0:
        print(line)
#####################################
import re
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if re.search('^From', line):  #line.startswith('From'):
        print(line)
