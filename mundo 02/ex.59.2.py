n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opção = 0
while opção != 5:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos numeros
    [ 5 ] sair do programa''')
    opção = int(input('Qual a sua opção? ')
    if opção == 1:
        soma = n1 + n2
        print(f'A soma dos valores {n1} + {n2} = {soma}')
    elif opção == 2:
        multi = n1 * n2
        print(f'A multiplicação dos valores {n1} X {n2} = {multi}')
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'Entre {n1} e {n2} o maior é {maior}')
    elif opção == 4:
    n1 = int(input('Digite o primeiro valor novamente: '))
    n2 = int(input('Digite o segundo valor novamente: '))
    else:
        print('opção invalida. Tente novamente'))
print('Fim do programa ! Volte sempre.')
