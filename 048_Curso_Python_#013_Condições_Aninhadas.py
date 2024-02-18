# Faça um programa que leia um número inteiro
# qualquer e mostre na tela a sua tabuada de 1 até 10

class Tabuada():
    def __init__(self, n_inteiro: int):
        self.n_inteiro = n_inteiro

    def tabuada(self):
        for i in range(1, 10):
            resultado = self.n_inteiro * i
            print(resultado)


Tabuada_n = Tabuada(5)
Tabuada_n.tabuada()
