import random
n = int(input('Digite um número entre 0 e 5: '))
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
think = random.choice([0, 1, 2, 3, 4, 5])
if n <= 5 and n == think:
    print(f'{cores["verde"]}Sucesso número igual!{cores["limpa"]}')
else:
    print(f'{cores["red"]}número errado tente novamente.{cores["limpa"]}')