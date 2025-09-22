def notas(*n, sit=False):
    """ -> Função para analisar notas e situacao de varios aluno.
    :param n: uma ou mais notas do aluno(aceita varias)
    :param sit: valor opcional, indicando se deve ou nao adicionar a situação
    :return: dicionario com varias informações sobre a situacao da turma."""
    
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n) / len(n)
    if sit:
        if r['media'] >= 7:
            r['situacao'] = 'BOA'
        elif r['media'] >= 5:
            r['situacao'] = 'RAZOAVEL'
        else:
            r['situacao'] = 'RUIM'
    return r


# Programa principal
resp = notas(5.5, 2.5, 9, 8.5, sit=True)
print(resp)
