# Faça um programa que leia um número inteiro
# qualquer e mostre na tela a sua tabuada de 1 até 10
import time


class Tabuada():
    def __init__(self, n_inteiro: int):
        self.n_inteiro = n_inteiro

    def tabuada(self):
        for i in range(1, 10):
            resultado = self.n_inteiro * i
            print(f"{i} * {self.n_inteiro} = {resultado}")
            time.sleep(0.2)


Tabuada_n = Tabuada(89)
Tabuada_n.tabuada()
