from datetime import date
ano_atual = date.today().year
cadastro = dict()
cadastro['nome'] = str(input('Digite o Nome: '))
cadastro['ano de nascimento'] = int(input('Digite o ano de nascimento: '))
cadastro['carteira de trabalho'] = int(input('Digite o numero da carteira de trabalho (caso nao tenha digite 0): '))
if cadastro['carteira de trabalho'] != 0:
    cadastro['ano de contratação'] = int(input('Digite o ano de contratação: '))
    cadastro['salario'] = float(input('Digite o salario: '))
print('-=' * 20)
print(f'O usuario {cadastro["nome"]}', end=' ')
idade = ano_atual - cadastro["ano de nascimento"]
print(f'possui {idade} anos.')
print(f'codigo da CTPS: {cadastro["carteira de trabalho"]}')
if cadastro['carteira de trabalho'] != 0:
    print(f'O usuario foi contratato no ano de {cadastro["ano de contratação"]}', end=' ')
    print(f'com salario de  {cadastro["salario"]:.2f}')
    ano_aposentadoria = cadastro["ano de contratação"] - cadastro["ano de nascimento"] + 35
    print(f'O usurio deve se aponsentar com {ano_aposentadoria} anos.')
