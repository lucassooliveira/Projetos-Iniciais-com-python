def menu():
    print('=' * 7, 'FIM DO PROGRAMA', '=' * 7)
    print('-' * 20)
    print('CADASTRE UMA PESSOA')
    print('-' * 20)


menu()
contm = contf = contd = 0
while True:
    while True:
        idade = int(input('Idade: '))
        sex = str(input('[M/F] ')).upper().strip()
        if sex == 'M':
            contm += 1
            break
        elif sex == 'F' and idade < 20:
            contf += 1
            break
        elif idade > 18:
            contd += 1
            break
    so = str(input('Quer continuar? [S/N] ')).upper().strip()
    print('-' * 20)
    if so == 'S':
        continue
    elif so == 'N':
        break
menu()
print(f'Total de pessoas com mais de 18 anos: {contd}')
print(f'Ao todo temos {contm} homens cadastrados')
print(f'E temos {contf} mulheres com menos de 20 anos')
