import random
from gameVariables import *


# Bird Class
class Bird:
    IMG = bird_image

    def __init__(self):
        self.x_pos = 50
        self.y_pos = 225
        self.gravity = 5
        self.img_count = 0
        self.image = self.IMG[0]

    def jump(self):
        self.y_pos -= self.gravity * 10

    def move(self):
        self.y_pos += self.gravity

    def draw(self):
        self.img_count += 1
        # if pygame.time.get_ticks() % 240 <= 80:
        #     self.image = self.IMG[2]
        # elif 80 <= pygame.time.get_ticks() % 240 <= 160:
        #     self.image = self.IMG[1]
        # elif 160 <= pygame.time.get_ticks() % 240 <= 240:
        #     self.image = self.IMG[0]
        # else:
        #     self.image = self.IMG[1]
        if self.img_count < 5:
            self.image = self.IMG[0]
        elif self.img_count <= 10:
            self.image = self.IMG[1]
        elif self.img_count <= 15:
            self.image = self.IMG[2]
        elif self.img_count <= 20:
            self.image = self.IMG[1]
        else:
            self.image = self.IMG[1]
            self.img_count = 0
        screen.blit(self.image, (self.x_pos, self.y_pos))


# Pipe Class
class Pipe:
    move_speed = 2
    pipe_width = pipe_image[0].get_width()
    pipe_height = pipe_image[0].get_height()
    bird_height = bird_image[0].get_height()
    bird_width = pipe_image[0].get_width()
    gap = 4 * bird_height

    def __init__(self, x):
        self.x = x
        self.top_height = random.randint(50, 300) - self.pipe_height
        self.bottom_height = self.top_height + self.gap + self.pipe_height
        self.passed = False

    def move(self):
        self.x -= self.move_speed

    def draw(self):
        screen.blit(pipe_image[0], (self.x, self.top_height))
        screen.blit(pipe_image[1], (self.x, self.bottom_height))

    def collision(self, bx, by):
        x_valid = bx + self.bird_width > self.x and bx < self.x + self.pipe_width
        y_valid = by + self.bird_height > self.bottom_height or by < self.top_height + self.pipe_height

        return x_valid and y_valid


# Base Class
class Base:
    move_speed = 2

    def __init__(self, y):
        self.x = 0
        self.y = y
        self.width = base2.get_width()
        self.x2 = self.width

    def move(self):
        self.x -= self.move_speed
        self.x2 -= self.move_speed

        if self.x + self.width < 0:
            self.x = self.x2 + self.width

        if self.x2 + self.width < 0:
            self.x2 = self.x + self.width

    def draw(self):
        screen.blit(base2, (self.x, self.y))
        screen.blit(base2, (self.x2, self.y))
