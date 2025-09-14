times = ('Flamengo', 'Cruzeiro', 'Palmeiras', 'Bahia',
         'Botafogo', 'Mirassol', 'Sao paulo', 'Red bull',
         'Fluminense', 'Internacional', 'Ceara',
         'Corinthians', 'Gremio', 'Atletico mineiro',
         'Vasco', 'Santos', 'Vitoria', 'Juventude', 'Fortaleza',
         'Sport')
print('-='*30)
print(f'lista dos times do brasileirao 2025: {times}')
print('-='*30)
print(f'Os 5 primeiros colocados são: {times[0:5]}')
print('-='*30)
print(f' os ultimos 4 colocados sao: {times[16:]}')
print('-='*30)
print(f'Times em ordem alfabetica: {sorted(times)}')
print('-='*30)
print(f'o flamengo esta na {times.index('Flamengo')+1} colocação')