import sys 

# define a quantidade máxima de dígitos da saída de uma operação matemática
#sys.set_int_max_str_digits(900000000)


# Valida um valor inteiro lido pelo teclado
def leiaInt(msg) -> int:
    n1 = 0
    while True:
        try:
            n1 = int(input(msg))
        except (ValueError, NameError, TypeError):
            print("\033[1;31mOps, por favor, informe apenas números inteiros!\033[m")
        except (KeyboardInterrupt):
            print('\n\033[1;31mPara sair, digite "0" no menu\033[m')
        else:
            return (n1)

# Valida um valor ponto flutuante pelo teclado
def leiaFloat(msg) -> float:
    n1 = 0.0
    while True:
        try:
            n1 = float(input(msg))
        except (NameError, ValueError, TypeError):
            print('\033[1;31mOps, por favor, digite apenas números de ponto flutuante!\033[m')

        except (KeyboardInterrupt):
            print('\n\033[1;31mPara sair, digite "0" no menu\033[m')
        else:
            return (n1)

# Verifica se a opção escolhida pelo usuário existe
def verificaSeOpcaoEscolhidaExisteNaLista(categoriaMatematicaEscolhida, operacaoMatematicaEscolhida) -> bool:
    from strings import menu

    # a opção existe
    if operacaoMatematicaEscolhida <= len(menu[categoriaMatematicaEscolhida]) and operacaoMatematicaEscolhida > 0 or operacaoMatematicaEscolhida == 999:
        return True

    # a opção não existe
    else:
        return False
   

# lê dois valores pelo teclado e os retorna em uma lista
def leValores() -> list:
    n1 = leiaFloat("1º valor: ")
    n2 = leiaFloat("2º valor: ")
    return [n1, n2]

# Retorna a soma de dois números de ponto flutuante
def somar() -> None:
    valores =  leValores()
    result = valores[0] + valores[1]
    print(f"{valores[0]} + {valores[1]} = {result}")

    pegaResultadoDaOperacaoMatematica("ADICAO", [valores[0], valores[1]], result)

# Retorna a subtração de dois número de ponto flutuante
def subtrair() -> None:
    valores = leValores()
    result = valores[0] - valores[1]
    print(f"{valores[0]} - {valores[1]} = {result}")

    pegaResultadoDaOperacaoMatematica("SUBTRACAO", [valores[0], valores[1]], result)

# Retorna a multiplicação de dois números ponto flutuante
def multiplicar() -> None:
    valores = leValores()
    result = valores[0] * valores[1]
    print(f"{valores[0]} x {valores[1]} = {result}")

    pegaResultadoDaOperacaoMatematica("MULTIPLICACAO", [valores[0], valores[1]], result)

# Retorna a divisão de dois números ponto flutuante
def dividir() -> None:
    while True:
        valores = leValores()
        try:
            result = valores[0] / valores[1]
        except (ZeroDivisionError):
            print("\033[1;31mÉ impossível dividir um número por 0!")
            print("Tente novamente...\033[m")
        else:
            print(f"{valores[0]} / {valores[1]} = {result}")
            break

    pegaResultadoDaOperacaoMatematica("DIVISAO", [valores[0], valores[1]], result)

# Imprime na tela a potência de um número de base "x" e expoente "y" (o usuário escolhe)
def potenciar() -> None:
    base = leiaFloat("Número: ")
    expoente = leiaInt("Índice: ")
    result = base ** expoente
    print(f"{base} ** {expoente} = {result}")

    pegaResultadoDaOperacaoMatematica("POTENCIACAO", [base, expoente], result)

# Imprime na tela a raiz quadrada de um número "x"
def RaizQuadrada() -> None:
    from math import sqrt


    numero = float(input("Número: "))
    result = sqrt(numero)
    print(f"Raiz quadrada = {result:.1f}")

    pegaResultadoDaOperacaoMatematica("RAIZ", [numero], result)


# Imprime na terla o fatorial de um número, juntamento com todo o cálculo por trás do resultado
def fatorial() -> None:
    f = 1
    n = leiaInt("Número a ser calculado: ")
    print(f"Fatorando número {n}!...")
    print(f"{n}! = ", end='')
    for vlr in range(n, 0, -1):
        f *= vlr
        print(f'{vlr} x ' if vlr != 1 else f'{vlr} = {f}', end='')

