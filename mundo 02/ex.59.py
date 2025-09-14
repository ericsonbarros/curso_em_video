n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))
c = 0
print('menu: \n '
      '[ 1 ] soma\n '
      '[ 2 ] multiplicar \n '
      '[ 3 ] maior \n '
      '[ 4 ] novos numeros \n '
      '[ 5 ] sair do programa')
while c < 5:
    c = int(input('Escolha entre uma das opções: '))
    if c == 1:
        soma = n1 + n2
        print(f'A soma dos valores {n1} + {n2} = {soma}')
    if c == 2:
        multi = n1 * n2
        print(f'A multiplicação dos valores {n1} X {n2} = {multi}')
    if c == 3:
        if n1 > n2:
            print(f'O numero {n1} e maior que o numero {n2}')
            print(f'O numero {n1} e igual ao numero {n2}')
        else:
            print(f'O numero {n2} e maior que o numero {n1}')
    if c == 4:
        n1 = float(input('Digite o primeiro valor: '))
        n2 = float(input('Digite o segundo valor: '))
    if c == 5:
        print('Fim do programa')

