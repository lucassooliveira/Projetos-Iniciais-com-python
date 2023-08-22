ano = int(input('Digite o ano de nascimento: '))
cond = 2023 - ano
lim = 18
if cond < lim:
    print('O jovem ainda vai se alistar, falta {} anos para o prazo! '.format(lim-cond))
elif cond > lim:
    print('O jovem já devia ter se alistado, já passou {} anos do prazo!'.format(cond-lim))
else:
    print('Está na hora de se alistar!')