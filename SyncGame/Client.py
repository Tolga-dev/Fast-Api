import pygame
import socket
import threading
import sys
from Entities.Ball import Ball
from Entities.Player import Player

pygame.init()

font20 = pygame.font.Font('freesansbold.ttf', 20)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()
FPS = 30
is_host = True

class PlayerNetwork:
    def __init__(self):
        global is_host
        self.host = "127.0.0.1"
        self.port = 5000
        self.player_a_position = [0, 0]
        self.player_b_position = [0, 0]
        self.ball_position = [0, 0]
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect((self.host, self.port))
        except:
            print("Could not make a connection to the server")
            input("Press enter to quit")
            sys.exit(0)

        receive_thread = threading.Thread(target=self.receive, args=(self.sock, True))
        receive_thread.start()
        
        message = input("Select Host(A) or Client(B) | if you press wrong, restart script:")
        if message != 'A':
            is_host = False
        
    def receive(self,socket, signal):
        while signal:
            try:
                data = socket.recv(1024).decode("utf-8")  # increased buffer size for safety

                parts = data.strip().split(":")
                if len(parts) != 3:
                    print("Invalid data format:", data)
                    continue

                self.player_a_position = list(map(int, parts[0].split(",")))
                self.player_b_position = list(map(int, parts[1].split(",")))
                self.ball_position = list(map(int, parts[2].split(",")))

            except Exception as e:
                print("Disconnected from server:", e)
                signal = False
                break

    def send(self, player_pos, ball_pos):
        message = str(player_pos[0]) + "," + str(player_pos[1])
        player_id = "A" if is_host else "B"
        payload = f"{player_id}:{message}"  # A:200,200

        if is_host:
            payload += f";Ball:{ball_pos[0]},{ball_pos[1]}"
        self.sock.sendall(payload.encode())

def main():
 
    running = True
    player1 = Player(20, 0, 10, 100, 10, GREEN, pygame, screen, HEIGHT)
    player2 = Player(WIDTH - 30, 0, 10, 100, 10, GREEN, pygame, screen, HEIGHT)
    ball = Ball(pygame,screen,WIDTH // 2, HEIGHT // 2, 7, 7, WHITE,HEIGHT,WIDTH)
    
    player_network = PlayerNetwork()
    if is_host:
        player_network.send(player1.getPos(), ball.get_pos())
    else:
        player_network.send(player2.getPos(), [0,0])
    
    listOfGeeks = [player1, player2]
    playerInput = 0

    while running:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    playerInput = -1
                if event.key == pygame.K_s:
                    playerInput = 1
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    playerInput = 0

        for geek in listOfGeeks:
            if pygame.Rect.colliderect(ball.getRect(), geek.getRect()):
                ball.hit()

        if is_host:

            player1.update(playerInput)
            point = ball.update()
            if point:
                ball.reset()
                
            player2.set_pos(player_network.player_b_position[1])
            
            player_network.player_a_position = player1.getPos()
            player_network.ball_position = ball.get_pos()
            player_network.send(player_network.player_a_position,player_network.ball_position)

        else:
            player2.update(playerInput)
            
            player1.set_pos(player_network.player_a_position[1])
            ball.set_pos(player_network.ball_position)
            
            player_network.player_b_position = player2.getPos()
            player_network.send(player_network.player_b_position,player_network.ball_position)
        
        player1.display()
        player2.display()
        ball.display()
        pygame.display.update()

        clock.tick(FPS)

if __name__ == "__main__":
    main()
    pygame.quit()
