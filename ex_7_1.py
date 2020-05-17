#!/usr/bin/python3
''' Exercise 1: Write a program to read through a file
and print the contents of the file (line by line) all
in upper case.'''

fname = input('Enter a filename: ')
fhand = open(fname)
for line in fhand:
    line = line.upper()
    line = line.rstrip()
    print(line)
############################################
#!/usr/bin/python3

''' Exercise 2: Write a program to prompt for a
file name, and then read through the file and look for
lines of the form: X-DSPAM-Confidence: 0.8475
When you encounter a line that starts with "X-DSPAM-Confidence:"
pull apart the line to extract the floating-point number on the line.
Count these lines and then compute the total of the spam confidence
values from these lines. When you reach the end of the file, print out
the average spam confidence.  Average spam confidence: 0.750718518519 '''

fname = input('Enter the filename: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened: ', fname)
    exit()
    
count = 0
snum = 0
for line in fhand:
    line = line.rstrip()
    if line.find('X-DSPAM-Confidence:') == -1:
        continue
    print(line, float(line[19:]))
    snum = snum + float(line[19:])
    count += 1
print(snum / count)
print('###########################')
############################
''' Exercise 3: Sometimes when programmers get bored or want to have
a bit of fun, they add a harmless Easter Egg to their program.
Modify the program that prompts the user for the file name so that
it prints a funny message when the user types in the exact file
name "na na boo boo". The program should behave normally for all
other files which exist and don't exist.'''

fname = input('Enter the file name: ')
search = input('Type what are you searching for: ')
if fname == 'na na boo boo':
    print("NA NA BOO BOO TO YOU - You have been punk'd!")
    exit()
try:
    fhand = open(fname)
except:
    print('File cannot be opened!', fname)
    exit()
count = 0
for line in fhand:
    line = line.rstrip()
    if line.find(search) == -1:
        continue
    count += 1
print('Thete were {} {} lines in {}'.format(count, search, fname))


