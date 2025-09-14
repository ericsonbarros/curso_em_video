gen = str(input('Informe seu genero [F/M]: ')).strip().upper()[0]
while gen not in 'MmFf':
    gen = str(input('Dados invalidos, Digite novamente: ')).strip().upper()[0]
print('OK, seu dado foi inserido com sucesso, voce selecionou {}'.format(gen))
