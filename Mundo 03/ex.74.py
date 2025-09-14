# metodo 1
import random
menor = 0
n1 = (random.randint(0,10))
n2 = (random.randint(0,10))
n3 = (random.randint(0,10))
n4 = (random.randint(0,10))
n5 = (random.randint(0,10))
num = (n1, n2, n3, n4, n5)
print(f'Os numeros sorteados foram: {num}')
print(f'O maior valor sorteado foi {max(num)}')
print(f'O menor valor sorteado foi {min(num)}')