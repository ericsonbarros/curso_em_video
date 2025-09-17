ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    print('-=' * 30)
    ficha.append([nome, [nota1, nota2], media])
    if resp == 'N':
        break
print(f'{"no.":<4}{"nome":<10}{"media":>8}')
print('-=' * 30)
for i, l in enumerate(ficha):
    print(f'{i:<4}{l[0]:<10}{l[2]:>8.1f}')
print('-=' * 30)
while True:
    opc = int(input('Mostrar notas de qual aluno? [999 para parar]: '))
    if opc == 999:
        print('finalizando...')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} sao {ficha[opc][1]}')
print('-=' * 30)
print('volte sempre')
