import random

def criarTabuleiro(tamanho):
    return [["~" for _ in range(tamanho)] for _ in range(tamanho)]


def mostrarTabuleiro(tabuleiro, esconder=False):

    print()
    print(" ", end=" ")

    for i in range(len(tabuleiro)):
        print(i, end=" ")

    print()

    for i, linha in enumerate(tabuleiro):

        print(i, end=" ")

        for valor in linha:

            if esconder and valor == "N":
                print("~", end=" ")

            else:
                print(valor, end=" ")

        print()


def validarPosicao(tabuleiro, linha, coluna, tamanhoNavio, orientacao):

    tamanho = len(tabuleiro)
    posicoes = []

    for i in range(tamanhoNavio):

        if orientacao == "H":
            l = linha
            c = coluna + i

        else:
            l = linha + i
            c = coluna

        if (l < 0 or c < 0 or l >= tamanho or c >= tamanho):
            return None

        if tabuleiro[l][c] == "N":
            return None

        posicoes.append((l, c))

    return posicoes


def posicionarNaviosJogador(tabuleiro, navios):

    for tamanhoNavio in navios:

        while True:

            try:

                mostrarTabuleiro(tabuleiro)

                print(f"\nNavio tamanho: {tamanhoNavio}")

                linha = int(input("Linha: "))
                coluna = int(input("Coluna: "))

                orientacao = (input("Orientacao (H/V): ").upper())

                posicoes = validarPosicao(tabuleiro,linha,coluna,tamanhoNavio,orientacao)

                if posicoes:

                    for l, c in posicoes:
                        tabuleiro[l][c] = "N"

                    break

                print("Posicao invalida")

            except:
                print("Entrada invalida")


def posicionarNaviosCpu(tabuleiro, navios):

    for tamanhoNavio in navios:

        while True:

            linha = random.randint(0, len(tabuleiro)-1)
            coluna = random.randint(0, len(tabuleiro)-1)

            orientacao = random.choice(["H", "V"])

            posicoes = validarPosicao(tabuleiro, linha, coluna, tamanhoNavio, orientacao)

            if posicoes:

                for l, c in posicoes:
                    tabuleiro[l][c] = "N"

                break


def realizarTiro(tabuleiro, linha, coluna):

    if tabuleiro[linha][coluna] == "X":
        return None

    if tabuleiro[linha][coluna] == "N":
        
        tabuleiro[linha][coluna] = "X"
        return True

    tabuleiro[linha][coluna] = "O"
    return False


def verificarVitoria(tabuleiro):

    for linha in tabuleiro:

        if "N" in linha:
            return False

    return True