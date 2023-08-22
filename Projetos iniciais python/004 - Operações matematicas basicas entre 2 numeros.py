n1 = int(input('Digite um valor:'))
n2 = int(input('Digite outro valor:'))
cores = {'limpa': '\033[m',
         'red': '\033[0;31;43m',
         'violeta': '\033[1;35;40m',
         'azul': '\033[4;34;40m',
         'amarelo': '\033[7;33;40m',
         'amarelo2': '\033[33;42m',
         'verde': '\033[1;32;40m',
         'cinza': '\033[7;37;40m'}
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}{}{}, O produto é {}{}{}, A divisão é {}{}{}'.format(cores['red'], s, cores['limpa'], cores['azul'], m, cores['limpa'], cores['verde'], d, cores['limpa']), end=' >> ' )
print('A divisão inteira é {}{}{}, A pontência é {}{}{}'.format(cores['cinza'], di, cores['limpa'], cores['violeta'], e, cores['limpa']))