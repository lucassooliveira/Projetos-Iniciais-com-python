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
print(f'{cores["red"]}Bem vindo ao calculador de passagem!{cores["limpa"]}\n')
di = int(input(f'{cores["red"]}Qual será a distância da sua viagem? {cores["limpa"]}'))
preco1 = 0.50
preco2 = 0.45
i = 0
valor1 = 200
if di <= valor1:
    i = (di * preco1)
    print('{}O valor da passagem será {} R${}'.format(cores["red"], i, cores["limpa"]))
else:
    i = (di * preco2)
    print('{}O valor da passagem será {} R${}'.format(cores["red"], i, cores["limpa"]))