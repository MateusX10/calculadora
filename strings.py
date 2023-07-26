# Menu de opções
def menu():
    print('''\nMenu:
[ 1 ] - Somar
[ 2 ] - Subtrair
[ 3 ] - Multiplicar
[ 4 ] - Dividir
[ 5 ] - Potenciar
[ 6 ] - Raiz quadrada
[ 7 ] - Fatorial
[ 8 ] - Porcentagem
[ 9 ] - Arredondar para cima
[ 10 ] - Arredondar para baixo
[ 11 ] - Seno
[ 12 ] - Cosseno
[ 13 ] - Tangente
[ 14 ] - Logaritmo
[ 15 ] - Média
[ 16 ] - mínimo e máximo
[ 17 ] - decimal para binário
[ 18 ] - binário para decimal
[ 19 ] - Decimal para octal
[ 20 ] - Octal para decimal
[ 21 ] - Decimal para hexadecimal
[ 22 ] - Hexadecimal para decimal
[ 23 ] - Módulo
[ 0 ] - Sair
''')
    
# Quebra linha
def QuebrarLinha(linhas=1):
    for linha in range(0, linhas):
        print("\n")

# Mostra uma sequência de traços a fim de deixar o programa mais bonito
def line():
    print('-=' * 30)

# Mostra um título na tela
def title(msg):
    QuebrarLinha()
    line()
    print(msg.center(30))
    line()