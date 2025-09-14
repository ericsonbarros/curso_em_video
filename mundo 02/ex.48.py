soma = 0
cont = 0
for n in range (1, 501, 2):
    if n % 3 == 0:
        soma = soma + n
        cont = cont + 1
        #soma += n
        #cont += 1
        # ambos fazem a operação de soma e cont
print(f'A soma dos {cont} valores encontrados corresponde a: {soma}')

