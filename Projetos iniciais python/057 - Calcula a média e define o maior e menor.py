n = 0
val = 'S'
cont = media = soma = maior = menor = 0
while val in 'Ss':
    n = int(input('Digite um valor: '))
    soma += n
    cont += 1
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
    val = str(input('Deseja continuar ?[S/N] ')).upper().strip()
media = soma / cont
print('A media dos números foi {}'.format(media))
print('Você tentou cerca {} vezes'.format(cont))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))