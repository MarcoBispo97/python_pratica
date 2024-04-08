# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla
# Depois disso mostre a listagem de números gerados e também indique a menor e maior valor
# Que estão na tupla
import random

list_numeros = []

for _ in range(5):
    list_numeros.append(random.randint(1, 100))

print("Tupla: ", tuple(list_numeros))
print("Menor valor da tupla: ", min(tuple(list_numeros)))
print("Maior valor da tupla: ", max(tuple(list_numeros)))
