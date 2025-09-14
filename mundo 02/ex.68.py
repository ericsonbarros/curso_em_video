from random import randint
cont = 0
while True:
    jogador = int(input('escolha um numero: '))
    maquina = randint(0,11)
    total = jogador + maquina
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('Voce quer ser par ou impar? ')).strip().upper()[0]
    print(f'Voce jogou {jogador}, e o computador {maquina}, o soma dos dois é {total}')
    if escolha == 'P':
        if total % 2 == 0:
            print('Voce GANHOU!')
            cont += 1
        else:
            print('Voce perdeu!')
            break
    elif escolha == 'I':
        if total % 2 == 1:
            print('Voce GANHOU!')
            cont += 1
        else:
            print('Voce perdeu!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER!, você ganhou {cont} vezes.')

