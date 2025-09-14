print(('='*10) + ('lojas') + ('='*10))
produto = float(input('Digite o valor do produto: '))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/Pix
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = str(input('Escolha a forma de pagamento?: '))
if opção == 1:
    total_1 = produto - (produto * 10 / 100)
    print('Sua compra de R$ {} vai custar {} no final'.format(produto, total_1))
elif opção == 2:
    total = produto - (produto *5 / 100)
elif opção == 3:
    total = produto
    parcela = total / 2
    print('sua compra derá parcelada em 2x de R$ {:.2f}'.format(parcela))





