from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1,8):
    nasc = int(input('Digite o ano de nascimento da {}º pessoa: '.format(pess)))
    idade = atual - nasc
    if idade >= 21:
        totmaior+= 1
    else:
        totmenor+= 1
print('O total de pessoas que atingiram a maioridade e de {}, ainda faltam {} atingirem a maioridade'.format(totmaior, totmenor))






