import pygame
import random
from src.sprites import pegar_sprite

meteoro_image1 = pegar_sprite("assets/imagens/meteoro.png", 0, 0, 80, 80, 2)
meteoro_image2 = pegar_sprite("assets/imagens/meteoro.png", 0, 0, 80, 80, 1.5)
meteoro_image3 = pegar_sprite("assets/imagens/meteoro.png", 0, 0, 80, 80, 1.2)
meteoro_image4 = pegar_sprite("assets/imagens/meteoro.png", 0, 0, 80, 80, 1.0)
meteoro_image5 = pegar_sprite("assets/imagens/meteoro.png", 0, 0, 80, 80, 0.8)

meteoros = [{
    "sprite": meteoro_image1,
    "rect": meteoro_image1.get_rect(topleft=(90, -90))
}, {
    "sprite": meteoro_image2,
    "rect": meteoro_image2.get_rect(topleft=(80, -300))
}, {
    "sprite": meteoro_image3,
    "rect": meteoro_image3.get_rect(topleft=(70, -600))
}, {
    "sprite": meteoro_image4,
    "rect": meteoro_image4.get_rect(topleft=(60, -1000))
}, {
    "sprite": meteoro_image5,
    "rect": meteoro_image5.get_rect(topleft=(50, -1500))
}]

def mover_meteoros(screen, dt):
    for meteoro in meteoros:
        if not meteoro['rect'].y > screen.height: 
            meteoro['rect'].y += 350 * dt
        else: 
            redefinir_posicao(meteoro, screen)
        #if meteoro.colliderect(nave): print("das")

def redefinir_posicao(meteoro, screen):
    meteoro['rect'].y = -meteoro['rect'].height
    meteoro['rect'].x = random.randint(0, screen.width - meteoro['rect'].width)