valores = list()
for cont in range(0,5):
    valores.append(int(input('Digite um valor: ')))
maior = max(valores)
menor = min(valores)
print(f'Voce digitou os valores{valores}')
print(f'O maior valor digitado foi {maior} na posição {valores.index(maior)+1}')
print(f'O menor valor digitado foi {menor} na posição {valores.index(menor)+1}')