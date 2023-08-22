import random
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
n = 1
tentativas = 0
think = random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
while 0 <= n <= 10:
    n = int(input('Digite um número entre 0 e 10: '))
    tentativas += 1
    if n <= 10 and n == think:
        print(f'{cores["verde"]}Sucesso número igual!Meus parabens!{cores["limpa"]}')
        print('{}Você precisou de {} tentativas{}'.format(cores['verde'], tentativas, cores['limpa']))
        if True:
            break
    else:
        print(f'{cores["red"]}número errado tente novamente.{cores["limpa"]}')