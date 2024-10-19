import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH


def main():
    pygame.init()
    gameClock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        pygame.display.flip()
        gameClock.tick(60)
        dt = 1000 / gameClock.tick(60)
        print(dt)


if __name__ == "__main__":
    main()
