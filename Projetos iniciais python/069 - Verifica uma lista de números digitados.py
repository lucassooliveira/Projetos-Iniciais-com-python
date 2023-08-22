valor = []
cont = 0
jok = ''
while True:
    num = input('Digite um valor: ')
    valor.append(num)
    cont += 1
    valor.sort(reverse=True)
    while True:
        op = str(input('Deseja continuar?[S/N] ')).upper().strip()
        if op == 'S' or op == 'N':
            if op == 'S':
                break
            elif op == 'N':
                jok = True
            break
        else:
            print('Opção invalida!')
    if jok:
        print('-=' * 30)
        print(f'Você digitou {cont} elementos.')
        print(f'Os valores em ordem decrescente são {valor}')
        if 5 in valor:
            print(f'O valor 5 faz parte da lista.')
        else:
            print('O valor 5 não faz parte da lista.')
        break
