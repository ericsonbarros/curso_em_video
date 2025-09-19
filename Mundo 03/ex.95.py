ficha = {}
gol = list()
dado = list()
while True:
    ficha['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {ficha["nome"]} jogou? '))
    for p in range(0, partidas):
        gol.append(int(input(f'Quantos gols na partida {p+1}? ')))
        ficha['gols'] = gol[:]
        ficha['total'] = sum(gol)
    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    gol.clear()
    dado.append(ficha.copy())
    if continuar in 'Nn':
        break
print('-=' * 30)
print('cod ', end='')
for i in ficha.keys():
    print(f'{i:<15} ', end='')
print()
print('-' * 40)
for k, v in enumerate(dado):
    print(f'{k:>2} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
while True:
    buscar = int(input('Mostrar dados de qual jogador? '))
    if buscar == 999:
        break
    if buscar >= len(dado):
        print(f'ERRO! Não existe jogador com codigo {buscar}.')
    else:
        print(f'-- Levantamento do jogador {dado[buscar]["nome"]}')
        for i, g in enumerate(dado[buscar]['gols']):
            print(f'No jogo {i+1} fez {g} gols.')
    print('-' * 40)
print('VOLTE SEMPRE!')
