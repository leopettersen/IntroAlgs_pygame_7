def salvar_recorde(caminho_arquivo, pontuacao):
    """Salva a pontuação recorde em arquivo texto."""
    with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
        arquivo.write(str(pontuacao))


def carregar_recorde(caminho_arquivo):
    """Carrega o recorde salvo; retorna 0 se não existir valor válido."""
    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read().strip()

            if conteudo == "":
                return 0

            return int(conteudo)

    except FileNotFoundError:
        return 0

def alterar_ranking(caminho_ranking, nome, pontuacao):
    """Atualiza o ranking, mantendo as 10 melhores pontuações com o nome do jogador."""
    ranking = []
    
    try:
        with open(caminho_ranking, "r") as arquivo:
            for linha in arquivo:
                nome_jogador, pontos = linha.strip().split(",")
                ranking.append((nome_jogador, int(pontos)))
    except FileNotFoundError:
        return 0
    
    ranking.append((nome, pontuacao))
    ranking.sort(key=lambda item: item[1],reverse=True)
    ranking = ranking[:10]

    with open(caminho_ranking, "w", encoding="utf-8") as arq:
        for nome_jogador, pontos in ranking:
            arq.write(f"{nome_jogador},{pontuacao}\n")