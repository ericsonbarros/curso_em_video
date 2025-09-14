n1 = int(input('Digite um valor: '))
n2 = int(input('Digite um valor: '))
n3 = int(input('Digite um valor: '))
n4 = int(input('Digite um valor: '))
num = (n1, n2, n3, n4)
print(f'O numero 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O numero 3 aparece na posição {num.index(3)+1}')
else:
    print('O valor 3 nao foi digitado nenhuma posição')
print('Os valores par digitados foram ', end='')
for n in num:
    if n % 2 == 0:
        print(n,end=' ')



