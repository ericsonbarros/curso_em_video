n= soma = cont = 0
while True:
    n = int(input('Digite um valor: '))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'Foram inseridos {cont} numeros')
print(f'A soma dos numeros inseridos totaliza {soma}')
print('FIM')