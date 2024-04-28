# Faça um programa que tenha uma função
# chamada contador()
# que receba três parâmetros
# inicio, fim e passo
# e realize a contagem

# seu programa tem que realizar três
# contagens atrabés da função criada

# a- De 1 até 1, de 1 em 1
# b- De 10 até 0, de 2 em 2
# c- Uma contagem personalizada

# inicio, fim, passo

import time


def contador():
    print("Contagem de 1 até 10 de 1 em 1")
    for i in range(11):
        print(i, "", end="")
        time.sleep(0.1)
    print("FIM !")
    print("-="*20)

    print("Contagem de 10 até 0 de 2 em 2")
    j = 10
    for i in range(6):
        print(j, "", end="")
        time.sleep(0.1)
        j = j - 2

    print("FIM !")
    print("-="*20)

    print("Agora é sua vez de personalizar a contagem !")
    inicio = int(input("Digite o início: "))
    final = int(input("Digite o final: "))
    passo = int(input("Digite o passo: "))

    print(f"Contagem de {inicio} até {final} de {passo} em {passo}")
    j = inicio
    for i in range(final + 1):
        print(j, "", end="")
        if passo != 0:
            j = j + passo
        if i == final:
            break
    print("\nFIM!")
    print("-" * 20)


contador()
