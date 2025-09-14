from datetime import date
ano_atual = date.today().year
nascimento = int(input('Digite o ano do seu nascimento: '))
idade = ano_atual - nascimento
print(f'Quem nasceu em {nascimento} tem {idade} anos em {ano_atual}')
if idade == 18:
    print('Você dese se alistar imediatamente')
elif idade < 18:
    idade_alistamento = 18 - idade
    print(f'Você possui atualmente {idade}, faltam {idade_alistamento} anos para o seu alistamento')
elif idade > 18:
    idade_superior = idade - 18
    print(f'Você possui atualmente {idade}, seu prazo para alistamento foi ultrapassado em {idade_superior} anos')
    print('Por favor procure um centro de alistamento militar para resolver sua situação junto ao exército brasileiro')
