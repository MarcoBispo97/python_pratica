# Faça um programa que leia o peso
# de cinco pessoas
# no final mostre qual foi o
# maior e monor peso lido

class Balanca:
    def __init__(self, pesos):
        self.pesos = pesos

    def maior_menor(self):
        print("Peso minimo: ", min(self.pesos), "kg")
        print("Peso máximo: ", max(self.pesos), "kg")


pesagem = Balanca([88, 89, 56, 78, 49])
pesagem.maior_menor()
