# Crie um programa que leia o ano
# de nascimento de sete pessoas.
# No final mostre quantas pessoas
# ainda não atingiram a maioriadade
# e quantas atingiram a maioridade
import datetime

ano_atual = datetime.datetime.now().year


class Ano_nasc:
    def __init__(self, anos_nasc):
        self.anos_nasc = anos_nasc

    def maioridade(self):
        anos_maioridade = []
        anos_menoridade = []
        for ano_nasc in self.anos_nasc:
            if (ano_atual - ano_nasc) > 18:
                anos_maioridade.append(ano_nasc)
            else:
                anos_menoridade.append(ano_nasc)
        print("Maiores de 18: ", anos_maioridade)
        print("Menores de 18: ", anos_menoridade)


anos_pessoas = Ano_nasc([1997, 1998, 1999, 2000, 2001,
                        2002, 2003, 2004, 2005, 2006, 2007, 2008])
anos_pessoas.maioridade()
