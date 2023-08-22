soma = 0
maior = 0
nomevei = ''
totmulher20 = 0
for c in range(1, 5):
    print('======== {}° PESSOA ========='.format(c))
    nome = str(input('Nome: ')).strip().upper()
    idad = int(input('Idade: '))
    soma += idad
    sexo = str(input('Sexo[M/F]: ')).strip().upper()
    if 'M' in sexo and c == 1:
        maior = idad
        nomevei = nome
    if 'M' in sexo and idad > maior:
        maior = idad
        nomevei = nome
    if 'F' in sexo and idad < 20:
        totmulher20 += 1
media = soma / 4
print('A média da idade de todos é {}'.format(media))
print('A homem com maior idade é {}'.format(nomevei))
print('Há um total de {} mulheres com menos de 20 anos.'.format(totmulher20))