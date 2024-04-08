# Crie um programa que tenha uma tupla
# totalmente preenchida com uma contagem por extensão
# de zero até vinte

# Seu programa deverá ler um número pelo teclado (entre 0 e 20)
# e mostra-lá por extenso

lista = [i for i in range(0, 21)]
tuple_20 = tuple(lista)
print(tuple_20)

while True:
    entrada_numerica = input("Digite um número entre 0 e 20: ")
    if entrada_numerica.isdigit and (int(entrada_numerica) < 21 and int(entrada_numerica) > 0):
        entrada = int(entrada_numerica)
        break

numeros = ["zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez",
           "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete",
           "dezoito", "dezenove", "vinte"]

for num, dig in zip(numeros, tuple_20):
    if entrada == dig:
        print(f"Você digitou o numero {num}")
