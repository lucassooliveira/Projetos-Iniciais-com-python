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
sal = float(input(f'{cores["verde"]}Digite o salário do funcionário: {cores["limpa"]}'))
base = 1250.00
aumentoma = 0.1
aumentome = 0.15
if sal <= base:
    i = sal + (base * aumentome)
    print('{}O novo salário com aumento é {}R$'.format(cores["verde"], i))
elif sal > base:
    i = sal + (base * aumentoma)
    print('{}O novo salário com aumento é {}R$'.format(cores["verde"], i))
else:
    pass