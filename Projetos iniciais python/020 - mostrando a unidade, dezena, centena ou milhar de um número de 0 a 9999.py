num = int(input('Digite um número entre 0 e 9999: '))
cores = {'limpa': '\033[m',
         'red': '\033[0;31;40m',
         'violeta': '\033[1;35;40m',
         'azul': '\033[4;34;40m',
         'amarelo': '\033[7;33;40m',
         'amarelo2': '\033[33;41m',
         'amarelo3': '\033[33;40m',
         'verde': '\033[1;32;40m',
         'cinza': '\033[4;37;40m'}
unidade = num % 10
dezena = (num - unidade)//10 % 10
centena = (num - dezena)//100 % 10
milhar = (num - centena)//1000 % 10

print('{}A unidade é {}'.format(cores['amarelo'], unidade))
print('{}A dezena é {}'.format(cores['amarelo2'], dezena))
print('{}A centena é {}'.format(cores['amarelo3'], centena))
print('{}O milhar é {}'.format(cores['verde'], milhar))