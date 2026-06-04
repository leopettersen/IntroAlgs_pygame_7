import pygame
import random

meteoros = [pygame.Rect(90, -90, 80, 80),
            pygame.Rect(80, -300, 35, 35),
            pygame.Rect(70, -600, 30, 30),
            pygame.Rect(60, -1000, 25, 25),
            pygame.Rect(50, -1500, 20, 20)]

def mover_meteoros(screen, dt):
    for meteoro in meteoros:
        if not meteoro.y > screen.height: 
            meteoro.y += 350 * dt
        else: 
            redefinir_posicao(meteoro, screen)
        #if meteoro.colliderect(nave): print("das")

def redefinir_posicao(meteoro, screen):
    meteoro.y = -meteoro.height
    meteoro.x = random.randint(0, screen.width - meteoro.width)