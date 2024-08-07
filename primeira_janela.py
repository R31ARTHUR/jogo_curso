import pygame
import sys

#inicializa o pygame
pygame.init()

#configurações da janela
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Minha primeira janela com pygame")

#loop principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Define a cor de fundo (RGB)
    screen.fill((0, 128, 255))

    # Atualiza a tela 
    pygame.display.flip()

#encerra o pygame
pygame.quit()
sys.exit        