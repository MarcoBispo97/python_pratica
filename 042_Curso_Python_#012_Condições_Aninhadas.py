# Receba os 3 lados de um triangulo e classifique ele em
# Equilátero, Isóceles ou Escaleno
l1 = int(input("Insira o valor do primeiro lado: "))
l2 = int(input("Insira o valor do segundo lado: "))
l3 = int(input("Insira o valor do terceiro lado: "))

if (l1 == l2) and (l2 == l3):
    print("Triangulo Equilatero")
elif (l1 == l2) or (l2 == l3) or (l1 == l3):
    print("Triangulo Isoceles")
else:
    print("Triangulo escaleno")
