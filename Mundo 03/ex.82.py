valores = list()
pares = list()
impares = list()
while True:
    valores.append(int(input('Digite um valor: ')))
    print('-='*30)
    print('valor adicionado com sucesso...')
    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
for i, v in enumerate(valores):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print(f'os valores da lista: {valores}')
print('-='*30)
print(f'os pares: {pares}')
print('-='*30)
print(f'os impares: {impares}')
print('-='*30)
