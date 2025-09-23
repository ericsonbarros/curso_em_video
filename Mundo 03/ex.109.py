from uteis import moeda

print('-' * 30)
p = float(input('Digite o preço:R$ '))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}')
print(f'Aumentando 10%, Temos {moeda.aumentar(p, 10, False)}')
print(f'diminuindo 13%, Temos {moeda.diminuir(p, 13, False)}')
