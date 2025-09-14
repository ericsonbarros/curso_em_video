palavras = ('aprender', 'programar', 'linguagem', 'python')
for p in palavras:
    print(f'\nna palavras {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end= ' ')




