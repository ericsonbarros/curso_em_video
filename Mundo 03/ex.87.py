matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_pares = maior = soma_coluna = 0
for i in range(0, 3):
    for j in range(0, 3):
        matriz[i][j] = int(input(f'Digite um valor para [{i}, {j}]: '))
        if matriz[i][j] % 2 == 0:
            soma_pares += matriz[i][j]
print('-=' * 30)
print(f'[ {matriz[0][0]} ][ {matriz[0][1]} ][ {matriz[0][2]} ]')
print(f'[ {matriz[1][0]} ][ {matriz[1][1]} ][ {matriz[1][2]} ]')
print(f'[ {matriz[2][0]} ][ {matriz[2][1]} ][ {matriz[2][2]} ]')
print('-=' * 30)
print(f'A soma dos valores pares é {soma_pares}')
print('-=' * 30)
soma_coluna += matriz[0][2] + matriz[1][2] + matriz[2][2]
print(f'A soma dos valores da terceira coluna é {soma_coluna}')
for c in range(0, 3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
print('-=' * 30)
print(f'O maior valor da segunda linha é {maior}')
print('-=' * 30)