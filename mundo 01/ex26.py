distancia = float(input('Quantos km foi percorrido:'))
if distancia <= 200:
    print('O valor a ser cobrado e de 0,50 por km percorrido, totalizando {}'.format(distancia*0.50))
else:
    print('O valor a ser cobrado e de 0,45 por km percorrido, totalizando {}'.format(distancia*0.45))
