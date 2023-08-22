n = int(input('Digite um número inteiro qualquer: '))
print('Escolha uma das bases para conversão:',
      '[1] converter para BINÁRIO',
      '[2] converter para OCTAL'
      '[3] converter para HEXADECIMAL')
op = int(input('Digite sua opção: '))
if op == 1:
    print('O número convertido de {} decimal em BINÁRIO é {}'.format(n, bin(n)[2:]))
elif op == 2:
    print('O número convertido de {} decimal em OCTAL é {}'.format(n, oct(n)[2:]))
elif op == 3:
    print('O número convertido de {} decimal em HEXADECIMAL é {}'.format(n, hex(n)[2:]))
else:
    pass
