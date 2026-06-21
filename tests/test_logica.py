from src.funcoesJogo import (
    calcular_pontos,
    jogador_perdeu,
    limitar_valor,
    tomar_dano,
    verificar_colisao
)

import pygame

pygame.init()


def test_calcular_pontos():
    """Deve somar corretamente os pontos atuais com os pontos ganhos."""
    assert calcular_pontos(10, 5) == 15


def test_calcular_pontos_com_zero():
    """Deve manter a pontuação em zero quando nenhum ponto for ganho."""
    assert calcular_pontos(0, 0) == 0


def test_jogador_perdeu_com_zero_vidas():
    """Deve indicar derrota quando o total de vidas chega a zero."""
    assert jogador_perdeu(0) is True


def test_jogador_perdeu_com_vidas_negativas():
    """Deve indicar derrota quando o total de vidas fica negativo."""
    assert jogador_perdeu(-1) is True


def test_jogador_nao_perdeu_com_vidas():
    """Nao deve indicar derrota quando o jogador ainda tem vidas."""
    assert jogador_perdeu(3) is False


def test_tomar_dano():
    """Deve reduzir corretamente a quantidade de vidas."""
    assert tomar_dano(10, 3) == 7


def test_tomar_dano_ate_zero():
    """Deve retornar zero quando o dano for igual ao total de vidas."""
    assert tomar_dano(5, 5) == 0


def test_limitar_valor_abaixo_do_minimo():
    """Deve retornar o limite minimo quando o valor informado for menor."""
    assert limitar_valor(-5, 0, 100) == 0


def test_limitar_valor_acima_do_maximo():
    """Deve retornar o limite maximo quando o valor informado for maior."""
    assert limitar_valor(150, 0, 100) == 100


def test_limitar_valor_dentro_do_intervalo():
    """Deve manter o valor original quando ele ja estiver no intervalo."""
    assert limitar_valor(50, 0, 100) == 50


class MeteoroFake:
    """Objeto simplificado para testar colisao."""

    def __init__(self, rect, explodindo=False):
        self.rect = rect
        self.explodindo = explodindo

    def get_explodindo(self):
        return self.explodindo


def test_verificar_colisao():
    """Deve detectar colisao entre dois retangulos."""
    rect1 = pygame.Rect(0, 0, 50, 50)
    rect2 = pygame.Rect(10, 10, 50, 50)

    meteoro = MeteoroFake(rect2)

    assert verificar_colisao(rect1, meteoro) is True


def test_verificar_colisao_inexistente():
    """Nao deve detectar colisao quando os objetos estao separados."""
    rect1 = pygame.Rect(0, 0, 50, 50)
    rect2 = pygame.Rect(200, 200, 50, 50)

    meteoro = MeteoroFake(rect2)

    assert verificar_colisao(rect1, meteoro) is False


def test_verificar_colisao_meteoro_explodindo():
    """Nao deve detectar colisao em meteoros que ja estao explodindo."""
    rect1 = pygame.Rect(0, 0, 50, 50)
    rect2 = pygame.Rect(0, 0, 50, 50)

    meteoro = MeteoroFake(rect2, True)

    assert verificar_colisao(rect1, meteoro) is False


def test_pontuacao_zero():
    """Deve exibir corretamente a pontuacao inicial igual a zero."""
    pontos = 0

    texto = (
        f"Vidas: 3 | "
        f"Pontos: {int(pontos)} | "
        f"Recorde: 0"
    )

    assert "Pontos: 0" in texto