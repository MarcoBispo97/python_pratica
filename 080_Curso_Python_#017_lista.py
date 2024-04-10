# Crie um programa onde o ususário possa
# digitar cinco valores numéricos e cadastre-o em uma lista
# já na posição correta de inserção sem usar .sort()
# No final mostre a lista ordenada na tela


class Lista_ordem:
    def __init__(self):
        self.lista = self.recebe_lista()

    def recebe_lista(self):
        lista = []
        for _ in range(5):
            while True:
                entrada = input("Digite um valor numérico: ")
                if entrada.isdigit():
                    lista.append(int(entrada))
                    break
                else:
                    print("Somente valores numéricos !")
        return lista

    def ordem_lista(self):
        for i in range(1, len(self.lista)):
            valor_atual = self.lista[i]
            posicao = i

        while posicao > 0 and self.lista[i - 1] > valor_atual:
            self.lista[posicao] = self.lista[posicao - 1]
            posicao -= 1

        self.lista[posicao] = valor_atual

        return self.lista


teste1 = Lista_ordem()
teste1.ordem_lista()
