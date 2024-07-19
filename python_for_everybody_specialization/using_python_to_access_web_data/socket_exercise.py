import socket

#   create the connection
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#   connect to data.pr4e.org host through port 80
sock.connect(('data.pr4e.org', 80))
#   encode() function converts the unicode from the Python string to utf-8, before sending it
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
#   send the command through the socket
sock.send(cmd)

while True:
    #   ask to receive up to 512 characters and get that back
    data = sock.recv(512)
    #   if we don't get data back when we reached the end of file then quit (break)
    if len(data) < 1:
        break
    #   otherwise, print the decoded the utf-8 encoded data into unicode
    print(data.decode())

#   close the connection
sock.close()