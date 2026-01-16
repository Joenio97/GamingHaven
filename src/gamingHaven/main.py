
from dominio.jogoPc import JogoPC
from dominio.JogoConsole import JogoConsole
from dominio.jogoMobile import JogoMobile


def main():
    jogo_pc = JogoPC(
        titulo="The Witcher 3",
        genero="RPG")

    jogo_console = JogoConsole(
        titulo="God of War",
        genero="Ação",)

    jogo_mobile = JogoMobile(
        titulo="Clash Royale",
        genero="Estratégia",)


    print("=== Jogos cadastrados ===")
    print(jogo_pc)
    print(jogo_console)
    print(jogo_mobile)


    jogo_pc.iniciar()
    jogo_pc.horas_jogadas = 12
    jogo_pc.finalizar()
    jogo_pc.avaliacao = 9.5

    jogo_console.iniciar()
    jogo_console.horas_jogadas = 5


    print("\n=== Estado após progresso ===")
    print(jogo_pc)
    print(jogo_console)
    print(jogo_mobile)


if __name__ == "__main__":
    main()
