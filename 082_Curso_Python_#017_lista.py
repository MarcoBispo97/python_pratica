# Crie um programa que leia vários números
# e coloque em uma lista
# Depois disso cria duas listas
# listas pares e impares
# digitadas respectitivamente
# Ao final mostre o conteúdo das três listas geradas

class Par_impar:
    def __init__(self):
        self.entradas = self.recebe_entradas()
        self.entradas_pares, self.entradas_impares = self.entradas_pares_impares()
    def recebe_entradas(self):
        entradas = []
        while True:
            entrada = input("Digite um número para alimentar a lista: ")
            if entrada.isdigit():
                entradas.append(int(entrada))
            else:
                ("Você não digitou um número !")
            sair = input("Deseja sair ? [s] ")
            if sair == "s":
                break
        return entradas
    def entradas_pares_impares(self):
        n_pares = []
        n_impares = []
        for n in self.entradas:
            if n % 2 == 0:
                n_pares.append(n)
            else:
                n_impares.append(n)
        return n_pares, n_impares
    def show(self):
        print("Lista digitada: ", self.entradas)
        print("Números pares: ", self.entradas_pares)
        print("Números ímpares: ", self.entradas_impares)

if __name__ == "__main__":
    teste1 = Par_impar()
    teste1.entradas_pares_impares()
    teste1.show()
