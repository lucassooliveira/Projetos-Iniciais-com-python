from random import choice
nome1 = str(input('Digite o nome do aluno 1: '))
nome2 = str(input('Digite o nome do aluno 2: '))
nome3 = str(input('Digite o nome do aluno 3: '))
nome4 = str(input('Digite o nome do aluno 4: '))
cores = {'limpa': '\033[m',
         'red': '\033[0;31;40m',
         'violeta': '\033[1;35;40m',
         'azul': '\033[4;34;40m',
         'amarelo': '\033[7;33;40m',
         'amarelo2': '\033[33;41m',
         'amarelo3': '\033[33;40m',
         'verde': '\033[1;32;40m',
         'cinza': '\033[4;37;40m'}
a = choice([nome1, nome2, nome3, nome4])
print('O aluno que vai apagar o quadro será {}{}!{}'.format(cores['amarelo3'], a, cores['limpa']))