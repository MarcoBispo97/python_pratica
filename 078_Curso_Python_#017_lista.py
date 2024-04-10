# Faça um programa que leia 5 valores numéricos e guarde em uma lista
# No final mostre qual foi o maior e menor valor digitado e as respectivas posições na lista

lista_de_5 = []

for i in range(5):
    while True:
        valor = input("Digite um valor numérico para alimentar a lista: ")
        if valor.isdigit():
            lista_de_5.append(int(valor))
            break
print("A lista de 5 valores é : ", lista_de_5)
