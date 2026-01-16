class Colecao:
    def __init__(self, nome):
        self.nome = nome
        self.jogos = []

    def adicionar_jogo(self, jogo):
        if jogo in self.jogos:
            raise ValueError("Jogo já está na coleção")
        self.jogos.append(jogo)

    def remover_jogo(self, jogo):
        self.jogos.remove(jogo)

    def listar_jogos(self):
        return self.jogos
