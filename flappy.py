import pygame, random

pygame.init()

display_width = 400
display_height = 600

pipe_width = 50
gap = 80

clock = pygame.time.Clock()

screen = pygame.display.set_mode((display_width, display_height))


class Bird:

    def __init__(self):
        self.x_pos = 50
        self.y_pos = 300

    def draw(self):
        pygame.draw.rect(screen, (255, 255, 255), (int(self.x_pos), int(self.y_pos), 30, 30))


class Pipe:
    def __init__(self, pipe_start_pos):
        self.pipe_start_pos = pipe_start_pos
        self.top_height = random.randint(20, 500)
        self.bottom_height = self.top_height + gap

    def move(self):
        self.pipe_start_pos -= 1

    def draw_pipe(self):
        pygame.draw.rect(screen, (255, 255, 255), (self.pipe_start_pos, 0, pipe_width, self.top_height))
        pygame.draw.rect(screen, (255, 255, 255), (self.pipe_start_pos, self.bottom_height, pipe_width,
                                                   display_height))


def draw_window():
    screen.fill((0, 0, 0))
    bird.draw()
    for p in pipe:
        p.draw_pipe()


gameStart = True
bird = Bird()
pipe = [Pipe(display_width)]

while gameStart:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pass

    for p in pipe:
        if p.pipe_start_pos == 100:
            pipe.append(Pipe(display_width))
        p.move()

    draw_window()

    clock.tick(60)
    pygame.display.update()
