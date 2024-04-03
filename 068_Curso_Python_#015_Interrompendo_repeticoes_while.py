# Faça um programa que jogue par ou ímpar
# O jogo só será interrompido quando o jogador PERDER
# Mostrar o total de vitórias consecutivas que ele conquistou no
# Final do jogo

# escolhe par ou ímpar
import random


class ParOuImpar:
    def __init__(self):
        self.derrotas = 0
        self.player_par_ou_impar = self.get_par_ou_impar()

    def get_par_ou_impar(self):
        while True:
            par_ou_impar = input("Digite 0 para par e 1 para ímpar: ")
            if par_ou_impar.isdigit() and (par_ou_impar == "0" or par_ou_impar == "1"):
                if par_ou_impar == "0":
                    return "par"
                else:
                    return "impar"

    def par_impar(self, num):
        if num % 2 == 0:
            return "par"
        else:
            return "impar"

    def jogar(self):
        while True:
            num_pc = random.randint(1, 100)
            while True:
                num_jogador = input("Digite o número para jogar:")
                if num_jogador.isdigit():
                    num_jogador = int(num_jogador)
                    break

            print("Num pc", num_pc)
            num_resultado = num_jogador + num_pc
            print("Resultado ", num_resultado)
            par_impar_resultado = self.par_impar(num_resultado)
            if par_impar_resultado == self.player_par_ou_impar:
                print("Você venceu!")
                break
            else:
                print("Você perdeu!")
                self.derrotas += 1
        print(f"Você perfeu {self.derrotas} vezes")


if __name__ == "__main__":
    jogo = ParOuImpar()
    jogo.jogar()
