'''
Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal, e condição de pagamento:

- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço normal
- em 3x ou mais no cartão: 20% de juros
'''
valor = float(input('Digite o valor do produto: '))
form = int(input('1- À vista dinheiro/cheque:\n2- À vista no cartão:\n'
                 '3- Até 2x no cartão:\n4- Em 3X ou mais no cartão:\n=>'))
if form == 1:
    desc = valor - valor /10
    print('Seu produto tem 10% de desconto, ficando de R${} reais para R${} reais. '.format(valor, desc))
elif form == 2:
    desc = valor - (valor / 100) * 5
    print('Seu produto tem 5% de desconto, ficando de R${} reais para R${} reais. '.format(valor, desc))
elif form == 3:
    parc = valor / 2
    print('O valor do produto é de R${} reais em duas parcelas de R${} reais, sem desconto. '.format(valor, parc))
elif form == 4:
    nov_en = int(input('Digite o númeor de parcelas: '))
    valor_n = (valor / 100) * 20 + valor
    parc = valor_n / nov_en
    print('O valor do produto com o juros é de {}, em {} parcelas de R${} reais. '.format(valor_n, nov_en, parc))
else:
    print('Escolha uma opção válida. ')
print("FIM.")