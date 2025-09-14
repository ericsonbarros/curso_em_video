velocidade = int(input('Digite a velocidade do veiculo:'))
print('O limite de velocidade é de 80 km/h')
if velocidade>80:
    print('Voce ultrapassou o limite de velocidade')
    print('O Valor da multa é de 7 reais por cada km/h acima da velocidade permitida, totalizando {} reais a serem pagos de multa'.format((velocidade-80)*7))
else:
    print('O veiculo está dentro do limite de velocidade')
