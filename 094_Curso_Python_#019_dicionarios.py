# Crie um programa que leia nome, sexo e idade
# de várias pessoas, guardando os dados de cada pessoa
# em um dicionário e todos os dicionários em uma lista
# No final mostre:
# A- Quantas pessoas foram cadastradas
# B- A média de idade do grupo
# C- Uma lista com todas as mulheres
# D- Uma lista com todas as pessoas com idade acima da média

dados_pessoas = []

while True:
    dado_pessoa = {
        "nome": input("Digite o nome da pessoa: "),
        "sexo": input("Digite o sexo da pessoa [m/f]: ").lower(),
        "idade": int(input("Digite a idade da pessoa: "))
    }
    dados_pessoas.append(dado_pessoa)
    sair = input("Deseja sair [s]: ").lower()
    if sair == "s":
        break

soma_idade = 0
mulheres = []
media_idade = 0
pessoas_velhas = []
for pessoa in dados_pessoas:
    soma_idade += pessoa["idade"]
    if pessoa["sexo"] == "f":
        mulheres.append(pessoa["nome"])

media_idade = soma_idade / len(dados_pessoas)

for pessoa in dados_pessoas:
    if pessoa["idade"] > media_idade:
        pessoas_velhas.append(pessoa["nome"])

print("Total de pessoas cadastradas: ", len(dados_pessoas))
print("A média das idades são: ", media_idade)
print("Lista de mulheres: ", mulheres)
print("Lista de pessoas mais velhas que a média: ", pessoas_velhas)
