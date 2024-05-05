# Crie um programa que tenha a função
# leiaint() que vai funcionar
# de forma semelhante a função input()
# só que fazendo a validação feita
# para aceitar apenas int
# Ex: n = leia("Digite um n")

def leiaint():
    while True:
        num = input("Digite um numero: ")
        if num.isnumeric():
            numint = int(num)
            print(f'você digitou o número {numint}')
            break
        else:
            print("\033[0;31mErro digite um número!\033[m")
    return numint

leiaint()
