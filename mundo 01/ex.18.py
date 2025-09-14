num = int(input('Digite o numero escolhido:'))
#n = str(num)
#('Analisando o numero {}'.format(num))
#print('Unidade: {}'.format(n[3]))
#('Dezena: {}'.format(n[2]))
#print('Centena: {}'.format(n[1]))
#print('Milhar: {}'.format(n[0]))
u = num // 1 % 10
d = num //10 % 10
c = num //100 % 10
m = num // 1000 % 10
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))


