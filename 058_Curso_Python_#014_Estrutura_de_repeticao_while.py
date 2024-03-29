# Melhore o desafio 28
# onde o computador vai pensar em um número de 0 até 10
# só que agora o jogador vai tentar adivinhar até acertar
# mostrando no final quantos palpites foram necessários
# para vencer

import random


class Try_to_guess:

    def __init__(self):
        self.num_aleatorio = random.choice([i for i in range(1, 11)])
        self.tentativa = None
        self.chances = []
        self.n_chances = None

    def adivinhar(self):
        self.tentativa = int(input("Tente adivinhar o número, tentativa 1: "))
        self.chances.append(self.tentativa)
        i = 1
        while (self.tentativa != self.num_aleatorio):
            i = i + 1
            self.tentativa = int(input(
                f"Tente adivinhar o número, tentativa {i}, {self.num_aleatorio}: "))
            self.chances.append(self.tentativa)

        print(
            f"Parabéns, vc acertou na tentativa {i}, vc digitou esses números, nessa ordem: {self.chances}")


teste = Try_to_guess()
teste.adivinhar()
