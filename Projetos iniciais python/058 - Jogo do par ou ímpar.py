import random


def menu():
    print('=-=' * 20)
    print('Vamos jogar par ou ímpar!')
    print('=-=' * 20)


menu()
cont = 0
while True:
    n = int(input('Digite um valor: '))
    pi = str(input('Par ou Ìmpar? [P/I] ')).upper().strip()
    comp = random.randint(1, 999)
    m = n + comp
    if m % 2 == 0:
        esc = 'P'
        if pi == esc:
            print('-' * 20)
            print(f'Você jogou {n} e o computador {comp}. o total de {m} DEU PAR')
            print('-' * 20)
            print('Você GANHOU!')
            cont += 1
        else:
            print('-' * 20)
            print(f'Você jogou {n} e o computador {comp}. o total de {m} DEU PAR')
            print('-' * 20)
            print('Você PERDEU!')
            break
    elif m % 2 != 0:
        esc = 'I'
        if pi == esc:
            print('-' * 20)
            print(f'Você jogou {n} e o computador {comp}. o total de {m} DEU ÍMPAR')
            print('-' * 20)
            print('Você GANHOU!')
            cont += 1
        else:
            print('-' * 20)
            print(f'Você jogou {n} e o computador {comp}. o total de {m} DEU ÍMPAR')
            print('-' * 20)
            print('Você PERDEU!')
            break
print('=-=' * 20)
print(f'GAME OVER! Você venceu {cont} vezes.')
