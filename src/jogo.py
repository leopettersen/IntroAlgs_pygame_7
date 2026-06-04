def executar_jogo():
    import pygame

    from src.funcoesNave import mover_nave, nave
    from src.funcoesMeteoro import mover_meteoros, meteoros
    from src.funcoesJogo import verificar_colisao, tomar_dano, jogador_perdeu

    #CONFIGURAÇÕES DO JOGO----------------------------------------------------
    from src.config import FPS, LARGURA_TELA, ALTURA_TELA, TITULO_JOGO
    pygame.init()
    screen = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption(TITULO_JOGO)
    clock = pygame.time.Clock()
    running = True
    vida_atual = 3
    #-----------------------------------------


    #LOOP DO JOGO--------------------------------
    while running:
        dt = clock.tick(FPS) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("purple")

        screen.blit(nave['sprite'], nave['rect'])

        mover_meteoros(screen, dt)
        mover_nave(dt);
        for meteoro in meteoros:
            screen.blit(meteoro['sprite'], meteoro['rect'])
            if verificar_colisao(nave['rect'], meteoro, screen):
                vida_atual = tomar_dano(vida_atual, 1)
                if jogador_perdeu(vida_atual):
                    print("Game Over!")
                    running = False
        
        pygame.display.set_caption(
            f"{TITULO_JOGO} | Vidas: {vida_atual}"
        )

        pygame.display.flip()
        clock.tick(FPS)  

    pygame.quit()