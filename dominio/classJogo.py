from datetime import date


class Jogo:
    STATUS_VALIDOS = {"NAO_INICIADO", "JOGANDO", "FINALIZADO"}

    def __init__(self, titulo, genero, plataforma):
        if not titulo:
            raise ValueError("Título não pode ser vazio")

        self.titulo = titulo
        self.genero = genero
        self.plataforma = plataforma

        self._horas_jogadas = 0.0
        self._avaliacao = None
        self.status = "NAO_INICIADO"

        self.data_inicio = None
        self.data_fim = None

    # ---------- Encapsulamento ----------
    @property
    def horas_jogadas(self):
        return self._horas_jogadas

    @horas_jogadas.setter
    def horas_jogadas(self, valor):
        if valor < 0:
            raise ValueError("Horas jogadas não podem ser negativas")
        self._horas_jogadas = valor

    @property
    def avaliacao(self):
        return self._avaliacao

    @avaliacao.setter
    def avaliacao(self, nota):
        if nota is not None and not (0 <= nota <= 10):
            raise ValueError("Avaliação deve estar entre 0 e 10")
        self._avaliacao = nota

    # ---------- Regras de negócio ----------
    def iniciar(self):
        self.status = "JOGANDO"
        self.data_inicio = date.today()

    def finalizar(self):
        if self.horas_jogadas < 1:
            raise ValueError("Não é possível finalizar com menos de 1h jogada")
        self.status = "FINALIZADO"
        self.data_fim = date.today()

    def reiniciar(self):
        self.status = "JOGANDO"
        self.horas_jogadas = 0
        self.data_fim = None

    def __str__(self):
        return f"{self.titulo} ({self.plataforma}) - {self.status}"

    def __repr__(self):
        return (
            f"Jogo(titulo={self.titulo}, genero={self.genero}, "
            f"plataforma={self.plataforma}, horas={self.horas_jogadas})"
        )

    def __eq__(self, other):
        return (
            isinstance(other, Jogo)
            and self.titulo == other.titulo
            and self.plataforma == other.plataforma
        )

    def __lt__(self, other):
        return self.horas_jogadas < other.horas_jogadas
