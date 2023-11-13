import socket

s = socket.socket(socket.AddressFamily.AF_INET, socket.SOCK_STREAM)

host = ('127.0.0.1', 30000)

s.bind(host)

print('Server listens on', host)
s.listen()

while True:
    print('Server waiting for connections')
    conn_socket, addr = s.accept()

    print('Received connection from', addr)
    data = conn_socket.recv(1024).decode()

    if data:
        data = str(data).upper()
        print("\trequest from client: " + str(data))

        data = input("type response: ")
        conn_socket.send(data.encode())

    conn_socket.close()
