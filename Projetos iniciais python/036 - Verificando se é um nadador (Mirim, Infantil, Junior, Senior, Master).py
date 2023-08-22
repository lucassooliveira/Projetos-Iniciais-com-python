ano = int(input('Ano de nascimento: '))
idade = 2023 - ano
if idade <= 9:
    print('Nadador: MIRIM')
elif 9 < idade <= 14:
    print('Nadador: INFANTIL')
elif 14 < idade <= 19:
    print('Nadador: JUNIOR')
elif 19 < idade <= 20:
    print('Nadador: SENIOR')
elif idade > 20:
    print('Nadador: MASTER')