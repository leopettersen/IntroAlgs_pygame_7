# Funções auxiliares relacionadas à lógica do jogo.


def calcular_pontos(pontos_atual, pontos_ganhos):
    """
    Soma os pontos ganhos à pontuação atual.
    """
    return pontos_atual + pontos_ganhos


def tomar_dano(vida_atual, dano):
    """
    Reduz a quantidade de vidas do jogador.
    """
    return vida_atual - dano


def jogador_perdeu(vidas):
    """
    Verifica se o jogador ficou sem vidas.
    """
    return vidas <= 0


def limitar_valor(valor, minimo, maximo):
    """
    Mantém um valor dentro do intervalo [minimo, maximo].
    """

    if valor < minimo:
        return minimo

    if valor > maximo:
        return maximo

    return valor


def verificar_colisao(rect1, meteoro):
    """
    O rect1 pode ser tanto um missil quanto a nave
    Verifica colisão entre a nave e um meteoro ou entre um missil e um meteoro.

    Caso haja colisão, inicia a animação de explosão
    do meteoro e retorna True.
    """

    # Ignora meteoros que já estão explodindo
    if meteoro.get_explodindo():
        return False

    # Verifica a colisão entre os retângulos
    if rect1.colliderect(meteoro.rect):
        return True

    return False