salario = float(input('Digite o valor do salario: '))
if salario > 1250:
    aumento1 = salario + (salario * 10 / 100)
    print( 'O aumento no salario e de {:.2f}, totalizando {:.2f}'.format((aumento1 - salario), aumento1))
else:
    aumento2 = salario + (salario * 15 / 100)
    print('O aumento no salario e de {:.2f}, totalizando {:.2f}'.format((aumento2 - salario), aumento2))