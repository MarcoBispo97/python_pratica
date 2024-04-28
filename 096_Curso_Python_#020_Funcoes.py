# Faça um programa que tenha uma função
# chamada área(), que receba as dimensões
# de um terreno retangular
# largura e comprimento e mostre a
# área do terreno

class Square:
    def __init__(self):
        self.l1 = int(input("Digite o valor do primeiro lado (m): "))
        self.l2 = int(input("Digite o valor do segundo lado (m): "))

    def area(self):
        self.area = self.l1 * self.l2
        print(
            f"O lado {self.l1}m x {self.l2}m resulta na área de {self.area}m2")


terreno1 = Square()
terreno1.area()
