from random import randint
from time import sleep
cont = 0
computador = randint(0, 10) # faz o computador escolher um numero aleatorio
print('-='*20)
print('Eu vou pensar em um numero de 0 a 10, tente advinhar...')
print('-='*20)
jogador = int(input('Em qual numero eu pensei ?: '))# faz o usuario escolher um numero
print('PROCESSANDO...')
sleep(3)
while jogador != computador:
    print('\033[0;31;40mvoce errou, tente novamente...\033[m')
    jogador =int(input('voce tentou o numero {} e errou, tente advinhar o numero correto: '.format(jogador)))
    print('PROCESSANDO...')
    sleep(2)
cont += jogador
print('PARABENS... VOCE VENCEU!!')
print(f'foram necessarias {cont} tentativas para conseguir advinhar o numero.')