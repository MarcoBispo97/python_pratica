# Crei um programa que leia dois valores e mostre
# um menu na tela:
# [1] - somar
# [2] - multiplicar
# [3] - maior
# [4] - novos números
# [5] - sair do programa

# seu programa deverá realizar a operação solicitada em cada caso

class Simple_calculator:
    def __init__(self):
        self.first_n = int(input("Digite o primeiro número: "))
        self.second_n = int(input("Digite o segundo número: "))
        self.options = int(input(
            "Digite: \n [1] - somar \n [2] - multiplicar \n [3] - maior número \n [4] - novos números \n [5] - sair do programa \n"))

    def reset(self):
        self.options = int(input(
            "Digite: \n [1] - somar \n [2] - multiplicar \n [3] - maior número \n [4] - novos números \n [5] - sair do programa \n"))

    def menu(self):
        while (self.options != 5):
            if self.options == 1:
                print("A soma é: ", self.first_n + self.second_n)
                self.reset()
            elif self.options == 2:
                print("A multiplicação é: ", self.first_n * self.second_n)
                self.reset()
            elif self.options == 3:
                if self.first_n > self.second_n:
                    print(
                        f"O primeiro número {self.first_n} é maior que o segundo número {self.second_n}")
                elif self.second_n > self.first_n:
                    print(
                        f"O segundo número {self.second_n} é maior que o segundo número {self.first_n}")
                else:
                    print(
                        f"O primeiro número {self.first_n} é igual ao segundo número {self.second_n}")
                self.reset()
            elif self.options == 4:
                self.first_n = int(input("Digite o primeiro número: "))
                self.second_n = int(input("Digite o segundo número: "))
                self.reset()
        print("Contas feitas, você saiu da calculadora !")


teste = Simple_calculator()
teste.menu()
