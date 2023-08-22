valores = []
par = []
impar = []
j = ''
while True:
    num = int(input('Digite um valor: '))
    valores.append(num)
    while True:
        op = str(input('Deseja continuar?[S/N] ')).upper().strip()
        if op == 'S' or op == 'N':
            if op == 'S':
                j = False
                break
            elif op == 'N':
                j = True
            break
        else:
            print('Opção invalida!')
    if j:
        for valor in valores:
            if valor % 2 == 0:
                par.append(valor)
            else:
                impar.append(valor)

        print(f'A lista completa é {valores}')
        print(f'A lista de pares é {par}')
        print(f'A lista de ímpares é {impar}')
        break