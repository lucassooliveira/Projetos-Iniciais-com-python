n1 = float(input('Digite a altura da parede:'))
n2 = float(input('Digite a largura da parede:'))
cores = {'limpa': '\033[m',
         'red': '\033[0;31;40m',
         'violeta': '\033[1;35;40m',
         'azul': '\033[4;34;40m',
         'amarelo': '\033[7;33;40m',
         'amarelo2': '\033[33;41m',
         'amarelo3': '\033[33;40m',
         'verde': '\033[1;32;40m',
         'cinza': '\033[4;37;44m'}
area = n1 * n2
lt = area/8.5
print('A sua parede tem dimensões:{} {}m² {}'.format(cores['amarelo3'], area, cores['limpa']))
print('{}Para pintar a parede completamente você precisa de {} litros de tinta{}'.format(cores['amarelo3'], lt, cores['limpa']))