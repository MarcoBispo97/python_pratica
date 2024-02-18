# Desenvolva um programa que leia seis numeros inteiros
# e mostre a soma apenas daqueles que forem pares
# se valor digitado for impar desconsidere-o

class Conta:
    def __init__(self, numeros):
        self.numeros = numeros

    def conta_numero(self):
        lista_pares = []
        for i in self.numeros:
            print(i)
            if i % 2 == 0:
                lista_pares.append(i)
        print("A soma dos numeros pares são: ", sum(lista_pares))


lista_6 = Conta([1, 2, 3, 4, 5, 6])
lista_6.conta_numero()
