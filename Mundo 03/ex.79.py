valores = list()
while True:
    valores.append(int(input('Digite um valor: ')))
    print('Valor adicionado com sucesso...')
    cont = str(input('quer continuar? ')).strip().upper()
    if cont == 'NAO':
        break
print(valores)
