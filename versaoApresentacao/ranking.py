from datetime import datetime

# Caminho do arquivo onde o ranking é armazenado
ARQUIVO = "versaoApresentacao/ranking.txt"


def salvarRanking(nome, resultado, tiros, dificuldade):
    """
    Salva uma partida no arquivo de ranking.
    
    Parameters:
        nome (str): Nome do jogador.
        resultado (str): Resultado da partida ("Vitoria" ou "Derrota").
        tiros (int): Número de tiros realizados pelo jogador.
        dificuldade (str): Dificuldade escolhida pelo jogador.
        
    Returns:
        None
    """

    with open(ARQUIVO, "a", encoding="utf8") as arq:

        data = (datetime.now().strftime("%d/%m/%Y"))

        arq.write(
            f"{nome};"
            f"{resultado};"
            f"{tiros};"
            f"{dificuldade};"
            f"{data}\n"
        )


def mostrarRanking():
    """
    Lê, ordena e exibe o ranking por quantidade de tiros.
    
    Parameters:
        None
    
    Returns:
        None
    """

    try:

        ranking = []

        with open(ARQUIVO, "r", encoding="utf8") as arq:

            for linha in arq:

                ranking.append(linha.strip().split(";"))

        def pegarTiros(linha):
            """
            Retorna a quantidade de tiros para ordenação.
            
            Parameters:
                linha (list): Uma linha do ranking.
            
            Returns:
                int: Quantidade de tiros.
            """
            return int(linha[2])


        # Ordena do menor número de tiros para o maior
        ranking.sort(key=pegarTiros)

        print("\n=== RANKING ===")

        for r in ranking:

            print(
                f"{r[0]}"
                f" | "
                f"{r[1]}"
                f" | "
                f"{r[2]} tiros"
                f" | "
                f"{r[3]}"
                f" | "
                f"{r[4]}"
            )

    except FileNotFoundError:

        # Tratamento para primeira execução sem arquivo criado
        print("Nenhum ranking encontrado.")