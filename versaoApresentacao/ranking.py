from datetime import datetime


ARQUIVO = "batalhaNaval/ranking.txt"


def salvarRanking(nome, resultado, tiros, dificuldade):

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

    try:

        ranking = []

        with open(ARQUIVO, "r", encoding="utf8") as arq:

            for linha in arq:

                ranking.append(linha.strip().split(";"))

        def pegarTiros(linha):
            return int(linha[2])


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

        print("Nenhum ranking encontrado.")