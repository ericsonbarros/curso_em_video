from datetime import date
ano_atual = date.today().year
nome = str(input('Insira o nome do atleta: '))
nascimento = int(input('Insira o ano do nascimento do atleta: '))
idade = ano_atual - nascimento
print(f'O atleta {nome}, possui {idade} anos.')
if idade <= 9:
    print('O atleta se encaixa na categoria: MIRIM  ')
elif idade<= 14:
    print('O atleta se encaixa na categoria: JÚNIOR')
elif idade <= 19:
    print('O atleta se encaixa na categoria: SÊNIOR')
else:
    print('O atleta se encaixa na categoria: MASTER')
