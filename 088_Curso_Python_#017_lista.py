# Crie um program que ajude a jogar na mega
# O programa vai perguntar quantos jogos
# serão gerados e vai sortear 6 números
# entre 1 e 60 para cada jogo
# Tudo em uma lista composta

from random import randint


def mega_palpite():
    while True:
        n_jogos = input("Quantos jogos vc precisa fazer ? ")
        if n_jogos.isdigit():
            n_jogos = int(n_jogos)
            break
        else:
            print("Por favor digite um número válido")
    jogo = []
    jogos = []
    for i in range(n_jogos):
        primeiro_numero = randint(1, 60)
        jogo.append(primeiro_numero)
        for j in range(5):
            while True:
                numero_aleatorio = randint(1, 60)
                if numero_aleatorio not in jogo:
                    jogo.append(numero_aleatorio)
                    break
        jogo.sort()
        jogos.append(jogo)
        jogo = []

    for index, jogo in enumerate(jogos, start=1):
        print(f"{index}o jogo: ", jogo)


mega_palpite()
