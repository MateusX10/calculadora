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

def obtemOPeracaoMatematica(operacaoMatematica):

    escreveOperacaoMatematicaNoHistorico(operacaoMatematica)


def escreveOperacaoMatematicaNoHistorico(operacaoMatematica):
    arquivo = abreArquivo("a")
    arquivo.write(operacaoMatematica)