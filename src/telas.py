"""
Telas auxiliares do jogo: menu inicial (com botão "Jogar") e
tela de game over (com campo para digitar o nome e botão
"Jogar novamente"), substituindo o uso de input()/print() no terminal.
"""

import pygame

from src.config import (
    LARGURA_TELA,
    ALTURA_TELA,
    BRANCO,
    PRETO,
)

VERDE = (60, 200, 100)
VERDE_HOVER = (90, 230, 130)
VERMELHO = (220, 60, 60)
CINZA_CAMPO = (40, 40, 40)
CINZA_CAMPO_ATIVO = (70, 70, 70)


def _texto_centralizado(screen, texto, fonte, cor, y):
    superficie = fonte.render(texto, True, cor)
    rect = superficie.get_rect(center=(LARGURA_TELA // 2, y))
    screen.blit(superficie, rect)


def tela_menu(screen, clock, fps):
    """
    Exibe a tela inicial com o título do jogo e um botão "JOGAR".
    Fica em loop próprio até o jogador clicar no botão ou fechar a janela.

    Retorna True se o jogador quer jogar, False se fechou a janela.
    """

    fonte_titulo = pygame.font.SysFont(None, 72)
    fonte_botao = pygame.font.SysFont(None, 40)
    fonte_dica = pygame.font.SysFont(None, 24)

    botao_jogar = pygame.Rect(0, 0, 220, 70)
    botao_jogar.center = (LARGURA_TELA // 2, ALTURA_TELA // 2 + 20)

    while True:
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if botao_jogar.collidepoint(event.pos):
                    return True

            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_RETURN, pygame.K_SPACE):
                    return True

        screen.fill(PRETO)

        _texto_centralizado(
            screen, "METEOR RAIN", fonte_titulo, BRANCO,
            ALTURA_TELA // 2 - 80
        )

        cor_botao = VERDE_HOVER if botao_jogar.collidepoint(mouse_pos) else VERDE
        pygame.draw.rect(screen, cor_botao, botao_jogar, border_radius=12)

        texto_botao = fonte_botao.render("JOGAR", True, PRETO)
        texto_rect = texto_botao.get_rect(center=botao_jogar.center)
        screen.blit(texto_botao, texto_rect)

        _texto_centralizado(
            screen, "Setas A/D para mover, ESPAÇO para atirar",
            fonte_dica, (180, 180, 180), ALTURA_TELA // 2 + 100
        )

        pygame.display.flip()
        clock.tick(fps)


def tela_game_over(screen, clock, fps, pontos_atual, ranking):
    """
    Exibe a tela de game over: pontuação final, ranking (top 10),
    um campo de texto para o jogador digitar o nome, um botão
    "Jogar novamente" e um botão "Sair".

    Retorna uma tupla (nome_digitado, acao):
    - nome_digitado: string com o nome digitado (ou "Jogador" se vazio)
    - acao: "jogar" se o jogador quer jogar de novo,
            "sair" se clicou em Sair ou fechou a janela.
    """

    fonte_titulo = pygame.font.SysFont(None, 64)
    fonte_media = pygame.font.SysFont(None, 36)
    fonte_pequena = pygame.font.SysFont(None, 26)
    fonte_botao = pygame.font.SysFont(None, 30)

    campo_nome = pygame.Rect(0, 0, 320, 44)
    campo_nome.center = (LARGURA_TELA // 2, 230)

    botao_confirmar = pygame.Rect(0, 0, 240, 56)
    botao_confirmar.center = (LARGURA_TELA // 2 - 130, 300)

    botao_sair = pygame.Rect(0, 0, 180, 56)
    botao_sair.center = (LARGURA_TELA // 2 + 130, 300)

    nome_digitado = ""
    campo_ativo = True
    LIMITE_NOME = 12

    # Apenas as 10 melhores pontuações são exibidas.
    top_10 = ranking[:10]

    while True:
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return (nome_digitado.strip() or "Jogador", "sair")

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                campo_ativo = campo_nome.collidepoint(event.pos)

                if botao_confirmar.collidepoint(event.pos):
                    return (nome_digitado.strip() or "Jogador", "jogar")

                if botao_sair.collidepoint(event.pos):
                    return (nome_digitado.strip() or "Jogador", "sair")

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return (nome_digitado.strip() or "Jogador", "jogar")

                elif event.key == pygame.K_ESCAPE:
                    return (nome_digitado.strip() or "Jogador", "sair")

                elif event.key == pygame.K_BACKSPACE:
                    nome_digitado = nome_digitado[:-1]

                elif campo_ativo and len(nome_digitado) < LIMITE_NOME:
                    if event.unicode.isprintable():
                        nome_digitado += event.unicode

        screen.fill(PRETO)

        _texto_centralizado(
            screen, "GAME OVER", fonte_titulo, VERMELHO, 80
        )

        _texto_centralizado(
            screen, f"Pontuação: {int(pontos_atual)}", fonte_media,
            BRANCO, 140
        )

        _texto_centralizado(
            screen, "Digite seu nome:", fonte_pequena,
            (200, 200, 200), 195
        )

        cor_campo = CINZA_CAMPO_ATIVO if campo_ativo else CINZA_CAMPO
        pygame.draw.rect(screen, cor_campo, campo_nome, border_radius=8)
        pygame.draw.rect(screen, BRANCO, campo_nome, width=2, border_radius=8)

        texto_nome = fonte_media.render(nome_digitado, True, BRANCO)
        texto_nome_rect = texto_nome.get_rect(midleft=(campo_nome.x + 12, campo_nome.centery))
        screen.blit(texto_nome, texto_nome_rect)

        # Botão "Jogar novamente"
        cor_confirmar = VERDE_HOVER if botao_confirmar.collidepoint(mouse_pos) else VERDE
        pygame.draw.rect(screen, cor_confirmar, botao_confirmar, border_radius=12)

        texto_confirmar = fonte_botao.render("JOGAR NOVAMENTE", True, PRETO)
        texto_confirmar_rect = texto_confirmar.get_rect(center=botao_confirmar.center)
        screen.blit(texto_confirmar, texto_confirmar_rect)

        # Botão "Sair"
        cor_sair_hover = (230, 90, 90)
        cor_sair = cor_sair_hover if botao_sair.collidepoint(mouse_pos) else VERMELHO
        pygame.draw.rect(screen, cor_sair, botao_sair, border_radius=12)

        texto_sair = fonte_botao.render("SAIR", True, BRANCO)
        texto_sair_rect = texto_sair.get_rect(center=botao_sair.center)
        screen.blit(texto_sair, texto_sair_rect)

        _texto_centralizado(
            screen, "===== TOP 10 RANKING =====", fonte_pequena, BRANCO, 370
        )

        y_ranking = 396
        for posicao, (nome_ranking, pontos) in enumerate(top_10, start=1):
            _texto_centralizado(
                screen,
                f"{posicao}º  {nome_ranking} - {pontos} pontos",
                fonte_pequena,
                (220, 220, 220),
                y_ranking,
            )
            y_ranking += 20

        pygame.display.flip()
        clock.tick(fps)
