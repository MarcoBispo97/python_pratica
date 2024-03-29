# Refaça o desafio 51, usando while
# Desenvolva um programa que leia o primeiro termo
# e a razao de uma PA.
# No final, mostre os 10 primeiros termos dessa
# progressão

class Pa:
    def __init__(self):
        self.primeiro_termo = int(input("Digite o primeiro termo: "))
        self.n_termo = 0
        self.razao = int(input("Digite a razão: "))
        self.contador = 0
        self.lista_pa = []

    def termos(self):
        while (self.contador < 10):
            self.contador = self.contador + 1
            if self.contador == 1:
                print(
                    f"O termo numero {self.contador} é: {self.primeiro_termo}")
                self.n_termo = self.primeiro_termo
            else:
                self.n_termo = self.n_termo + self.razao
                print(
                    f"O termo numero {self.contador} é: {self.n_termo}")
            self.lista_pa.append(self.n_termo)
        print("A sequência ficou assim: \n", self.lista_pa)


if __name__ == "__main__":
    teste = Pa()
    teste.termos()
