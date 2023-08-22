n = int(input('Digite o número para verificação: '))
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
         'teste': '\033[1;30;47m'}
if n % 2 != 0:
    print(f'{cores["violeta"]}{n} é um número ímpar!{cores["limpa"]}')
else:
    print(f'{cores["azul"]}{n} é um número par!{cores["limpa"]}')