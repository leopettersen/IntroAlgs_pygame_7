def executar_jogo():
    import pygame

    from src.funcoesNave import mover_nave, nave
    from src.funcoesMeteoro import mover_meteoros, desenha_explosao, meteoros
    from src.funcoesJogo import verificar_colisao, tomar_dano, jogador_perdeu, calcular_pontos
    from src.dados import carregar_recorde, salvar_recorde, alterar_ranking, carregar_recorde, salvar_recorde, alterar_ranking,carregar_ranking, carregar_maior_pontuacao

    #CONFIGURAÇÕES DO JOGO----------------------------------------------------
    from src.config import FPS, LARGURA_TELA, ALTURA_TELA, TITULO_JOGO, CAMINHO_RECORDE, CAMINHO_RANKING
    pygame.init()
    screen = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    from src.sprites import pegar_sprite
    fundo = pegar_sprite("assets/imagens/fundo.png", 0, 0, 100, 100, 9)
    pygame.display.set_caption(TITULO_JOGO)
    clock = pygame.time.Clock()
    running = True
    vida_atual = 3
    pontos_atual = 0
    recorde = carregar_maior_pontuacao(CAMINHO_RANKING)
    #ranking = carregar_recorde(CAMINHO_RANKING)
    #-----------------------------------------


    #LOOP DO JOGO--------------------------------
    while running:
        dt = clock.tick(FPS) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.blit(fundo, (0, 0))

        mover_nave(dt)
        screen.blit(nave['sprite'], nave['rect'])

        meteoros_passados = 0

        for meteoro in meteoros:

            meteoros_passados += mover_meteoros(
                screen,
                dt,
                meteoro,
                pontos_atual
            )

            if meteoro['explodindo']:
                desenha_explosao(screen, meteoro)
            else:
                screen.blit(meteoro['sprite'], meteoro['rect'])

            if verificar_colisao(nave['rect'], meteoro, screen):
                vida_atual = tomar_dano(vida_atual, 1)

                if jogador_perdeu(vida_atual):
                    
                    nome = input("Digite seu nome: ")

                    alterar_ranking(
                        CAMINHO_RANKING,
                        nome,
                        int(pontos_atual)
                    )

                    ranking = carregar_ranking(CAMINHO_RANKING)

                    print("Game Over!")
                    print("\n===== RANKING =====")
                    for posicao, (nome, pontos) in enumerate(ranking[:10], start=1):
                        print(f"{posicao}º {nome}: {pontos} pontos")
                    print(f"\nSua pontuação: {int(pontos_atual)} pontos")
                    running = False

        pontos_atual = calcular_pontos(
            pontos_atual,
            meteoros_passados
        )

        pygame.display.set_caption(
            f"{TITULO_JOGO} | Vidas: {vida_atual} | "
            f"Pontos: {int(pontos_atual)} | "
            f"Recorde: {int(recorde)}"
        )

        pygame.display.flip()

    pygame.quit()