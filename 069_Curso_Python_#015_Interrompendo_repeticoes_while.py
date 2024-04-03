# Crie um programa que leia a idade e o sexo de várias pessoas
# A cada pessoa cadastrada o programa deverá perguntar se o usuário
# quer ou não continuar
# No final mostre:
# A - Quantas pessoas tem mais de 18 anos
# B - Quantos homens foram cadastrados
# c - Quantas mulheres tem menos de 20 anos.

mais_18 = 0
homens = 0
mulheres_menos_20 = 0

idades = []
sexos = []

print("-"*5, "Program de cadastros:", "-"*5)
sair = True
while sair:
    while True:
        idade = input("Digite a idade da pessoa: ")
        if idade.isdigit():
            idades.append(int(idade))
            break
    while True:
        sexo = input("Digite o sexo da pessoa [m/f]: ")
        if sexo == "m" or sexo == "f":
            sexos.append(sexo)
            break
    quer_sair = input("Deseja sair [s] ?")
    if quer_sair == "s":
        break
    else:
        print("-"*5, "Cadastro realizado", "-"*5)

for idade in idades:
    if idade > 18:
        mais_18 += 1

for sexo in sexos:
    if sexo == "m":
        homens += 1

for idade, sexo in zip(idades, sexos):
    if sexo == "f" and idade < 20:
        mulheres_menos_20 += 1

print("A - Quantas pessoas tem mais de 18 anos: ", mais_18)
print("B - Quantos homens foram cadastrados: ", homens)
print("C - Quantas mulheres tem menos de 20 anos: ", mulheres_menos_20)
