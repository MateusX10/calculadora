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


'''def valorMinimoMaximo():
    lista_temporaria = []
    lista_valores = []
    quantidade_valores = int(input("Quantid"))
    while True:
        lista_temporaria.append(leiaFloat())'''