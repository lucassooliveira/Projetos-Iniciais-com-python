n1 = float(input('Digite a distância em metros:'))
cores = {'limpa': '\033[m',
         'red': '\033[0;31;40m',
         'violeta': '\033[1;35;40m',
         'azul': '\033[4;34;40m',
         'amarelo': '\033[7;33;40m',
         'amarelo2': '\033[33;42m',
         'verde': '\033[1;32;40m',
         'cinza': '\033[4;37;44m'}
cm = n1 * 100
mili = n1 * 1000
print('{}Em centímetros a distância fica {:.0f}cm, \n e em milímetros {:.0f}mm. {}'.format(cores['violeta'], cm, mili, cores['limpa']))