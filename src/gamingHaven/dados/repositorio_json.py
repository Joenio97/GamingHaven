import json
from gamingHaven.dominio.classJogo import Jogo
from gamingHaven.dominio.jogoPc import JogoPC
from gamingHaven.dominio.jogoConsole import JogoConsole
from gamingHaven.dominio.jogoMobile import JogoMobile


ARQUIVO = "jogos.json"

def salvar_jogos(jogos):
    dados = []
    for j in jogos:
        dados.append({
            "titulo": j.titulo,
            "genero": j.genero,
            "plataforma": j.plataforma,
            "horas": j.horas_jogadas,
            "status": j.status,
            "nota": j.nota,
            "inicio": str(j.data_inicio) if j.data_inicio else None,
            "fim": str(j.data_fim) if j.data_fim else None
        })

    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)


def carregar_jogos():
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            dados = json.load(f)
    except FileNotFoundError:
        return []

    jogos = []
    for d in dados:
        if d["plataforma"] == "PC":
            jogo = JogoPC(d["titulo"], d["genero"])
        elif d["plataforma"] == "Console":
            jogo = JogoConsole(d["titulo"], d["genero"])
        else:
            jogo = JogoMobile(d["titulo"], d["genero"])

        jogo._horas_jogadas = d["horas"]
        jogo.status = d["status"]
        jogo._nota = d["nota"]

        jogos.append(jogo)

    return jogos
