# Crie um programa onde o usuário digite uma
# expressão qualquer que use parenteses
# Seu aplicativo deverá analisar se a expressão passada
# Está com os parêntenses abertos ou fechados na ordem correta;

class Orden_parenteses:
    def __init__(self):
        self.expressao = self.leitura_espressao()

    def leitura_espressao(self):
        expressao = input("Digite a espressão: ")
        lista_abre = []
        lista_fecha = []

        if expressao.count("(") > 0 and expressao.count(")") > 0:
            for letra in expressao:
                if letra == "(":
                    lista_abre.append(letra)
                elif letra == ")":
                    lista_fecha.append(letra)

            if len(lista_abre) == len(lista_fecha):
                print("Expressão válida !")
            else:
                print("Expressão não válida !")

        else:
            print("Expressão não válida !")


if __name__ == "__main__":
    Orden_parenteses_1 = Orden_parenteses()
