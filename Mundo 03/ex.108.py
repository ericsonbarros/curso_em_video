from uteis import moeda

print('-' * 30)
p = float(input('Digite o preço:R$ '))
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'Aumentando 10%, Temos {moeda.moeda(moeda.aumentar(p, 10))}')
print(f'diminuindo 13%, Temos {moeda.moeda(moeda.diminuir(p, 13))}')