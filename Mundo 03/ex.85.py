valores = [[], []]
valor = 0
for c in range(0, 7):
    valor = int(input('Digite um valor: '))
    if valor % 2 == 0:
        valores[0].append(valor)
    else:
        valores[1].append(valor)
print('-=' * 30)
valores[0].sort()
valores[1].sort()
print(f'Os valores pares digitados foram {valores[0]}')
print('-=' * 30)
print(f'os valores impares digitados foram {valores[1]}')


