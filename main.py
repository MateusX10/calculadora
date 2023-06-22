from strings import *
from numeros import *
from time import sleep

title("CALCULADORA")
sleep(1)
escolha_user = result_soma = result_sub = result_mult = result_div = 0
valores = NovosValores()
while True:
    menu()
    escolha_user = leiaInt("Faça a sua escolha: ")
    if (escolha_user == 1):
        result_soma = somar(valores[0], valores[1])
        print(f"{valores[0]} + {valores[1]} = {result_soma}")

    elif (escolha_user == 2):
        result_sub = subtrair(valores[0], valores[1])
        print(f"{valores[0]} - {valores[1]} =  {result_sub}")

    elif (escolha_user == 3):
        result_mult = multiplicar(valores[0], valores[1])
        print(f"{valores[0]} x {valores[1]} =  {result_mult}")

    elif (escolha_user == 4):
        result_div = dividir(valores[0], valores[1])
        print(f'{valores[0]} / {valores[1]} = {result_div}')

    elif (escolha_user == 5):
        potenciar()
    
    elif (escolha_user == 6):
        RaizQuadrada()
    
    elif (escolha_user == 7):
        fatorial()

    elif (escolha_user == 8):
        percentual()

    elif (escolha_user == 9):
        ArredondarParaCima()

    elif (escolha_user == 10):
        ArredondarParaBaixo()

    elif (escolha_user == 11):
        seno()

    elif (escolha_user == 12):
        cosseno()

    elif (escolha_user == 13):
        tangente()

    elif (escolha_user == 14):
        valores = NovosValores()


    elif (escolha_user == 0):
        print("<<< VOLTE SEMPRE >>>")
        quit()

    else:
        print("\033[1;31mPor favor, digite apenas os números especificados no menu...\033[m")
    
    sleep(1.5)
    


