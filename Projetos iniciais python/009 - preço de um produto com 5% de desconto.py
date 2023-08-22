preço = float(input('Digite o preço do produto:'))
cores = {'limpa': '\033[m',
         'red': '\033[0;31;40m',
         'violeta': '\033[1;35;40m',
         'azul': '\033[4;34;40m',
         'amarelo': '\033[7;33;40m',
         'amarelo2': '\033[33;42m',
         'verde': '\033[1;32;40m',
         'cinza': '\033[4;37;40m'}
desconto = preço - (preço*0.05)
print('{}O preço do produto R${:.2f}, e com desconto de 5% fica R${:.2f} reais! {}'.format(cores['cinza'], preço, desconto, cores['limpa']))