valor = float(input('Digite o valor do produto: '))
print('''#A condição de pagamento será:
#[1] À vista dinheiro/cheque: 10% de desconto.
#[2] À vista no cartão: 5% de desconto.
#[3] Em até 2x no cartão: preço normal.
#[4] 3x ou mais no cartão: 20% de juros ''')

opcpag = int(input('Digite o número da opção de pagamento: '))
valor1 = valor - (valor * 0.1)
valor2 = valor - (valor * 0.05)
valor3 = valor + (valor * 0.2)
if opcpag == 1:
    print('O valor final do produto será {}!'.format(valor1))
elif opcpag == 2:
    print('O valor final do produto será {}!'.format(valor2))
elif opcpag == 3:
    print('O valor final do produto será {}!'.format(valor))
elif opcpag == 4:
    print('O valor final do produto será {}!'.format(valor3))