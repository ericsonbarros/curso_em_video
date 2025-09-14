import random
numR = random.randint(0,5)
numP = int(input('Adivinhe o numero escolhido entre 0 e 5:'))
if numP == numR:
    print('parabens voce acertou o numero')
else:
    print('Desculpe voce errou o numero')
print('O numero era {}, e voce escolheu {}'.format(numR, numP))
