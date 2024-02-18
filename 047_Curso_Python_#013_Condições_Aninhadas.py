# Crie um programa que mostre todos os números pares
# defina o intervalo
import time


class N_pares():
    def __init__(self, inicio: int, fim: int):
        self.inicio = inicio
        self.fim = fim

    def qnt_n_pares(self):
        for i in range(self.inicio, self.fim):
            if i % 2 == 0:
                time.sleep(0.10)
                print(i)


N_pares_1 = N_pares(5, 22)
N_pares_1.qnt_n_pares()
