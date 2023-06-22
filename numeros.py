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


def somar(n1, n2) -> float:
    return (n1 + n2)

def subtrair(n1, n2) -> float:
    return (n1 - n2)

def multiplicar(n1, n2) -> float:
    return (n1 * n2)

def dividir(n1, n2) -> float:
    try:
        return (n1 / n2)
    except (ZeroDivisionError):
        print("\033[1;31mOps, não é possível dividir um número por 0!!!\033[m")

def NovosValores() -> float:
    n1 = leiaInt("Primeiro valor: ")
    n2 = leiaInt("Segundo valor: ")
    return [n1, n2]

def potenciar():
    base = leiaFloat("Número: ")
    expoente = leiaInt("Índice: ")
    result = base ** expoente
    print(f"{base} ** {expoente} = {result}")

def RaizQuadrada():
    from math import sqrt


    numero = float(input("Número: "))
    result = sqrt(numero)
    print(f"Raiz quadrada = {result}")


def fatorial():
    f = 1
    n = leiaInt("Número a ser calculado: ")
    print(f"Fatorando número {n}!...")
    print(f"{n}! = ", end='')
    for vlr in range(n, 0, -1):
        f *= vlr
        print(f'{vlr} x ' if vlr != 1 else f'{vlr} = {f}', end='')
    
def percentual():
    n1 = leiaFloat("Número: ")
    percentual = leiaFloat("Percentual: ")
    result = n1 * percentual / 100
    print(f'{n1} % {percentual} = {result}')

def ArredondarParaCima():
    from math import ceil


    n1 = leiaFloat('Informe o número que deseja arredondar para cima: ')
    result = ceil(n1)
    print(f'{n1} arredondado para cima = {result}')


def ArredondarParaBaixo():
    from math import floor

    n1 = leiaFloat('Informe o número que deseja arredondar para baixo: ')
    result = floor(n1)
    print(f'{n1} arredondado para baixo = {result}')


def seno():
    from math import sin, radians


    n = radians(float(input("Valor do seno a ser calculado: ")))
    result = sin(n)
    print(f"Seno de {n}° = {result:.1f}")


def cosseno():
    from math import cos, radians


    n = radians(float(input("Valor do cosseno a ser calculado: ")))
    result = cos(n)
    print(f"Cosseno de {n}° = {result:.1f}")


def tangente():
    from math import tan, radians


    n = radians(float(input("Valor da tangente a ser calculada: ")))
    result = tan(n)
    print(f"Tangente de {n}° = {result:.1f}")