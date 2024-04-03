# Crie um porgrama que leia o nome e o preço do produto
# O programa deverá perguntar se o usuário vai continuar
# No final mostre:

# A Qual é o total de gastos na compra
# B Quantos produtos custam mais de R$1000
# C Qual é o nome do produto mais barato

total_gastps = 0
produto_maior_mil = 0


precos = []
nomes = []

print("-"*5, "Program de cadastros:", "-"*5)
sair = True
while sair:
    while True:
        preco = input("Digite o preço do produto: ")
        if preco.isdigit():
            precos.append(int(preco))
            break

    nome = input("Digite o nome do produto: ")
    nomes.append(nome)

    quer_sair = input("Deseja sair [s] ?")
    if quer_sair == "s":
        break
    else:
        print("-"*5, "Cadastro realizado", "-"*5)

for preco in precos:
    if preco > 1000:
        produto_maior_mil += 1


produto_mais_barato = nomes[precos.index(min(precos))]

print("A Qual é o total de gastos na compra: ", sum(precos))
print("B Quantos produtos custam mais de R$1000: ", produto_maior_mil)
print("C Qual é o nome do produto mais barato: ",
      produto_mais_barato, min(precos))
