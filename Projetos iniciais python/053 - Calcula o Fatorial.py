n = int(input('Digite um número inteiro qualquer: '))
fat = 1
while n > 1:         #Condiciona que a variável 'n' só pode ser maior que 1
    fat *= n
    n -= 1
print('O fatorial do número é igual a {}.'.format(fat))