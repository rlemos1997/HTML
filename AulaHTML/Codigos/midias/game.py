import random
import pygame


# Inicializa o Pygame
pygame.init()

# Configura a tela
largura = 800
altura = 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Meu Jogo")

# Cores
preto = (0, 0, 0)
branco = (255, 255, 255)
vermelho = (255, 0, 0)

# Loop principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Preenche a tela com preto
    tela.fill(preto)

    # Desenha um retângulo vermelho
    pygame.draw.rect(tela, vermelho, (random.randint(0, largura-50), random.randint(0, altura-50), 50, 50))

    # Atualiza a tela
    pygame.display.flip()

# Finaliza o Pygame
pygame.quit()
