import threading
import sys
import pygame

BLACK = pygame.Color('black')
WHITE = pygame.Color('white')

def tprint(string):
    print(string)

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((500, 700))
    clock = pygame.time.Clock()

    ticks = 30
    while(True):
        screen.fill(WHITE)
        pygame.display.flip()
        clock.tick(ticks)

        screen.fill(BLACK)
        pygame.display.flip()
        clock.tick(ticks)
