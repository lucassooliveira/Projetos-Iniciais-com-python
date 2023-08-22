n1 = int(input('Digite um número:'))
cores = {'limpa': '\033[m',
         'red': '\033[0;31;40m',
         'violeta': '\033[1;35;40m',
         'azul': '\033[4;34;40m',
         'amarelo': '\033[7;33;40m',
         'amarelo2': '\033[33;42m',
         'verde': '\033[1;32;40m',
         'cinza': '\033[4;37;44m'}
x1 = n1 * 1
x2 = n1 * 2
x3 = n1 * 3
x4 = n1 * 4
x5 = n1 * 5
x6 = n1 * 6
x7 = n1 * 7
x8 = n1 * 8
x9 = n1 * 9
print(f'{cores["azul"]}A tabuada de {n1} e seus resultados respectivamente são: \n {n1}x1 = {x1} \n {n1}x2 = {x2} \n {n1}x3 = {x3} \n {n1}x4 = {x4} \n {n1}x5 = {x5} \n {n1}x6 = {x6} \n {n1}x7 = {x7} \n {n1}x8 = {x8} \n {n1}x9 = {x9} {cores["limpa"]}')