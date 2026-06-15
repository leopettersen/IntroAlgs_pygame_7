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

    pygame.init()

    screen = pygame.display.set_mode(
        (LARGURA_TELA, ALTURA_TELA)
    )

    pygame.display.set_caption(
        TITULO_JOGO
    )

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
        x = random.randint(
            30,
            LARGURA_TELA - 30
        )

        y = random.randint(
            -1000,
            -33
        )

        meteoros.append(
            Meteoro(x, y)
        )

    clock = pygame.time.Clock()

    running = True

    vida_atual = 3
    pontos_atual = 0

    recorde = carregar_maior_pontuacao(
        CAMINHO_RANKING
    )

    # ==================================================
    # LOOP PRINCIPAL
    # ==================================================

    while running:

        dt = clock.tick(FPS) / 1000

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

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

        nave.mover(
            screen,
            dt
        )

        nave.desenhar(
            screen
        )

        # ==================================================
        # METEOROS
        # ==================================================

        meteoros_passados = 0

        for meteoro in meteoros:

            meteoros_passados += meteoro.mover(
                screen,
                dt,
                pontos_atual
            )

            meteoro.desenhar(
                screen
            )

            if verificar_colisao(
                nave,
                meteoro
            ):

                vida_atual = tomar_dano(
                    vida_atual,
                    1
                )

                if jogador_perdeu(
                    vida_atual
                ):

                    nome = input(
                        "Digite seu nome: "
                    )

                    alterar_ranking(
                        CAMINHO_RANKING,
                        nome,
                        int(pontos_atual)
                    )

                    ranking = carregar_ranking(
                        CAMINHO_RANKING
                    )

                    print(
                        "\nGame Over!"
                    )

                    print(
                        "\n===== RANKING ====="
                    )

                    for posicao, (
                        nome_ranking,
                        pontos
                    ) in enumerate(
                        ranking[:10],
                        start=1
                    ):

                        print(
                            f"{posicao}º "
                            f"{nome_ranking}: "
                            f"{pontos} pontos"
                        )

                    print(
                        f"\nSua pontuação: "
                        f"{int(pontos_atual)} pontos"
                    )

                    running = False

        # ==================================================
        # PONTUAÇÃO
        # ==================================================

        pontos_atual = calcular_pontos(
            pontos_atual,
            meteoros_passados
        )

        pygame.display.set_caption(
            f"{TITULO_JOGO} | "
            f"Vidas: {vida_atual} | "
            f"Pontos: {int(pontos_atual)} | "
            f"Recorde: {int(recorde)}"
        )

        pygame.display.flip()

    pygame.quit()