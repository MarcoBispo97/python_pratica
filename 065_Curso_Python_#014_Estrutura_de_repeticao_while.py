# Crie um programa que leia vários números
# inteiros pelo teclado.
# no final da execução mostre a média entre todos
# os valores e qual foi o maior e menor valor lido.
# O programa deve perguntar ao usuários se ele quer ou não continuar a gigitar valores
class Program:
    def __init__(self):
        self.numeros = []

    def run_program(self):
        while True:
            try:
                entrada = input("Digite um número inteiro ou 's' para sair: ")
                if entrada.lower() == 's':
                    break
                numero = int(entrada)
                self.numeros.append(numero)
            except ValueError:
                print("Por favor, digite um número inteiro válido.")

    def calculate(self):
        media = sum(self.numeros)/len(self.numeros)
        print("A média é:", media)
        print("O maior valor é:", max(self.numeros))
        print("O menor valor é:", min(self.numeros))


if __name__ == "__main__":
    programa = Program()
    programa.run_program()
    programa.calculate()
