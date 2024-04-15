# Crie um programa que gerencie o aproveitamento de um
# jogador de futebol. O programa vai ler o
# Nome do jogador e quantas partidas ele jogou
# Depois vai ler a quantidade de gols
# feitos em cada partida
# no final, tudo isso será guardado em um dicionário,
# incluindo o total de gols feitos durante o campeonatio

jogador_dados = {}


while True:
    nome_jogador = input("Digite o nome do jogador: ")
    if nome_jogador.isdigit():
        print("Por favor digite um nome !")
    else:
        jogador_dados["Nome Jogador"] = nome_jogador
        break

while True:
    partidas = input("Digite o número de partidas: ")
    if partidas.isdigit():
        jogador_dados["Número de partidas"] = int(partidas)
        break
    else:
        print("Por vaor digite um número válido !")

jogador_dados["Quantidade de gols na partida"] = []
for i in range(jogador_dados["Número de partidas"]):
    while True:
        quantidade_gols = input(
            f"Digite quantos gols ele fez na partida {i +1}: ")
        if quantidade_gols.isdigit():
            jogador_dados["Quantidade de gols na partida"].append(
                int(quantidade_gols))
            break
        else:
            print("Por favor digite um número válido !")

jogador_dados["Total de gols"] = sum(
    jogador_dados["Quantidade de gols na partida"])

print(jogador_dados.items())
print("Dados do jogador:")
print("+---------------------+----------------------+")
print("| Nome do jogador     | Partidas jogadas     |")
print("+---------------------+----------------------+")
print(
    f"| {jogador_dados['Nome Jogador']:<20}| {jogador_dados['Número de partidas']:^20}|")
print("+---------------------+----------------------+")
print("Partidas          Gols")
for i, gols in enumerate(jogador_dados['Quantidade de gols na partida'], start=1):
    print(f"  Partida {i}:        {gols} gols")
print("+---------------------+----------------------+")
print(f"| Total de gols:      | {jogador_dados['Total de gols']:^20}|")
print("+---------------------+----------------------+")
