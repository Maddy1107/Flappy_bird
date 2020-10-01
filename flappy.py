from gameClasses import *
import gameVariables


def startScreen():
    start = True
    bird = Bird()
    base = Base(450)

    while start:
        screen.blit(bg1, (0, 0))
        if base.x2 == 0:
            base.draw()
        base.move()
        bird.draw()

        base.draw()
        screen.blit(start_img, (43, 73))

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
    lost = False

    bird = Bird()
    base = Base(450)
    pipe = [Pipe(display_width)]

    while gameStart:
        screen.blit(bg1, (0, 0))
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
                lost = True
            if p.x + p.pipe_width < 0:
                rem.append(p)
            if not p.passed and p.x < bird.x_pos:
                p.passed = True
                add_pipe = True
            p.move()

        if add_pipe:
            gameVariables.gameScore += 1
            pipe.append(Pipe(display_width))

        for r in rem:
            pipe.remove(r)

        if base.x2 == 0:
            base.draw()
        base.move()
        bird.draw()

        for pi in pipe:
            pi.draw()
        base.draw()
        bird.move()
        screen.blit(font.render(str(gameVariables.gameScore), True, (255, 255, 255)), (115, 30))

        if lost:
            GameOver()

        clock.tick(FPS)
        pygame.display.update()


def GameOver():
    gameOver = True

    while gameOver:
        screen.blit(over_img, (10, 10))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    gameVariables.gameScore = 0
                    startScreen()

        pygame.display.update()


startScreen()
