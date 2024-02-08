# Faça um programa que leia o ano de nascimento de
# um jovem e informe, de acordo com sua idade:

# Se ele ainda vai se alistar ao serviço militar
# Se é hora de se alistar
# Se já passou o tempo do alistamento
from datetime import datetime

ano_nasc = int(input("Informe o ano do seu nascimento: "))
ano = str(datetime.now())
ano_atual = int(ano[:4])
diferenca = ano_atual - ano_nasc

if diferenca == 17:
    print("É hora de se alistar")
elif diferenca > 18:
    print("Já passou da hora de se alistar")
elif diferenca < 17:
    print("Não é seu ano de alistamento")
