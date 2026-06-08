import random
from src.sprites import pegar_sprite
from src.funcoesJogo import calcular_pontos

meteoro1_image = pegar_sprite("assets/imagens/meteoro.png", 0, 0, 38, 33, 1.5)
meteoro2_image = pegar_sprite("assets/imagens/meteoro.png", 0, 0, 38, 33, 1.5)
meteoro3_image = pegar_sprite("assets/imagens/meteoro.png", 0, 0, 38, 33, 1.5)
meteoro4_image = pegar_sprite("assets/imagens/meteoro.png", 0, 0, 38, 33, 1.5)
meteoro5_image = pegar_sprite("assets/imagens/meteoro.png", 0, 0, 38, 33, 1.5)

frames_explosao = [
    pegar_sprite("assets/imagens/Exxplode.png", 0, 0, 92, 96, 1.5),
    pegar_sprite("assets/imagens/Exxplode.png", 0, 0, 92, 96, 1.5),
    pegar_sprite("assets/imagens/Exxplode.png", 92, 0, 92, 96, 1.5),
    pegar_sprite("assets/imagens/Exxplode.png", 92, 0, 92, 96, 1.5),
    pegar_sprite("assets/imagens/Exxplode.png", 184, 0, 92, 96, 1.5),
    pegar_sprite("assets/imagens/Exxplode.png", 184, 0, 92, 96, 1.5),
    pegar_sprite("assets/imagens/Exxplode.png", 276, 0, 92, 96, 1.5),
    pegar_sprite("assets/imagens/Exxplode.png", 276, 0, 92, 96, 1.5),
    pegar_sprite("assets/imagens/Exxplode.png", 368, 0, 92, 96, 1.5),
    pegar_sprite("assets/imagens/Exxplode.png", 368, 0, 92, 96, 1.5),
    pegar_sprite("assets/imagens/Exxplode.png", 460, 0, 92, 96, 1.5),
    pegar_sprite("assets/imagens/Exxplode.png", 460, 0, 92, 96, 1.5),
    pegar_sprite("assets/imagens/Exxplode.png", 552, 0, 92, 96, 1.5),
    pegar_sprite("assets/imagens/Exxplode.png", 552, 0, 92, 96, 1.5)
]

meteoros = [{
    "sprite": meteoro1_image,
    "rect": meteoro1_image.get_rect(topleft=(90, -90)),
    "explodindo": False,
    "frame_explosao": 0
}, {
    "sprite": meteoro2_image,
    "rect": meteoro2_image.get_rect(topleft=(80, -300)),
    "explodindo": False,
    "frame_explosao": 0
}, {
    "sprite": meteoro3_image,
    "rect": meteoro3_image.get_rect(topleft=(70, -600)),
    "explodindo": False,
    "frame_explosao": 0
}, {
    "sprite": meteoro4_image,
    "rect": meteoro4_image.get_rect(topleft=(60, -1000)),
    "explodindo": False,
    "frame_explosao": 0
}, {
    "sprite": meteoro5_image,
    "rect": meteoro5_image.get_rect(topleft=(50, -1500)),
    "explodindo": False,
    "frame_explosao": 0
}]

vel_meteoro = 350 

def mover_meteoros(screen, dt, meteoro, pontos_atual):
    """Move os meteoros para baixo e os reposiciona quando saem da tela."""
    velocidade = 350 + (pontos_atual // 10) * 75
    if meteoro['explodindo']:
        meteoro['frame_explosao'] += 1
        if meteoro['frame_explosao'] >= len(frames_explosao):
            meteoro['explodindo'] = False
            meteoro['frame_explosao'] = 0
            redefinir_posicao(meteoro, screen)
    
    elif not meteoro['rect'].y > screen.height: 
        meteoro['rect'].y += velocidade * dt
    else: 
        redefinir_posicao(meteoro, screen)
        return 1
    return 0

def redefinir_posicao(meteoro, screen):
    """Reposiciona o meteoro para o topo da tela em uma posição horizontal aleatória."""
    meteoro['rect'].y = -meteoro['rect'].height
    meteoro['rect'].x = random.randint(0, screen.width - meteoro['rect'].width)

def desenha_explosao(screen, meteoro):
    """Desenha a animacao de explosao"""
    screen.blit(frames_explosao[meteoro['frame_explosao']], (meteoro['rect'].x, meteoro['rect'].y - 32))