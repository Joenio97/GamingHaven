from classJogo import Jogo

class JogoConsole(Jogo):
    def __init__(self, titulo, genero, console):
        super().__init__(titulo, genero, "Console")
        self.console = console
