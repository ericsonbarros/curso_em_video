valores = list()
cont = 0
while True:
    print('-='*30)
    valores.append(int(input('Digite um valor: ')))
    print('valor adicionado com sucesso...')
    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    cont += 1
    if continuar == 'N':
        break
print('-='*30)
print(f'Os valores adicionados foram {valores}')
print('-='*30)
print(f'Foram adicionado {cont} numeros a lista.')
print('-='*30)
valores.sort(reverse=True)
print(f'Os valores adicionado em ordem decrescente {valores}')
print('-='*30)
if 5 in valores:
    print('o numero 5 foi adicionado na lista')
else:
    print('O numero 5 nao foi adicionado na lista')