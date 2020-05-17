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
