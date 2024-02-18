# Faça um programa que leia um número inteiro
# e diga se ele é ou não um número primo

class CheckPrimo:
    def __init__(self, n_primo: int):
        self.n_primo = n_primo

    def verifica(self):
        if self.n_primo > 1:
            for i in range(2, self.n_primo):
                if self.n_primo % i == 0:
                    print("Não é primo!")
                    break
            else:
                print("É primo!")
        else:
            print("Não é primo!")


n_89 = CheckPrimo(89)
n_89.verifica()
