# Desenvolva um programa que leia o primeiro termo
# e a razao de uma PA.
# No final, mostre os 10 primeiros termos dessa
# progressão

class PA:
    def __init__(self, primeiro_termo, razao):
        self.primeiro_termo = primeiro_termo
        self.razao = razao

    def calculo(self):
        termo = 0
        for i in range(10):
            termo = int(self.razao) * i + int(self.primeiro_termo)
            print(f"termo {i+1}: {termo}")


PA_1 = PA(2, 5)
PA_1.calculo()
