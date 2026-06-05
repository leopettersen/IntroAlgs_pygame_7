from src.funcoesMeteoro import redefinir_posicao, desenha_explosao

def calcular_pontos(pontos_atual, pontos_ganhos):
    """Soma os pontos ganhos à pontuação atual."""
    return pontos_atual + pontos_ganhos


def tomar_dano(vida_atual, dano):
    """Reduz a vida atual com base no dano recebido."""
    return vida_atual - dano


def jogador_perdeu(vidas):
    """Indica se o jogador ficou sem vidas."""
    return vidas <= 0


def limitar_valor(valor, minimo, maximo):
    """Mantém um valor dentro do intervalo [minimo, maximo]."""
    if valor < minimo:
        return minimo
    if valor > maximo:
        return maximo
    return valor


def verificar_colisao(nave, meteoro, screen):
    """Verifica se a nave colidiu com um meteoro e reposiciona o meteoro se houver colisão."""
    if meteoro['explodindo']:
        return False
    if nave.colliderect(meteoro['rect']):
        meteoro['explodindo'] = True
        desenha_explosao(screen, meteoro)
        return True
    return False