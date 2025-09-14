name = str(input('Digite seu nome:')).strip()
print('Analisando seu nome...')
print('Seu nome com letras maiusculas é {}'.format(name.upper()))
print('Seu nome em letras minusculas é {}'.format(name.lower()))
print('Seu nome tem ao todo {} letras'.format(len(name) - name.count(' ')))
print('Seu primeiro nome tem {} letras'.format(name.find(' ')))

