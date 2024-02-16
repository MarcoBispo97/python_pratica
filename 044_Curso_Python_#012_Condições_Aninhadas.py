# Elabora um programa que calcule o valor a ser pago
# por um produto, considerando o seu preço normal e
# condição de pagamento
# A vista dinheiro/cheque 10% de desconto
# em até 2x no cartão preço normal
# 3x ou mais no cartão 20% de juros
class valor_pago:
    def __init__(self, valor, metodo_pagamento, vezes_cartao):
        self.valor = valor
        self.metodo_pagamento = metodo_pagamento
        self.vezes_cartao = vezes_cartao

    def calcula(self):
        if (self.metodo_pagamento == "a vista") or (self.metodo_pagamento == "cheque"):
            self.valor = self.valor - (self.valor * 0.1)
        elif self.metodo_pagamento == "cartão":
            if self.vezes_cartao == 2:
                self.valor
            elif self.vezes_cartao >= 2:
                self.valor = self.valor + (self.valor * 0.2)
        return self.valor


pagamento1 = valor_pago(100, "a vista", 1)
valor1 = pagamento1.calcula()
print(valor1)

pagamento2 = valor_pago(200, "cartão", 2)
valor2 = pagamento2.calcula()
print(valor2)

pagamento3 = valor_pago(300, "cartão", 3)
valor3 = pagamento3.calcula()
print(valor3)
