# crie um programa que leia duas notas de um aluno e calciule sua media:
# de caordo com e media, abaixo de 5 reprovado entre 5 e 6.9 reporvado
# 7 ou superior aprovado

class Escola:
    def __init__(self, nota: int):
        self.nota = nota

    def situacao(self):
        if self.nota > 7:
            print("Aluno aprovado")
        elif 5 < self.nota < 6.9:
            print("Aluno para recuperação")
        else:
            print("Aluno reporvado")


nota = int(input("Por favor digite a nota do aluno: "))
flavio = Escola(nota)
flavio.situacao()
