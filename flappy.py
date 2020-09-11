import pygame

from gameClasses import *
from gameVariables import *


def startScreen():
    start = True
    bird = Bird()
    base = Base(450)
    while start:

        screen.blit(bg1, (0, 0))

        if base.x2 == 0:
            base.draw()
        base.move()

        base.draw()
        bird.draw()

        screen.blit(start_img, (43, 73))
        screen.blit(font.render(str(gameScore), True, (255, 255, 255)), (115, 30))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_play()

        clock.tick(FPS)
        pygame.display.update()


def game_play():
    gameStart = True
    bird = Bird()
    pipe = [Pipe(display_width)]
    base = Base(450)

    while gameStart:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird.jump()

        rem = []
        add_pipe = False
        for p in pipe:
            if p.collision(bird.x_pos, bird.y_pos):
                print("Collide")
            if p.x + p.pipe_width < 0:
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
            base.draw()
        base.move()

        bird.move()

        screen.blit(bg1, (0, 0))
        bird.draw()
        for pi in pipe:
            pi.draw()
        base.draw()
        screen.blit(font.render(str(gameScore), True, (255, 255, 255)), (115, 30))

        clock.tick(FPS)
        pygame.display.update()


startScreen()
