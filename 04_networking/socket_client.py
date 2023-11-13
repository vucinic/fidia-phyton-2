import socket

host = '127.0.0.1'
port = 30001

s = socket.socket(
    socket.AddressFamily.AF_INET,
    socket.SOCK_STREAM
)
s.connect((host, port))

message = input("type request: ")

s.send(message.encode())
data = s.recv(1024).decode()
if data:
    print('Received from server: ' + data)
else:
    print('Error')

s.close()
