# Crie um programa que leia nome
# ano de nascimento e carteira de trabalho
# cadastre-os com idade em um dicionário
# se por acaso o CTPS for diferente de ZERO
# o dicionário receberá também o ano de contratação
# e o salário
# Calcule e acrescente, além da idade, com quantos
# anos a pessoa vai se aposentar

import time


ano = time.localtime().tm_year

dados_ibge = {}
while True:
    nome = input("Digite o seu nome: ")
    if nome.isdigit:
        dados_ibge["nome"] = nome
        break
    else:
        print("Por favor digite um nome válido !")


while True:
    ano_nasc = input("Digite o ano de nascimento: ")
    if nome.isdigit:
        dados_ibge["Idade: "] = ano - int(ano_nasc)
        break
    else:
        print("Por favor digite um número válido !")

while True:
    carteira = input("Digite a carteira de trabalho: (0 não tem !)")
    if carteira.isdigit and carteira != "0":
        dados_ibge["ctps"] = int(carteira)
        break
    elif carteira.isdigit and carteira == "0":
        dados_ibge["ctps"] = 0
    else:
        print("Por favor digite um número válido !")

while True:
    if carteira.isdigit and carteira != "0":
        salario = input("Salário: ")
        if nome.isdigit:
            dados_ibge["Salário: "] = salario
            break
        else:
            print("Por favor digite um número válido !")
    else:
        break

print(dados_ibge)
print(dados_ibge.items())
