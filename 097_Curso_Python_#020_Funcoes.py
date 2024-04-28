# Faça um programa que tenha uma função
# chamada escreva(), que receba um texto
# qualquer como parâmetro e mostre uma mensagem
# com tamanhamo adaptável


def escreva(texto):
    print((len(texto) + 3) * '~')
    print(" ", texto, " ")
    print((len(texto) + 3) * '~')


texto = "Teste !"
escreva(texto=texto)
