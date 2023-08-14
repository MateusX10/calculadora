# lista do menu - 
menu = [["OPERAÇÕES BÁSICAS", "POTENCIAÇÃO/RAIZ", "ESTATÍSTICAS", "TRIGONOMETRIA","CONJUNTOS", "CONVERSÃO DE BASES", "ARREDONDAMENTO", "OUTROS", "SAIR"],

["ADIÇÃO", "SUBTRAÇÃO", "MULTIPLICAÇÃO", "DIVISÃO"],
        
["POTENCIAÇÃO", "RAIZ"],

["Média", "MEDIANA", "MODA", "Mínimo e Máximo"],

["HIPOTENUSA", "SENO", "COSSENO", "TANGENTE"],

["UNIÃO", "INTERSEÇÃO","DIFERENÇA", "SUBCONJUNTO"],

["DECIMAL PARA BINÁRIO", "BINÁRIO PARA DECIMAL", "DECIMAL PARA OCTAL","OCTAL PARA DECIMAL", "DECIMAL PARA HEXADECIMAL","HEXADECIMAL PARA DECIMAL"],

["PARA CIMA", "PARA BAIXO"],

["PORCENTAGEM", "FATORIAL", "LOGARITMO", "MÓDULO"]
]


# Menu de opções
def exibeMenu(codigo):
    print("\nMENU:\n")
    for indice, valor in enumerate(menu[codigo]):
        print(f"[ {indice + 1} ] - {valor}\n")

        if (indice + 1) == len(menu[codigo]) and codigo != 0:
            print(f"[ 999 ] - Voltar\n")



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