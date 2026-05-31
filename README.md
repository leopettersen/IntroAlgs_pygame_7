# Nome do Jogo

>Meteor Rain

## Integrantes do grupo

- Daniel Gomes Rolando
- Leonardo Federici Pettersen
- Rafael Ferreira Torres Modesto
- Samuel Henrique Alvarenga e Lopes

## Estrutura do projeto

- `main.py`: ponto de entrada da aplicação.
- `src/`: código-fonte principal do jogo (loop, regras, sprites e dados).
- `assets/`: imagens, fontes e sons.
- `data/`: arquivos persistentes (recorde/ranking).
- `tests/`: testes unitários com `pytest`.
- `docs/`: documentação do projeto, incluindo proposta inicial.

## Descrição do jogo

Este projeto consiste em um jogo inspirado em Space Invaders (Nave desviando de meteoros), desenvolvido utilizando a biblioteca Pygame e programação procedural (sem orientação a objetos). O jogador controla uma nave espacial na parte inferior da tela e deve eliminar ondas de inimigos que descem em direção à sua posição.

## Objetivo do jogador

O objetivo do jogador é desviar do maior número possível de meteoros, evitando que os meteoros alcancem sua posição. Conforme o jogo avança, o desafio aumenta devido à movimentação e à quantidade de meteoros na tela.

## Regras do jogo

O jogador controla uma nave espacial localizada na parte inferior da tela.
Os meteoros se movimentam verticalmente pela tela e descem gradualmente.
Cada meteoro desviado aumenta a pontuação do jogador.
Cada colisão entre a nave e um meteoro faz o jogador perder uma vida. Depois de perder 3 vidas se encerra a partida.

## Controles

Seta para esquerda: mover a nave para a esquerda
Seta para direita: mover a nave para a direita

## Como executar o projeto

### 1. Clonar o repositório

```bash
git clone LINK_DO_REPOSITORIO
cd NOME_DA_PASTA
pip install -r requirements.txt
python main.py
```

## Como executar os testes

```bash
python -m pytest
```

## Checklist mínimo para entrega

- Preencher este README com nome final, descrição real, regras e controles do jogo.
- Atualizar `docs/proposta.MD` com a proposta do grupo.
- Garantir que o jogo executa com `python main.py`.
- Garantir que os testes passam com `pytest`.

## Observações para os alunos

- Mantenham o código organizado em módulos pequenos e com responsabilidade clara.
- Comentem partes importantes da lógica, principalmente regras do jogo.
- Registrem decisões técnicas no README do grupo ao longo do desenvolvimento.
