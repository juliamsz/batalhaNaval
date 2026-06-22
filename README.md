# Batalha Naval em Python

## Descrição do projeto

Este projeto consiste no desenvolvimento de um jogo de Batalha Naval utilizando Python.

O jogo funciona entre um jogador e a CPU, em que ambos possuem tabuleiros contendo navios posicionados previamente. Durante cada rodada, o jogador escolhe coordenadas para realizar disparos enquanto a CPU executa suas jogadas automaticamente.

O objetivo é localizar e destruir todos os navios adversários antes que todos os próprios navios sejam atingidos.

O projeto foi desenvolvido com o objetivo de aplicar conceitos estudados na disciplina de Introdução à Programação para Engenharias, como manipulação de arquivos, estruturas de dados e lógica de programação.

---

## Estrutura do projeto

* `main.py`
  Arquivo principal responsável pelo menu e pelo início da execução do programa.

* `jogo.py`
  Responsável pelo controle da partida, gerenciamento dos turnos e integração entre os módulos.

* `tabuleiro.py`
  Implementa funções relacionadas à criação, exibição e manipulação do tabuleiro.

* `ranking.py`
  Responsável pelo armazenamento, leitura e exibição do ranking das partidas.

* `ranking.txt`
  Arquivo utilizado para persistência dos resultados.

---

## Instruções de uso

1. Certifique-se de que todos os arquivos estejam no mesmo diretório.
2. Execute o arquivo `main.py`.
3. Escolha uma das opções do menu:

   * `1` → Iniciar partida
   * `2` → Visualizar ranking
   * `3` → Encerrar programa
4. Durante a partida:

   * Escolha a dificuldade;
   * Informe linha e coluna para realizar os disparos;
   * Continue jogando até destruir todos os navios adversários.

---

## Divisão de tarefas

**Luiz Carlos de Oliveira Junior**

* Desenvolvimento das funções do arquivo `ranking.py`;
* Documentação da seção correspondente no relatório.

**Gisele Ferreira Reis Faleiros**

* Desenvolvimento das funções do arquivo `tabuleiro.py`;
* Documentação da seção correspondente no relatório.

**Júlia Martins Souza**

* Desenvolvimento dos arquivos `jogo.py` e `main.py`;
* Documentação das seções correspondentes no relatório.
* Elaboração do arquivo `README`

### Atividades em conjunto

* Planejamento geral do projeto;
* Integração dos módulos;
* Testes e correções finais.

---

## Tecnologias utilizadas

* Python
* Arquivos `.txt`
* Programação modular
