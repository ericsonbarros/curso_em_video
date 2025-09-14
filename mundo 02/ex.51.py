termo = int(input('Digite o termo: '))
razao = int(input('Digite a razão: '))
decimo = termo + (11 - 1) * razao
pa = termo + razao + 1
for c in range (termo, decimo, razao):
    print(c, end= ' ')

