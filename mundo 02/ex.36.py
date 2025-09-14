#entrada
valor_imovel = float(input('Digite o valor a ser financiado do imóvel: '))
salario_comprador = float(input('Informe o valor da renda mensal: '))
temp_financiamento = int(input('Informe o tempo desejavel do financiamento em anos: '))
#processamento
parcela_mensal = valor_imovel / (temp_financiamento*12)
if parcela_mensal <=  salario_comprador * 30 /100:
    #saida
    print(f"Parabens, Seu financiamento foi APROVADO\nO financiamento ficou com a parcela mensal de{parcela_mensal} reais durante o período de {temp_financiamento} anos")
else:
    print('Desculpe, seu financiamento nao foi aprovado')
