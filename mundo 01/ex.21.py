frase = str(input('Digite a frase:')).lower()
print('A sua frase aparece a letra A {} vezes'.format(frase.count('a')))
print('A primeira vez que a letra A aparece e na posição {}'.format(frase.find('a')+1))
print('A ultima vez que a letra A aparece e na posição {}'.format(frase.rfind('a')+1))