# Calcula o percentual de um número
def percentual() -> None:
    n1 = leiaFloat("Número: ")
    percentual = leiaFloat("Percentual: ")
    result = n1 * percentual / 100
    print(f'{n1} % {percentual} = {result}')

    pegaResultadoDaOperacaoMatematica("PORCENTAGEM", [n1, percentual], result)


# Arredonda um número para cima
def ArredondarParaCima() -> None:
    from math import ceil


    n1 = leiaFloat('Informe o número que deseja arredondar para cima: ')
    result = ceil(n1)
    print(f'{n1} arredondado para cima = {result}')

# Arredonda um número para baixo
def ArredondarParaBaixo() -> None:
    from math import floor

    n1 = leiaFloat('Informe o número que deseja arredondar para baixo: ')
    result = lambda numero: floor(numero)
    print(f'{n1} arredondado para baixo = {result(n1)}')

# Calcula a hipotenusa
def hipotenusa():
    from math import hypot

    catetoOposto = leiaFloat("Cateto oposto: ")
    catetoAdjacente = leiaFloat("Cateto adjacente: ")
    
    hipotenusa = lambda cateto1, cateto2: hypot(cateto1, cateto2)
    print(f"A hipotenusa vale {hipotenusa(catetoOposto, catetoAdjacente)}")

# Calcula o seno
def seno() -> None:
    from math import sin, radians


    #n = float(input("Valor do seno a ser calculado: "))
    n = leiaFloat("Valor do seno a ser calculado: ")
    #result = sin(radians(n))
    result = lambda num: sin(radians(num))
    print(f"Seno de {n}° = {result(n)}")

# Calcula o cosseno
def cosseno() -> None:
    from math import cos, radians


    n = leiaFloat("Valor do cosseno a ser calculado: ")
    result = cos(radians(n))
    print(f"Cosseno de {n}° = {result}")

# Calcula a tangente
def tangente() -> None:
    from math import tan, radians


    n = leiaFloat("Valor da tangente a ser calculada: ")
    result = tan(radians(n))
    print(f"Tangente de {n}° = {result}")


# Calcula o logaritmo de uma dada base e logaritmando
def logaritmo() -> None:
    from math import log
    from time import sleep


    base = leiaFloat("Base do logaritmo: ")
    logaritmando = leiaFloat("Logaritmando do logaritmo: ")
    result = log(logaritmando, base)
    print(f"Calculando logaritmo de base {base:.1f} e de logaritmando {logaritmando:.1f}...")
    sleep(1)
    print(f"= {result}")

    pegaResultadoDaOperacaoMatematica("LOGARITMO", [base,logaritmando], result)



# Calcula a média entre n valores determinados pelo usuário
def media() -> None:
    QuantidadeValores = media =  0
    valores = list()
    listaTemporaria = list()
    while True:
        QuantidadeValores = leiaInt("Calcular a média entre quantos valores? ")
        if (QuantidadeValores < 2):
            print("\033[1;31mImpossível calcular a média!")
            print("Tente novamente...\033[m")
        else:
            break
    
    for cont in range(0, QuantidadeValores):
        listaTemporaria.append(leiaInt(f"{cont + 1}º valor: "))
    valores.extend(listaTemporaria)
        
    media = (sum(valores)) / QuantidadeValores
    print(f"A média vale {media:.1f}")


# Imprime o maior e o menor valor dentre uma lista de valores informados pelo usuário
def valorMinimoMaximo() -> None:
    quantidade_valores = 0
    lista_valores = []

    # while é executado até que o usuário defina uma quantidade de valores superior a 1
    while True:
        quantidade_valores = leiaInt("Quantos valores a lista terá? ")
        if (quantidade_valores < 1):
            print("\033[1;31mImpossível definir um mínimo e um máximo em uma lista vazia!")
            print("Por favor, tente novamente...\033[m")
        else:
            break
    
    # permite ao usuário adicionar "n" valores a lista "lista_valores"
    for vlr in range(0, quantidade_valores):
        lista_valores.append(leiaFloat(f"{vlr + 1}º valor: "))

    # Função lambda que retorna o mínimo e máximo de uma lista de números
    minimoMaximo = lambda lista: [min(lista), max(lista)]
    # pega o menor valor da lista de núumeros
    menor_valor = minimoMaximo(lista_valores)[0]
    # Pega o maior valor da lista de números
    maior_valor = minimoMaximo(lista_valores)[-1]

    print(f"Valor mínimo = {menor_valor} \nValor máximo = {maior_valor}")


