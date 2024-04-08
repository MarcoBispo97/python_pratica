# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela
# do Campeonato Brasileiro de Futebol, na ordem da colocação
# depois mostre:
# Apenas os 5 primeiros colocados
# Os últimos 4 colocados da tabela
# Uma lista com os times em ordem alfabética
# Em que posição na tabela está o time Chapecoense

tabela_brasileirao = (
    "Flamengo",
    "Atlético Mineiro",
    "Palmeiras",
    "Fortaleza",
    "Bragantino",
    "Atlético Paranaense",
    "Atlético Goianiense",
    "Ceará",
    "Fluminense",
    "Santos",
    "Corinthians",
    "Internacional",
    "Juventude",
    "Sport Recife",
    "Bahia",
    "São Paulo",
    "América Mineiro",
    "Cuiabá",
    "Grêmio",
    "Chapecoense"
)

tabela_brasileirao_lista = list(tabela_brasileirao)

print("5 primeiros colocados: ", tabela_brasileirao[:5])
print("Os últimos 4 colocados da tabela: ", tabela_brasileirao[-4:])
print("Times em ordem alfabética: ", sorted(tabela_brasileirao_lista))
print("A posição do Chapecoense é : ",
      tabela_brasileirao.index("Chapecoense") + 1)
