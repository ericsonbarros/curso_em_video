def maior(*num):
    print('-=' * 30)
    print('Analisando os valores passados...')
    for n in num:
        print(n, end=' ')
        tam = len(num)
    print(f'foram informados {tam} valores ao todo')
    print(f'O maior valor informado foi {max(num)}')


# Programa principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
# Programa roda porem se colocar apenas maior() da erro por causa do espaço vazio, entao ideal e rodar o ex.99b
