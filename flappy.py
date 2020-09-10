import pygame
import random

pygame.init()

display_width = 268
display_height = 512

pipe_width = 50
gap = 80
bg = pygame.image.load('bg.png')
bg1 = pygame.transform.scale(bg, (display_width,display_height))
base1 = pygame.image.load('base.png')
base2 = pygame.transform.scale(base1, (display_width, 72))

clock = pygame.time.Clock()

screen = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Flappy Bird')


# pygame.display.set_icon(icon)


class Bird:
    def __init__(self):
        self.x_pos = 50
        self.y_pos = 300

    def draw(self):
        pygame.draw.rect(screen, (255, 0, 0), (self.x_pos, self.y_pos, 30, 30))


class Pipe:
    move_speed = 5

    def __init__(self, x):
        self.x = x
        self.top_height = random.randint(20, 350)
        self.bottom_height = self.top_height + gap
        self.passed = False

    def move(self):
        self.x -= self.move_speed

    def draw_pipe(self):
        pygame.draw.rect(screen, (255, 100, 100), (self.x, 0, pipe_width, self.top_height))
        pygame.draw.rect(screen, (255, 100, 100), (self.x, self.bottom_height, pipe_width,
                                                   450 - self.bottom_height))
        pygame.draw.rect(screen, (255, 100, 100), (self.x - 10, self.bottom_height, 70, 20))
        pygame.draw.rect(screen, (255, 100, 100), (self.x - 10, self.top_height, 70, 20))


class Base:
    def __init__(self, x):
        self.x = x
        self.width = base2.get_width()
        self.x2 = self.width
        self.image = base2

    def move(self):
        self.x -= 5
        self.x2 -= 5

        if self.x + self.width < 0:
            self.x = self.x2 + self.width

        if self.x2 + self.width < 0:
            self.x2 = self.x + self.width

    def draw_base(self):
        screen.blit(self.image, (self.x, 450))
        screen.blit(self.image, (self.x2, 450))


def draw_window():
    screen.blit(bg1, (0, 0))
    base.draw_base()
    bird.draw()
    for pi in pipe:
        pi.draw_pipe()


gameStart = True
bird = Bird()
pipe = [Pipe(display_width)]
base = Base(0)

while gameStart:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pass
    rem = []
    add_pipe = False
    for p in pipe:
        if p.x + pipe_width < 0:
            rem.append(p)
        if not p.passed and p.x < bird.x_pos:
            p.passed = True
            add_pipe = True
        p.move()

    if add_pipe:
        pipe.append(Pipe(display_width))

    for r in rem:
        pipe.remove(r)

    if base.x2 == 0:
        base.draw_base()
    base.move()

    draw_window()
    print(pipe)

    clock.tick(30)
    pygame.display.update()
