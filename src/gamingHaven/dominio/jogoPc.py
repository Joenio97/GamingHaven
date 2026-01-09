from classJogo import Jogo


class JogoPC(Jogo):
    def __init__(self, titulo, genero):
        super().__init__(titulo, genero, "PC")
