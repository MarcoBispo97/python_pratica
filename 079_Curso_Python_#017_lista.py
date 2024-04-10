# Crie um programa onde o usuário possa digitar vários valores numéricos
# e cadastreos em uma lista.  Caso o número já exista lá dentro ele não será adicionado
# No final serão exibidos todos os valores únicos digitados em ordem crescente

class Valor_num:
    def __init__(self):
        self.lista = self.recebe_num()

    def recebe_num(self):
        lista = []
        while True:
            entrada = input("Digite um valor numérico: ")
            if entrada.isdigit():
                entrada = int(entrada)
                if not (entrada in lista):
                    lista.append(int(entrada))
            else:
                print("Esse valor não é numérico !")
            if input("Deseja parar [s]: ") == "s":
                break
        lista.sort()
        return lista

    def show_valor(self):
        print(self.lista)


teste = Valor_num()
teste.show_valor()
