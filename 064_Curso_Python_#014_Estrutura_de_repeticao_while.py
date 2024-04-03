# crie um programa que leia vários numeros inteiros pelo teclado
# o programa só vai parar quando o usuário digitar 999
# no final mostra quantos numeros foram digitados, quais eles e a soma deles
class Program:
    def __init__(self):
        self.run_program()

    def run_program(self):
        num_digi = []
        while True:
            try:
                entrada = input(
                    "Digite um número inteiro e tecle 999 para sair: ")
                num_digi.append(int(entrada))
                if entrada == '999':
                    print("Encerrando o programa...")
                    break
                numero = int(entrada)
                print("Número digitado:", numero)
            except ValueError:
                print("Por favor, digite um número inteiro válido.")
        print("total de num digitados:", len(num_digi))
        print("Numeros digitados", num_digi)
        print("Soma dos números digitados", sum(num_digi))


if __name__ == "__main__":
    programa = Program()
