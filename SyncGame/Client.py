import pygame
import socket
import threading
import sys
from Ball import Ball

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

class Player_Network:
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

        receiveThread = threading.Thread(target=self.receive, args=(self.sock, True))
        receiveThread.start()
        
        message = input("Select A or B")
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
                
                # print()
                # print(f"A: {self.player_a_position}, B: {self.player_b_position}, Ball: {self.ball_position}")
                # 
                # if is_host:
                #     print(f"Your Position A: {player_a_position}")
                # else:
                #     print(f"Your Position B: {player_b_position}")

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


class Player:
    def __init__(self, posx, posy, width, height, speed, color):
        self.posx = posx
        self.posy = posy
        self.width = width
        self.height = height
        self.speed = speed
        self.color = color
        self.geekRect = pygame.Rect(posx, posy, width, height)
        self.geek = pygame.draw.rect(screen, self.color, self.geekRect)

    def display(self):
        self.geek = pygame.draw.rect(screen, self.color, self.geekRect)

    def update(self, yFac):
        self.posy = self.posy + self.speed * yFac
        if self.posy <= 0:
            self.posy = 0
        elif self.posy + self.height >= HEIGHT:
            self.posy = HEIGHT - self.height
        self.geekRect = (self.posx, self.posy, self.width, self.height)
        
    def set_pos(self, posY):
        self.posy = posY
        self.geekRect = (self.posx, self.posy, self.width, self.height)

    def getRect(self):
        return self.geekRect
    def getPos(self):
        return self.posx, self.posy

def main():
 
    running = True
    player1 = Player(20, 0, 10, 100, 10, GREEN)
    player2 = Player(WIDTH - 30, 0, 10, 100, 10, GREEN)
    ball = Ball(pygame,screen,WIDTH // 2, HEIGHT // 2, 7, 7, WHITE,HEIGHT,WIDTH)
    
    player_network = Player_Network()
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
