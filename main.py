from strings import *
from numeros import *
from sistema_operacional import *
from os import system
from time import sleep

# Chama a função "title" para que imprima o título "CALCULADORA"
title("CALCULADORA")
sleep(1)
escolha_user = result_soma = result_sub = result_mult = result_div = 0

# Retorna uma lista com 2 valores a serem usados nas operações matemáticas
while True:
    # Imprime o menu de opções na tela
    exibeMenu(0)
    # a operação matemática escolhida pelo usuário
    escolha_user = leiaInt("Faça a sua escolha: ")
    
    # Sair
    if escolha_user == 9:
        print("<<< VOLTE SEMPRE >>>")
        quit()


    if (escolha_user >= len(menu[0]) or escolha_user < 0):
        print("\033[1;31mPor favor, digite apenas os números especificados no menu...\033[m")
        continue
        

    #title(menu_opcs[escolha_user - 1])
    # <<< MENU >>>

    while True:
        exibeMenu(escolha_user)

        escolha_user2 = leiaInt("Faça a sua escolha: ")

        if verificaSeOpcaoEscolhidaExisteNaLista(escolha_user, escolha_user2):
            break
        print("\033[1;31mPor favor, escolha uma operação matemática existente!\033[m")

    if escolha_user2 == 999:
        continue

    title(menu[escolha_user][escolha_user2 - 1])

    # Operações básicas
    if (escolha_user == 1):
        
        # operação de adição
        if escolha_user2 == 1:
            somar()

        # Operação de subtração
        elif escolha_user2 == 2:
            subtrair()
        # Operação de multiplicação
        elif escolha_user2 == 3:
            multiplicar()
        # Operação de divisão
        elif escolha_user2 == 4:
            dividir()

    # Potencia e raiz
    elif (escolha_user == 2):

        # Operação de potenciação
        if escolha_user2 == 1:
            potenciar()

        # Operação de radiciação
        elif escolha_user2 == 2:
            RaizQuadrada()

    # Operações de estatística
    elif escolha_user == 3:

        # Operação de calcular a média
        if escolha_user2 == 1:
            media()

        # Operação de calcular a mediana
        elif escolha_user2 == 2:
            calculaMedianaDeUmaListaDeNumeros()

        # Operação de calcular a moda
        elif escolha_user2 == 3:
            calculaModaDeUmaListaDeNumeros()

        # Operação de valor mínimo e máximo
        elif escolha_user2 == 4:
            valorMinimoMaximo()

    # Operações de trigonometria
    elif escolha_user == 4:

        # operação de calcular a hipotenusa
        if escolha_user2 == 1:
            hipotenusa()

        # Operação de calcular o seno
        elif escolha_user2 == 2:
            seno()

        # Operação de calcular o cosseno
        elif escolha_user2 == 3:
            cosseno()

        # Operação de calcular a tangente
        elif escolha_user2 == 4:
            tangente()

    # Operações de conjuntos
    elif escolha_user == 5:

        # Operação de união entre conjuntos
        if escolha_user2 == 1:
            UnirDoisConjuntos()

    elif escolha_user == 6:

        # Operação de conversão decimal - binário
        if escolha_user2 == 1:
            decimalParaBinario()

        # Operação de conversão binário - decimal
        elif escolha_user2 == 2:
            binarioParaDecimal()
        
        # Operação de conversão decimal - octal
        elif escolha_user2 == 3:
            decimalParaOctal()

        # Operação de conversão octal - decimal
        elif escolha_user2 == 4:
            octalParaDecimal()

        # Operação de conversão decimal - hexadecimnal
        elif escolha_user2 == 5:
            decimalParaHexadecimal()

        # Operação de conversão hexadecimal - decimal
        elif escolha_user == 6:
            hexadecimalParaDecimal()

    # Operações de arredondamento
    elif escolha_user == 7:

        # Operação de arredondar um número para cima
        if escolha_user2 == 1:
            ArredondarParaCima()

        # Operação de arredondar um número para baixo
        elif escolha_user2 == 2:
            ArredondarParaBaixo()

    # Outras operações matemáticas
    elif escolha_user == 8:

        # Operação de porcentagem
        if escolha_user2 == 1:
            percentual()

        # Operação de calcular o fatorial
        elif escolha_user2 == 2:
            fatorial()

        # Operação de calcular o logaritmo
        elif escolha_user2 == 3:
            logaritmo()
        
        # Operação de calcular o módulo
        elif escolha_user2 == 4:
            calculaMóduloDeUmNumero()

    sleep(1.5)
    print("\n\nPressione qualquer tecla para continuar")
    input()
    sistemaOperacionalDoUsuario = verificaSistemaOperacionalDoUsuario()
    system(sistemaOperacionalDoUsuario)
    
    


