# Faça um mini sistema
# que utilize o interactive Help
# do Python
# O usuário vai digitar o comando e o manual
# vai aparecer
# quandoo o ususário digitar "FIM"
# o programa se encerra

# OBS.: Use cores.

from time import sleep

c = (
    '\33[m',         # 0 sem cores
    '\33[0;30;41m',  # 1 vermelho
    '\33[0;30;42m',  # 2 verde
    '\33[0;30;43m',  # 3 amarelo
    '\33[0;30;44m',  # 4 azul
    '\33[0;30;45m',  # 5 roxo
    '\33[0;30;47m',  # 6 branco
)


def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(2)


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end="")
    print("~" * tam)
    print(f' {msg}')
    print("~" * tam)
    print(c[0], end="")
    sleep(1)


comando = ''
while True:
    titulo("SISTEMA DE AJUDA PyHelp", 2)
    comando = str(input("Função ou Biblioteca >"))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)

titulo('ATÉ LOGO', 1)
