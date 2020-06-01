#!/usr/bin/python3
# https://www.w3.org/Protocols/rfc2616/rfc2616.txt
# The world’s simplest web browser############
import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)          # socket
mysock.connect(('data.pr4e.org', 80))                               # connect
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)                                                    # send

while True:
    data = mysock.recv(512)                                         # recv
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()
#   Retrieving an image over HTTP################
#!/usr/bin/python3
import socket
import time

HOST = 'data.pr4e.org'
PORT = 80
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((HOST, PORT))
mysock.sendall(b'GET http://data.pr4e.org/cover3.jpg HTTP/1.0\r\n\r\n')
count = 0
picture = b""

while True:
    data = mysock.recv(5120)
    if len(data) < 1: break
    #time.sleep(0.25)
    count = count + len(data)
    print(len(data), count)
    picture = picture + data

mysock.close()

# Look for the end of the header (2 CRLF)
pos = picture.find(b'\r\n\r\n')
print('Header length', pos)
print(picture[:pos].decode())

# Skip past the header and save the picture data
picture = picture[pos+4:]
fhand = open('stuf.jpg', 'wb')
fhand.write(picture)
fhand.close()
#####Retrieving web pages with urllib########################
import urllib.request

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())
    
#############
import urllib.request

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
count = {}
for line in fhand:
    words = line.decode().split()
    for word in words:
        count[word] = count.get(word, 0) + 1

print(count)
## Reading binary files using urllib  #####

'''This program reads all of the data in at once across the network and stores it in the variable img in the main
memory of your computer, then opens the file cover.jpg and writes the data out to your disk. The wb argument for open() 
opens a binary file for writing only. This program will work if the size of the file is less than the size of the memory
of your computer.
However if this is a large audio or video file, this program may crash or at least run extremely slowly when your computer
runs out of memory. In order to avoid running out of memory, we retrieve the data in blocks (or buffers) and then write each
block to your disk before retrieving the next block. This way the program can read any size file without using up all of the
memory you have in your computer.'''
import urllib.request, urllib.parse, urllib.error

img = urllib.request.urlopen('https://upload.wikimedia.org/wikipedia/commons/7/7d/Crew_Dragon_at_the_ISS_for_Demo_Mission_1_%28cropped%29.jpg').read()
fhand = open('dragon.jpg', 'wb')
fhand.write(img)
fhand.close()
#####
import urllib.request, urllib.parse, urllib.error

img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg')
fhand = open('cover3.jpg', 'wb')
size = 0
while True:
    info = img.read(100000)
    if len(info) < 1: break
    size = size + len(info)
    fhand.write(info)

print(size, 'characters copied.')
fhand.close()

# Code: http://www.py4e.com/code3/curl2.py
#################################
# Parsing HTML and scraping the web
'''One of the common uses of the urllib capability in Python is to scrape the web. Web scraping is when we write 
a program that pretends to be a web browser and retrieves pages, then examines the data in those pages looking for patterns.'''
### Parsing HTML using regular expressions
'''Our regular expression looks for strings that start with “href="http://” or “href="https://”, followed by one or more
characters (.+?), followed by another double quote. The question mark behind the [s]? indicates to search for the string
“http” followed by zero or one “s”.
The question mark added to the .+? indicates that the match is to be done in a “non-greedy” fashion instead of a “greedy” 
fashion. A non-greedy match tries to find the smallest possible matching string and a greedy match tries to find the largest
possible matching string.
We add parentheses to our regular expression to indicate which part of our matched string we would like to extract, and produce
the following program:'''

# Search fo link values within URL input
import urllib.request, urllib.parse, urllib.error
import re
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verigy_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
links = re.findall(b'href="(http[s]?://.*?)"', html)
for link in links:
    print(link.decode())

'''The ssl library allows this program to access web sites that strictly enforce HTTPS. The read method returns HTML
source code as a bytes object instead of returning an HTTPResponse object. The findall regular expression method will give
us a list of all of the strings that match our regular expression, returning only the link text between the double quotes.'''

##Parsing HTML using BeautifulSoup
'''Even though HTML looks like XML1 and some pages are carefully constructed to be XML, most HTML is generally broken in
ways that cause an XML parser to reject the entire page of HTML as improperly formed.
There are a number of Python libraries which can help you parse HTML and extract data from the pages. Each of the libraries
has its strengths and weaknesses and you can pick one based on your needs.
As an example, we will simply parse some HTML input and extract links using the BeautifulSoup library. BeautifulSoup tolerates 
highly flawed HTML and still lets you easily extract the data you need. You can download and install the BeautifulSoup code from:
https://pypi.python.org/pypi/beautifulsoup4
Information on installing BeautifulSoup with the Python Package Index tool pip is available at:
https://packaging.python.org/tutorials/installing-packages/
We will use urllib to read the page and then use BeautifulSoup to extract the href attributes from the anchor (a) tags.'''

