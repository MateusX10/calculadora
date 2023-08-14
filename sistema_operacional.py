# Verifica a família do S.O do user e retorna o comando que limpa a tela do terminal
def verificaSistemaOperacionalDoUsuario() -> str:
    from os import name

    # Família unix (linux, mac os)
    if name == "posix":
        return "clear"
    
    # Família DOS (windows)
    else:
        return "cls"