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

#Background
background = pygame.image.load("img/background.png")

#Adicionando Nave
playerImg = pygame.image.load("img/player.png")
playerX = 370
playerY = 480
playerX_change = 0

#Adicionando aliens
enemyImg = pygame.image.load("img/enemy.png")
enemyX = random.randint(0, 800)
enemyY = random.randint(50, 150)
enemyX_change = 1.5
enemyY_change = 40

#Adicionando míssil
bulletImg = pygame.image.load("img/bullet.png")
bulletX = 0
bulletY = 480
bulletX_change = 4
bulletY_change = 40
bullet_state = "ready"

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16 , y + 10))


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
    
    #adicionando imagem de fundo
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Vericar qual qual seta esta sendo clicada
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletX = playerX
                    fire_bullet(playerX, bulletY)
        
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
        enemyX_change = 1.5
        enemyY += enemyY_change
    elif enemyX >= 710:
        enemyX_change = -1.5
        enemyY += enemyY_change

    #Movimento do míssil
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state is "fire":
        fire_bullet(playerX, bulletY)
        bulletY -= bulletX_change

    #chamando player na tela
    player(playerX, playerY)
    
    #chamando alien na tela
    enemy(enemyX, enemyY)
    
    # Atualiza a tela
    pygame.display.update()