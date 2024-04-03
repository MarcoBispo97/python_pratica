# Faça um programa que mostre a tabuada de vários números
# Um de cada vez. para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solocitado for negativo

class Tabuada_positivos:

    def __init__(self):
        self.num_digitado = int(
            input("Digite um num positivo para saber a tabuada dele: "))
        self.inicio_tabuada = int(input("Digite o início da tabuada: "))
        self.fim_tabuda = int(input("Digite o final da tabuada: "))
        self.tamanho_tabuada = [i for i in range(
            self.inicio_tabuada, self.fim_tabuda + 1)]

    def tabu_positivos(self):
        print(f"A tabuada de {self.num_digitado} é:")
        while self.num_digitado > 0:
            for n in self.tamanho_tabuada:
                print("x" * 10, "-" * 10, "x" * 10)
                print(
                    f"{n} x {self.num_digitado} = {n * self.num_digitado}:".center(30))
            self.num_digitado = int(
                input("Digite um num positivo para saber a tabuada dele: "))
            if self.num_digitado < 0:
                break


teste = Tabuada_positivos()
teste.tabu_positivos()
