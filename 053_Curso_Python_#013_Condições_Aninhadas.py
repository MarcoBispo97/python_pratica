# Crie um program que leia uma frase
# e diga se ele á um polindrama
# desconsidese espaços
# apos a sopa
# a sacada da casa
# o lobo ama bolo
# anotaram a data da maratona

class check_poli:
    def __init__(self, palavra):
        self.palavra = palavra

    def programa(self):
        palavra_cortada = list(self.palavra)
        print(palavra_cortada)


palavra_1 = check_poli('Marco Bispo')
palavra_1.programa()
