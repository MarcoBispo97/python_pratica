# Crie um programa que tenha
# uma função fatorial
# que receba dois parâmetros
# o primeiro indique o numero e calcula
# e o outro chamado show, que será um valor lógico
# opicional indica se será mostrado

def fatorial(n, show=False):
    '''
    -> Calcula o fatorial de um número
    param n: O n fatorial a ser escolhido
    param show: mostra a conta ou não, é opicional
    return: O valor do fatorial de um numero n
    '''
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


# programa principal
print(fatorial(5, True))
help(fatorial)
