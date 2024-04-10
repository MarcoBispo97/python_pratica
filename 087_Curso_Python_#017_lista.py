# Crie uma matriz 3x3
# preencha pelos valores do treclado
# No final mostre a matriz na tela
# com formatação correta
# mostre:
# A- A soma de todos os valores pares digitados
# B- A soma dos valores da terceira coluna
# c- O maior valor da segunda linha

class Matriz:
    def __init__(self):
        self.matriz = self.recebe_matriz()

    def recebe_matriz(self):
        linha = []
        matriz = []
        for _ in range(3):
            for i in range(3):
                while True:
                    entrada = input(
                        f"Digite o valor da linha {_+1} e coluna {i+1} : ")
                    if entrada.isdigit():
                        linha.append(int(entrada))
                        break
                    else:
                        print("Por favor digite um valor numérico !")
            matriz.append(linha)
            linha = []
        return matriz

    def motrar_matriz(self):
        for line in self.matriz:
            for element in line:
                print(f"[ {element} ]", end=' ')
            print("")

    def aprimorar(self):
        segunda_linha = []
        soma_pares = 0
        soma_terceira_coluna = 0
        for index_linha, line in enumerate(self.matriz, start=1):
            for index_coluna, element in enumerate(line, start=1):
                if element % 2 == 0:
                    soma_pares = soma_pares + element
                if index_coluna == 3:
                    soma_terceira_coluna = soma_terceira_coluna + element
                if index_linha == 2:
                    segunda_linha.append(element)

        print("A- A soma de todos os valores pares digitados: ", soma_pares)
        print("B- A soma dos valores da terceira coluna: ", soma_terceira_coluna)
        print("C- O maior valor da segunda linha: ", max(segunda_linha))


test_1 = Matriz()
test_1.motrar_matriz()
test_1.aprimorar()
