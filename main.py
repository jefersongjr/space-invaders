import pygame
import random

# Inicializando o pygame
pygame.init()

# Criando a janela
screen = pygame.display.set_mode((800, 600))

# Adicionando título
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("img/ufo.png")
pygame.display.set_icon(icon)

#Adicionando Nave
playerImg = pygame.image.load("img/player.png")
playerX = 370
playerY = 480
playerX_change = 0

#Adicionando aliens

enemyImg = pygame.image.load("img/enemy.png")
enemyX = random.randint(0, 800)
enemyY = random.randint(50, 150)
enemyX_change = 0.3
enemyY_change = 40


#função que cria a nave
def player(x, y):
    screen.blit(playerImg, (x, y))

#função que cria a nave
def enemy(x, y):
    screen.blit(enemyImg, (x, y))

# Loop do jogo
running = True
while running:
    
    #Cor da tela
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Vericar qual qual seta esta sendo clicada
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.1
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
 

    # adicionando movimento ao eixo horizontal
    playerX += playerX_change

    # evitando que o nava saia do limite da tela
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX =736


    # adicionando movimento ao eixo horizontal do inimigo
    enemyX += enemyX_change

    # evitando que o inimigo saia do limite da tela
    if enemyX <= -20:
        enemyX_change = 0.3
        enemyY += enemyY_change
    elif enemyX >= 710:
        enemyX_change = -0.3
        enemyY += enemyY_change

    #chamando player na tela
    player(playerX, playerY)
    
    #chamando alien na tela
    enemy(enemyX, enemyY)
    
    # Atualiza a tela
    pygame.display.update()