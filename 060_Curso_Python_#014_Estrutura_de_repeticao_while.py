# Faça um programa que leia um número e mostre o seu fatorial

class Factorial:

    def __init__(self):
        self.num = int(input("Digite o número para saber o fatorial: "))
        self.factorial = 1

    def cal_fatorial(self):
        if self.num in [0, 1]:
            self.factorial = 1
        else:
            while (self.num > 1):
                self.factorial = self.factorial * self.num
                self.num = self.num - 1
        print(self.factorial)
        return self.factorial


teste = Factorial()
teste.cal_fatorial()
