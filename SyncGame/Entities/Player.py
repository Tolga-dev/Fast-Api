class Player:
    def __init__(self, posx, posy, width, height, speed, color,pygame, screen, HEIGHT):
        self.posx = posx
        self.posy = posy
        self.width = width
        self.height = height
        self.speed = speed
        self.color = color
        self.pygame = pygame
        self.screen = screen
        self.HEIGHT = HEIGHT
        self.geekRect = pygame.Rect(posx, posy, width, height)
        self.geek = pygame.draw.rect(screen, self.color, self.geekRect)

    def display(self):
        self.geek = self.pygame.draw.rect(self.screen, self.color, self.geekRect)

    def update(self, yFac):
        self.posy = self.posy + self.speed * yFac
        if self.posy <= 0:
            self.posy = 0
        elif self.posy + self.height >= self.HEIGHT:
            self.posy = self.HEIGHT - self.height
        self.geekRect = (self.posx, self.posy, self.width, self.height)

    def set_pos(self, posY):
        self.posy = posY
        self.geekRect = (self.posx, self.posy, self.width, self.height)

    def getRect(self):
        return self.geekRect

    def getPos(self):
        return self.posx, self.posy