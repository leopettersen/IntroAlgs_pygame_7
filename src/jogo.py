def executar_jogo():
    import random
    import pygame
    
    import src.funcoesNave
    import src.funcoesMeteoro
    from src.dados import carregar_recorde, salvar_recorde, alterar_ranking, carregar_recorde, salvar_recorde, alterar_ranking,carregar_ranking, carregar_maior_pontuacao
    from src.funcoesJogo import verificar_colisao, tomar_dano, jogador_perdeu, calcular_pontos

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

    # OBJETOS DO JOGO-----------------------------------------
    nave = src.funcoesNave.Nave()
    meteoros = []

    for _ in range(5):
        x = random.randint(30, LARGURA_TELA - 30)
        y = random.randint(-1000, -33)

        meteoros.append(src.funcoesMeteoro.Meteoro(x, y))
    #-------------------------------------------


    #LOOP DO JOGO--------------------------------
    while running:
        dt = clock.tick(FPS) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.blit(fundo, (0, 0))

        nave.mover(screen, dt)
        nave.desenhar(screen)

        for meteoro in meteoros:

            meteoro.mover(screen, dt, pontos_atual)
            meteoro.desenhar(screen)

            if meteoro.get_passou():
                pontos_atual = calcular_pontos(pontos_atual, 1)
                
            if verificar_colisao(nave, meteoro):
                vida_atual = tomar_dano(vida_atual, 1)

                if jogador_perdeu(vida_atual):
                    nome = input("Digite seu nome: ")
                    alterar_ranking(
                        CAMINHO_RANKING,
                        nome,
                        int(pontos_atual)
                    )

                    ranking = carregar_ranking(CAMINHO_RANKING)
                    if pontos_atual > recorde:
                        recorde = pontos_atual
                        salvar_recorde(CAMINHO_RECORDE, recorde)
                    print("Game Over!")
                    print("\n===== RANKING =====")
                    for posicao, (nome, pontos) in enumerate(ranking[:10], start=1):
                        print(f"{posicao}º {nome}: {pontos} pontos")
                    print(f"\nSua pontuação: {int(pontos_atual)} pontos")
                    running = False

        pygame.display.set_caption(
            f"{TITULO_JOGO} | Vidas: {vida_atual} | "
            f"Pontos: {int(pontos_atual)} | "
            f"Recorde: {int(recorde)}"
        )

        pygame.display.flip()
    pygame.quit()