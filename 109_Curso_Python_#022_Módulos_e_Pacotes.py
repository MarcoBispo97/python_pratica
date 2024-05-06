# Modifique as funções do desafio 107
# para que elas aceitem um parametro
# a mais informando se o valor retornado por elas vai ser ou não
# formatado pela função moeda()
# desenvolvido no 108

import ex109_moeda

while True:
    moeda = input("Digite o preço R$: ")
    if moeda.isdigit():
        moeda = float(moeda)
        break

print(
    f"O dobro de {ex109_moeda.formatar(moeda)} é {ex109_moeda.dobro(moeda)}")
print(
    f"O metade de {ex109_moeda.formatar(moeda)} é {(ex109_moeda.metade(moeda))}")
print(f"{ex109_moeda.formatar(moeda)} mais dez porcento do mesmo é é {(ex109_moeda.aumentar(10, moeda, False))}")
print(f"{ex109_moeda.formatar(moeda)} menos vinte porcento do mesmo é é {(ex109_moeda.diminuir(20, moeda, False))}")
