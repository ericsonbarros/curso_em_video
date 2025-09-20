from random import randint
from time import sleep
def sorteio(lista):
    print('Sorteando 5 valores da lista', end=' ')
    for c in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='')
        sleep(0.5)
    print('PRONTO!')
def somapar(lista):
    soma = 0
    for c in lista:
        if c % 2 == 0:
            soma += c
    print(f'Somando os valores pares de {lista}, temos {soma}')


# programa principal
numeros = list()
sorteio(numeros)
somapar(numeros)




