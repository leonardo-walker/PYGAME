import pygame
import random

pygame.init()

display_largura = 800
display_altura = 450
tamanho_tela=(display_largura, display_altura)


pygameDisplay = pygame.display
pygameDisplay.set_caption("Comet SpaceShip")

gameDisplay = pygame.display.set_mode(tamanho_tela)
gameEvents = pygame.event
clock = pygame.time.Clock()

icone = pygame.image.load("resources/icon.png")
pygameDisplay.set_icon(icone)

white = (255, 255, 255)

background = pygame.image.load("resources/bg.jpg")
background = pygame.transform.scale(background, (800, 450))

def perdeu(pontos):
    gameDisplay.blit(background, (0,0))
    pygame.mixer.music.stop()
    fonte = pygame.font.Font("freesansbold.ttf", 100)
    texto = fonte.render("Pontos: "+str(pontos), True, white)
    gameDisplay.blit(texto, (287, 125))
    fonteContinue = pygame.font.Font("freesansbold.ttf", 30)
    textoContinue = fonteContinue.render("Press enter to restart...", True, white)
    gameDisplay.blit(textoContinue, (312,250))

    pygameDisplay.update()

def game():
    gameplay = True
    movimentoXMeteoro = movimentoX = random.randrange(0, display_largura)
    movimentoYMeteoro = -185
    velocidade = 10
    direcao = True
    posicaoXNave = 740
    posicaoYNave = 750
    movimentoXNave = 0
    movimentoYNave = 0
    pontos = 0
    pontosMorrer = 2
    meteoro = pygame.image.load("resources/meteoro.png")
    meteoro = pygame.transform.scale(meteoro, (36, 68))
    nave = pygame.image.load("resources/nave.png")
    nave = pygame.transform.scale(nave, (88, 95))
    larguraNave = 88
    alturaNave = 95
    larguraMeteoro = 36
    alturaMeteoro = 68
    velocidadeNave = 50

    while True:
        for event in gameEvents.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a :
                    movimentoXNave = -velocidadeNave
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    movimentoXNave = velocidadeNave
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    movimentoYNave = -velocidadeNave
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    movimentoYNave = velocidadeNave
                elif event.key == pygame.K_RETURN:
                    game()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_a or event.key == pygame.K_w or event.key == pygame.K_s or event.key == pygame.K_d :
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
                gameDisplay.blit(
                    meteoro, (movimentoXMeteoro, movimentoYMeteoro))
                    
                
                if direcao == True:
                    if movimentoYMeteoro < 450 :
                        movimentoYMeteoro = movimentoYMeteoro + velocidade
                        
                    
                    else:
                        movimentoYMeteoro = -185
                        movimentoXMeteoro = random.randrange(0, display_largura-larguraMeteoro)
                        velocidade = velocidade + 1
                        pontos+=1
                
                fonte = pygame.font.Font('freesansbold.ttf', 20)
                texto = fonte.render("Pontos: "+str(pontos), True, white)
                gameDisplay.blit(texto, (20, 5))
                vidas = fonte.render("Vidas: "+str(pontosMorrer), True, white)
                gameDisplay.blit(vidas, (20, 30))

       
                #colisão        
                naveRect = nave.get_rect()
                naveRect.x = posicaoXNave
                naveRect.y = posicaoYNave

                meteoroRect = meteoro.get_rect()
                meteoroRect.x = movimentoXMeteoro 
                meteoroRect.y = movimentoYMeteoro-22

                if naveRect.colliderect(meteoroRect) == True:
                    gameplay = True
                    pontosMorrer -=1
                    movimentoYMeteoro = -185
                    movimentoXMeteoro = random.randrange(0, display_largura)
                if pontosMorrer == 0:
                    perdeu(pontos)
                    gameplay = False
                else:    
                    direcao = True
        print(pontos)    

        pygameDisplay.update()
        clock.tick(60)
game()
