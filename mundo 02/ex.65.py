r = 'S'
soma = 0
cont = 0
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N] ')).upper()
    cont += 1
    soma += n
    media = soma / cont
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
print('RESUMO')
print('O total de numeros digitados foi de {}'.format(cont))
print('O somatorio dos numeros digitados foi de {}'.format(soma))
print('A media dos valores digitados foi de {}'.format(media))
print('O maior numero foi {}, e o menor {}'.format(maior, menor))

print('FIM')