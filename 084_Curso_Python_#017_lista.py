# CRIE UM PROGRAMA QUE LEIA NOME E PESO
# De várias pessoas guardando tudo em uma lista
# No final mostre:
# A- Quantas pessoas foram cadastradas
# B- Um listagem com as pessoas mais pesadas
# C- Um listagem com as pessoas mais leves

class Nome_peso:
    def __init__(self):
        self.lista_nome_peso = self.atribuir_nome_peso()

    def atribuir_nome_peso(self):
        nome_peso = []
        nomes_pesos = []

        while True:
            while True:
                nome = input("Digite o nome da pessoa: ")
                if nome.isdigit():
                    print("Preciso de um nome, não um dígito !")
                else:
                    nome_peso.append(nome)
                    break
            while True:
                peso = input(f"Digite o peso de/da {nome}: ")
                if peso.isdigit():
                    nome_peso.append(int(peso))
                    break
                else:
                    print("Preciso de um dígito, não uma string !")

            nomes_pesos.append(nome_peso)
            nome_peso = []
            sair = input("Deseja sair ? [s] ")
            if sair == "s":
                break

        return nomes_pesos

    def respostas(self):

        pesos = []
        for nome_peso in self.lista_nome_peso:
            pesos.append(nome_peso[1])
        pesos = sorted(pesos)

        nomes = []
        for peso in pesos:
            for nome_peso in self.lista_nome_peso:
                if peso == nome_peso[1]:
                    nomes.append(nome_peso[0])

        print("A- Total de pessoas cadastradas: ", len(self.lista_nome_peso))
        nomes.reverse()
        print("B- Um listagem com as pessoas mais pesadas (maior para menor): ", nomes)
        nomes.reverse()
        print("C- Um listagem com as pessoas mais leves (menor para maior): ", nomes)


if __name__ == "__main__":
    teste_1 = Nome_peso()
    teste_1.respostas()
