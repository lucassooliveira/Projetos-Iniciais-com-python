num = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze',
       'Quartoze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    while True:
        n = input('Digite um número entre 0 e 20: ')
        if n.isnumeric():
            n = int(n)
            if 0 < n < 21:
                c = num[n]
                j = True
                break
            else:
                print('Tente novamente.', end='')
        else:
            print('Tente novamente.', end='')
    if j:
        print(f'Você digitou o número {c}')
        break
