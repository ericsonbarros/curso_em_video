n = 0
cont = 0
soma = 0
# pode se usar quando todas as variavbeis tiver mesmo valor: n = cont = soma = 0
# pode colcoar o N antes do while para nao precisar usar o soma - 999, e depois coloca o n no while pra gerar condição, eliminando assim o flag
while n != 999:
    n = int(input('digite um valor: '))
    cont += 1
    soma += n
print('RESUMO')
print('O total de numeros digitados foi de {}'.format(cont -1))
print('O somatorio dos numeros digitados foi de {}'.format(soma - 999))
print('FIM')