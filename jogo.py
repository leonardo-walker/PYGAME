import pygame
import random

pygame.init()

display_largura = 1600
display_altura = 900


pygameDisplay= pygame.display
pygameDisplay.set_caption("Comet Space Ship")

gameDisplay = pygame.display.set_mode((display_largura, display_altura))
gameEvents = pygame.event
clock = pygame.time.Clock()

icone = pygame.image.load("resources/icon.png")
pygameDisplay.set_icon(icone)

white = (255, 255, 255)

background = pygame.image.load("resources/bg.jpg")

def game ():
    gameplay = True
    movimentoXMeteoro = random.randrange(0, display_altura)
    movimentoYMeteoro = 0
    posicaoXNave = 850
    posicaoYNave = 400
    movimentoXNave = 0
    movimentoYNave = 0
    pontos = 0
    meteoro = pygame.image.load("resources/meteoro.png")
    nave = pygame.image.load("resources/nave.png")
    larguraNave = 794
    alturaNave = 1123
    larguraMissel = 150
    alturaMissel = 52
    velocidadeNave = 10

    while True:
        for event in gameEvents.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    movimentoXNave = -velocidadeNave
                elif event.key == pygame.K_RIGHT:
                    movimentoXNave = velocidadeNave
                elif event.key == pygame.K_UP:
                    movimentoYNave = -velocidadeNave
                elif event.key == pygame.K_DOWN:
                    movimentoYNave = velocidadeNave
                elif event.key == pygame.K_RETURN:
                    gameplay()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    movimentoXNave = 0
                    movimentoYNave = 0

            if gameplay == True:
                posicaoXNave = posicaoXNave + movimentoXNave
                if posicaoXNave < 0:
                    posicaoXNave = 0
                elif posicaoXNave > display_largura - larguraNave:
                    posicaoXNave = display_largura - larguraNave

                posicaoYNave = posicaoYNave + movimentoYNave
                if posicaoYNave < 0:
                    posicaoYNave = 0
                elif posicaoYNave > display_altura - alturaNave:
                    posicaoYNave = display_altura - alturaNave
                gameDisplay.fill(white)
                gameDisplay.blit(background, (0, 0))
                gameDisplay.blit(nave, (posicaoXNave, posicaoYNave))
                gameDisplay.blit(meteoro, (movimentoXMeteoro, movimentoYMeteoro))
                

        pygame.display.update()
        clock.tick(60)

game()