from random import randint
from time import sleep
print(('\033[1;37;40m-=\033[m'*11) + '\033[4;30;47mJOKENPO\033[m' + ('\033[1;37;40m-=\033[m')*11)
itens = ('Pedra', 'Papel', 'tesoura')
computador = randint(0,2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('\033[1;37;40m-=\033[m' *15)
print ('O computador escolheu {}'.format(itens[computador]))
print ('O jogador escolheu {}'.format(itens[jogador]))
print('\033[1;37;40m-=\033[m' *15)
if computador == 0: # computador jogou pedra
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCEU')
    elif jogador == 2:
        print('COMPUTADOR VENCEU')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 1: # computador jogou papel
    if jogador == 0:
        print('COMPUTADOR VENCEU')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCEU')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 2: # computador jogou tesoura
    if jogador == 0:
        print('JOGADOR VENCEU')
    elif jogador == 1:
        print('COMPUTADOR VENCEU')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA!')
