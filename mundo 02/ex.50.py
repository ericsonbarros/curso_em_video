soma = 0
cont = 0
for c in range (0, 6):
    c = int(input('Digite um valor: '))
    if c % 2 == 0:
        soma += c
        cont += 1
print(f'A soma dos {cont} valores encontrados corresponde a: {soma}')
