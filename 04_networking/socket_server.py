import socket

s = socket.socket(
    socket.AddressFamily.AF_INET,
    socket.SOCK_STREAM)

host = ('127.0.0.1', 30_000)

s.bind(host)

print('Server listens on', host)
s.listen()

while True:
    print('Server waiting for connections')
    conn_socket, addr = s.accept()

    print('Received connection from', addr)

    buf = bytes()
    is_first = True
    data = bytes
    while len(data) == 1024 or is_first:
        is_first = False
        data = conn_socket.recv(1024)
        buf = b''.join([buf, data])

    if data is not None:
        msg = str(buf).upper()
        print("\trequest from client: " + str(msg))

        resp = input("type response: ")
        conn_socket.send(resp.encode())
    else:
        print('Connection closed by client', data)
    conn_socket.close()


