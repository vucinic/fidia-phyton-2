import socketserver


class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        print('Start serving')
        data = self.request.recv(1024).strip()
        host, port = self.client_address
        print('Received connection from', host, port)
        print('Request from client', data.decode())
        msg = input("type response: ")
        self.request.sendall(msg.encode())


if __name__ == "__main__":
    HOST, PORT = "localhost", 30001
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        server.serve_forever()

