maior = 0
menor = 0
for c in range(0, 5):
    pes = float(input(f'Digite o peso da pessoa {c + 1}°: '))
    if c == 0:
        maior = pes
        menor = pes
    elif pes > maior:
        maior = pes
    elif pes < menor:
        menor = pes
print('O maior peso lido foi {}'.format(maior))
print('O menor peso lido foi {}'.format(menor))