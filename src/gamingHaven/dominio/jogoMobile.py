from classJogo import Jogo

class JogoMobile(Jogo):
    def __init__(self, titulo, genero, sistema):
        super().__init__(titulo, genero, "Mobile")
        self.sistema = sistema

