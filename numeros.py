# Valida um valor inteiro lido pelo teclado
def leiaInt(msg):
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
def leiaFloat(msg):
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

def leValores():
    n1 = leiaFloat("1º valor: ")
    n2 = leiaFloat("2º valor: ")
    return [n1, n2]

# Retorna a soma de dois números de ponto flutuante
def somar() -> None:
    valores =  leValores()
    result = valores[0] + valores[1]
    print(f"{valores[0]} + {valores[1]} = {result}")

# Retorna a subtração de dois número de ponto flutuante
def subtrair() -> None:
    valores = leValores()
    result = valores[0] - valores[1]
    print(f"{valores[0]} - {valores[1]} = {result}")

# Retorna a multiplicação de dois números ponto flutuante
def multiplicar() -> None:
    valores = leValores()
    result = valores[0] * valores[1]
    print(f"{valores[0]} x {valores[1]} = {result}")

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

# Imprime na tela a potência de um número de base "x" e expoente "y" (o usuário escolhe)
def potenciar():
    base = leiaFloat("Número: ")
    expoente = leiaInt("Índice: ")
    result = base ** expoente
    print(f"{base} ** {expoente} = {result}")

# Imprime na tela a raiz quadrada de um número "x"
def RaizQuadrada():
    from math import sqrt


    numero = float(input("Número: "))
    result = sqrt(numero)
    print(f"Raiz quadrada = {result:.1f}")

# Imprime na terla o fatorial de um número, juntamento com todo o cálculo por trás do resultado
def fatorial():
    f = 1
    n = leiaInt("Número a ser calculado: ")
    print(f"Fatorando número {n}!...")
    print(f"{n}! = ", end='')
    for vlr in range(n, 0, -1):
        f *= vlr
        print(f'{vlr} x ' if vlr != 1 else f'{vlr} = {f}', end='')

# Calcula o percentual de um número
def percentual():
    n1 = leiaFloat("Número: ")
    percentual = leiaFloat("Percentual: ")
    result = n1 * percentual / 100
    print(f'{n1} % {percentual} = {result}')

# Arredonda um número para cima
def ArredondarParaCima():
    from math import ceil


    n1 = leiaFloat('Informe o número que deseja arredondar para cima: ')
    result = ceil(n1)
    print(f'{n1} arredondado para cima = {result}')

# Arredonda um número para baixo
def ArredondarParaBaixo():
    from math import floor

    n1 = leiaFloat('Informe o número que deseja arredondar para baixo: ')
    result = floor(n1)
    print(f'{n1} arredondado para baixo = {result}')

# Calcula o seno
def seno():
    from math import sin, radians


    n = float(input("Valor do seno a ser calculado: "))
    result = sin(radians(n))
    print(f"Seno de {n}° = {result:.1f}")

# Calcula o cosseno
def cosseno():
    from math import cos, radians


    n = float(input("Valor do cosseno a ser calculado: "))
    result = cos(radians(n))
    print(f"Cosseno de {n}° = {result:.1f}")

# Calcula a tangente
def tangente():
    from math import tan, radians


    n = float(input("Valor da tangente a ser calculada: "))
    result = tan(radians(n))
    print(f"Tangente de {n}° = {result:.1f}")


# Calcula o logaritmo de uma dada base e logaritmando
def logaritmo():
    from math import log
    from time import sleep


    base = float(input("Base do logaritmo: "))
    logaritmando = float(input("Logaritmando do logaritmo: "))
    result = log(logaritmando, base)
    print(f"Calculando logaritmo de base {base:.1f} e de logaritmando {logaritmando:.1f}...")
    sleep(1)
    print(f"= {result:.1f}")


# Calcula a média entre n valores determinados pelo usuário
def media():
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
def valorMinimoMaximo():
    quantidade_valores = 0
    lista_valores = []
    while True:
        quantidade_valores = leiaInt("Quantos valores a lista terá? ")
        if (quantidade_valores < 1):
            print("\033[1;31mImpossível definir um mínimo e um máximo em uma lista vazia!")
            print("Por favor, tente novamente...\033[m")
        else:
            break
    for vlr in range(0, quantidade_valores):
        lista_valores.append(leiaFloat(f"{vlr + 1}º valor: "))
    vlr_min = min(lista_valores)
    vlr_max = max(lista_valores)
    print(f"Valor mínimo = {vlr_min} \nValor máximo = {vlr_max}")


# Converte um valor decimal em binário
def decimalParaBinario():
    valor = leiaInt("Valor decimal a ser convertido: ")
    decimalConvertidoParaBin = bin(valor)[2:]
    print(f'{"decimal":>10}{"binário":>20}')
    print(f"{valor:>10}  {decimalConvertidoParaBin:>20}")

# Converte um valor binário em decimal
def binarioParaDecimal():
    valorBinario = input("Valor binário: ")
    binarioConvertidoParaDecimal = int(valorBinario, 2)
    print(f"{'Valor binário':>10}{'Valor decimal':>20}")
    print(f"{valorBinario:>10}{binarioConvertidoParaDecimal:>20}")


def decimalParaOctal():
    valor = leiaInt("Valor decimal a ser convertido: ")
    decimalParaOctal = oct(valor)[2:]
    print(f"{'decimal':>10}{'octal':>20}")
    print(f'{valor:>10}{decimalParaOctal:>20}')

def octalParaDecimal():
    valorEmOctal = input("Valor em octal: ")
    octalConvertidoEmDecimal = int(valorEmOctal, 8)
    print(f"{'octal':>10}{'decimal':>20}")
    print(f"{valorEmOctal:>10}{octalConvertidoEmDecimal:>20}")


def decimalParaHexadecimal():
    valor = leiaInt("Valor decimal: ")
    decimalConvertidoEmHexadecimal = hex(valor)[2:]
    print(f"{'decimal':>10}{'hexadecimal':>20}")
    print(f"{valor:>10}{decimalConvertidoEmHexadecimal:>20}")


def hexadecimalParaDecimal():
    valor = input("Valor em hexadecimal: ")
    hexadecimalConvertidoEmDecimal = int(valor, 16)
    print(f"{'HEXADECIMAL':>10}{'DECIMAL':>20}")
    print(f"{valor:>10}{hexadecimalConvertidoEmDecimal:>20}")


def calculaMóduloDeUmNumero():
    num = leiaInt("Valor: ")
    modulo = num * -1 if num < 0 else num
    print(f"{'valor':>10}{'módulo':>20}")
    print(f"{num:>8}{modulo:>19}")

def calculaModaDeUmaListaDeNumeros():
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
            

    #define a moda
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


def calculaMedianaDeUmaListaDeNumeros():
    listaNumeros = []
    quantidadeValores = leiaInt("Quantidade de valores: ")
    cont = 0
    while cont < quantidadeValores:
        listaNumeros.append(leiaInt(f"{cont + 1}º valor: "))
        cont += 1
    listaNumeros.sort()
    tamanhoLista = len(listaNumeros)
    if tamanhoLista % 2 == 0:
        # [1, 2, 3, 4, 5, 6]
        mediana = ((listaNumeros[((tamanhoLista - 1) // 2)]) + (listaNumeros[((tamanhoLista - 1) // 2) + 1])) / 2
    else:
        mediana = (listaNumeros[tamanhoLista // 2])

    print(f"A mediana da lista de números {listaNumeros} vale {mediana} ")
    
    