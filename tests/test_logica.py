from src.funcoesJogo import calcular_pontos, jogador_perdeu, limitar_valor

def test_calcular_pontos():
    """Deve somar corretamente os pontos atuais com os pontos ganhos."""
    assert calcular_pontos(10, 5) == 15


def test_jogador_perdeu_com_zero_vidas():
    """Deve indicar derrota quando o total de vidas chega a zero."""
    assert jogador_perdeu(0) is True


def test_jogador_nao_perdeu_com_vidas():
    """Nao deve indicar derrota quando o jogador ainda tem vidas."""
    assert jogador_perdeu(3) is False


def test_limitar_valor_abaixo_do_minimo():
    """Deve retornar o limite minimo quando o valor informado for menor."""
    assert limitar_valor(-5, 0, 100) == 0


def test_limitar_valor_acima_do_maximo():
    """Deve retornar o limite maximo quando o valor informado for maior."""
    assert limitar_valor(150, 0, 100) == 100


def test_limitar_valor_dentro_do_intervalo():
    """Deve manter o valor original quando ele ja estiver no intervalo."""
    assert limitar_valor(50, 0, 100) == 50

def test_verificar_colisao_entre_retangulos_sobrepostos():
    """Deve detectar colisao entre dois retangulos."""
    from src.funcoesMeteoro import Meteoro
    from pygame import Rect
    rect1 = Rect(0, 0, 60, 60)
    meteoro = Meteoro(50, 50)
    from src.funcoesJogo import verificar_colisao
    assert verificar_colisao(rect1, meteoro) is True

def test_verificar_colisao_entre_retangulos_distantes():
    """Nao deve detectar colisao entre retangulos que nao se sobrepoem."""
    
    from src.funcoesMeteoro import Meteoro
    from pygame import Rect
    rect1 = Rect(0, 0, 50, 50)
    meteoro = Meteoro(100, 100)
    from src.funcoesJogo import verificar_colisao
    assert verificar_colisao(rect1, meteoro) is False