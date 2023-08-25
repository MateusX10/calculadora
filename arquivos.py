arquivo = open("historico.txt", "a")
print('oi')


# abre arquivo "historico.txt" em um determinado modo (a, w, x...)
def abreArquivo(modo):

    try:
        arquivo = open("historico.txt", modo)

    except:
        print("\033[1;31mOcorreu um erro ao fazer a leitura/escrita do arquivo.\033[m")

    else:
        return arquivo

# obtem operação matemática da função pegaResultadoDaOperacaoMatematica do módulo "numeros.py"
def obtemOperacaoMatematica(operacaoMatematica):

    escreveOperacaoMatematicaNoHistorico(operacaoMatematica)


# Escreve a última operação matemática no histórico
def escreveOperacaoMatematicaNoHistorico(operacaoMatematica):
    arquivo = abreArquivo("a")
    arquivo.write(operacaoMatematica)


def mostraHistoricoDaCalculadora():
    from strings import menu
    from numeros import verificaSeLinhaAtual_e_NomeDeUmaOperacao


    # Abre o arquivo para leitura
    arquivo = abreArquivo("r")
    is_MathOperationName = False
    # indica o número de operações já mostradas, o que ajuda na contagem da exibição.Por exemplo, se não tiver sido mostrada nenhuma operação, o resultado provavelmente será esse:
    # 1 - Operação matemática
    quantidadeOperacoesMostradas = 0

    # pega o arquivo "historico.txt" e coloca cada linha como um elemento na lista
    conteudoArquivo = arquivo.readlines()

    # percorre a lista de conteúdo de histórico inteira
    for linha in range(len(conteudoArquivo)):
        # pega a linha atual do arquivo
        linhaAtual = conteudoArquivo[linha]
        # verifica se a linha atual é o nome de uma operação matemática
        is_MathOperationName = verificaSeLinhaAtual_e_NomeDeUmaOperacao(linhaAtual)

        # se a linha atual for o nome de uma operação matemática, então o nome da operação matemática será imprimida formatada de acordo com a sua numeração/posição (se tiver sido a primeira operação matemática feita pelo usuário, então aparecerá assim:   1 - operação matemática)
        if is_MathOperationName:
            quantidadeOperacoesMostradas += 1

            # Imprime a operação matemática formatada de acordo com sua posição como usada pelo usuário
            print(f"{quantidadeOperacoesMostradas} - {linhaAtual}")
            is_MathOperationName = False

        # Imprirá provavelmente o cálculo de uma operação matemática
        else:
            print(f"{linhaAtual}")


