# Valida um valor inteiro lido pelo teclado
def leiaInt(msg):
    n1 = 0
    while True:
        try:
            n1 = int(input(msg))
        except (ValueError, NameError, TypeError):
            print("\033[1;31mOps, por favor, informe apenas números inteiros!\033[m")
        except (KeyboardInterrupt):
            print('\n\033[1;31mPara sair, digite "0"\033[m')
        else:
            return (n1)

# Valida um valor ponto flutuante pelo teclado
def leiaFloat(msg):
    n1 = 0.0
    while True:
        try:
            n1 = float(input(msg))
        except (NameError, ValueError, TypeError):
            print('\033[1;31mOps, por favor, digite apenas número de ponto flutuante!\033[m')

        except (KeyboardInterrupt):
            print('\033[1;31Para sair, digite "0"\033[m')
        else:
            return (n1)

# Retorna a soma de dois números de ponto flutuante
def somar(n1, n2) -> float:
    return (n1 + n2)

# Retorna a subtração de dois número de ponto flutuante
def subtrair(n1, n2) -> float:
    return (n1 - n2)

# Retorna a multiplicação de dois números ponto flutuante
def multiplicar(n1, n2) -> float:
    return (n1 * n2)

# Retorna a divisão de dois números ponto flutuante
def dividir(n1, n2) -> float:
    try:
        return (n1 / n2)
    except (ZeroDivisionError):
        print("\033[1;31mOps, não é possível dividir um número por 0!!!\033[m")

# Retorna dois novos valores a serem usados nas operações
def NovosValores() -> float:
    n1 = leiaInt("Primeiro valor: ")
    n2 = leiaInt("Segundo valor: ")
    return [n1, n2]

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