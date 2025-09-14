nome = str(input('Insira o nome do aluno(a): '))
nota1 = float(input('Insira a primeira nota: '))
nota2 = float(input('Insira a segunda nota: '))
media = (nota1 + nota2) / 2
print(f'A média do aluno(a) {nome} foi {media}')
if media >= 7:
    print('O aluno foi APROVADO')
elif media < 5:
    print('O aluno foi REPROVADO')
else:
    print('O aluno está em RECUPERAÇÃO')