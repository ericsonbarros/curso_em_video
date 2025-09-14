soma_idade = 0
media_idade = 0
maior_idade_homem = 0
nome_velho = ''
totmulher20 = 0
for pess in range (1, 5):
    nome = str(input('Digite o nome da {} pessoa: '.format(pess))).strip()
    idade = int(input('Digite a idade da {} pessoa: '.format(pess)))
    genero = str(input('Digite o genero da {} pessoa: '.format(pess))).lower()
    soma_idade += idade
    if pess == 1 and genero in 'm':
        maior_idade_homem = idade
        nome_velho = nome
    if genero in 'm' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_velho = nome
    if genero in 'f' and idade < 20:
        totmulher20 += 1
media_idade = soma_idade / 4
print('A media de idade do grupo e de  {} anos'.format(media_idade))
print('O homem mais velho tem {} anos e se chama {}'.format(maior_idade_homem, nome_velho))
print('Ao todo sao {} mulheres com menos de 20 anos'.format(totmulher20))
