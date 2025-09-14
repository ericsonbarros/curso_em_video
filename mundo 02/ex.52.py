num = int(input('Digite um numero: '))
cont=0
for c in range(1, num+1):
    if num % c == 0:
        print('\033[34m', end='')
        cont+= 1
    else:
        print('\033[31m', end='')
    print(' {} '.format(c), end='')
print(f'\n\033[mO numero {num} foi divisivel {cont} vezes')
if cont == 2:
    print('O numero e primo')
else:
    print('O numero nao e primo')
