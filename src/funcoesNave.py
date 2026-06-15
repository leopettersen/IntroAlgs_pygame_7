import pygame
from src.sprites import pegar_sprite

class Nave:
    def __init__(self, x=295, y=400):
        self.sprite = pegar_sprite(
            "assets/imagens/nave.png",
            0, 0, 496, 423, 0.135
        )

        self.rect = self.sprite.get_rect(
            topleft=(x, y)
        )

        self.velocidade = 450

    def mover(self, screen, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            if self.rect.left > 30:
                self.rect.x -= self.velocidade * dt

        if keys[pygame.K_d]:
            if self.rect.right < screen.get_width() - 30:
                self.rect.x += self.velocidade * dt

    def desenhar(self, screen):
        screen.blit(
            self.sprite,
            self.rect
        )