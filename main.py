import pygame
import sys
from constants import *
from player import *

def main():
    print('Starting asteroids!')
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')
    pygame.init()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        player.update(dt)
        screen.fill((0, 0, 0))
        player.draw(screen)  
        pygame.display.flip()
        dt = clock.tick(60) / 1000

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
