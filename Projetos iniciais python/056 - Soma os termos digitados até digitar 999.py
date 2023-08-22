n = 0
soma = somatt = 0
while True:
    n = int(input('Digite um valor inteiro qualquer: '))
    if n > 999:
        break
    elif n == 999:
        print('A soma total deu {}'.format(somatt))
        break
    else:
        soma += n
        somatt = soma - 999
        print('A soma dos termos digitados foi {}'.format(soma))