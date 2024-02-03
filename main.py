import pygame

#Inicializando o pyGame
pygame.init()

#Criando a Janela
screen = pygame.display.set_mode((800, 600))

#Loop do Jogo
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False