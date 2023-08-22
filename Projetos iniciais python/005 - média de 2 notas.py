n1 = int(input('Digite a primeira nota:'))
n2 = int(input('Digite a segunda nota:'))
cores = {'limpa': '\033[m',
         'red': '\033[0;31;40m',
         'violeta': '\033[1;35;40m',
         'azul': '\033[4;34;40m',
         'amarelo': '\033[7;33;40m',
         'amarelo2': '\033[33;42m',
         'verde': '\033[1;32;40m',
         'cinza': '\033[4;37;44m'}

con = (n1 + n2)/2
print('A média de suas notas é {}{}{}'.format(cores['red'], con, cores['limpa']))