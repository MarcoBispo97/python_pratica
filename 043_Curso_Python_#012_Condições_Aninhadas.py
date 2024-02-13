# Desenvolva uma lógica que leia o peso e a altura de uma pessoa
# calcule o seu IMC e mostre seu status, de acordo com a tabela abaixo
# abaixo de 18.5: Abaixo do peso
# entre 18.5 e 15: Peso Ideal
# 25 até 30: Sobrepeso
# 30 até 40: Obesidade
# acima de 40: Obesidade mórbita
# Função para calcular o IMC
# Função para calcular o IMC
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

# Função para mostrar o status de acordo com o IMC


def mostrar_status(imc):
    if imc < 18.5:
        print("Abaixo do peso")
    elif imc >= 18.5 and imc < 25:
        print("Peso ideal")
    elif imc >= 25 and imc < 30:
        print("Sobrepeso")
    elif imc >= 30 and imc < 40:
        print("Obesidade")
    else:
        print("Obesidade mórbida")


# Leitura do peso e altura
peso = float(input("Digite seu peso (em kg): "))
altura = float(input("Digite sua altura (em metros): "))

# Cálculo do IMC
imc = calcular_imc(peso, altura)

# Mostrar o status
mostrar_status(imc)
