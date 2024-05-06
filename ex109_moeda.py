def formatar(num):
    num = str("RS " + str(num))
    return num


def metade(moeda, format=True):
    resultado = moeda / 2
    if format == True:
        return formatar(resultado)
    else:
        return resultado


def dobro(moeda, format=True):
    resultado = moeda * 2
    if format == True:
        return formatar(resultado)
    else:
        return resultado


def aumentar(p, moeda, format=True):
    resultado = moeda + ((moeda * p) / 100)
    if format == True:
        return formatar(resultado)
    else:
        return resultado


def diminuir(p, moeda, format=True):
    resultado = moeda - ((moeda * p) / 100)
    if format == True:
        return formatar(resultado)
    else:
        return resultado
