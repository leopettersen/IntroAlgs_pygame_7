def executar_jogo():
    import random
    import pygame

    from src.funcoesNave import Nave
    from src.funcoesMeteoro import Meteoro

    from src.funcoesJogo import (
        verificar_colisao,
        tomar_dano,
        jogador_perdeu,
        calcular_pontos
    )

    from src.dados import (
        alterar_ranking,
        carregar_ranking,
        carregar_maior_pontuacao
    )

    from src.config import (
        FPS,
        LARGURA_TELA,
        ALTURA_TELA,
        TITULO_JOGO,
        CAMINHO_RANKING
    )

    from src.telas import tela_menu, tela_game_over

    pygame.init()

    screen = pygame.display.set_mode(
        (LARGURA_TELA, ALTURA_TELA)
    )

    pygame.display.set_caption(
        TITULO_JOGO
    )

    clock = pygame.time.Clock()

    # ==================================================
    # TELA DE MENU INICIAL
    # ==================================================

    quer_jogar = tela_menu(screen, clock, FPS)

    if not quer_jogar:
        pygame.quit()
        return

    jogar_novamente = True

    while jogar_novamente:
        # ==================================================
        # ESTRELAS DO FUNDO
        # ==================================================

        estrelas = []

        for _ in range(150):
            estrelas.append([
                random.randint(0, LARGURA_TELA),
                random.randint(0, ALTURA_TELA),
                random.randint(1, 3)
            ])

        # ==================================================
        # OBJETOS DO JOGO
        # ==================================================

        nave = Nave()
        meteoros = []

        for _ in range(5):
            x = random.randint(30, LARGURA_TELA - 30)

            y = random.randint(-1000, -33)

            meteoros.append(Meteoro(x, y))

        running = True

        vida_atual = 3
        pontos_atual = 0

        recorde = carregar_maior_pontuacao(
            CAMINHO_RANKING
        )

        jogador_morreu = False

        # ==================================================
        # LOOP PRINCIPAL
        # ==================================================

        while running:
            dt = clock.tick(FPS) / 1000

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    jogar_novamente = False

            # ==================================================
            # FUNDO
            # ==================================================

            screen.fill((0, 0, 0))

            for estrela in estrelas:
                estrela[1] += estrela[2] * 100 * dt

                if estrela[1] > ALTURA_TELA:

                    estrela[0] = random.randint(
                        0,
                        LARGURA_TELA
                    )

                    estrela[1] = 0

                pygame.draw.circle(
                    screen,
                    (255, 255, 255),
                    (
                        int(estrela[0]),
                        int(estrela[1])
                    ),
                    estrela[2]
                )

            # ==================================================
            # NAVE
            # ==================================================

            nave.mover(screen, dt)

            nave.desenhar(screen)

            # ==================================================
            # METEOROS
            # ==================================================

            meteoros_passados = 0

            for meteoro in meteoros:
                meteoros_passados += meteoro.mover(screen, dt, pontos_atual)
                meteoro.desenhar(screen)

                for missil in nave.get_misseis():
                    if verificar_colisao(missil, meteoro):
                        meteoro.vida = tomar_dano(meteoro.vida, 25)
                        missil.y = -5
                        if meteoro.vida < 0:
                            meteoro.explodir()

                if verificar_colisao(nave.rect, meteoro):
                    meteoro.explodir()
                    vida_atual = tomar_dano(vida_atual, 1)

                    if jogador_perdeu(vida_atual):
                        running = False
                        jogador_morreu = True

            # ==================================================
            # PONTUAÇÃO
            # ==================================================

            pontos_atual = calcular_pontos(pontos_atual, meteoros_passados)

            pygame.display.set_caption(
                f"{TITULO_JOGO} | "
                f"Vidas: {vida_atual} | "
                f"Pontos: {int(pontos_atual)} | "
                f"Recorde: {int(recorde)}"
            )

            pygame.display.flip()

        # ==================================================
        # TELA DE GAME OVER
        # ==================================================

        if jogador_morreu:
            ranking_atual = carregar_ranking(CAMINHO_RANKING)

            nome, acao = tela_game_over(
                screen, clock, FPS, pontos_atual, ranking_atual
            )

            alterar_ranking(CAMINHO_RANKING, nome, int(pontos_atual))

            jogar_novamente = (acao == "jogar")

    pygame.quit()
