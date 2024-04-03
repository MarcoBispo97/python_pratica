# Crie um programa que leia vários npumeros inteiros no teclado
# O programa só vai parar quando o usuário digitar o valor 999
# que é a condição de parada
# No final mostre quantos números foram digitados foram digitados e qual a soma entre eles

class Total_contagem:

    def __init__(self):
        self.numeros = []
        self.entrada = int(input("Digite um número: "))

    def function(self):
        self.numeros.append(self.entrada)
        while (self.entrada != 999):
            self.entrada = int(input("Digite um número: "))
            if self.entrada != 999:
                self.numeros.append(self.entrada)
        print("Total de números:", len(self.numeros))
        print("Soma dos números:", sum(self.numeros))


if __name__ == "__main__":
    teste1 = Total_contagem()
    teste1.function()
