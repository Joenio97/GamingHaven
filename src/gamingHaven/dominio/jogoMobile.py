from gamingHaven.dominio.classJogo import Jogo

class JogoMobile(Jogo):
    def __init__(self, titulo, genero):
        super().__init__(titulo, genero, "Mobile")


