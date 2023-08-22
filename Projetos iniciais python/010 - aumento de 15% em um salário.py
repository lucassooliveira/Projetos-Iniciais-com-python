salario = float(input('Digite o salário: R$'))
cores = {'limpa': '\033[m',
         'red': '\033[0;31;40m',
         'violeta': '\033[1;35;40m',
         'azul': '\033[4;34;40m',
         'amarelo': '\033[7;33;40m',
         'amarelo2': '\033[33;41m',
         'amarelo3': '\033[33;40m',
         'verde': '\033[1;32;40m',
         'cinza': '\033[4;37;40m'}
aumento = salario + (salario*0.15)
print('O saláio do funcionário aumentou para{} R${:.2f} reais!{}'.format(cores['red'], aumento, cores['limpa']))