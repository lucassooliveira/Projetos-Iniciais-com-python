from math import cos, sin, tan, radians
ang = float(input('Digite o ângulo: '))
cores = {'limpa': '\033[m',
         'red': '\033[0;31;40m',
         'violeta': '\033[1;35;40m',
         'azul': '\033[4;34;40m',
         'amarelo': '\033[7;33;40m',
         'amarelo2': '\033[33;41m',
         'amarelo3': '\033[33;40m',
         'verde': '\033[1;32;40m',
         'cinza': '\033[4;37;40m'}
sen = sin(radians(ang))
cose = cos(radians(ang))
tane = tan(radians(ang))
print('{}O coseno do ângulo é {:.2f}, o seno é {:.2f} e a tangente é {:.2f}{}'.format(cores['amarelo2'], cose, sen, tane, cores['limpa']))