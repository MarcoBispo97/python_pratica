# Melhore o desafio 061
# perguntando para o usuário se ele quer mostrar mais alguns termos
# o programa encerra quando ele disser que quer mostrar 0 termos
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
        self.num_termo = None

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

    def mostrar_termos(self):
        self.num_termo = int(
            input("Digite o termo que queria mostrar \n Caso queira sair digite zero "))
        while (self.num_termo != 0):
            print(
                f"O termo {self.num_termo} é {self.lista_pa[self.num_termo - 1]}")
            self.num_termo = int(
                input("Digite o termo que queria mostrar \n Caso queira sair digite zero "))


if __name__ == "__main__":
    teste = Pa()
    teste.termos().mostrar_termos()
