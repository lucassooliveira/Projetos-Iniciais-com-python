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
r1 = float(input(f'{cores["azul2"]}Digite um segmento de reta: '))
r2 = float(input(f'{cores["azul2"]}Digite um segmento de reta: '))
r3 = float(input(f'{cores["azul2"]}Digite um segmento de reta: '))
cond1 = r1 < (r2 + r3)
cond2 = r2 < (r1 + r3)
cond3 = r3 < (r1 + r2)
if cond1 and cond2 and cond3:
    print(f'{cores["azul"]}As três retas formam um triângulo!')
else:
    print(f'{cores["azul"]}Não formam um triângulo!')