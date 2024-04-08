# Desenvolva um programa que leia quatro valores
# pelo teclado e guarde em um tupla
# No final mostre:

# A quantas vezes apareceu o valor 9
# B Em que posição foi digitado o primeiro valor 3
# C Quais foram os números pares

entradas = []

for i in range(4):
    while True:
        entrada = input("Insira valores numéricos: ")
        if entrada.isdigit():
            entradas.append(int(entrada))
            break
print(entradas)

tuple_entrada = tuple(entradas)

print(f"O numero 9 apareceu: {tuple_entrada.count(9)} vezes")

for indice, valor in enumerate(tuple_entrada):
    if valor == 3:
        local_3 = indice + 1
        break

if local_3 is not None:
    print(f"O número 3 está na posição {local_3}.")
else:
    print("O número 3 não foi digitado.")


pares = []

for n in tuple_entrada:
    if n % 2 == 0:
        pares.append(n)

print("Esse são os números pares: ", pares)
