# Crie um program que leia uma frase
# e diga se ele á um polindrama
# desconsidese espaços
# apos a sopa
# a sacada da casa
# o lobo ama bolo
# anotaram a data da maratona

class check_poli:
    def __init__(self, palavra):
        self.palavra = palavra.lower()

    def programa(self):
        palavra_cortada = list(self.palavra)
        lista_filtrada = []
        for l in palavra_cortada:
            if l != " ":
                lista_filtrada.append(l)

        lista_regular = lista_filtrada
        lista_inversa = list(reversed(lista_filtrada))
        if lista_regular == lista_inversa:
            print("É polindrama")
        else:
            print("Não é polindrama")


palavra_1 = check_poli('Marco Bispo')
palavra_1.programa()
palavra_1 = check_poli('o lobo ama bolo')
palavra_1.programa()
palavra_1 = check_poli('ana')
palavra_1.programa()
palavra_1 = check_poli('anotaram a data da maratona')
palavra_1.programa()
