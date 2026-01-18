from gamingHaven.dominio.Colecao import Colecao

class GerenciadorColecao:
    def __init__(self, nome):
        self.colecao = Colecao(nome)

    def acionar(self, jogo):
        self.colecao.adicionar_jogo(jogo)

    def remover(self, jogo):
        self.colecao.remover_jogo(jogo)

    def listar(self):
        return self.colecao.listar_jogos()
