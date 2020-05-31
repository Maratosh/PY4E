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
###############

