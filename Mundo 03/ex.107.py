from uteis import moeda

print('-' * 30)
p = float(input('Digite o preço:R$ '))
print(f'A metade de R$ {p} é {moeda.metade(p)}')
print(f'O dobro de R$ {p} é {moeda.dobro(p)}')
print(f'Aumentando 10%, Temos {moeda.aumentar(p, 10)}')
print(f'diminuindo 13%, Temos {moeda.diminuir(p, 13)}')
