valores = []

while True:
    num = int(input('Digite um valor: '))
    if not num in valores:
        valores.append(num)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado! não vou adicionar...')

    op = input('Deseja continuar?[S/N] ').upper()
    if op == 'N':
        valores.sort()
        print(f'Você digitou os valores {valores}')
        break
