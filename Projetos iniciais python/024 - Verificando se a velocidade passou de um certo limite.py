vel = int(input('Digite a velocidade do veículo: '))
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
print('A velocidade do veículo é {}{}km/h{}'.format(cores['red'], vel, cores['limpa']))
print('{}Velocidade máxima foi ultrapassada!{}'.format(cores['red'], cores['limpa']) if vel > 80 else '{}Velocidade normal, tenha um bom dia!{}'.format(cores['verde'], cores['limpa']))
max = 80
none = 0
multa = (vel - max) * 7
if vel > 80:
    print(f'{cores["red"]}Multa aplicada!', multa, f'R${cores["limpa"]}')
else:
    print(f'{cores["teste"]}fim!')