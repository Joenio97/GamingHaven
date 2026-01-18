def filtrar_por_generos(jogos, generos_preferidos):
    return [j for j in jogos if j.genero in generos_preferidos]


def filtrar_por_plataforma(jogos, plataforma):
    return [j for j in jogos if j.plataforma == plataforma]


def filtrar_por_status(jogos, status):
    return [j for j in jogos if j.status == status]
