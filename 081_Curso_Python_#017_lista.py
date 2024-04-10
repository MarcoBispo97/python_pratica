# Crie um programa que vai ler vários números
# e colocar em uma lista
# Depois disso, mostre:

# A - Quantos números foram digitados
# B - A lista de valores ordenada de forma decrescente
# C - Se o valor 5 foi digitado e está ou não na lista

class Listas_leitura:

    def __init__(self):
        self.numeros = self.receber_lista()

    def receber_lista(self):
        numeros = []
        while True:
            entrada = input("Digite um número para alimenta a lista: ")
            if entrada.isdigit():
                numeros.append(int(entrada))
            else:
                print("Você não digitou um número !")

            sair = input("Deseja sair ? [s] ")
            if sair == "s":
                break
        numeros = sorted(numeros, reverse=True)
        return numeros

    def resultado(self):
        tamanho = len(self.numeros)
        print(f"Você digitou {tamanho} números")
        print(self.numeros)
        print(
            f"A lista decrescente é: \n {self.numeros}")
        print(f"O valor 5 foi digitado {self.numeros.count(5)} vezes")


teste1 = Listas_leitura()
teste1.resultado()