# Converte um valor decimal em binário
def decimalParaBinario() -> None:
    valor = leiaInt("Valor decimal a ser convertido: ")
    decimalConvertidoParaBin = bin(valor)[2:]
    print(f'{"decimal":>10}{"binário":>20}')
    print(f"{valor:>10}  {decimalConvertidoParaBin:>20}")

# Converte um valor binário em decimal
def binarioParaDecimal() -> None:
    valorBinario = input("Valor binário: ")
    binarioConvertidoParaDecimal = int(valorBinario, 2)
    print(f"{'Valor binário':>10}{'Valor decimal':>20}")
    print(f"{valorBinario:>10}{binarioConvertidoParaDecimal:>20}")


# Converte de decimal para octal
def decimalParaOctal() -> None:
    valor = leiaInt("Valor decimal a ser convertido: ")
    decimalParaOctal = oct(valor)[2:]
    print(f"{'decimal':>10}{'octal':>20}")
    print(f'{valor:>10}{decimalParaOctal:>20}')

# Converte de octal para decimal
def octalParaDecimal() -> None:
    valorEmOctal = input("Valor em octal: ")
    octalConvertidoEmDecimal = int(valorEmOctal, 8)
    print(f"{'octal':>10}{'decimal':>20}")
    print(f"{valorEmOctal:>10}{octalConvertidoEmDecimal:>20}")

# Converte de decimal para hexadecimal
def decimalParaHexadecimal() -> None:
    valor = leiaInt("Valor decimal: ")
    decimalConvertidoEmHexadecimal = hex(valor)[2:]
    print(f"{'decimal':>10}{'hexadecimal':>20}")
    print(f"{valor:>10}{decimalConvertidoEmHexadecimal:>20}")

# Converte de hexadecimal para decimal
def hexadecimalParaDecimal() -> None:
    valor = input("Valor em hexadecimal: ")
    hexadecimalConvertidoEmDecimal = int(valor, 16)
    print(f"{'HEXADECIMAL':>10}{'DECIMAL':>20}")
    print(f"{valor:>10}{hexadecimalConvertidoEmDecimal:>20}")


# Calcula o módulo
def calculaMóduloDeUmNumero() -> None:
    num = leiaInt("Valor: ")
    modulo = num * -1 if num < 0 else num
    print(f"{'valor':>10}{'módulo':>20}")
    print(f"{num:>8}{modulo:>19}")


# Calcula moda
def calculaModaDeUmaListaDeNumeros() -> None:
    #variáveis/variáveis compostas
    valores = {}
    listaNumeros = list()
    cont = 0
    ultimoValorAdicionado = maiorLista = moda =  0
    valorAdicionadoAoDicionario = False
    totalNumeros = leiaInt("Quantidade de números: ")

    # while vai executar o número de vezes especificada pelo usuário na variáveis "totalNumeros",isto é, a quantidade de números que o usuário vai dar na entrada de dados
    while (cont < totalNumeros) :
        listaNumeros.append(leiaInt(f"{cont + 1}º valor: "))
        ultimoValorAdicionado = listaNumeros[-1]
        cont += 1
        # verifica se o dicionário está vazio
        if valores:
            # pega cada lista contida no dicionário e verifica se o último valor lido pelo teclado já existe no dicionário: se já existir em uma lista "x" do dicionário, então o valor que já existe é adicionado a essa lista de números que corresponde com esse número a fim de que no final possa-se medir o tamanho de cada lista, a lista que tiver mais valores indica a moda.Cada valor adicionado lido pelo teclado é adicionado em uma lista diferente do dicionário, isto é, os mesmos valores ficam na mesma lista e valores diferentes ficam em listas diferentes e assim no final a lista que tiver mais valores será a moda.Ex: {"2":[2,2,2,2]   "1":[1,1,1,1,1] "5":[5,5,5,5,5] "3":[3] "10":[10,10]  "12":[12,12]} --> mesmos valores são colocados na mesma lista
            for lista in valores.values():
                if ultimoValorAdicionado in lista:
                    lista.append(ultimoValorAdicionado)
                    #indica que um valor já foi adicionado ao dicionário
                    valorAdicionadoAoDicionario = True

        #  se o dicionário estiver vazio ou o valor lido pelo usuário não existir no dicionário, então é criada uma nova chave com esse valor e o valor da chave será o mesmo que a chave.
        if not valores or not valorAdicionadoAoDicionario:
            valores[f"{ultimoValorAdicionado}"] = [ultimoValorAdicionado]
        valorAdicionadoAoDicionario = False
            
    # daqui para baixo é o código que determina a moda
    for lista in valores.values():
        # significa que é o primeiro laço do for e então a variável "maiorLista" está zerada
        if maiorLista == 0:
            # var "maiorLista" está recebendo o comprimento/tamanho da lista atual do laço
            maiorLista = len(lista)
            # nesse caso, é atribuído um valor da lista contida no dicionário
            moda = lista[0]
        # significa que é a segunda iteração do for ou adiante
        else:
            # verifica se o comprimento da lista atual lida no laço é maior que o tamanho da maior lista lida até agora
            if len(lista) > maiorLista:
                maiorLista = len(lista)
                moda = lista[0]
    print(f"A moda da lista de números {listaNumeros} vale {moda}")


