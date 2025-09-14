termo = int(input('Digite o termo: '))
razao = int(input('Digite a razão: '))
cont = 1
while cont <= 10:
    print(f'{termo}', end=' ')
    termo += razao
    cont += 1
print('FIM')