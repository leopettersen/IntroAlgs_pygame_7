import random
from src.sprites import pegar_sprite
class Meteoro:

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

    def __init__(self, x, y):
        self.sprite = pegar_sprite(
            "assets/imagens/meteoro.png",
            0, 0, 38, 33, 1.5
        )

        self.rect = self.sprite.get_rect(
            topleft=(x, y)
        )

        self.explodindo = False
        self.frame_explosao = 0
        self.passou = False
        self.vida = 100

    def mover(self, screen, dt, pontos_atual):
        velocidade = 350 + (pontos_atual // 10) * 40

        if self.explodindo:
            self.frame_explosao += 1
            if self.frame_explosao >= len(
                Meteoro.frames_explosao
            ):

                self.explodindo = False
                self.frame_explosao = 0
                self.redefinir_posicao(screen)
        elif self.rect.y <= screen.get_height():
            self.rect.y += velocidade * dt
        else:
            self.redefinir_posicao(screen)
            self.passou = True
            return 1
        return 0

    def redefinir_posicao(self, screen):
        self.rect.y = -self.rect.height

        self.rect.x = random.randint(
            30,
            screen.get_width() - self.rect.width - 30
        )

    def desenhar(self, screen):
        if self.explodindo:
            screen.blit(
                Meteoro.frames_explosao[
                    self.frame_explosao
                ],
                (
                    self.rect.x,
                    self.rect.y - 32
                )
            )
        else:
            screen.blit(self.sprite, self.rect)

    def explodir(self):
        self.explodindo = True
        self.frame_explosao = 0

    def get_explodindo(self):
        return self.explodindo

    def get_passou(self):
        if self.passou:
            self.passou = False
            return True
        return False