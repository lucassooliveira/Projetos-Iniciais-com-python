from math import sqrt
num = float(input('Digite o numero do cateto oposto: '))
num2 = float(input('Digite o número do cateto adjacente: '))
cores = {'limpa': '\033[m',
         'red': '\033[0;31;40m',
         'violeta': '\033[1;35;40m',
         'azul': '\033[4;34;40m',
         'amarelo': '\033[7;33;40m',
         'amarelo2': '\033[33;41m',
         'amarelo3': '\033[33;40m',
         'verde': '\033[1;32;40m',
         'cinza': '\033[4;37;40m'}
hipo1 = (num**2)+(num2**2)
print('{}O comprimento da hipotenusa é {:.3f}'.format(cores['amarelo'], sqrt(hipo1)))