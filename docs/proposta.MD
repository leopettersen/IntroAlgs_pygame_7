# Proposta Inicial do Jogo

Este projeto consiste em um jogo inspirado em Space Invaders (Nave desviando de meteoros), desenvolvido utilizando a biblioteca Pygame e programação procedural (sem orientação a objetos). O jogador controla uma nave espacial na parte inferior da tela e deve eliminar ondas de inimigos que descem em direção à sua posição.

## 1. Nome provisório do jogo

>Meteor Rain

## 2. Integrantes do grupo

Liste os integrantes do grupo.

- Nome 1: Daniel Gomes Rolando
- Nome 2: Leonardo Federici Pettersen
- Nome 3: Rafael Ferreira Torres Modesto 
- Nome 4: Samuel Henrique Alvarenga e Lopes

## 3. Tipo de jogo

> Tipo escolhido pelo grupo: Nave desviando de meteoros

## 4. Descrição geral do jogo

> Na tela aparecem a nave do jogador, meteoros caindo do espaço e a pontuação ou tempo de sobrevivência. O jogador controla uma nave espacial localizada na parte inferior da tela, podendo movê-la para a esquerda e para a direita. O objetivo é sobreviver o maior tempo possível desviando dos meteoros que surgem continuamente na tela. Conforme o tempo passa, novos meteoros aparecem, aumentando a dificuldade da partida. O principal desafio é evitar colisões com os meteoros, utilizando reflexos rápidos e movimentação precisa. O jogo termina quando um meteoro atinge a nave do jogador.

## 5. Objetivo do jogador

> Sobreviver pelo maior tempo possível desviando dos meteoros que caem em direção à nave. A cada segundo sobrevivido, a pontuação aumenta, e o jogador deve evitar colisões para continuar na partida.

## 6. Regras principais

Regra 1: O jogador controla uma nave que pode se mover apenas para a esquerda e para a direita.
Regra 2: Meteoros caem continuamente do topo da tela em direção à nave.
Regra 3: O jogador ganha pontos ou tempo de sobrevivência enquanto permanece vivo.
Regra 4: Cada colisão entre a nave e um meteoro faz o jogador perder uma vida. Depois de perder 3 vidas se encerra a partida.
Regra 5: O objetivo é sobreviver o máximo de tempo possível e alcançar a maior pontuação.

## 7. Condição de vitória

> A condição de vitória consiste em sobreviver o maior tempo possível, mesma mecânica do jogo Spacce Invaders, o qual você não avança para uma tela de vitória definitiva, mas progride através de um ciclo infinito de desafios.

## 8. Condição de derrota ou encerramento

> O jogador deve evitar ser atingido por um meteoro. Cada colisão entre a nave e um meteoro faz o jogador perder uma vida. Depois de perder 3 vidas se encerra a partida.

## 9. Elementos previstos no jogo

Meteoro: Elementos que caem verticalmente e têm como objetivo atigir o jogador.
Nave: Representa o jogador. Deve mover-se no eixo x para desviar dos meteoros.

## Jogador ou elemento principal

> A nave

Descrição:

> Deve mover-se no eixo x para desviar dos meteoros

## Obstáculos, inimigos ou desafios

> Obstáculos (meteoros) aparecem em posições aleatórias e devem ser evitados.

## Itens, alvos ou objetos de interação

> As interações acontecem quando um meteoro colide com a nave do jogador ou quando o meteoro chega ao fim da tela, o renderizando novamente em uma posição aleatória.

## Pontuação, vidas, tempo ou progresso

> O jogador começa com 3 vidas, a cada meteoro que o atinge ele perde uma, a pontuação é crecente com o tempo de sobrevivência.

## 10. Controles previstos

Seta para esquerda: mover a nave para a esquerda
Seta para direita: mover a nave para a direita

## 11. Organização inicial do código

Organização planejada:

> - `main.py`: inicia o jogo;
> - `src/jogo.py`: contém o loop principal;
> - `src/config.py`: guarda configurações como tamanho da tela e cores;
> - `src/funcoes.py`: contém funções auxiliares;
> - `src/dados.py`: contém funções de leitura e escrita de arquivos.

## 12. Recursos externos previstos

Recursos previstos:

> - imagens obtidas de banco gratuito;
> - sons gratuitos;
> - fontes personalizadas

## 13. Principais dificuldades esperadas

Dificuldades previstas:

- Dificuldade 1: Colisão entre objetos;
- Dificuldade 2: Controle de tempo;
- Dificuldade 3: Criação do ranking

## 14. Escopo mínimo para a entrega final

Escopo mínimo:

> A versão mínima do jogo terá uma nave que se movimenta lateralmente pelo teclado, meteoros descendo a tela, sistema de vidas, ranking de maior pontuação e tela de Game Over.

## 15. Possíveis melhorias, caso haja tempo

Melhorias possíveis:

- Melhoria 1: Diferentes naves;
- Melhoria 2: Aumento de dificuldade;
- Melhoria 3: Animações;
- Melhoria 4: Disparos pela nave.