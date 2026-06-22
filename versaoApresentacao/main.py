from jogo import jogar
from ranking import mostrarRanking


def menu():

    while True:

        print("\n=== MENU ===")
        print("1 - Jogar")
        print("2 - Ranking")
        print("3 - Sair")

        escolha = input()

        if escolha == "1":
            jogar()

        elif escolha == "2":
            mostrarRanking()

        elif escolha == "3":
            break

        else:
            print("Opcao invalida")

menu()