# Calcula a mediana 
def calculaMedianaDeUmaListaDeNumeros() -> None:
    listaNumeros = []
    quantidadeValores = leiaInt("Quantidade de valores: ")
    cont = 0
    while cont < quantidadeValores:
        listaNumeros.append(leiaInt(f"{cont + 1}º valor: "))
        cont += 1
    listaNumeros.sort()
    tamanhoLista = len(listaNumeros)
    # var "numeroDoMeio" --> o número do meio da lista de número fornecida 
    numeroDoMeio = listaNumeros[tamanhoLista // 2]
    # var "numeroDoMeioDois" --> o "segundo" número do meio da lista que nesse caso será de uma lista com quantidade par de valores
    numeroDoMeioDois = listaNumeros[(tamanhoLista // 2) - 1]
    # daqui para baixo, o código define a mediana
    if tamanhoLista % 2 == 0:
        # mediana de uma lista par de valores
        mediana = (numeroDoMeio + numeroDoMeioDois)  / 2
    else:
        #mediana de uma lista ímpar de valores
        mediana = numeroDoMeio

    print(f"A mediana da lista de números {listaNumeros} vale {mediana} ")


# Lê e retorna dois conjuntos definidos e não nulos
def defineDoisConjuntos() -> list:
    from strings import title

    
    conjunto1 = set()
    conjunto2 = set()
    quantidadeValoresDoConjunto1 = quantidadeValoresDoConjunto2 = 0

    # define quantos valores terá cada um dos dois conjuntos.Conjuntos vazios não são permitidos.O 
    while not quantidadeValoresDoConjunto1 or not quantidadeValoresDoConjunto2:
        quantidadeValoresDoConjunto1 = leiaInt("Quantos valores terá o conjunto 1? ")
        quantidadeValoresDoConjunto2 = leiaInt("Quantos valores terá o conjunto 2? ")
        if quantidadeValoresDoConjunto1 == 0 or quantidadeValoresDoConjunto2 == 0:
            print("\033[1;31mPor favor, não deixe nenhum conjunto vazio!\033[m")

    title("conjunto 1")
    # O for vai iterar o número de vezes de acordo com a quantidade de valores que o usuário requisitou para o conjunto 1.Em cada iteração, é adicionado um novo valor ao conjunto, valor esse que é definido pelo usuário.(o mesmo para o segundo for logo abaixo)
    for indice in range(0,quantidadeValoresDoConjunto1):
        conjunto1.add(leiaInt(f"{indice + 1}º valor: "))
    title("conjunto 2")
    for indice in range(0, quantidadeValoresDoConjunto2):
        conjunto2.add(leiaInt(f"{indice + 1}º valor: "))

    return [conjunto1,conjunto2]
    

# Faz a união de dois conjuntos
def UnirDoisConjuntos():
    lista_conjunto = defineDoisConjuntos()

    conjunto1 = lista_conjunto[0]
    conjunto2 = lista_conjunto[1]
    # faz a união entre os dois conjuntos 
    uniao = conjunto1.union(conjunto2)

    print(f"\nA união entre os conjuntos {conjunto1} e {conjunto2} é {uniao}")


# Calcula a interseção entre dois conjuntos
def InterseçãoDeDoisConjuntos():
    lista_conjuntos = defineDoisConjuntos()
    conjunto1 = lista_conjuntos[0]
    conjunto2 = lista_conjuntos[1]
    intersecao = conjunto1.intersection(conjunto2)

    print(f"A interseção entre os conjuntos {conjunto1} e {conjunto2} é {intersecao}")

# Calcula a diferença entre dois conjuntos
def diferencaDeDoisConjuntos():
    lista_conjuntos = defineDoisConjuntos()
    conjunto1 = lista_conjuntos[0]
    conjunto2 = lista_conjuntos[1]
    
    # determina a diferença do conjunto A para o conjunto B
    diferenca = conjunto1.difference(conjunto2)

    # indica que não há diferença 
    if not diferenca:
        print(f"\033[1;31mNão há diferença do conjunto {conjunto1} para o conjunto {conjunto2}\033[m")
        return

    # há diferença
    print(f"A diferença do conjunto {conjunto1}  para o conjunto {conjunto2} vale {diferenca}")


def verificaSeConjunto_e_SubconjuntoDeOutro():
    lista_conjuntos = defineDoisConjuntos()

    conjunto1 = lista_conjuntos[0]
    conjunto2 = lista_conjuntos[1]

    # determina se é subconjunto - True (é subconjunto) ; False (não é subconjunto)
    isSubSet = conjunto1.issubset(conjunto2)

    # Verifica se conjunto 1 é subconjunto de conjunto 2
    if isSubSet:
        print(f"Conjunto {conjunto1} é um subconjunto do conjunto {conjunto2}")

    else:
        print(f"Conjunto {conjunto1} não é um subconjunto do conjunto{conjunto2}")
        


# pega o cálculo e o resultado de uma operação matemática e retorna para o módulo "arquivos.py" para que as novas operações matemáticas sejam inclusas no histórico da calculadora
def pegaResultadoDaOperacaoMatematica(operacao, valoresCalculo, resultadoOperacao) -> str:
    from arquivos import obtemOperacaoMatematica


    valorFormatado = formataCalculoDeUmaOPeracaoMatematica(operacao, valoresCalculo,resultadoOperacao)

    # chama a função do módulo "arquivos.py" que vai obter a operação 
    obtemOperacaoMatematica(valorFormatado)



# Formata o cálculo e o seu resultado para que seja exibido no histórico da calculadora
def formataCalculoDeUmaOPeracaoMatematica(operacaoMatematica, valoresCalculo, resultadoOperacao):

    valorFormatado = ' '

    operacoesBasicas = {"ADICAO": "+", "SUBTRACAO": "-", "MULTIPLICACAO": "x", "DIVISAO": "/", "POTENCIACAO": "**", "PORCENTAGEM": "%"}

    for nomeOperacao, simboloOperacao in operacoesBasicas.items():
        if operacaoMatematica == nomeOperacao:
            simboloMatematico = simboloOperacao

    if operacaoMatematica in operacoesBasicas:
        valorFormatado = f'''{operacaoMatematica} \n{valoresCalculo[0]} {simboloMatematico} {valoresCalculo[1]} = {resultadoOperacao}\n'''


    elif operacaoMatematica == "LOGARITMO":
        valorFormatado = f'''{operacaoMatematica} \nlog_{valoresCalculo[0]}({valoresCalculo[1]}) = {resultadoOperacao}'''
    

        

    return str(valorFormatado)



# Verifica se a linha atual do arquivo "historico.txt" é o nome de uma operação matemática (ex: ADIÇÃO, SUBTRAÇÃO, MULTIPLICAÇÃO...).Se for, é retornado True
def verificaSeLinhaAtual_e_NomeDeUmaOperacao(linhaAtual) -> bool:
    from strings import menu

    # começa com "1" para ignorar as categorias de operações matemáticas (ex: OPERAÇÕES BÁSICAS, CONJUNTOS)
    cont = 1

    # percorre a lista de operações matemáticas "menu" inteira
    while cont < len(menu):
            # percorre uma categoria específica inteira da lista "menu"
            for operacao in menu[cont]:
                # Verifica se a linha atual é o nome de uma operação matemática (ex: ADIÇÃO)
                if linhaAtual.strip() == operacao:
                    return True
            
            cont += 1

    # se não for o nome de uma operação matemática, mas sim provavelmente o próprio cálculo ou resultado, é retorna "False"
    return False