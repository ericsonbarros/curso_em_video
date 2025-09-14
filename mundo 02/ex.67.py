cont = 0
while True:
  tabuada = int(input('Digite o numero da tabuada que quer ver: '))
  if tabuada <= -1:
    break
  for c in range (0,11):
    print(f'{tabuada} X {c} = {tabuada * c}')
    cont += 1
print('FIM')