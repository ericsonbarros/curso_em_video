def escreva(texto):
    tamanho = len(texto) + 4
    print('~'*tamanho)
    print(f'  {texto}')
    print('~'*tamanho)


# programa principal
escreva('Ola, mundo')
escreva('Curso em Video Python')
escreva('flamengo')