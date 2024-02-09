# A confederação Nacional de Natação precisa de um
# programa que leia o ano de nascimento de um atleta
# e mostre sua categoria, de acordo com a idade:

class Cat_esportista:
    def __init__(self, idade: int):
        self.idade = idade

    def categoria(self):
        if self.idade > 20:
            print("sênior")
        elif 14 < self.idade < 19:
            print("junior")
        elif 9 < self.idade <= 14:
            print("infantil")
        elif self.idade < 9:
            print("Mirim")


idade = int(input("Digite a idade do jogador: "))

jogador_1 = Cat_esportista(idade)
jogador_1.categoria()
