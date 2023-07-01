from strings import *
from numeros import *
from time import sleep

# Chama a função "title" para que imprima o título "CALCULADORA"
title("CALCULADORA")
sleep(1)
escolha_user = result_soma = result_sub = result_mult = result_div = 0
# Menu de opções
menu_opcs = ["SOMAR", "SUBTRAIR", "MULTIPLICAR", "DIVIDIR", "POTENCIAÇÃO",
             "RADICIAÇÃO", "FATORIAL", "PORCENTAGEM", "ARREDONDAR PARA CIMA",
             "ARREDONDAR PARA BAIXO", "SENO", "COSSENO", "TANGENTE",
             "LOGARITMO", "MÉDIA", "SAIR"]
# Retorna uma lista com 2 valores a serem usados nas operações matemáticas
while True:
    # Imprime o menu de opções na tela
    menu()
    # a operação matemática escolhida pelo usuário
    escolha_user = leiaInt("Faça a sua escolha: ")
    title(menu_opcs[escolha_user - 1])

    # <<< MENU >>>
    # Operação de adição
    if (escolha_user == 1):
        somar()
    # Operação de subtração
    elif (escolha_user == 2):
        subtrair()
    # Operação de multiplicação
    elif (escolha_user == 3):
       multiplicar()
    # Operação de divisão
    elif (escolha_user == 4):
        dividir()
    # Operação de potenciação
    elif (escolha_user == 5):
        potenciar()
    # Operação de raiz quadrada
    elif (escolha_user == 6):
        RaizQuadrada()
    # Operação de fatorial
    elif (escolha_user == 7):
        fatorial()
    # Operação de percentual
    elif (escolha_user == 8):
        percentual()
    # operação de arredondar um número para cima
    elif (escolha_user == 9):
        ArredondarParaCima()

    # Operação de arredondar um número para abaixo
    elif (escolha_user == 10):
        ArredondarParaBaixo()

    # Operação de calcular o seno
    elif (escolha_user == 11):
        seno()

    # Operação de calcular o cosseno
    elif (escolha_user == 12):
        cosseno()
    
    # Operação de calcular a tangente
    elif (escolha_user == 13):
        tangente()

    elif (escolha_user == 14):
        logaritmo()

    elif (escolha_user == 15):
        media()
    # Sair do programa
    elif (escolha_user == 0):
        print("<<< VOLTE SEMPRE >>>")
        quit()

    # Opção inválida
    else:
        print("\033[1;31mPor favor, digite apenas os números especificados no menu...\033[m")
    
    sleep(1.5)
    


