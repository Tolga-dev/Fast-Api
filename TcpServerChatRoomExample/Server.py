import os
import socket
import threading


class Server(threading.Thread):

    def __init__(self, host, port):
        super().__init__()
        self.host = host
        self.port = port
        self.connections = []

    def run(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind((self.host, self.port))

        sock.listen(1)
        print('Listening at', sock.getsockname())

        while True:
            sc, sockname = sock.accept()
            print("Accept a new connection from {} to {}".format(sc.getpeername(), sc.getsockname()))

            server_socket = ServerSocket(sc, sockname, self)
            server_socket.start()

            self.connections.append(server_socket)
            print("Ready to receive messages from", sc.getpeername())

    def broadcast(self, message, source):
        for connection in self.connections:
            if connection.sockname != source:
                connection.send(message)

    def remove_connection(self, connection):
        self.connections.remove(connection)


class ServerSocket(threading.Thread):
    def __init__(self, sc, sockname, server):
        super().__init__()
        self.sc = sc
        self.sockname = sockname
        self.server = server

    def run(self):
        while True:
            message = self.sc.recv(1024).decode('ascii')
            if message:
                print("{} says {!r}".format(self.sockname, message))
                self.server.broadcast(message, self.sockname)
            else:
                print("{} has closed the connection".format(self.sockname))
                self.sc.close()
                self.server.remove_connection(self)
                return

    def send(self, message):
        self.sc.sendall(message.encode('ascii'))


def exit(server):
    while True:
        ipt = input('')
        if ipt == 'q':
            print("Closing all connections...")
            for connection in server.connections:
                connection.sc.close()
            print("Shutting down the server...")
            os._exit(0)


if __name__ == '__main__':
    server = Server("127.0.0.1", 5000)
    server.start()

    exit = threading.Thread(target=exit, args=(server,))
    exit.start()
