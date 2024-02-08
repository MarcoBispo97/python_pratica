# Escreva um programa que leia dois números inteiros e compare-os,
# mostrando na tela uma mensagem:
# O primeiro valor é maior
# O segundo valor é maiorNão existe valor maior, os dois são iguais
primeiro_n_inteiro = int(input("Digite o primeiro número inteiro: "))
segundo_n_inteiro = int(input("Digite o segundo número inteiro: "))
if primeiro_n_inteiro > segundo_n_inteiro:
    print("O primeiro número é maior")
elif segundo_n_inteiro > primeiro_n_inteiro:
    print("O segundo número é maior")
else:
    print("Os número são iguais")
