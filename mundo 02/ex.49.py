num = int(input('Digite a tabuada escolhida: '))
print('-'*16)
for c in range (1, 11):
    print('   {} x {:2} = {}'.format(num, c, (num*c)))
print('-'*16)
#print('{} x 1 = {}'.format(num, (num*1)))