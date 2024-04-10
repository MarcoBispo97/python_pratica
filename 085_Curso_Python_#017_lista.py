# Crie um programa onde o usuário possa digitar
# 7 valores numéricos e cadastre-os em uma lista
# única que mantenha separadas os valores pares e ímpares
# no final mostre os valores pares e ímpares em ordem crescente

class Seven_list:
    def __init__(self):
        self.lista = self.absorve_lista()

    def absorve_lista(self):
        lista = []
        pares = []
        impares = []
        for _ in range(7):
            while True:
                entrada = input(f"Digite o {_ + 1}o.s valor: ")
                if entrada.isdigit():
                    if int(entrada) % 2 == 0:
                        pares.append(int(entrada))

                    else:
                        impares.append(int(entrada))

                    break
                else:
                    print("Por favor digite uma valor numérico !")
        pares.sort()
        impares.sort()
        lista.append(pares)
        lista.append(impares)
        return lista

    def show(self):
        print("Lista de pares ordenada: ", self.lista[0])
        print("Lista de ímpares ordenada: ", self.lista[1])


if __name__ == "__main__":
    teste1 = Seven_list()
    teste1.show()
