# Faça um programa que tenha
# uma lista chamada números e
# duas funções chamadas
# sorteiro() e somaPar()
# A primeira função vai sortear 5
# números aleatórios e vai colocalos
# dentro da lista e a segunda função
# vai mostrar a soma entre todos os
# valores PARES sorteados
# pela função anterior
import random


def sorteio(tam_lista):
    lista = random.sample(range(1, 101), tam_lista)
    print("Lista normal: ", lista)
    return lista


def somaPAR():
    lista_par = []
    for num in sorteio(5):
        if num % 2 == 0:
            lista_par.append(num)
    return sum(lista_par)


resultado = somaPAR()
print("A soma dos números pares sorteados é:", resultado)
