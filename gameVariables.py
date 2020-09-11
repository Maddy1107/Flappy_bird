import pygame

pygame.init()
clock = pygame.time.Clock()
FPS = 30

# Display Size
display_width = 270
display_height = 512

# Images
bird_image = [

    pygame.image.load('assets/upflap.png'),
    pygame.image.load('assets/midflap.png'),
    pygame.image.load('assets/downflap.png')

]
pipe_image = [
    pygame.image.load('assets/pipe-up.png'),
    pygame.image.load('assets/pipe-down.png'),
]
bg = pygame.image.load('assets/bg.png')
bg1 = pygame.transform.scale(bg, (display_width, display_height))
base1 = pygame.image.load('assets/base.png')
base2 = pygame.transform.scale(base1, (display_width, 72))
start_img = pygame.image.load('assets/start.png')

# Screen
screen = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Flappy Bird')

# Fonts
font = pygame.font.Font('assets/Option_f.ttf', 50)

gameScore = 0
