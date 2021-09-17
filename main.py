import pygame
from pygame.constants import K_DOWN

HEIGHT = 720
WIDTH = 1280
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PINGPONG")
WHITE = (255, 255, 255)


class Ball:
    def __init__(self) -> None:
        self.x = WIDTH//2
        self.y = HEIGHT//2
        self.radius = 5
        self.velx = 10
        self.vely = 5

    def draw(self, win):
        pygame.draw.circle(win, WHITE, (self.x, self.y), self.radius)

    def bounce(self):
        self.velx = 0
        self.vely = 0

    def move(self):
        self.x += self.velx
        self.y += self.vely


class Player:
    def __init__(self, x) -> None:
        self.width = 5
        self.height = 150
        self.x = x
        self.y = (HEIGHT//2)+(self.height//2)
        self.vel = 20

    def draw(self, win):
        pygame.draw.rect(win, WHITE, (self.x, self.y, self.width, self.height))


def draw(win, p1, p2, ball):
    win.fill((0, 0, 0))
    ball.draw(win)
    p1.draw(win)
    p2.draw(win)
    pygame.display.update()
    pygame.display.flip()


def main():
    running = True
    clock = pygame.time.Clock()
    FPS = 75
    P1 = Player(10)
    P2 = Player(WIDTH-10)
    ball = Ball()

    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        keys = pygame.key.get_pressed()
        # print(P1.y)
        if keys[pygame.K_SPACE] == 1:
            ball = Ball()
        if 0 <= P1.y:
            P1.y -= (keys[pygame.K_w])*P1.vel
        if P1.y <= HEIGHT-P1.height:
            P1.y += (keys[pygame.K_s])*P1.vel

        if 0 <= P2.y:
            P2.y -= (keys[pygame.K_UP])*P2.vel
        if P2.y <= HEIGHT-P2.height:
            P2.y += (keys[pygame.K_DOWN])*P2.vel

        if ball.y <= 0 or ball.y > HEIGHT:
            ball.vely = -ball.vely
        if (ball.x == P1.x and P1.y <= ball.y <= P1.y+P1.height) or (ball.x == P2.x and P2.y <= ball.y <= P2.y+P2.height):
            ball.velx = -ball.velx

        ball.move()
        draw(win, P1, P2, ball)


if __name__ == "__main__":
    main()
