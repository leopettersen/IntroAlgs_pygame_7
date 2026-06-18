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
        
        self.quantidade_missil = 15
        self.misseis = []
        self.index_missil = 0
        for i in range (self.quantidade_missil):
            self.misseis.append(pygame.Rect(-5, -5, 5, 5))
        self.missil_cooldown = 0

        self.velocidade = 450

    def mover(self, screen, dt):
        keys = pygame.key.get_pressed()

        if(self.missil_cooldown == 13): self.missil_cooldown = 0
        else: self.missil_cooldown += 1
        
        if keys[pygame.K_a]:
            if self.rect.left > 30:
                self.rect.x -= self.velocidade * dt

        if keys[pygame.K_d]:
            if self.rect.right < screen.get_width() - 30:
                self.rect.x += self.velocidade * dt
                
        if keys[pygame.K_SPACE]:
            if self.missil_cooldown >= 13:
                self.atirar()
            
        self.mover_missil(dt)
    
    def mover_missil(self, dt):
        for i in range (len(self.misseis)):
            
            self.misseis[i].y -= self.velocidade * dt/2 

    def desenhar(self, screen):
        screen.blit(
            self.sprite,
            self.rect
        )
        for missil in self.misseis:
            pygame.draw.rect(screen, (255, 0, 255), missil)

    def atirar(self):
        self.misseis[self.index_missil].x = (self.rect.x + self.rect.x  + self.rect.width)/2
        self.misseis[self.index_missil].y = self.rect.y
        if self.index_missil < self.quantidade_missil - 1:
            self.index_missil += 1
        else:
            self.index_missil = 0
            
    def get_misseis(self):
        return self.misseis