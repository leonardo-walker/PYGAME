import pygame
import random

pygame.init()

display_largura = 800
display_altura = 600

gameDisplay = pygame.display.set_mode((display_largura, display_altura))
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.display.update()
    clock.tick(60)
