import socket
import threading

connections = []
total_connections = 0

player_a_position = [0,0]
player_b_position = [0,0]
ball_position = [0,0]

class Client(threading.Thread):
    def __init__(self, socket, address, id, name, signal):
        threading.Thread.__init__(self)
        self.socket = socket
        self.address = address
        self.id = id
        self.name = name
        self.signal = signal

    def __str__(self):
        return str(self.id) + " " + str(self.address)

    def run(self):
        global player_a_position, player_b_position, ball_position
        while self.signal:
            try:
                data = self.socket.recv(64)
            except:
                print("Client " + str(self.address) + " has disconnected")
                self.signal = False
                connections.remove(self)
                break

            if data:
                try:
                    data = data.decode("utf-8")
                    # print("ID " + str(self.id) + ": " + str(data))

                    parts = data.split(";")
                    main_info = parts[0]
                    player_id, position_str = main_info.split(":")
                    position = list(map(int, position_str.split(",")))

                    if player_id == "A":
                        player_a_position[:] = position
                    elif player_id == "B":
                        player_b_position[:] = position

                    if len(parts) > 1 and parts[1].startswith("Ball:"):
                        ball_info = parts[1].split(":")[1]
                        ball_position[:] = list(map(int, ball_info.split(",")))

                    send_data = f"{player_a_position[0]},{player_a_position[1]}:{player_b_position[0]},{player_b_position[1]}:{ball_position[0]},{ball_position[1]}"
                    print(player_id + " Sending to clients:", send_data)

                    for client in connections:
                            client.socket.sendall(send_data.encode())

                except Exception as e:
                    print("Error while parsing or sending:", e)

def newConnections(socket):
    while True:
        sock, address = socket.accept()
        global total_connections
        connections.append(Client(sock, address, total_connections, "Name", True))
        connections[len(connections) - 1].start()
        print("New connection at ID " + str(connections[len(connections) - 1]))
        total_connections += 1


def main():
    host = "127.0.0.1"
    port = 5000

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, port))
    sock.listen(5)

    newConnectionsThread = threading.Thread(target=newConnections, args=(sock,))
    newConnectionsThread.start()

main()