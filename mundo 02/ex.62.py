termo = int(input('Digite o termo: '))
razao = int(input('Digite a razão: '))
cont = 1
mais  = 10
total = 0
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{termo}', end=' ')
        termo += razao
        cont += 1
    mais = int(input('\nquantos termos a mais voce quer? '))
print('progressao finalizada com  {} termos mostrados.'.format(total))
print('FIM')