def percentual_por_status(jogos):
    total = len(jogos)
    if total == 0:
        return {}

    contagem = {}

    for jogo in jogos:
        contagem[jogo.status] = contagem.get(jogo.status, 0) + 1

    return {
        status: round((qtd / total) * 100, 2)
        for status, qtd in contagem.items()
    }
