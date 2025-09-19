ficha = {}
gol = list()
ficha['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {ficha["nome"]} jogou? '))
for p in range(0, partidas):
    gol.append(int(input(f'Quantos gols na partida {p+1}? ')))
    ficha['gols'] = gol[:]
    ficha['total'] = sum(gol)
print('-=' * 30)
print(ficha)
print('-=' * 30)
for k, v in ficha.items():
    print(f'O campo {k} tem o valor {v}.')
print('-=' * 30)
print(f'O jogador {ficha["nome"]} jogou {partidas} partidas.')
for p in range(0, partidas):
    print(f'  => na partida {p+1}, fez {ficha['gols'][p]}')
    
print(f'Foi um total de {ficha["total"]} gols.')
