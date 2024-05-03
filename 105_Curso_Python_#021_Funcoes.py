# Faça um programa que tenha uma
# função notas que pode receber várias notas
# de um aluno e vai retornar um dicionário
# com a seguintes informações
# quantidade de notas
# a maior nota
# a média da turma
# a situação (opcional)

# adcicione tambem as docstrings
# na função

def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas e a situações de vários alunos (aceita várias notas)
    :param sit: valor opicional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = round(sum(n) / len(n), 2)
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'BOA'
        elif r['média'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r


resp = notas(3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 9, 8, 9, sit=True)
print(resp)
