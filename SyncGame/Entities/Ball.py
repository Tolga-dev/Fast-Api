
class Ball:
    def __init__(self, pygame, screen,posx, posy, radius, speed, color, HEIGHT, WIDTH):
        self.pygame = pygame
        self.HEIGHT = HEIGHT
        self.WIDTH = WIDTH
        self.screen = screen
        self.posx = posx
        self.posy = posy
        self.radius = radius
        self.speed = speed
        self.color = color
        self.xFac = 1
        self.yFac = -1
        self.ball = pygame.draw.circle(screen, self.color, (self.posx, self.posy), self.radius)
        self.firstTime = 1

    def display(self):
        self.ball = self.pygame.draw.circle(self.screen, self.color, (self.posx, self.posy), self.radius)

    def update(self):
        self.posx += self.speed * self.xFac
        self.posy += self.speed * self.yFac

        if self.posy <= 0 or self.posy >= self.HEIGHT:
            self.yFac *= -1

        if self.posx <= 0 and self.firstTime:
            self.firstTime = 0
            return 1
        elif self.posx >= self.WIDTH and self.firstTime:
            self.firstTime = 0
            return -1
        else:
            return 0
    def set_pos(self,pos):
        self.posx = pos[0]
        self.posy = pos[1]

    def reset(self):
        self.posx = self.WIDTH // 2
        self.posy = self.HEIGHT // 2
        self.xFac *= -1
        self.firstTime = 1

    def hit(self):
        self.xFac *= -1

    def getRect(self):
        return self.ball
    def get_pos(self):
        return self.posx, self.posy