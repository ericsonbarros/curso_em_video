aluno = dict()
aluno['nome'] = str(input('Digite o Nome do aluno(a): '))
aluno['media'] = float(input(f'Digite a media de {aluno["nome"]}: '))
print('-=' * 20)
print(f'O aluno {aluno["nome"]} esta com', end='')
print(f' a media e igual a {aluno["media"]}')
print('Situação...')
print('-=' * 20)
if aluno["media"] >= 7:
    print(f'O aluno {aluno["nome"]} esta APROVADO')
else:
    print(f'O aluno {aluno["nome"]} esta REPROVADO')