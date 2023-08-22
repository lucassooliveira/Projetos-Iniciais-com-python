n1 = int(input('Digite o primeiro valor:'))
n2 = int(input('Digite o segundo número:'))
cores = {'limpa': '\033[m',
         'red': '\033[0;31;43m',
         'violeta': '\033[1;35;40m',
         'azul': '\033[4;34;40m',
         'amarelo': '\033[7;33;40m',
         'amarelo2': '\033[33;42m',
         'verde': '\033[1;32;40m',
         'cinza': '\033[4;37;44m'}
s = n1 + n2
print('A soma entre {}{} e {}{} é {}{}{}'.format(cores['verde'], n1, cores['violeta'], n2, cores['red'], s, cores['limpa']))
a = input('Digite algo: ')
print('{} O tipo primitivo desse valor é: {}'.format(cores['azul'], cores['limpa']), type(a))
print('{}Só tem espaços: {}'.format(cores['azul'], cores['limpa']), a.isspace())
print('{}É um número?{}'.format(cores['azul'], cores['limpa']), a.isnumeric())
print('{}É alfabético?{}'.format(cores['azul'], cores['limpa']), a.isalpha())
print('{}É alphanumérico{}'.format(cores['azul'], cores['limpa']), a.isalnum())
print('{}Está em maiuscula{}'.format(cores['azul'], cores['limpa']), a.isupper())
print('{}Está em minuscula{}'.format(cores['azul'], cores['limpa']), a.islower())
print('{}Está capitalizada{}'.format(cores['azul'], cores['limpa']), a.istitle())