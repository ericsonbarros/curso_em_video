total_maior = total_homem = total_mulher20 = 0
while True:
  idade = int(input('Digite a idade : '))
  sexo = str(input('Digite o sexo: ')).strip().upper()[0]
  continuar = str(input('Deseja cadastar mais algum usuario: ')).strip().upper()[0]
  if idade >= 18:
    total_maior += 1
  if sexo == 'M':
    total_homem += 1
  if sexo in 'F' and idade < 20:
    total_mulher20 += 1
  if continuar == 'N':
    break
print(f'total de pessoas maiores de idade cadastrado foi de: {total_maior}')
print(f'total de homens cadastrado foi de: {total_homem}')
print(f'total de mulher cadastrada com menos de 20 anos sao: {total_mulher20}')