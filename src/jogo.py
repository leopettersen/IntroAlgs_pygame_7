def executar_jogo():
    import pygame

    from src.funcoesNave import mover_nave, nave
    from src.funcoesMeteoro import mover_meteoros, desenha_explosao, meteoros
    from src.funcoesJogo import verificar_colisao, tomar_dano, jogador_perdeu
    from src.dados import carregar_recorde, salvar_recorde

    #CONFIGURAÇÕES DO JOGO----------------------------------------------------
    from src.config import FPS, LARGURA_TELA, ALTURA_TELA, TITULO_JOGO, CAMINHO_RECORDE
    pygame.init()
    screen = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    from src.sprites import pegar_sprite
    fundo = pegar_sprite("assets/imagens/fundo.png", 0, 0, 100, 100, 9)
    pygame.display.set_caption(TITULO_JOGO)
    clock = pygame.time.Clock()
    running = True
    vida_atual = 3
    pontos_atual = 0
    recorde = carregar_recorde(CAMINHO_RECORDE)
    #-----------------------------------------


    #LOOP DO JOGO--------------------------------
    while running:
        dt = clock.tick(FPS) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.blit(fundo)

        screen.blit(nave['sprite'], nave['rect'])

        mover_meteoros(screen, dt)
        mover_nave(dt);
        for meteoro in meteoros:
            if meteoro['explodindo']:
                desenha_explosao(screen, meteoro)
            else:
                screen.blit(meteoro['sprite'], meteoro['rect']) 
                
            if verificar_colisao(nave['rect'], meteoro, screen):
                vida_atual = tomar_dano(vida_atual, 1)
                if jogador_perdeu(vida_atual):
                    if pontos_atual > recorde:
                        recorde = pontos_atual
                        salvar_recorde(CAMINHO_RECORDE, recorde)
                    print("Game Over!")
                    running = False

        pygame.display.set_caption(
            f"{TITULO_JOGO} | Vidas: {vida_atual} | Pontos: {int(pontos_atual)} | Recorde: {int(recorde)}"
        )

        pygame.display.flip()
        clock.tick(FPS)  

    pygame.quit()