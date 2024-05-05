# Melhore o 107
# crie a função adicional chamada moeda()
# que consiga mostrar os valores como um
# valor monetário formatado

import moeda_contas

while True:
    moeda = input("Digite o preço R$: ")
    if moeda.isdigit():
        moeda = float(moeda)
        break

print(
    f"O dobro de {moeda_contas.formatar(moeda)} é {moeda_contas.formatar(moeda_contas.dobro(moeda))}")
print(
    f"O metade de {moeda_contas.formatar(moeda)} é {moeda_contas.formatar(moeda_contas.metade(moeda))}")
print(f"{moeda_contas.formatar(moeda)} mais dez porcento do mesmo é é {moeda_contas.formatar(moeda_contas.aumentar(10, moeda))}")
print(f"{moeda_contas.formatar(moeda)} menos vinte porcento do mesmo é é {moeda_contas.formatar(moeda_contas.diminuir(20, moeda))}")
