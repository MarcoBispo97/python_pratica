# crie um programa que tenha uma tupla com várias palavras
# Não usar acento depois disso voce mostrará para cada palavra
# quais são suas vogais

palavras_sem_acento = (
    "banana",
    "cachorro",
    "gato",
    "carro",
    "casa",
    "futebol",
    "escola",
    "janela",
    "computador",
    "livro",
    "cidade",
    "menino",
    "menina",
    "frio",
    "verao",
    "chocolate",
    "amigo",
    "amor",
    "trabalho",
    "musica"
)


for palavra in palavras_sem_acento:
    a = 0
    e = 0
    i = 0
    o = 0
    u = 0
    for letra in palavra:
        if letra == "a":
            a += 1
        elif letra == "e":
            e += 1
        elif letra == "i":
            i += 1
        elif letra == "o":
            o += 1
        elif letra == "u":
            u += 1
    print(f"A palavra {palavra}, tem: \n {a} a, {e} e, {i} i, {o} o, {u} u")
