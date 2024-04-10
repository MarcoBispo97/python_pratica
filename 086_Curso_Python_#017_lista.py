# Crie uma matriz 3x3
# preencha pelos valores do treclado
# No final mostre a matriz na tela
# com formatação correta

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


test_1 = Matriz()
test_1.motrar_matriz()
