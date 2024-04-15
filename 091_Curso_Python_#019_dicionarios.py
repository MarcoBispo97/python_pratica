# Crie um programa onde 4 jogadores joguem um dado e
# tenha resultados aleatórios
# No final coloque esse dicionário em ordem
# sabendo que p vencedor tirou o maior número no dado

from random import randint
from collections import OrderedDict
jogo = {
    "jogador_1": randint(1, 6),
    "jogador_2": randint(1, 6),
    "jogador_3": randint(1, 6),
    "jogador_4": randint(1, 6)
}
print(jogo)

dicionario_ordenado = OrderedDict(sorted(jogo.items()))

for index, (jogador, dado) in enumerate(jogo.items()):
    print(index, jogador, dado)
