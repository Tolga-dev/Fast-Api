import os
import socket
import threading

class Server(threading.Thread):
    def __init__(self, host, port):
        super().__init__()
        self.host = host
        self.port = port
        self.connections = []

    def start(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind((self.host, self.port))
        sock.listen()
        print('Listening at', sock.getsockname())

        while True:
            sc, sockname = sock.accept()
            print(f"Accepted connection from {sc.getpeername()} to {sc.getsockname()}")
            server_socket = ServerSocket(sc, sockname, self)
            self.connections.append(server_socket)
            print("Ready to receive messages from", sc.getpeername())

    def broadcast(self, message, source):
        for connection in self.connections:
            if connection.sockname != source:
                connection.send(message)

    def remove_connection(self, connection):
        connection.stop()
        self.connections.remove(connection)

class ServerSocket:
    def __init__(self, sc, sockname, server):
        self.sc = sc
        self.sockname = sockname
        self.server = server
        self.thread = threading.Thread(target=self.start)
        self.thread.start()

    def start(self):
        try:
            while True:
                message = self.sc.recv(1024).decode('ascii')
                if message:
                    print(f"{self.sockname} says {message!r}")
                    self.server.broadcast(message, self.sockname)
                else:
                    print(f"{self.sockname} has closed the connection")
                    self.stop()
                    break
        except Exception as e:
            print(f"Error with {self.sockname}: {e}")
            self.stop()

    def stop(self):
        try:
            self.sc.close()
            self.server.remove_connection(self)
        except:
            pass

    def send(self, message):
        self.sc.sendall(message.encode('ascii'))

def exit_from_server(inited_server):
    while True:
        ipt = input()
        if ipt.strip().lower() == 'q':
            print("Closing all connections...")
            for connection in inited_server.connections:
                connection.stop()
            print("Shutting down the server...")
            os._exit(0)

if __name__ == '__main__':
    server = Server("127.0.0.1", 5000)
    server.start()

    exit_thread = threading.Thread(target=exit_from_server, args=(server,))
    exit_thread.start()
