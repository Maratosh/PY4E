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

############################################
# Combining searching and extracting

# Search for lines that start with 'X' followed by any non
# whitespace characters and ':'
# followed by a space and any number.
# The number can include a decimal.
import re
fhand = open('mbox-short.txt')           # we want lines that start with X-, followed by zero 
for line in fhand:                       # or more characters (.*), followed by a colon (:)                    
    line = line.rstrip()                 # and then a space. After the space we are looking for  
    if re.search('X-.*: [0-9.]+', line): # one or more characters that are either a digit (0-9)  
        print(line)                      # or a period [0-9.]+. 
###############################################
#!/usr/bin/python3
# Combining searching and extracting

# Search for lines that start with 'X' followed by any
# non whitespace characters and ':' followed by a space
# and any number. The number can include a decimal.
# Then print the number if it is greater than zero.
import re                                       # Instead of calling search(), we add parentheses around the part
fhand = open('mbox-short.txt')                  # of the regular expression that represents the floating-point
for line in fhand:                              # number to indicate we only want findall() to give us back the
    line = line.rstrip()                        #  floating-point number portion of the matching string.  
    x = re.findall('^X\S*: ([0-9.]+)', line)    #
    if len(x) > 0:                              #
        print(x)
###########################################
#!/usr/bin/python3
# Combining searching and extracting

# Search for lines that start with 'Details: rev='
# followed by numbers and '.'
# Then print the number if it is greater than zero
import re
fhand = open('mbox-short.txt')                          # Translating our regular expression, we are looking
for line in fhand:                                      # for lines that start with Details:, followed by any
    line = line.rstrip()                                # number of characters (.*), followed by rev=, and then
    x = re.findall('^Details:.*rev=([0-9.]+)', line)    # by one or more digits. We want to find lines that match
    if len(x) > 0:                                      # the entire expression but we only want to extract the integer
        print(x)                                        # number at the end of the line, so we surround [0-9]+ with parentheses.

#################################################
#!/usr/bin/python3
# Search for lines that start with From and a character
# followed by a two digit number between 00 and 99 followed by ':'
# Then print the number if it is greater than zero
import re

fhand = open('mbox-short.txt')                      # The translation of this regular expression is that we are looking 
for line in fhand:                                  # for lines that start with From (note the space), followed by any 
    line = line.rstrip()                            # number of characters (.*), followed by a space, followed by two 
    x = re.findall('^From .* ([0-9][0-9]):', line)  # digits [0-9][0-9], followed by a colon character. This is the 
    if len(x) > 0:                                  # definition of the kinds of lines we are looking for.
        print(x)                                    #

################################
'''Exercise 1: Write a simple program to simulate the operation of the grep
command on Unix. Ask the user to enter a regular expression and count the
number of lines that matched the regular expression:'''
#!/usp/bin/python3
import re
rex = input('Enter a regular expression: ')
i = 0
fhand = open('mbox.txt')
for line in fhand:
    line = line.rstrip()
    if re.search(rex, line):
        i += 1
print('This file has {} lines that matches {}'.format(i, rex))
#########################
#!/usr/bin/python3
'''Exercise 2: Write a program to look for lines of the form:
New Revision: 39772
Extract the number from each of the lines using a regular expression
and the findall() method. Compute the average of the numbers and print
out the average as an integer.'''
#!/usp/bin/python3
import re
#rex = input('Enter a regular expression: ')
i = 0
lst = []
fname = input('Enter file: ')
try:
    fhand = open(fname)
except:
    print('The file cannot be opened!', fname)
    exit()
for line in fhand:
    line = line.rstrip()
    x = re.findall('New Revision: ([0-9]+)', line)
    if len(x) > 0:
        #print(x)
        for i in x:
            #print(i)
            i = int(i)
            lst.append(i)
print(int(sum(lst)/len(lst)))
    

##########################
import re
from urllib.request import urlopen
with urlopen('https://www.python-course.eu/simpsons_phone_book.txt') as fh:
    for line in fh:
        line = line.decode('utf-8').rstrip()
        #print(line)
        if re.search(r'J.*N', line):
            print(line)
        
