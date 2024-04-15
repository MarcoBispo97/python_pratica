# Crie um programa que leia nome e duas notas
# de vários alunos e guarde tudo em uma lista composta
# No final mostre um boletim contendo a média de cada um
# e permita que o usuário posssa mostrar as notas de cada aluno
# individualmente

class Escola:
    def __init__(self):
        self.nomes_notas = self.recebe_nomes_notas()
        self.lista_index = self.medias()
    def recebe_nomes_notas(self):
        lista_nomes_notas = []
        dados_aluno_n = []
        while True:
            nome = input("Nome: ")
            if nome.isdigit():
                print("Por favor digite um nome válido")
            else:
                dados_aluno_n.append(nome)
            nota_1 = input("Nota 1: ")
            if nota_1.isdigit():
                dados_aluno_n.append(int(nota_1))
            else:
                print("Por favor digite um número")
            nota_2 = input("Nota 2: ")
            if nota_2.isdigit():
                dados_aluno_n.append(int(nota_2))
            else:
                print("Por favor digite um número")

            lista_nomes_notas.append(dados_aluno_n)
            dados_aluno_n = []

            sair = input("Deseja sair [s] ? ")
            if sair == "s":
                break
        return lista_nomes_notas
    def medias(self):
        lista_index = []
        print("{:<5} {:<12} {:<4}".format("No.", "Aluno", "Média"))
        for index, dados_aluno in enumerate(self.nomes_notas):
            media = round((dados_aluno[1] + dados_aluno[2]) / 2, 3)
            print("{:<5} {:<12} {:<4f}".format(index, dados_aluno[0], media))
            lista_index.append(index)
        return lista_index

    def notas(self):
        while True:
            entrada = input(
                "Deseja mostrar a nota de algum aluno ?\ndigite o index da tabela aicma para saber qual aluno deseja\n(999 interrompe) :")
            if entrada == "999":
                break
            elif entrada.isdigit() and int(entrada) in self.lista_index:
                nome_aluno = self.nomes_notas[int(entrada)][0]
                nota_1 = self.nomes_notas[int(entrada)][1]
                nota_2 = self.nomes_notas[int(entrada)][2]
                print(
                    f"O aluno {nome_aluno}, teve nota1={nota_1} e nota2={nota_2}")
            elif entrada.isdigit() and int(entrada) not in self.lista_index:
                print("Não existe aluno com esse número, olhe a tabela acima")
            else:
                print("Digite um número válido")
teste1 = Escola()
teste1.notas()
