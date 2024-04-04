# Crie um programa que simule o funcionamento
# de uma caixa eletrônica
# No início pergunte ao usuário qual será o valor a ser sacado
# (númereo inteiro)
# e o programa vai informar quantas células de cada valor
# serão entregues

# Obs.: Considere que o caixa possui cédulas de R$50, R$20, R$10 E R$1

class Caixa_eletronica:
    def __init__(self):
        self.saque = self.entrada_inteiro()
        self.nota50 = 0
        self.nota20 = 0
        self.nota10 = 0
        self.nota1 = 0

        print("Entrada", self.saque)

    def entrada_inteiro(self):
        while True:
            entrada = input("Digite um número inteiro para saque em R$: ")
            if entrada.isdigit():
                entrada = int(entrada)
                return entrada

    def cedula(self):

        while True:
            if (self.saque / 50) > 1:
                self.saque = self.saque - 50
                self.nota50 += 1
            else:
                print("Notas de 50:", self.nota50)
                break
        while True:
            if (self.saque / 20) > 1:
                self.saque = self.saque - 20
                self.nota20 += 1
            else:
                print("Notas de 20:", self.nota20)
                break
        while True:
            if (self.saque / 10) > 1:
                self.saque = self.saque - 10
                self.nota10 += 1
            else:
                print("Notas de 10:", self.nota10)
                break
        while True:
            if self.saque >= 1:
                self.saque = self.saque - 1
                self.nota1 += 1
            else:
                print("Notas de 1:", self.nota1)
                break


if __name__ == "__main__":
    caixa1 = Caixa_eletronica()
    caixa1.cedula()
