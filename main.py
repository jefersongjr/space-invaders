import pygame
import random
import math

# Inicializando o pygame
pygame.init()

# Criando a janela
screen = pygame.display.set_mode((800, 600))

# Adicionando título
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("img/ufo.png")
pygame.display.set_icon(icon)

# Background
background = pygame.image.load("img/background.png")

# Adicionando Nave
playerImg = pygame.image.load("img/player.png")
playerX = 370
playerY = 480
playerX_change = 0

# Adicionando aliens
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load("img/enemy.png"))
    enemyX.append(random.randint(0, 800))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(1.5)
    enemyY_change.append(40)

# Adicionando míssil
bulletImg = pygame.image.load("img/bullet.png")
bulletX = 0
bulletY = 480
bulletX_change = 4
bulletY_change = 40
bullet_state = "ready"

# Pontuação
score = 0

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))

# função que cria a nave
def player(x, y):
    screen.blit(playerImg, (x, y))

# função que cria o inimigo
def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow((enemyX + 60) - bulletX, 2) + (math.pow((enemyY + 32) - bulletY, 2)))
    if distance < 60 and bullet_state == "fire":
        return True
    return False

# Loop do jogo
running = True
while running:
    # Cor da tela
    screen.fill((0, 0, 0))

    # adicionando imagem de fundo
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Verificar qual seta está sendo clicada
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -3
            if event.key == pygame.K_RIGHT:
                playerX_change = 3
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletX = playerX
                    fire_bullet(playerX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # adicionando movimento ao eixo horizontal
    playerX += playerX_change

    # evitando que o nave saia do limite da tela
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # adicionando movimento ao eixo horizontal do inimigo
    for i in range(num_of_enemies):
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= -20:
            enemyX_change[i] = 1.5
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 710:
            enemyX_change[i] = -1.5
            enemyY[i] += enemyY_change[i]

        # Colisão
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = 480
            bullet_state = "ready"
            score += 1
            print(score)
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(50, 150)

        # chamando alien na tela
        enemy(enemyX[i], enemyY[i], i)

    # Movimento do míssil
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(playerX, bulletY)
        bulletY -= bulletX_change

    # chamando player na tela
    player(playerX, playerY)

    # Atualiza a tela
    pygame.display.update()