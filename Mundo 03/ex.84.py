galera = list()
dado = list()
maior = menor = 0
while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    if len(galera) == 0:
        maior = menor = dado[1]
    else:
        if dado[1] > maior:
            maior = dado[1]
        if dado[1] < menor:
            menor = dado[1]
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    galera.append(dado[:])
    dado.clear()
    if continuar == 'N':
        break
print('-='*30)
print(f'Os dados cadastrados foram: {galera}')
print('-='*30)
print(f'Ao todo temos {len(galera)} pessoas cadastradas')
print('-='*30)
print(f'o maior peso foi de {maior} Kg,o peso foi de ', end='')
for p in galera:
    if p[1] == maior:
        print(f'{p[0]} ')
print('-='*30)
print(f'o menor peso foi de {menor} Kg, o peso foi de ', end='')
for p in galera:
    if p[1] == menor:
        print(f'{p[0]} ')


