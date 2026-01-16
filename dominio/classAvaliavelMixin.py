class AvaliavelMixin:
    def atualizar_avaliacao(self, nota):
        if 0 <= nota <= 10:
            self._avaliacao = nota