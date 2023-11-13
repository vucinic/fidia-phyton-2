import socket

host = '127.0.0.1'
port = 30000

s = socket.socket()
s.connect((host, port))

message = input("type request: ")

s.send(message.encode())
data = s.recv(1024).decode()
print('Received from server: ' + data)

s.close()
