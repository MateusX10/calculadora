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
[ 14 ] - Novos valores
[ 0 ] - Sair
''')

def line():
    print('-=' * 30)

def title(msg):
    line()
    print(msg.center(30))
    line()