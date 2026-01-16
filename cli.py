import json
from gamingHaven.dominio.classJogo import Jogo
from gamingHaven.dominio.jogoConsole import JogoConsole
from gamingHaven.dominio.jogoMobile import JogoMobile
from gamingHaven.dominio.jogoPc import JogoPC
from gamingHaven.dados.repositorio_json import salvar_jogos, carregar_jogos

def carregar_settings():
    with open("settings.json", "r", encoding="utf-8") as f:
        return json.load(f)

def menu():
    print("\n--- CATÁLOGO DE JOGOS ---")
    print("1 - Cadastrar jogo")
    print("2 - Atualizar progresso")
    print("3 - Relatórios")
    print("0 - Sair")

def cadastrar_jogo(jogos):
    titulo = input("Título: ")
    genero = input("Gênero: ")
    plataforma = input("Plataforma (PC/Console/Mobile): ")

    if plataforma == "PC":
        jogo = JogoPC(titulo, genero)
    elif plataforma == "Console":
        jogo = JogoConsole(titulo, genero)
    else:
        jogo = JogoMobile(titulo, genero)

    if jogo in jogos:
        print("Jogo já cadastrado!")
        return

    jogos.append(jogo)
    print("Jogo cadastrado com sucesso!")

def atualizar_progresso(jogos):
    for i, j in enumerate(jogos):
        print(i, "-", j)

    idx = int(input("Escolha o jogo: "))
    horas = float(input("Horas jogadas: "))

    jogos[idx].adicionar_horas(horas)

    if input("Finalizar jogo? (s/n): ") == "s":
        jogos[idx].finalizar()
        nota = float(input("Nota (0-10): "))
        jogos[idx].nota = nota

def relatorios(jogos):
    total = sum(j.horas_jogadas for j in jogos)
    finalizados = [j for j in jogos if j.status == "FINALIZADO"]

    print("Total de horas jogadas:", total)

    if finalizados:
        media = sum(j.nota for j in finalizados if j.nota is not None) / len(finalizados)
        print("Média de avaliação:", round(media, 2))

    top5 = sorted(jogos, reverse=True)[:5]
    print("\nTop 5 mais jogados:")
    for j in top5:
        print(j)

def main():
    jogos = carregar_jogos()
    settings = carregar_settings()

    while True:
        menu()
        opcao = input("Opção: ")

        if opcao == "1":
            cadastrar_jogo(jogos)
        elif opcao == "2":
            atualizar_progresso(jogos)
        elif opcao == "3":
            relatorios(jogos)
        elif opcao == "0":
            salvar_jogos(jogos)
            break

if __name__ == "__main__":
    main()
