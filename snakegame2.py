import os
import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Cores
olivegreen = (140, 165, 110)

# 1. Carregamento e redimensionamento direto (Sem código redundante)
img_head = pygame.transform.scale(
    pygame.image.load("assets/head_edited.png").convert_alpha(), (20, 20)
)
img_midbody = pygame.transform.scale(
    pygame.image.load("assets/midbody_edited.png").convert_alpha(), (20, 20)
)
img_tail = pygame.transform.scale(
    pygame.image.load("assets/tail_edited.png").convert_alpha(), (20, 20)
)

fullbody = [img_head, img_midbody, img_tail]

# 2. Rects alinhados no grid de 20px (Cabeça em 400, Corpo em 380, Rabo em 360)
headr = img_head.get_rect(topleft=(400, 300))
midbodyr = img_midbody.get_rect(topleft=(380, 300))
tailr = img_tail.get_rect(topleft=(360, 300))

snake = [headr, midbodyr, tailr]

# Direção inicial (Começa parada)
dir = [0, 0]

running = True
while running:
    # Captura de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and dir != [0, 20]:
                dir = [0, -20]
            elif event.key == pygame.K_DOWN and dir != [0, -20]:
                dir = [0, 20]
            elif event.key == pygame.K_LEFT and dir != [20, 0]:
                dir = [-20, 0]
            elif event.key == pygame.K_RIGHT and dir != [-20, 0]:
                dir = [20, 0]

    # Lógica de movimentação (Apenas se a cobra estiver se movendo)
    if dir != [0, 0]:
        snakehead = snake[0].copy()
        snakehead.move_ip(dir)
        snake.insert(0, snakehead)
        snake.pop()

    # RENDERIZAÇÃO
    screen.fill(olivegreen)

    # Desenha cada parte da cobra com o sprite correto
    for i, segment in enumerate(snake):
        if i == 0:
            screen.blit(fullbody[0], segment)  # Cabeça
        elif i == len(snake) - 1:
            screen.blit(fullbody[2], segment)  # Rabo
        else:
            screen.blit(fullbody[1], segment)  # Corpo

    pygame.display.flip()
    clock.tick(10)

pygame.quit()