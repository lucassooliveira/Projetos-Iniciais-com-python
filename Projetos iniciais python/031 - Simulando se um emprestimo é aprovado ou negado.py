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
casa = int(input(f'{cores["verde"]}Qual o valor da casa ? '))
sal = int(input(f'{cores["verde"]}Qual o salário do comprador ? '))
anos = int(input(f'{cores["verde"]}Em quantos anos planeja pagar ? '))
mes = anos * 12
salmes = sal * 0.3
if salmes * mes < casa:
    print(f'{cores["red"]}Emprestimo negado!{cores["limpa"]}')
elif salmes * mes >= casa:
    print(f'{cores["verde"]}Emprestimo aprovado{cores["limpa"]}')
else:
    pass