import pygame

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

#função que cria a nave
def player():
    screen.blit(playerImg, (playerX, playerY))

# Loop do jogo
running = True
while running:
    
    #Cor da tela
    screen.fill((0, 0, 0))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Preenche a tela com a cor vermelha

    #chamando player na tela
    player()
    # Atualiza a tela
    pygame.display.update()