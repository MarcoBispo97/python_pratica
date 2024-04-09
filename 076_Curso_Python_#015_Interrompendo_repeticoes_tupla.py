# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos
# preços na sequencia
# no final, mostre uma listagem de preços organizando os dados de forma tabular
# Definindo a tupla com os produtos e preços
produtos_precos = (
    ("Arroz", 5.99),
    ("Feijão", 3.49),
    ("Macarrão", 2.29),
    ("Azeite de oliva", 12.99),
    ("Sal", 1.49),
    ("Açúcar", 3.99),
    ("Café", 8.49),
    ("Leite", 2.99),
    ("Ovos", 4.99),
    ("Carne", 15.99),
    ("Frango", 10.99),
    ("Peixe", 8.99),
    ("Pão", 3.49),
    ("Queijo", 6.99),
    ("Manteiga", 4.49)
)

# Imprimir cabeçalho da tabela
print("{:<20} {:<10}".format("Produto", "Preço"))

# Imprimir linha separadora
print("-" * 30)

# Imprimir cada produto e seu preço
for produto, preco in produtos_precos:
    print("{:<20} R$ {:<10.2f}".format(produto, preco))
