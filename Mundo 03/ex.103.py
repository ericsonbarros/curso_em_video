def ficha(nome, gols=0):
    if nome == '': # para um nome desconhecido\ em branco
        nome = '<desconhecido>'

    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


print('-'*40)
nome = str(input('Nome do jogador: '))
gols = str(input('Quantidade de gol(s): '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
ficha(nome, gols)
