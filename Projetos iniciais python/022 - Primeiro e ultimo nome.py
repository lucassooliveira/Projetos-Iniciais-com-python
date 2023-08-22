nome = input('Digite seu nome: ').strip()
prim = nome.split()
cores = {'limpa': '\033[m',
         'red': '\033[0;31;40m',
         'violeta': '\033[1;35;40m',
         'azul': '\033[4;34;40m',
         'amarelo': '\033[7;33;40m',
         'amarelo2': '\033[33;41m',
         'amarelo3': '\033[33;40m',
         'verde': '\033[1;32;40m',
         'cinza': '\033[4;37;40m',
         'cinza2': '\033[1;37;40m',
         'teste': '\033[30;47m'}
print('{}Seu primeiro nome é {}'.format(cores['amarelo'], prim[0]))
print('{}Seu ultimo nome é {}'.format(cores['amarelo2'], prim[-1]))