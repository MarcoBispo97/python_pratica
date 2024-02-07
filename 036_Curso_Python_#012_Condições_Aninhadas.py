# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação que ela não pode exceder 30% do salário ou entrão o empréstimo é negado

salario = int(input("Digite o valor do seu salário: "))
valor_casa = int(input("Digite o valor do imóvel: "))
anos_a_pagar = int(input("Quantos anos você deseja pagar ? "))

if (salario * 0.3) > (valor_casa/(anos_a_pagar * 12)):
    print("Infelizmente o imóvel foi negado !")
else:
    print("Parabéns, imóvel aprovado !")
