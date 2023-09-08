# obtem operação matemática da função pegaResultadoDaOperacaoMatematica do módulo "numeros.py"
def obtemOperacaoMatematica(operacaoMatematica):

    escreveOperacaoMatematicaNoHistorico(operacaoMatematica)


# Escreve a última operação matemática no histórico
def escreveOperacaoMatematicaNoHistorico(operacaoMatematica):
    with open("historico.txt", "a") as arquivo:
        arquivo.write(operacaoMatematica)
    




def mostraHistoricoDaCalculadora() -> None:
    from strings import menu
    from numeros import verificaSeLinhaAtual_e_NomeDeUmaOperacao


    # Abre o arquivo para leitura
    with open("historico.txt", "r") as arquivo:

        is_MathOperationName = False
        # indica o número de operações já mostradas, o que ajuda na contagem da exibição.Por exemplo, se não tiver sido mostrada nenhuma operação, o resultado provavelmente será esse:
        # 1 - Operação matemática
        quantidadeOperacoesMostradas = 0

        # pega o arquivo "historico.txt" e coloca cada linha como um elemento na lista
        conteudoArquivo = arquivo.readlines()

        isHistoryEmpty = verificaSeHistoricoEstaVazio()

        # histórico vazio
        if isHistoryEmpty:
            print("\033[1;31mHistórico vazio!\033[m")
            return



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
            
            


def verificaTamanhoDoArquivo():

    with open("historico.txt", "r") as arquivo:

        conteudoArquivo = arquivo.readlines()

        arquivo.close()

        if len(conteudoArquivo) >= 200:
            return True

        else:
            return False


def resetaArquivo():
    '''--> Reseta o arquivo "historico.txt"
            :return: sem retorno'''

    with open("historico.txt", "r+") as arquivo:
        
        # reseta o arquivo o deixando com 0 bytes
        arquivo.truncate(0)



    

def verificaSeHistoricoEstaVazio():
    '''--> Verifica se o histórico de cálculos está vazio
            :return: retorna um valor booleano ("True" significa que o arquivo está vazio, "False" indica que não está)
    '''


    with open("historico.txt", "r") as arquivo:

        conteudoArquivo = arquivo.readlines()

        # arquivo vazio
        if len(conteudoArquivo) == 0:
            return True

        # arquivo não vazio
        else:
            return False