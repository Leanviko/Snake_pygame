import pygame, sys

pygame.init()
screen_width = 400
screen_height = 500
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()

while True:

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
        
        pygame.display.update()
        clock.tick(60)