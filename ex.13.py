import math
an = float(input('Digite o valor do angulo:'))
sen = math.sin(math.radians(an))
cos = math.cos(math.radians(an))
tan = math.tan(math.radians(an))
print('Sendo o angulo {}, o cosseno é {:.2f}, o seno é {:.2f} e a tangente corresponde a {:.2f}'.format(an, cos, sen, tan))


