# Crie um modulo chamado moeda.py
# que tenha as funções aumentar()
# diminuir(), dobro() e metade()
# aumentar e reduzir em porcentagem

# Faça tambem um programa que importe
# esse módulo e usae algumas desas funções

import moeda_contas

while True:
    moeda = input("Digite o preço: ")
    if moeda.isdigit():
        moeda = float(moeda)
        break

print(f"O dobro de {moeda} é {moeda_contas.dobro(moeda)}")
print(f"O metade de {moeda} é {moeda_contas.metade(moeda)}")
print(f"{moeda} mais dez porcento do mesmo é é {moeda_contas.aumentar(10, moeda)}")
print(f"{moeda} menos vinte porcento do mesmo é é {moeda_contas.diminuir(20, moeda)}")
