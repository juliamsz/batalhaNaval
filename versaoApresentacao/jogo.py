import random

from tabuleiro import *
from ranking import *


DIFICULDADES = {

    "1": {
        "nome": "Facil",
        "tamanho": 5,
        "navios": [2, 2]
    },

    "2": {
        "nome": "Medio",
        "tamanho": 8,
        "navios": [2, 2, 2, 3]
    },

    "3": {
        "nome": "Dificil",
        "tamanho": 10,
        "navios": [2, 2, 2, 3, 3, 4]
    }

}


def escolherDificuldade():
    
    while True:
        
        print("\n=== DIFICULDADE ===")
        print("1 - Facil")
        print("2 - Medio")
        print("3 - Dificil")

        escolha = input("Escolha: ")

        if escolha in DIFICULDADES:
            return (DIFICULDADES[escolha])

        print("Opcao invalida.")


def tiroCpu(tabuleiro, tirosCpu):
    
    while True:
        
        linha = random.randint(0, len(tabuleiro)-1)
        coluna = random.randint(0, len(tabuleiro)-1)

        if (linha, coluna) in tirosCpu:
            continue

        tirosCpu.add((linha, coluna))

        resultado = (realizarTiro(tabuleiro, linha, coluna))

        print(f"\nCPU atirou em ({linha}, {coluna})")

        if resultado:
            print("CPU acertou!")

        else:
            print("CPU errou!")

        return


def jogar():

    nome = input("\nNome: ")
    config = (escolherDificuldade())

    tabuleiroJogador = (criarTabuleiro(config["tamanho"]))
    tabuleiroCpu = (criarTabuleiro(config["tamanho"]))

    posicionarNaviosJogador(tabuleiroJogador, config["navios"])
    posicionarNaviosCpu(tabuleiroCpu, config["navios"])

    tiros = 0
    tirosCpu = set()

    while True:

        print("\nSEU TABULEIRO")
        mostrarTabuleiro(tabuleiroJogador)

        print("\nTABULEIRO INIMIGO")
        mostrarTabuleiro(tabuleiroCpu, True)

        try:

            linha = int(input("\nLinha: "))
            coluna = int(input("Coluna: "))

            resultado = (realizarTiro(tabuleiroCpu, linha, coluna))

            if resultado is None:
                print("Posicao repetida.")
                continue

            tiros += 1

            if resultado:
                print("\nAcertou!")

            else:
                print("\nAgua!")

            if verificarVitoria(tabuleiroCpu):
                salvarRanking(nome, "Vitoria", tiros, config["nome"])
                print("\nVOCE VENCEU!")

                break


            tiroCpu(tabuleiroJogador, tirosCpu)

            if verificarVitoria(tabuleiroJogador):
                salvarRanking(nome, "Derrota", tiros, config["nome"])
                print("\nCPU VENCEU!")

                break

        except ValueError:

            print("Digite apenas numeros.")