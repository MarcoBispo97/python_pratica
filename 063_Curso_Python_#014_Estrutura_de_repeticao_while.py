class Fibonacci:

    def __init__(self):
        self.numero = int(
            input("Digite o número de elementos da sequência de Fibonacci: "))
        self.lista_fibonacci = [1, 1]

    def calcular_fibonacci(self):
        if self.numero <= 0:
            print("Por favor, insira um número inteiro positivo maior que zero.")
            return
        elif self.numero == 1:
            print([1])
            return
        elif self.numero == 2:
            print(self.lista_fibonacci)
            return

        i = 2
        while i < self.numero:
            self.lista_fibonacci.append(
                self.lista_fibonacci[i-1] + self.lista_fibonacci[i-2])
            i += 1

        print(self.lista_fibonacci)


if __name__ == "__main__":
    teste = Fibonacci()
    teste.calcular_fibonacci()
