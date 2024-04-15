# Faça um programa que leia nome e média
# de um aluno, guargando também a situação
# em um dicionário
# No final mostre o conteúdo da estrutura da tela
nomes_medias = {
    "Nome": [],
    "Média": []
}
while True:
    nome = input("Digite o nome do aluno: ")
    if nome.isdigit():
        print("Voce não digitou um nome")
    else:
        nomes_medias["Nome"] = nome
    media = input("Digite a média do aluno: ")
    if media.isdigit():
        nomes_medias["Média"] = media
        if float(media) >= 7:
            nomes_medias["Situação"] = "Aprovado"
        else:
            nomes_medias["Situação"] = "Reprovado"
        break
    else:
        print("Voce não digitou um número")
print(nomes_medias.values())
print(nomes_medias.keys())
print(nomes_medias.items())
for k, v in nomes_medias.items():
    print(f"{k} é {v}")
