def metade(moeda):
    resultado = moeda / 2
    return resultado


def dobro(moeda):
    resultado = moeda * 2
    return resultado


def aumentar(p, moeda):
    resultado = moeda + ((moeda * p) / 100)
    return resultado


def diminuir(p, moeda):
    resultado = moeda - ((moeda * p) / 100)
    return resultado


def formatar(num):
    num = str("RS " + str(num))
    return num
