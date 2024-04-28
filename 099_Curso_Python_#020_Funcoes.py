# Faça um programa que tenha
# uma função chamada maior(),
# que receba vários parâmetros inteiros

import random


# Gerar um tamanho aleatório entre 2 e 10
tamanho = random.randint(2, 10)

# Gerar uma lista com números únicos
lista = random.sample(range(1, 101), tamanho)


def maior(lista_aleatoria):
    if len(lista_aleatoria) == 0:
        return None
    else:
        return max(lista_aleatoria)


print("Lista aleatória sem elementos repetidos:", lista)
print("Maior elemento: ", maior(lista))
