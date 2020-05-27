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
    if re.search('F..m', line):     #line.find('From') >=0:
        print(line)
#####################################
import re                           
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if re.search('^F..m', line):  #line.startswith('From'):
        print(line)
########################################
import re
fhand = open('mbox-short.txt')        # The search string ^From:.+@ will successfully match lines that start with “From:”, 
for line in fhand:                    # followed by one or more characters (.+), followed by an at-sign.      
    line = line.rstrip()              # So this will match the following line: From: stephen.marquard@uct.ac.za
    if re.search('^F..m:.+@', line): 
        print(line)                   
        
        
#############################################        
# Extracting data using regular expressions        
# Searching for lines that have an at-sign between characters
import re                             # The findall() method searches the string in the second argument 
fhand = open('mbox.txt')              # and returns a list of all of the strings that look like email addresses. 
for line in fhand:                    # We are using a two-character sequence that matches a non-whitespace character (\S).
    line = line.rstrip()
    x = re.findall('\S+@\S+', line)
    if len(x) > 0: 
        print(x)
        
####################################
# Search for lines that have an at sign between characters
# The characters must be a letter or number
import re                                               # we are looking for substrings that start with a single lowercase letter, 
fhand = open('mbox.txt')                                # uppercase letter, or number “[a-zA-Z0-9]”, followed by zero or more 
for line in fhand:                                      # non-blank characters (\S*), followed by an at-sign, followed by zero or 
    line = line.rstrip()                                # more non-blank characters (\S*), followed by an uppercase or 
    x = re.findall('[a-zA-Z0-9]\S*@\S*[a-zA-Z]', line)  # lowercase letter [a-zA-Z]
    if len(x) > 0:
        print(x)





