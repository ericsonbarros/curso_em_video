#Entrada
num = int(input('Digite o número escolhido'))
print('Escolha entre uma das base para conversão'
      '[1] binario'
      '[2] octal'
      '[3] hexadecimal')
base = int(input('Qual será a base escolhida pra conversão: '))
#processamento
if base == 1:
    binario = bin(num)
    #saida
    print(f"O número decial {num} em binário é {binario[2:]}")
#processamento
elif base == 2:
    octal = oct(num)
    #saida
    print(f"O número decial {num} em octal é {octal[2:]}")
#processamento
elif base == 3:
    hexadecimal = hex(num)
    #saida
    print(f"O número decial {num} em hexadecial é {hexadecimal[2:]}")
else:
    #saida
    print('Opção inválida. Tente novamente')