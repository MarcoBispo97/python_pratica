# Faça um progama que mostra na tela regressiva
# para o estouro de fogos de artificio indo de
# 10 até 0 com uma paousa de 1 segundo entre eles
import time


class Contagem_fogos:
    def __init__(self, contagem):
        self.contagem = contagem

    def contar(self):
        for i in range(self.contagem, 0, -1):
            print(i)
            time.sleep(1)
        print("Bom, estourou !")


Contagem_fogos_1 = Contagem_fogos(10)
Contagem_fogos_1.contar()
