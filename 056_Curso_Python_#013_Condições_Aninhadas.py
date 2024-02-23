# desenvolva um program que leia
# o nome, a idede e o sexo
# de 4 pessoas e no final mostre:

# a média de idade
# o nome do homem mais velho
# quantas mulheres tem menos de 20 anos

class Ibge:
    def __init__(self, nomes, idades, sexos):
        self.nomes = nomes
        self.idades = idades
        self.sexos = sexos

    def conta(self):
        mulheres_jovens = []
        homens = []
        homens_idade = []
        print("A media de idade é: ", round(
            sum(self.idades)/len(self.idades), 2))
        for nome, idade, sexo in zip(self.nomes, self.idades, self.sexos):
            if sexo == "M":
                homens.append(nome)
                homens_idade.append(idade)

            if idade <= 20 and sexo == "F":
                mulheres_jovens.append(nome)
        for nome, idade in zip(homens, homens_idade):
            if idade == max(homens_idade):
                print("O Homem mais velho é:", nome)
        print("As mulheres menores de 20 anos são: ", mulheres_jovens)


pesquisa = Ibge(
    ["Ana", "Gabriela", "Marco", "Leticia", "Rafael", "Lais"],
    [18, 28, 26, 19, 30, 30],
    ["F", "F", "M", "F", "M", "F"]
)
pesquisa.conta()
