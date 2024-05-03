# Faça um programa que tenha
# uma função chamada ficha()
# recebe dois parametros opicionais
# o nome do jogador e quantos gols

# o programa deverá ser capaz de mostrar a ficha
# do jogador, mesmo que algum da dado não tenha
# sido informado corretamente

def ficha(nome="Desconhecido", gols=0):
    print(f"O jogador {nome} fez {gols} gol(s) no campeonato.")


# Solicitando ao usuário que insira os dados do jogador
nome_jogador = input("Digite o nome do jogador: ")
num_gols = input("Digite a quantidade de gols: ")

# Verificando se o nome do jogador foi inserido
if nome_jogador.strip():  # Verifica se o nome não está vazio
    # Verificando se o número de gols foi inserido
    if num_gols.strip():  # Verifica se o input não está vazio
        if num_gols.isdigit():  # Verifica se o input é um número
            num_gols = int(num_gols)
            ficha(nome_jogador, num_gols)
        else:
            # print("Valor inválido para a quantidade de gols. Usando 0 como padrão.")
            ficha(nome_jogador)
    else:
        ficha(nome_jogador)
else:
    # Caso o nome não tenha sido inserido, utiliza o valor padrão
    # print("Nome do jogador não fornecido. Usando 'Desconhecido' como padrão.")
    if num_gols.strip() and num_gols.isdigit():
        num_gols = int(num_gols)
        ficha(gols=num_gols)
    else:
        ficha()
