import random

def criarTabuleiro(tamanho):
    """
    Cria um tabuleiro quadrado preenchido com água (~).
    
    Parameters:
        tamanho (int): O tamanho do tabuleiro (número de linhas e colunas).
    
    Returns:
        list: Um tabuleiro representado como uma lista de listas.
    """
    return [["~" for _ in range(tamanho)] for _ in range(tamanho)]


def mostrarTabuleiro(tabuleiro, esconder=False):
    """
    Exibe o tabuleiro.
    Se esconder=True, oculta os navios inimigos.
    
    Parameters:
        tabuleiro (list): O tabuleiro a ser exibido.
        esconder (bool): Se True, oculta os navios inimigos.
    
    Returns:
        None
    """

    print()
    print(" ", end=" ")

    for i in range(len(tabuleiro)):
        print(i, end=" ")

    print()

    # Exibe cada linha do tabuleiro com seu índice
    for i, linha in enumerate(tabuleiro):

        print(i, end=" ")

        # Exibe cada valor da linha do tabuleiro
        for valor in linha:

            # Oculta navios não atingidos do tabuleiro inimigo
            if esconder and valor == "N":
                print("~", end=" ")

            else:
                print(valor, end=" ")

        print()


def validarPosicao(tabuleiro, linha, coluna, tamanhoNavio, orientacao):
    """
    Verifica se um navio pode ser colocado na posição desejada.
    
    Parameters:
        tabuleiro (list): O tabuleiro onde o navio será colocado.
        linha (int): Linha inicial para colocar o navio.
        coluna (int): Coluna inicial para colocar o navio.
        tamanhoNavio (int): Tamanho do navio a ser colocado.
        orientacao (str): Orientação do navio ("H/V").     
        
    Returns:
        list or None: Lista de posições válidas para o navio ou None se inválido.  
    """

    tamanho = len(tabuleiro)
    posicoes = []

    # Verifica cada posição do navio baseado na orientação
    for i in range(tamanhoNavio):

        if orientacao == "H":
            l = linha
            c = coluna + i

        else:
            l = linha + i
            c = coluna

        # Impede posições fora do tabuleiro
        if (l < 0 or c < 0 or l >= tamanho or c >= tamanho):
            return None

        # Impede sobreposição de navios
        if tabuleiro[l][c] == "N":
            return None

        posicoes.append((l, c))

    return posicoes


def posicionarNaviosJogador(tabuleiro, navios):
    """
    Permite ao jogador posicionar seus navios manualmente.
    
    Parameters:
        tabuleiro (list): O tabuleiro do jogador.
        navios (list): Lista de tamanhos dos navios a serem posicionados.
        
    Returns:
        None
    """

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
                    
                    # Marca as posições válidas do navio no tabuleiro
                    for l, c in posicoes:
                        tabuleiro[l][c] = "N"

                    break

                print("Posicao invalida")

            except:
                print("Entrada invalida")


def posicionarNaviosCpu(tabuleiro, navios):
    """
    Posiciona automaticamente os navios da CPU.
    
    Parameters:
        tabuleiro (list): O tabuleiro da CPU.
        navios (list): Lista de tamanhos dos navios a serem posicionados.
    
    Returns:
        None
    """

    for tamanhoNavio in navios:

        while True:

            # Gera posições aleatórias para o navio
            linha = random.randint(0, len(tabuleiro)-1)
            coluna = random.randint(0, len(tabuleiro)-1)

            orientacao = random.choice(["H", "V"])

            posicoes = validarPosicao(tabuleiro, linha, coluna, tamanhoNavio, orientacao)

            if posicoes:

                for l, c in posicoes:
                    tabuleiro[l][c] = "N"

                break


def realizarTiro(tabuleiro, linha, coluna):
    """
    Processa um tiro e retorna:
    
    Parameters:
        tabuleiro (list): O tabuleiro onde o tiro será realizado.
        linha (int): Linha do tiro.
        coluna (int): Coluna do tiro.
    
    Returns:
        True (Acerto), False (Erro) or None (Posição Repetida): Resultado do tiro.
    """

    if tabuleiro[linha][coluna] == "X":
        return None

    if tabuleiro[linha][coluna] == "N":
        
        tabuleiro[linha][coluna] = "X"
        return True

    tabuleiro[linha][coluna] = "O"
    return False


def verificarVitoria(tabuleiro):
    """
    Verifica se ainda existem navios no tabuleiro.
    
    Parameters:
        tabuleiro (list): O tabuleiro a ser verificado.
        
    Returns:
        bool: True se todos os navios foram destruídos, False caso contrário.
    """

    for linha in tabuleiro:

        if "N" in linha:
            return False

    return True