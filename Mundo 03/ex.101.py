from datetime import date
def voto(ano_nasc):
    idade = date.today().year - ano_nasc
    if 16 <= idade < 18 or idade >= 65:
        print(f'Com {idade} anos o voto é OPCIONAL.')
    elif idade <= 15:
        print(f'Com {idade} anos NÃO E LIBERADO VOTAR')
    elif idade >= 18:
        print(f'Com {idade} anos o voto e OBRIGADO')


# programa principal
ano_nasc = int(input('Digite o ano de nascimento: '))
voto(ano_nasc)




