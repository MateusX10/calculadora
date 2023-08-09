menu = [["OPERAÇÕES BÁSICAS", "POTENCIAÇÃO/RAIZ", "ESTATÍSTICAS", "TRIGONOMETRIA","CONJUNTOS", "CONVERSÃO DE BASES", "ARREDONDAMENTO", "OUTROS", "SAIR"],

["ADIÇÃO", "SUBTRAÇÃO", "MULTIPLICAÇÃO", "DIVISÃO"],
        
["POTENCIAÇÃO", "RAIZ"],

["Média", "MEDIANA", "MODA", "Mínimo e Máximo"],

["HIPOTENUSA", "SENO", "COSSENO", "TANGENTE"],

["UNIÃO"],

["DECIMAL PARA BINÁRIO", "BINÁRIO PARA DECIMAL", "DECIMAL PARA OCTAL","OCTAL PARA DECIMAL", "DECIMAL PARA HEXADECIMAL","HEXADECIMAL PARA DECIMAL"],

["PARA CIMA", "PARA BAIXO"],

["PORCENTAGEM", "FATORIAL", "LOGARITMO", "MÓDULO"]
]


# Menu de opções
def exibeMenu(codigo):
    print("\nMENU:\n")
    for indice, valor in enumerate(menu[codigo]):
        print(f"[ {indice + 1} ] - {valor}\n")

        if (indice + 1) == len(menu[codigo]):
            print(f"[ 999 ] - Voltar\n")


    

'''# Menu de opções
menu_opcs = ["SOMAR", "SUBTRAIR", "MULTIPLICAR", "DIVIDIR","POTENCIAÇÃO","RADICIAÇÃO", "FATORIAL", "PORCENTAGEM", "ARREDONDAR PARA CIMA","ARREDONDAR PARA BAIXO", "SENO", "COSSENO", "TANGENTE","LOGARITMO", "MÉDIA", "MÍNIMO E MÁXIMO", "DECIMAL PARA BINÁRIO",
            "BINÁRIO PARA DECIMAL", "DECIMAL PARA OCTAL",
               "OCTAL PARA DECIMAL", "DECIMAL PARA HEXADECIMAL",
               "HEXADECIMAL PARA DECIMAL","MÓDULO", "MODA", "MEDIANA",
                "UNIÃO DE CONJUNTOS", "SAIR"]

menu_principal = ["OPERAÇÕES BÁSICAS", "POTENCIAÇÃO/RAIZ", "ESTATÍSTICAS", "TRIGONOMETRIA","CONJUNTOS", "CONVERSÃO DE BASES", "ARREDONDAMENTO", "OUTROS"]

menu_operacoes_basicas = ["SOMAR", "SUBTRAIR", "MULTIPLICAR", "DIVIDIR"]

menu_potencia_raiz = ["POTENCIAÇÃO", "RAIZ"]

menu_estatistica = ["Média", "Mínimo e Máximo", "Moda","Mediana"]

menu_trigonometria = ["HIPOTENUSA", "SENO", "COSSENO", "TANGENTE"]

menu_conjuntos = ["UNIÃO"]

menu_conversao_bases = ["DECIMAL PARA BINÁRIO",
            "BINÁRIO PARA DECIMAL", "DECIMAL PARA OCTAL","OCTAL PARA DECIMAL", "DECIMAL PARA HEXADECIMAL","HEXADECIMAL PARA DECIMAL"]

menu_arredondamento = ["PARA CIMA", "PARA BAIXO"]

menu_outros = ["FATORIAL", "PORCENTAGEM", "LOGARITMO", "MÓDULO"]'''
    
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