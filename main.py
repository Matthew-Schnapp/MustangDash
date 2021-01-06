import threading
import sys
import pygame

BLACK = pygame.Color('black')
WHITE = pygame.Color('white')
TURQUOISE = pygame.Color(35, 200, 170);


def tprint(string):
    print(string)


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((700, 700))
    clock = pygame.time.Clock()



    ticks = 30
    i = 0
    j = 5

    while True:
        screen.fill(WHITE)
        rectangle = pygame.Rect(i, i, j, j)
        pygame.draw.rect(screen, BLACK, rectangle, 4)
        pygame.display.flip()

        i = i+5
        j = (j+1)%50 + 5

        clock.tick(ticks)
