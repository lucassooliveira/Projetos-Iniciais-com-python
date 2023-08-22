cores = {'limpa': '\033[m',
         'red': '\033[0;31;40m',
         'violeta': '\033[1;35;40m',
         'azul': '\033[4;34;40m',
         'azul2': '\033[1;34;40m',
         'amarelo': '\033[7;33;40m',
         'amarelo2': '\033[33;41m',
         'amarelo3': '\033[33;40m',
         'verde': '\033[1;32;40m',
         'cinza': '\033[4;37;40m',
         'cinza2': '\033[1;37;40m',
         'teste': '\033[1;30;47m'}
n1 = int(input(f'{cores["azul2"]}Digite um número: '))
n2 = int(input(f'{cores["azul2"]}Digite um número: '))
n3 = int(input(f'{cores["azul2"]}Digite um número: '))
cond1 = n1 > n2 > n3
cond2 = n3 > n2 > n1
cond3 = n2 > n1 > n3
cond4 = n3 > n1 > n2
cond5 = n1 > n3 > n2
cond6 = n2 > n3 > n1
if cond1:
    print('{}O maior número é {} e o menor é {}'.format(cores['violeta'], n1, n3))
elif cond2:
    print('{}O maior número é {} e o menor é {}'.format(cores['violeta'], n3, n1))
elif cond3:
    print('{}O maior número é {} e o menor é {}'.format(cores['violeta'], n2, n3))
elif cond4:
    print('{}O maior número é {} e o menor é {}'.format(cores['violeta'], n3, n2))
elif cond5:
    print('{}O maior número é {} e o menor é {}'.format(cores['violeta'], n1, n2))
elif cond6:
    print('{}O maior número é {} e o menor é {}'.format(cores['violeta'], n2, n1))
else:
    pass