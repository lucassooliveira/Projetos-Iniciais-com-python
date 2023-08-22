c = float(input('Digite a temperatura em °C: '))
cores = {'limpa': '\033[m',
         'red': '\033[0;31;40m',
         'violeta': '\033[1;35;40m',
         'azul': '\033[4;34;40m',
         'amarelo': '\033[7;33;40m',
         'amarelo2': '\033[33;41m',
         'amarelo3': '\033[33;40m',
         'verde': '\033[1;32;40m',
         'cinza': '\033[4;37;40m'}
f = (9*c/5)+32
print('A temperatura em{} {:.2f}°C {}fica{} {:.2f}°F !{}'.format(cores['red'], c, cores['limpa'], cores['azul'], f, cores['limpa']))