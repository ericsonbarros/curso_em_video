total = cont = menor = 0
while True:
    nome = str(input('Digite o nome do produto: '))
    valor = float(input('Digite o valor do produto: '))
    continuar = str(input('Deseja continuar a cadastrar produto: ')).strip().upper()[0]
    total += valor
    if valor >= 1000:
        cont += 1
    if cont == 1:
      menor = valor
      barato = nome
    else:
      if valor < menor:
        menor = valor
        barato = nome
    if continuar == 'N':
        break
    #if menor < valor:
       # menor = valor
print(f'O valor total gasto foi: {total} reais')
print(f'Ao todo foram {cont} produtos acima de 1.000 reais')
print(f'O menor produto custou {menor} e foi {barato}')