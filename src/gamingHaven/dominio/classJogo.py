from datetime import date

class Jogo:
    def __init__(self, titulo, genero, plataforma):
        if not titulo:
            raise ValueError("Título não pode ser vazio")

        self._titulo = titulo
        self.genero = genero
        self.plataforma = plataforma

        self._horas_jogadas = 0
        self._nota = None
        self.status = "NAO_INICIADO"

        self.data_inicio = None
        self.data_fim = None

    # ---------- ENCAPSULAMENTO ----------
    @property
    def titulo(self):
        return self._titulo

    @property
    def horas_jogadas(self):
        return self._horas_jogadas

    @property
    def nota(self):
        return self._nota

    @nota.setter
    def nota(self, valor):
        if not 0 <= valor <= 10:
            raise ValueError("Nota deve estar entre 0 e 10")
        if self.status != "FINALIZADO":
            raise ValueError("Só é possível avaliar jogo finalizado")
        self._nota = valor

    # ---------- REGRAS DE NEGÓCIO ----------
    def adicionar_horas(self, horas):
        if horas < 0:
            raise ValueError("Horas não podem ser negativas")

        self._horas_jogadas += horas

        if self.status == "NAO_INICIADO":
            self.status = "JOGANDO"
            self.data_inicio = date.today()

    def finalizar(self):
        if self.horas_jogadas < 1:
            raise ValueError("Não é possível finalizar com menos de 1h jogada")

        self.status = "FINALIZADO"
        self.data_fim = date.today()

    def reiniciar(self):
        self.status = "JOGANDO"
        self._horas_jogadas = 0
        self._nota = None
        self.data_inicio = date.today()
        self.data_fim = None

    # ---------- MÉTODOS ESPECIAIS ----------
    def __str__(self):
        return f"{self.titulo} ({self.plataforma}) - {self.status}"

    def __repr__(self):
        return f"Jogo(titulo='{self.titulo}', plataforma='{self.plataforma}')"

    def __eq__(self, other):
        return (
            isinstance(other, Jogo)
            and self.titulo == other.titulo
            and self.plataforma == other.plataforma
        )

    def __lt__(self, other):
        return self.horas_jogadas < other.horas_jogadas

