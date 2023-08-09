def verificaSistemaOperacionalDoUsuario() -> str:
    from os import name

    if name == "posix":
        return "clear"
    
    else:
        return "cls"