# Crie um porgrama que faça jokepo por você
import random


class jokenpo:
    def __init__(self, escolha_player):
        self.escolha_player = escolha_player.lower()
        self.escolha_cpu = random.choice(["tesoura", "papel", "pedra"])

    def resultado(self):
        if self.escolha_player == self.escolha_cpu:
            print("empate")
        elif self.escolha_player != self.escolha_cpu:
            if self.escolha_player == 'tesoura' and self.escolha_cpu == 'papel':
                print("player venceu !")
            elif (self.escolha_player == 'pedra' and self.escolha_cpu == 'tesoura') or \
                (self.escolha_player == 'papel' and self.escolha_cpu == 'pedra') or \
                    (self.escolha_player == 'tesoura' and self.escolha_cpu == 'papel'):
                print("player venceu")
            elif (self.escolha_cpu == 'pedra' and self.escolha_player == 'tesoura') or \
                (self.escolha_cpu == 'papel' and self.escolha_player == 'pedra') or \
                    (self.escolha_cpu == 'tesoura' and self.escolha_player == 'papel'):
                print("cpu venceu")


jogo1 = jokenpo("pedra")
jogo1.resultado()
