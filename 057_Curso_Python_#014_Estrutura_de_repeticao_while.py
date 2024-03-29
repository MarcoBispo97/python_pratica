# Faça um programa que leia o sexo de uma pessoa
# mas só aceite os valores 'M' ou 'F'.
# Caso esteja errado, peça a digitação
# novamente até ter um valor correto

class Masc_Fem:
    def __init__(self):
        self.sexo = None

    def check_sex(self):
        self.sexo = input("Digite o sexo (M_F): ")
        while self.sexo not in ["M", "F"]:
            self.sexo = input("Digite o sexo (M_F): ")
        print("Sexo válido:", self.sexo)


teste = Masc_Fem()
teste.check_sex()
