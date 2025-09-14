import math
oppSide = float(input('Digite o valor do cateto oposto:'))
adjSide = float(input('Digite o valor do cateto adjacente:'))
hypotenuse = math.sqrt((math.pow(oppSide,2))+(math.pow(adjSide,2)))
print('O Cateto oposto sendo {}, e o cateto adjacente sendo {} a hipotenusa e igual a {:.2f}'.format(oppSide, adjSide, hypotenuse))

