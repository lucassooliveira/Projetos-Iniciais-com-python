nome = input('Digite o nome completo: ').strip()
cores = {'limpa': '\033[m',
         'red': '\033[0;31;40m',
         'violeta': '\033[1;35;40m',
         'azul': '\033[4;34;40m',
         'amarelo': '\033[7;33;40m',
         'amarelo2': '\033[33;41m',
         'amarelo3': '\033[33;40m',
         'verde': '\033[1;32;40m',
         'cinza': '\033[4;37;40m'}
nome1 = nome.upper()
nome2 = nome.lower()
nome4 = nome.split()
nome7 = ''.join(nome4)
nome3 = len(nome7)
nome5 = nome4[0]
nome6 = len(nome5)
print('{}O nome com todas a letras maiusculas é {}'.format(cores['cinza'], nome1))
print('{}O nome com todas as letras minusculas é {}'.format(cores['red'], nome2))
print('{}O nome completo tem o total de {} letras'.format(cores['violeta'], nome3))
print('{}E o primeiro nome tem o total de {} letras'.format(cores['azul'], nome6))