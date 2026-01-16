from classJogo import Jogo

class JogoConsole(Jogo):
    def __init__(self, titulo, genero):
        super().__init__(titulo, genero, "Console")

