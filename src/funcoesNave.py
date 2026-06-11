import pygame

from src.sprites import pegar_sprite
nave_image = pegar_sprite("assets/imagens/nave.png", 0, 0, 496, 423, 0.135)
nave = {
            "sprite": nave_image,
            "rect": nave_image.get_rect(topleft = (295, 400)) 
        }
vel_nave = 450

def mover_nave(screen, dt):
    """Move a nave para a esquerda ou direita com base na entrada do jogador."""
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        if not nave['rect'].x < 30: 
            nave['rect'].x -= vel_nave * dt
    if keys[pygame.K_d]:
        if not nave['rect'].x > screen.width - nave['rect'].width - 30:
            nave['rect'].x += vel_nave * dt